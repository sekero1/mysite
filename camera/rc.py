import paho.mqtt.client as mqtt  #import the client1
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_message(client, userdata, message):
    print("received message =",str(message.payload.decode("utf-8")))


mqtt.Client.connected_flag=False #create flag in class
broker="192.168.0.36"

client = mqtt.Client()             #create new instance 
client.on_connect=on_connect  #bind call back function
 # client.loop_start()
print("Connecting to broker ",broker)
client.connect(broker)      #connect to broker
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)

print("Subscribing to topic","camera1")
client.subscribe("camera1", hostname=broker)
print("in Main Loop")
client.loop()  #check for messages
time.sleep(3000)

# client.loop_stop()    #Stop loop 

