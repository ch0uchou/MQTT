import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Outside")
client.username_pw_set("123","456")
client.connect("localhost")

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
