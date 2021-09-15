import paho.mqtt.client as mqtt
import time
import json

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Factory Status")
client.connect(mqttBroker)



#client.publish("TEMPERATURE", randNumber)
#print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
#time.sleep(1)