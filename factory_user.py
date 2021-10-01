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

choice = ''

# python object (dict):
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

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    #message_received_flag = True

### MQTT Set up ###
print("CREATING CLIENT")
client = mqtt.Client("Factory User")
client.connect(mqttBroker)

while choice != 'q':
    client.loop_start()
    client.subscribe("UofICapstone_Sim")
    client.on_message = on_message

    choice = input("Waiting for input: ")

    if choice == '1':
        client.publish("UofICapstone_User", payload=json.dumps(send_order))
        print("Just published " + str(send_order))
    elif choice == '2':
        print("Nothing yet.....")
    elif choice == 'q':
        print("Exiting.....")

    time.sleep(2)