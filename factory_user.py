#!/usr/bin/python

"""factory_user.py: User testing for factory_sim. """
__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

import paho.mqtt.client as mqtt
import time,logging,sys
import json

mqttBroker = "mqtt.eclipseprojects.io"
#port = 8883

# Flags
message_received_flag = False

# Variables
choice = ''
so_number = 1000

# Dictionaries
hand_shake={
    "msg_type": "message confirmation",
    "msg_confirmation_id": "CC####",
    "msg_type_received": "order",
    "msg_id": "SO####"
}

send_order={
    "msg_type": "order",
    "sim_msg_id": "SO####",
    "x": 1,
    "y": 1
}

request_status={
    "msg_type": "request status",
    "sim_msg_id": "RS####"
}

perform_inventory={
    "msg_type": "perform inventory",
    "sim_msg_id": "PI####"
}

cancel_order={
    "msg_type": "cancel order",
    "sim_msg_id": "CO####",
    "order_id": "SO####"
}

def on_message(client, userdata, message):
    global message_received_flag
    print("RECEIVED MESSAGE: ")
    print(str(message.payload.decode("utf-8")))
    message_received_flag = True

### MQTT Set up ###
print("CREATING CLIENT")
client = mqtt.Client("Factory User")
client.connect(mqttBroker)

print("************************")
print("1: Send Order")
print("2: Request Status")
print("3: Perform Inventory")
print("4: Cancel Order")
print("q: Quit")
print("************************")

### User Input Loop ###
while choice != 'q':
    client.loop_start()
    client.subscribe("UofICapstone_Sim")
    client.on_message = on_message

    #print("TEST ON MESSAGE: " + client.on_message)

    choice = input("Waiting for input: ")

    ### CHOICE 1: Order a product from the factory ###
    if choice == '1':
        so_number = so_number + 1
        send_order["sim_msg_id"] = "SO" + str(so_number)
        client.publish("UofICapstone_User", payload=json.dumps(send_order))
        #client.on_message = on_message
        time.sleep(3)

        while message_received_flag == False:
            client.publish("UofICapstone_User", payload=json.dumps(send_order))
            print("HANDSHAKE NOT RECIEVED.................")
            time.sleep(3)

        print("...JUST PUBLISHED...")
        print(str(send_order))
        print("...")
        message_received_flag = False
    elif choice == '2':
        print("Sent Request Status.....")
        client.publish("UofICapstone_User", payload=json.dumps(request_status))
    elif choice == '3':
        print("Sent Perform Inventory Request.....")
        client.publish("UofICapstone_User", payload=json.dumps(perform_inventory))
    elif choice == '4':
        print("Sent Request Status.....")
        client.publish("UofICapstone_User", payload=json.dumps(cancel_order))
    elif choice == 'q':
        print("Exiting.....")
    else:
        print("!WRONG!")

    time.sleep(2)