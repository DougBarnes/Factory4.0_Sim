#!/usr/bin/python

"""factory_sim.py: Runs a simulation of the factory 4.0. """
__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import paho.mqtt.client as mqtt
from datetime import datetime
import time,logging,sys
import json
import os

mqttBroker = "mqtt.eclipseprojects.io"
port = 8883

#import psycopg2
#from psycopg2 import Error

# Flags
message_received_flag = False
factory_running = False
hbw_flag = False
vgr_flag = False
mpo_flag = False
ssc_flag = False
sld_flag = False

# Variables
fc_number = 1000
os_number = 1000

# Dictionaries
hand_shake={
    "msg_type": "message confirmation",
    "msg_confirmation_id": "FC####",
    "msg_type_received": "order",
    "msg_id": "SO####"
}
#hand_shake["msg_confirmation_id"] = "CC1000"

order_status={
    "msg_type": "status",
    "sim_msg_id": "S####",
    "cloud_id": "SO####",
    "disk_color_id": "RED01", 
    "order_complete": "True"
}

status={
    "msg_type": "order status",
    "sim_msg_id": "OS####",
    "cloud_id": "SO####",
    "running": "False", 
    "HBW": "False",
    "VGR": "False", 
    "MPO": "False",
    "SSC": "False", 
    "SLD": "False"
}

inventory={
    "msg_type": "inventory",
    "sim_msg_id": "I####",
    "cloud_id": "PI####",

    "location01": "RED01", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location02": "RED02", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location03": "RED03", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location04": "BLUE01", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location05": "BLUE02", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location06": "BLUE03", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location07": "White01", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location08": "White02", 
    "disk_stored": "True", 
    "pallet_stored": "True",

    "location09": "White03", 
    "disk_stored": "True", 
    "pallet_stored": "True",
}

cancel_status={
    "msg_type": "cancel status",
    "sim_msg_id": "CS####",
    "cloud_id": "CO####",
    "canceled": "False"
}

webcam_status={
    "msg_type": "webcam status",
    "sim_msg_id": "WS####",
    "power": "False",
    "y_turntable": "0",
    "x_turntable": "0"
}

unable_status={
    "msg_type": "unable status",
    "sim_msg_id": "US####",
    "cloud_id": "PI####"
}

def factory_master():
    global factory_running
    global message_received_flag

    ### MQTT Set up ###
    print("CREATING CLIENT")
    client = mqtt.Client("Factory Sim")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("UofICapstone_User")
    client.on_message = on_message

    #print("Factory Check ....")
    while True:
        time.sleep(0.5)
        
        if message_received_flag == True:
            handshake(client, hand_shake)
            factory_running = True
            print("Factory Started ....")
            #update status*** also add a cancel in here somehow
            time.sleep(1)

            print("HBW Start ....")
            hbw_flag = True
            #update status***
            time.sleep(2)
            hbw_flag = False
            print("HBW End ....")

            print("VGR Start ....")
            vgr_flag = True
            #update status***
            time.sleep(2)
            vgr_flag = False
            print("VGR End ....")

            print("MPO Start ....")
            mpo_flag = True
            #update status***
            time.sleep(2)
            mpo_flag = False
            print("MPO End ....")

            print("SLD Start ....")
            sld_flag = True
            #update status***
            time.sleep(2)
            sld_flag = False
            print("SLD End ....")

            message_received_flag = False
            print("Factory Ended ....")
         
def update_status(cloud_id, factory_running, hbw_flag, vgr_flag, mpo_flag, ssc_flag, sld_flag):
    status["cloud_id"] = cloud_id
    status["running"] = factory_running
    status["HBW"] = hbw_flag
    status["VGR"] = vgr_flag
    status["MPO"] = mpo_flag
    status["SSC"] = ssc_flag
    status["SLD"] = sld_flag

def on_message(client, userdata, message):
    global message_received_flag
    recieved_message = str(message.payload.decode("utf-8"))
    print("***")
    #print(recieved_message["msg_type"])
    print("***")
    print("Received message: ", recieved_message)
    message_received_flag = True

def handshake(client, hand_shake):
    client.publish("UofICapstone_Sim", payload=json.dumps(hand_shake))
    print("....SENT HANDSHAKE...")

#MAIN
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    time_now = datetime.now() + timedelta(seconds=2)
    scheduler.add_job(factory_master, 'date', run_date=time_now, id='factory_job')
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
