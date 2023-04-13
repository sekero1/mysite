#publisher 

import paho.mqtt.client as mqtt

mqttc = mqtt.Client("client2")
mqttc.connect("192.168.0.36", 1883)
mqttc.publish("sensor/camera1", " Bingo !!!!!!")
