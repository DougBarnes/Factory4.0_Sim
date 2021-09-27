#!/usr/bin/python

#http://www.steves-internet-guide.com/mqttv5-request-response/
"""factory_sim.py: Runs a simulation of the factory 4.0. """
__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes 
import time,logging,sys
import json

mqttv=mqtt.MQTTv5
messages=[]
mqttBroker = "mqtt.eclipseprojects.io"
port = 8883

import psycopg2
from psycopg2 import Error

#a python object (dict):
send_order_status={
    "msg_type": "order status",
    "sim_msg_id": "OS####",
    "cloud_id": "SO####",
    "disk_color_id": "RED01", 
    "order_complete": "True"
}

def on_publish(client, userdata, mid):
    print("published")

def on_connect(client, userdata, flags, reasonCode,properties=None):
    print('Connected ',flags)
    print('Connected properties',properties)
    print('Connected ',reasonCode)

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    time.sleep(2)

def on_disconnect(client, userdata, rc,properties):
    print('Received Disconnect ',rc)

def on_subscribe(client, userdata, mid, granted_qos,properties=None):
    print('SUBSCRIBED')

def on_unsubscribe(client, userdata, mid, properties, reasonCodes):
    print('UNSUBSCRIBED') 

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
print("creating client")
client = mqtt.Client("Factory Sim", protocol=mqttv)

client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_publish = on_publish

properties = None
client.connect(mqttBroker, port, properties=properties)
client.loop_start()

client.subscribe("FactoryStatus")
time.sleep(2)

client.message_received_flag=False
print("Publish response topic")
properties=Properties(PacketTypes.PUBLISH)
properties.ResponseTopic='FactoryStatus'
print("Starting Factory client")

while True:
    client.publish("FactoryStatus", payload=json.dumps(send_order_status))

    while not client.message_received_flag:
        time.sleep(1) #wait for message
    client.message_received_flag=False
    if len(messages)==0:
        print("test failed")
    else:
        print("not failed")

    time.sleep(5)

client.disconnect()


'''except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
 '''   