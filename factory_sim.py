#!/usr/bin/python

"""factory_sim.py: Runs a simulation of the factory 4.0. """
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

import psycopg2
from psycopg2 import Error

# Flags
message_received_flag = False

# python object (dict)
hand_shake={
    "msg_type": "message confirmation",
    "msg_confirmation_id": "CC####",
    "msg_type_received": "order",
    "msg_id": "SO####"
}

send_order_status={
    "msg_type": "order status",
    "sim_msg_id": "OS####",
    "cloud_id": "SO####",
    "disk_color_id": "RED01", 
    "order_complete": "True"
}

def on_message(client, userdata, message):
    global message_received_flag
    print("Received message: ", str(message.payload.decode("utf-8")))
    message_received_flag = True

'''try:
    #### Connect to an existing database ####
    connection = psycopg2.connect(user="postgres",
                                  password="qwerty",
                                  host="localhost",
                                  database="factorydb")

    #### Create a cursor to perform database operations ####
    cursor = connection.cursor()
'''
### MQTT Set up ###
print("CREATING CLIENT")
client = mqtt.Client("Factory Sim")
client.connect(mqttBroker)

while True:
    client.loop_start()
    client.subscribe("UofICapstone_User")
    client.on_message = on_message

    if message_received_flag == True:
        message_received_flag = False
        print("HERE")
        client.publish("UofICapstone_Sim", payload=json.dumps(send_order_status))

    print("-----Loop-----")
    time.sleep(1)
    #client.loop_end()


    #while not client.message_received_flag:
        #time.sleep(1) #wait for message
    #client.message_received_flag=False
    #if len(messages)==0:
        #print("test failed")
    #else:
        #print("not failed")

#client.disconnect()


'''except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
 '''   
