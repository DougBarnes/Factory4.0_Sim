import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io" #Broker alt(broker.hivemq.com)
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("FactoryStatus")
client.on_message = on_message
time.sleep(30)
client.loop_end()