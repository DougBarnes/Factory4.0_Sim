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
#Removed _ from mes_type to match the slicer better.
send_order={
    "msgtype": "order",
    "sim_msg_id": "SO####",
    "location" : "location01"
}

request_status={
    "msgtype": "request status",
    "sim_msg_id": "RS####"
}

perform_inventory={
    "msgtype": "perform inventory",
    "sim_msg_id": "PI####"
}

cancel_order={
    "msgtype": "cancel order",
    "sim_msg_id": "CO####",
    "order_id": "SO####"
}

webcam={
    "msgtype": "webcam",
    "cloud_msg_id": "WP####",
    "power": "True"
}

control_webcam={
    "msgtype": "control webcam",
    "cloud_msg_id": "CW####",
    "y_turntable": 1, 
    "x_turntable": 1
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
print("5: Webcam")
print("6: Control Webcam")
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
        so_number = so_number + 1 #SO number generation
        send_order["sim_msg_id"] = "SO" + str(so_number)
        client.publish("UofICapstone_Cloud", payload=json.dumps(send_order))
        #client.on_message = on_message
        time.sleep(3)

        while message_received_flag == False:
            client.publish("UofICapstone_Cloud", payload=json.dumps(send_order))
            print("HANDSHAKE NOT RECIEVED.................")
            time.sleep(1)

        print("...JUST PUBLISHED...")
        print(str(send_order))
        print("...")
        message_received_flag = False
    elif choice == '2':
        print("Sent Request Status.....")
        client.publish("UofICapstone_Cloud", payload=json.dumps(request_status))
    elif choice == '3':
        print("Sent Perform Inventory Request.....")
        client.publish("UofICapstone_Cloud", payload=json.dumps(perform_inventory))
    elif choice == '4':
        print("Sent Cancel Status.....")
        client.publish("UofICapstone_Cloud", payload=json.dumps(cancel_order))
    elif choice == '5':
        print("Sent Webcam.....")
        client.publish("UofICapstone_Cloud", payload=json.dumps(webcam))
    elif choice == '6':
        print("Sent Control Webcam.....")
        client.publish("UofICapstone_Cloud", payload=json.dumps(control_webcam))
    elif choice == 'q':
        print("Exiting.....")
    else:
        print("!WRONG!")

    time.sleep(2)