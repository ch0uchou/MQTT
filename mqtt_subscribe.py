import paho.mqtt.client as mqtt
import mysql.connector
import time

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
    mycursor.execute('INSERT INTO DATA(PAYLOAD) VALUES ("'+msg+'");')
    # mycursor.execute('SELECT * FROM DATA')
    # tables = mycursor.fetchall()
    # print(tables)
    mydb.commit()
    

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect MQTT Broker success")
        client.subscribe("a")
    else:
        print("Connect MQTT Broker failed") 


client = mqtt.Client("Smartphone")

client.on_connect = on_connect
client.connect("localhost")

client.on_message = on_message
client.loop_forever()


