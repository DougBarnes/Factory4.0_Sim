import paho.mqtt.client as mqtt
import time
import json

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Factory Status")
client.connect(mqttBroker)

#a python object (dict):
send_msg={
    "Factory Status": "Ready",
    "HBW Storage": 9,
    "Light Sensors": "Clear"
}
#HBW Visual
#|1||2||3|
#|4||5||6|
#|1||2||3|
#HBW_Storage={
#    ""
#}

while True:
    client.publish("FactoryStatus", payload=json.dumps(send_msg)) #Sends data as json
    print("Just published " + json.dumps(send_msg) + " to Topic FactoryStatus")
    time.sleep(1)
    


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