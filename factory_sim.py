#!/usr/bin/python

"""factory_sim.py: Runs a simulation of the factory 4.0. """
__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

from apscheduler.schedulers.background import BackgroundScheduler
#import paho.mqtt.client as mqtt
import mqtt_clients
from datetime import datetime
import time,logging,sys
import json
import os

#import psycopg2
#from psycopg2 import Error

# Flags
factory_running = False
hbw_flag = False
vgr_flag = False
mpo_flag = False
ssc_flag = False
sld_flag = False

# Variables
fc_number = 1000
os_number = 1000

def factory_start():
    #global FJbo
    global factory_running
    factory_running = True
    print("Factory Started ....")
    scheduler.FJob.Job.pause()
    #FJob.remove()
    
def hbw_running():
    print("HBW Started ....")

def vgr_running():
    print("VGR Started ....")

def mpo_running():
    print("MPO Started ....")

def sld_running():
    print("SLD Started ....")

def ssc_running():
    print("SSC Started ....")

def factory_end():
    #client.publish("UofICapstone_Sim", payload=json.dumps(order_status))
    print("....SENT ORDERSTATUS...")
    print("Factory Ended ....")

#MAIN (Add pause job)
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(factory_start, 'interval', seconds=1, id=factorystart)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()

'''
### MQTT Set up ###
print("CREATING CLIENT")
client = mqtt.Client("Factory Sim")
client.connect(mqttBroker)
hand_shake["msg_confirmation_id"] = "FC" + str(fc_number)
client.loop_start()
client.subscribe("UofICapstone_User")
client.on_message = on_message
'''
'''try:
    #### Connect to an existing database ####
    connection = psycopg2.connect(user="postgres",
                                  password="qwerty",
                                  host="localhost",
                                  database="factorydb")

    #### Create a cursor to perform database operations ####
    cursor = connection.cursor()

### MQTT Set up ###
print("CREATING CLIENT")
client = mqtt.Client("Factory Sim")
client.connect(mqttBroker)
hand_shake["msg_confirmation_id"] = "FC" + str(fc_number)

while True:
    client.loop_start()
    client.subscribe("UofICapstone_User")
    client.on_message = on_message

    if message_received_flag == True:
        message_received_flag = False
        handshake(hand_shake)
'''
        #scheduler.resume(factory_start)
        #time.sleep(3)
        #client.publish("UofICapstone_Sim", payload=json.dumps(order_status))
        #print("....SENT ORDERSTATUS...")

    #print("-----Loop-----")
    #time.sleep(5)
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
