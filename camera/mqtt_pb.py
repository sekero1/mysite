import paho.mqtt.client as paho
from camera import get_img
broker="192.168.0.36"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n", msg)
    pass

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

client1= paho.Client()                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
msg = get_img(3)
ret= client1.publish("sensor/camera1",msg)                   #publish
client1.loop_forever()

