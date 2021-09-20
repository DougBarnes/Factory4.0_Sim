#!/usr/bin/python

"""factory_sim.py: Runs a simulation of the factory 4.0. """
__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

import paho.mqtt.client as mqtt
import time
import json

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Factory Status")
client.connect(mqttBroker)

import psycopg2
from psycopg2 import Error

#a python object (dict):
send_msg={
    "Factory Status": "Ready",
    "HBW Storage": 9,
    "Light Sensors": "Clear"
}

try:
    #### Connect to an existing database ####
    connection = psycopg2.connect(user="postgres",
                                  password="qwerty",
                                  host="localhost",
                                  database="factorydb")

    #### Create a cursor to perform database operations ####
    cursor = connection.cursor()

    ### Main Loop ###
    while True:
        client.publish("FactoryStatus", payload=json.dumps(send_msg)) #Sends data as json
        print("Just published " + json.dumps(send_msg) + " to Topic FactoryStatus")
        time.sleep(1)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    


#client.publish("TEMPERATURE", randNumber)
#print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
#time.sleep(1)




#def on_message(client, userdata, message):
    #print("Received message: ", str(message.payload.decode("utf-8")))

#mqttBroker = "mqtt.eclipseprojects.io" #Broker alt(broker.hivemq.com)
#client = mqtt.Client("Smartphone")
#client.connect(mqttBroker)

#client.loop_start()
#client.subscribe("TEMPERATURE")
#client.on_message = on_message
#time.sleep(30)
#client.loop_end()