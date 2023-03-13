import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

print("enter message (X to exit): ")
s = input()
while s != "X":
    client.publish("TEMPERATURE", s)
    print("Just published " + s + " to Topic WELCOME")
    print("enter message (X to exit): ")
    s = input()