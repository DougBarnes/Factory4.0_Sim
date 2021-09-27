#!/usr/bin/python

"""factory_pub_sub.py interacts with the factory simulator 
    acting as both a publisher and subscrber """
__author__      = "Doug Barnes"
__version__     = "1.0.0"
__maintainer__  = "Doug Barnes"
__email__       = "barn1855@vandals.uidaho.edu"
__status__      = "Production"

import paho.mqtt.client as mqtt
import time
import json

mqttBroker = "mqtt.eclipseprojects.io"

send_order={
    "msg_type": "order",
    "cloud_msg_id": "SO####",
    "x": "1",
    "y": "1"
}

client = mqtt.Client("User Side")
client.connect(mqttBroker)

client.publish("FactoryStatus", payload=json.dumps(send_order))
print("Just published " + json.dumps(send_order) + " to Topic FactoryStatus")
