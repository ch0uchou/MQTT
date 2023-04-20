import paho.mqtt.client as mqtt
# import mysql.connector
from random import randrange, uniform
import time


client = None

# mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "11111111",
#         database = "MQTT",
#    )

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("Received message: ", msg)
    # print('\n',message.topic)
    # mycursor = mydb.cursor()
    # mycursor.execute('INSERT INTO DATA(TOPIC,PAYLOAD) VALUES ("'+str(message.topic)+'","'+str(message.payload.decode("utf-8"))+'b")')
    # mycursor.execute('SELECT * FROM DATA')
    # tables = mycursor.fetchall()
    # print(tables)
    # mydb.commit()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect success")
    else:
        print("Connect failed") 

if __name__ == '__main__':
    client = mqtt.Client()
    print("enter user ")    
    user = input()
    print("enter password:")
    password = input()
    client.username_pw_set(username=user,password=password)

    client.on_connect = on_connect
    client.connect("localhost")
    client.loop(1)
    client.subscribe("a")



# print("enter sending topic: ")
# topic = input()
# print("enter sending message: ")
# s = input()
while True:
    # client.publish(topic=topic, payload=s)
    client.on_message = on_message
    client.loop_start()
    # print("Just published: " + s + " to topic: " + topic)

    # print("enter sending topic: ")
    # topic = input()
    # print("enter sending message: ")
    # s = input()

