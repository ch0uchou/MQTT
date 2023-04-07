import tkinter as tk
from tkinter import ttk
# import mqtt_client
# import paho.mqtt.client as mqtt


window = tk.Tk()
window.title("MMT_MQTT")
# window.resizable(width=False,height=False)
window.geometry('1500x1500')

# Frame1: broker, user, general
Frame1 = tk.Frame(window,bd=0)
# Frame1.pack()

## broker
broker = tk.LabelFrame(Frame1,text="MQTT Broker Setting",bd=2)
broker.pack(fill='x')

_host = tk.StringVar()
hostframe = tk.Frame(broker)
hostframe.pack(side='top',fill='both')
host = tk.Label(hostframe,text="Broker Host:",width=15)
host.pack(side='left')
entryhost = tk.Entry(hostframe,textvariable=_host)
entryhost.pack(side='left')

_port = tk.StringVar()
portframe = tk.Frame(broker)
portframe.pack(side='top',fill='both')
port = tk.Label(portframe,text='Broker Port:',width=15)
port.pack(side='left')
entryport = tk.Entry(portframe,textvariable=_port)
entryport.pack(side='left')

_clientid = tk.StringVar()
clientidframe = tk.Frame(broker)
clientidframe.pack(side='top',fill='both')
clientid = tk.Label(clientidframe,text='Client ID:',width=15)
clientid.pack(side='left')
clientidentry = tk.Entry(clientidframe,textvariable=_clientid)
clientidentry.pack(side='left')

## user
userinfo = tk.LabelFrame(Frame1,text="User Information",bd=2)
userinfo.pack(fill='both')

_user = tk.StringVar()
userframe = tk.Frame(userinfo)
userframe.pack(side='top',fill='both')
user = tk.Label(userframe,text='User Name:',width=15)
user.pack(side='left')
userentry = tk.Entry(userframe,textvariable=_user)
userentry.pack(side='left')

_psw = tk.StringVar()
pswframe = tk.Frame(userinfo)
pswframe.pack(side='top',fill='both')
psw = tk.Label(pswframe,text='Password:',width=15)
psw.pack(side='left')
pswentry = tk.Entry(pswframe, textvariable=_psw)
pswentry.pack(side='left')

##general
general = tk.LabelFrame(Frame1,text="General",bd=2)
general.pack(fill='both')

_ConnectTimeout = tk.StringVar()
ConnectTimeoutframe = tk.Frame(general)
ConnectTimeoutframe.pack(side='top',fill='both')
ConnectionTimeout = tk.Label(ConnectTimeoutframe,text='Connection Timeout:',width=15)
ConnectionTimeout.pack(side='left')
ConnectionTimeoutentry = tk.Entry(ConnectTimeoutframe,textvariable=_ConnectTimeout)
ConnectionTimeoutentry.pack(side='left')

_KeepAliveInterval = tk.StringVar()
KeepAliveIntervalframe = tk.Frame(general)
KeepAliveIntervalframe.pack(side='top',fill='both')
KeepAliveInterval = tk.Label(KeepAliveIntervalframe,text='Keep Alive Interval:',width=15)
KeepAliveInterval.pack(side='left')
KeepAliveIntervalentry = tk.Entry(KeepAliveIntervalframe,textvariable=_KeepAliveInterval)
KeepAliveIntervalentry.pack(side='left')

CleanSessionCheckVar = tk.IntVar()
CleanSessionframe = tk.Frame(general)
CleanSessionframe.pack(side='top',fill='both')
CleanSession = tk.Label(CleanSessionframe,text='Clean Session:',width=15)
CleanSession.pack(side='left')
CleanSessionCheck = tk.Checkbutton(CleanSessionframe,variable=CleanSessionCheckVar,onvalue=1,offvalue=0)
CleanSessionCheck.pack(side='left')

# AutoReconnectframe = tk.Frame(general)
# AutoReconnectframe.pack(side='top',fill='both')
# AutoReconnect = tk.Label(AutoReconnectframe,text='Auto Reconnect:',width=15)
# AutoReconnect.pack(side='left')
# AutoReconnectCheckVar = tk.IntVar()
# AutoReconnectCheck = tk.Checkbutton(AutoReconnectframe,variable=AutoReconnectCheckVar,onvalue=1,offvalue=0)
# AutoReconnectCheck.pack(side='left')

DefaultCheckVar = tk.IntVar()
Defaultframe = tk.Frame(general)
Defaultframe.pack(side='top',fill='both')
Default = tk.Label(Defaultframe,text='Default:',width=15)
Default.pack(side='left')
DefaultCheck = tk.Checkbutton(Defaultframe,variable=DefaultCheckVar,onvalue=1,offvalue=0)
DefaultCheck.pack(side='left')

# Connect button
Connectframe = tk.Frame(Frame1,width=15)
Connectframe.pack(side='top',fill='both')
ConnectButton = tk.Button(Connectframe, text='Connect')
ConnectButton.pack(side='right')
DisConnectButton = tk.Button(Connectframe, text='Disconnect')
DisConnectButton.pack(side='right')

## Status
status = tk.Message(Connectframe,text="connected",bg='green',width=100)
status.pack(side='left',fill='both')
status = tk.Message(Connectframe,text="disconnected",bg='red',width=100)
status.pack(side='left',fill='both')


# Frame2: publish
Frame2 = tk.Frame(window)
Frame2.grid(column=1,row=1)

# publish

publish = tk.Label(Frame2,text="Publish")
publish.pack(side='top')

dk = tk.Frame(Frame2)
dk.pack(side='top')
topicpub = tk.LabelFrame(dk,text="Topic",border=0)
topicpub.pack(side='left')
_topicpubentry = tk.StringVar()
topicpubentry = tk.Entry(topicpub,textvariable=_topicpubentry,width=50)
topicpubentry.pack()

qos = tk.LabelFrame(dk,text="QoS",border=0)
qos.pack(side='left')
_qos = tk.StringVar()
qoschoosen = ttk.Combobox(qos,width=5,textvariable=_qos)
qoschoosen['values'] = ('0','1','2')
qoschoosen.pack()

retain = tk.LabelFrame(dk,text="Retain",border=0)
retain.pack(side='left')
_retain = tk.IntVar()
retaincheck = tk.Checkbutton(retain,variable=retain,onvalue=1,offvalue=0)
retaincheck.pack()

message = tk.LabelFrame(Frame2,text="Message",border=0)
message.pack(side='top')
_message = tk.StringVar()
input = tk.Text(message)
input.pack()

publish = tk.Button(Frame2,text="publish")
publish.pack()


# Frame3: subscribe
Frame3 = tk.Frame(window)
Frame3.grid(column=2,row=1)

topicsub = tk.LabelFrame(Frame3,text="Topic",border=0)
topicsub.pack()
_topicsubentry = tk.StringVar()
topicsubentry = tk.Entry(topicsub,textvariable=_topicsubentry,width=50)
topicsubentry.pack()

window.mainloop()
