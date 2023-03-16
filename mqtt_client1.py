import paho.mqtt.client as mqtt
import mysql.connector
from random import randrange, uniform
import time

client = mqtt.Client("client1")
sub = "a"

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "11111111",
        database = "MQTT",
   )

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("Received message: ", msg)
    mycursor = mydb.cursor()
    mycursor.execute('INSERT INTO DATA(TOPIC,PAYLOAD) VALUES ("'+sub+'","'+msg+'b")')
    # mycursor.execute('SELECT * FROM DATA')
    # tables = mycursor.fetchall()
    # print(tables)
    mydb.commit()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect success")
        client.subscribe(sub)
    else:
        print("Connect failed") 



# print("enter user ")
# user = input()
# print("enter password:")
# password = input()
# client.username_pw_set(username=user,password=password)

client.on_connect = on_connect
client.connect("localhost")
client.loop(1)

print("enter sending topic: ")
topic = input()
print("enter sending message: ")
s = input()
while True:
    client.publish(topic=topic, payload=s)
    client.on_message = on_message
    client.loop_start()
    print("Just published: " + s + " to topic: " + topic)
    print("enter sending message: ")
    s = input()

