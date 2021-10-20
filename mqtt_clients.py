#!/usr/bin/python
import paho.mqtt.client as mqtt

mqttBroker = "mqtt.eclipseprojects.io"
port = 8883

message_received_flag = False

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

def mqtt_client():
    ### MQTT Set up ###
    print("CREATING CLIENT")
    client = mqtt.Client("Factory Sim")
    client.connect(mqttBroker)
    #hand_shake["msg_confirmation_id"] = "FC" + str(fc_number)
    client.loop_start()
    client.subscribe("UofICapstone_User")
    client.on_message = on_message

def on_message(client, userdata, message):
    global message_received_flag
    print("Received message: ", str(message.payload.decode("utf-8")))
    message_received_flag = True

def handshake(hand_shake):
    client.publish("UofICapstone_Sim", payload=json.dumps(hand_shake))
    print("....SENT HANDSHAKE...")