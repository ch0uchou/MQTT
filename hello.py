#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import paho.mqtt.client as mqtt
import random
import string
import json


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


class MmtWidget(ttk.Notebook):
    client = mqtt.Client()


    def __init__(self, master=None, **kw):
        super(MmtWidget, self).__init__(master, **kw)
        self.frame5 = ttk.Frame(self)
        self.frame5.configure(height=200, width=200)
        labelframe1 = ttk.Labelframe(self.frame5)
        labelframe1.configure(height=200, text='General', width=200)
        frame8 = ttk.Frame(labelframe1)
        frame8.configure(height=200, width=200)
        self.Clientid = ttk.Label(frame8)
        self.Clientid.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='ClientID')
        self.Clientid.pack(pady=5, side="top")
        self.Host = ttk.Label(frame8)
        self.Host.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Host')
        self.Host.pack(pady=5, side="top")
        self.Port = ttk.Label(frame8)
        self.Port.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Port')
        self.Port.pack(pady=5, side="top")
        self.Username = ttk.Label(frame8)
        self.Username.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Username')
        self.Username.pack(pady=5, side="top")
        self.Password = ttk.Label(frame8)
        self.Password.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Password')
        self.Password.pack(pady=5, side="top")
        frame8.pack(anchor="center", padx=30, side="left")
        frame11 = ttk.Frame(labelframe1)
        frame11.configure(height=200, width=200)
        self.clientIDentry = ttk.Entry(frame11)
        self.client_id = tk.StringVar()
        self.clientIDentry.configure(textvariable=self.client_id)
        self.client_id.set(get_random_string(8))
        self.clientIDentry.pack(pady=1, side="top")
        self.hostentry = ttk.Entry(frame11)
        self.host = tk.StringVar(value='localhost')
        self.hostentry.configure(textvariable=self.host)
        _text_ = 'localhost'
        self.hostentry.delete("0", "end")
        self.hostentry.insert("0", _text_)
        self.hostentry.pack(pady=1, side="top")
        self.portentry = ttk.Entry(frame11)
        self.port = tk.StringVar(value='1883')
        self.portentry.configure(textvariable=self.port)
        _text_ = '1883'
        self.portentry.delete("0", "end")
        self.portentry.insert("0", _text_)
        self.portentry.pack(pady=1, side="top")
        self.userentry = ttk.Entry(frame11)
        self.username = tk.StringVar()
        self.userentry.configure(textvariable=self.username)
        self.userentry.pack(pady=1, side="top")
        self.passentry = ttk.Entry(frame11)
        self.password = tk.StringVar()
        self.passentry.configure(textvariable=self.password)
        self.passentry.pack(pady=1, side="top")
        frame11.pack(anchor="center", padx=30, side="left")
        frame6 = ttk.Frame(labelframe1)
        frame6.configure(height=200, width=200)
        self.button3 = ttk.Button(frame6)
        self.button3.configure(text='random ID', width=7)
        self.button3.pack(side="left")
        self.button3.configure(command=self.randomID)
        frame6.pack(anchor="n", pady=3, side="left")
        labelframe1.pack(fill="both", side="top")
        button1 = ttk.Button(self.frame5)
        self.connectionstatus = tk.StringVar(value='connect')
        button1.configure(text='connect', textvariable=self.connectionstatus)
        button1.pack(anchor="ne", pady=5, side="top")
        button1.configure(command=self.connect)
        button1.bind("<1>", self.callback, add="+")
        labelframe2 = ttk.Labelframe(self.frame5)
        labelframe2.configure(height=200, text='Advanced', width=200)
        frame12 = ttk.Frame(labelframe2)
        frame12.configure(height=200, width=200)
        self.label16 = ttk.Label(frame12)
        self.label16.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Connect Timeout (s)')
        self.label16.pack(pady=5, side="top")
        self.label17 = ttk.Label(frame12)
        self.label17.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Keep Alive (s)')
        self.label17.pack(pady=5, side="top")
        self.label18 = ttk.Label(frame12)
        self.label18.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Clean Session')
        self.label18.pack(pady=5, side="top")
        self.label19 = ttk.Label(frame12)
        self.label19.configure(
            compound="none",
            cursor="based_arrow_down",
            font="TkTextFont",
            text='Auto Reconnect')
        self.label19.pack(pady=5, side="top")
        frame12.pack(anchor="n", padx=30, side="left")
        frame13 = ttk.Frame(labelframe2)
        frame13.configure(height=200, width=200)
        self.timeentry = ttk.Entry(frame13)
        self.connect_timeout = tk.StringVar(value='10')
        self.timeentry.configure(textvariable=self.connect_timeout)
        _text_ = '10'
        self.timeentry.delete("0", "end")
        self.timeentry.insert("0", _text_)
        self.timeentry.pack(pady=1, side="top")
        self.keepaliveentry = ttk.Entry(frame13)
        self.keepalive = tk.StringVar(value='60')
        self.keepaliveentry.configure(textvariable=self.keepalive)
        _text_ = '60'
        self.keepaliveentry.delete("0", "end")
        self.keepaliveentry.insert("0", _text_)
        self.keepaliveentry.pack(pady=1, side="top")
        self.cleansee = ttk.Frame(frame13)
        self.cleansee.configure(height=200, width=200)
        self.radiobutton4 = ttk.Radiobutton(self.cleansee)
        self.clean_session = tk.StringVar(value='1')
        self.radiobutton4.configure(
            text='true',
            value=1,
            variable=self.clean_session)
        self.radiobutton4.pack(side="left", pady=5)
        self.radiobutton5 = ttk.Radiobutton(self.cleansee)
        self.radiobutton5.configure(
            text='false',
            value=0,
            variable=self.clean_session)
        self.radiobutton5.pack(side="right", pady= 5)
        self.cleansee.pack(pady=1, side="top")
        self.autoreconnect = ttk.Frame(frame13)
        self.autoreconnect.configure(height=200, width=200)
        self.radiobutton6 = ttk.Radiobutton(self.autoreconnect)
        self.reconnect_on_failure = tk.StringVar(value='1')
        self.radiobutton6.configure(
            text='true',
            value=1,
            variable=self.reconnect_on_failure)
        self.radiobutton6.pack(side="left", pady=5)
        self.radiobutton7 = ttk.Radiobutton(self.autoreconnect)
        self.radiobutton7.configure(
            text='false',
            value=0,
            variable=self.reconnect_on_failure)
        self.radiobutton7.pack(side="right", pady=5)
        self.autoreconnect.pack(pady=1, side="top")
        frame13.pack(anchor="n", padx=30, side="left")
        labelframe2.pack(expand="true", fill="both", side="top")
        self.frame5.pack(side="top")
        self.add(
            self.frame5,
            compound="left",
            state="normal",
            text='connection',
            underline=1)
        
        
        # ##########publish#############
        
        frame1 = ttk.Frame(self)
        frame1.configure(height=200, width=200)
        notebook1 = ttk.Notebook(frame1)
        notebook1.configure(height=200, width=200)
        frame4 = ttk.Frame(notebook1)
        frame4.configure(height=200, width=200)
        frame5 = ttk.Frame(frame4)
        frame5.configure(height=200, width=200)
        label4 = ttk.Label(frame5)
        label4.configure(text='topic')
        label4.pack(padx=5, side="left")
        self.topicsubentry = ttk.Entry(frame5)
        self.topic = tk.StringVar()
        self.topicsubentry.configure(textvariable=self.topic)
        self.topicsubentry.pack(padx=5, side="left")
        self.button1 = ttk.Button(frame5)
        self.button1.configure(text='send', width=4)
        self.button1.pack(side="left")
        self.button1.configure(command=self.publishsigle)
        combobox2 = ttk.Combobox(frame5)
        self.qos = tk.StringVar()
        combobox2.configure(textvariable=self.qos, values='0 1 2', width=1)
        combobox2.pack(pady=0, side="right")
        label5 = ttk.Label(frame5)
        label5.configure(text='QoS')
        label5.pack(padx=2, side="right")
        self.checkbutton1 = ttk.Checkbutton(frame5)
        self.retain = tk.StringVar()
        self.checkbutton1.configure(
            offvalue=0, onvalue=1, variable=self.retain)
        self.checkbutton1.pack(side="right")
        label6 = ttk.Label(frame5)
        label6.configure(text='Retain')
        label6.pack(padx=2, side="right")
        frame5.pack(fill="x", pady=10, side="top")
        panedwindow2 = ttk.Panedwindow(frame4, orient="horizontal")
        panedwindow2.configure(height=200, width=200)
        labelframe3 = ttk.Labelframe(panedwindow2)
        labelframe3.configure(height=200, text='Payload input', width=200)
        self.payloadsub = tk.Text(labelframe3)
        self.payloadsub.configure(height=10, width=50)
        self.payloadsub.pack(expand="true", fill="both", side="top")
        labelframe3.pack(expand="true", fill="both", side="top")
        panedwindow2.add(labelframe3, weight="1")
        labelframe4 = ttk.Labelframe(panedwindow2)
        labelframe4.configure(height=200, text='Payload status', width=200)
        treeview1 = ttk.Treeview(labelframe4)
        treeview1.configure(selectmode="extended")
        treeview1.pack(expand="true", fill="both", side="top")
        labelframe4.pack(side="top")
        panedwindow2.add(labelframe4, weight="1")
        panedwindow2.pack(expand="true", fill="both", side="top")
        frame4.pack(side="top")
        notebook1.add(frame4, text='Sigle')
        frame6 = ttk.Frame(notebook1)
        frame6.configure(height=200, width=200)
        frame8 = ttk.Frame(frame6)
        frame8.configure(height=200, width=200)
        text5 = tk.Text(frame8)
        text5.configure(height=10, state="disabled", takefocus=False, width=50)
        _text_ = 'message theo dạng\n{\n   "messsage":[\n      {\n\t"topic":"<topic>", \t\n\t"payload":"<payload"", \n\t"qos":<qos>,\n\t"retain":<retain>\n\t}\n   ]\n}'
        text5.configure(state="normal")
        text5.insert("0.0", _text_)
        text5.configure(state="disabled")
        text5.pack(fill="both", side="top")
        frame8.pack(fill="x", pady=10, side="top")
        panedwindow3 = ttk.Panedwindow(frame6, orient="horizontal")
        panedwindow3.configure(height=200, width=200)
        labelframe5 = ttk.Labelframe(panedwindow3)
        labelframe5.configure(height=200, text='Message input', width=200)
        self.multipayloadsub = tk.Text(labelframe5)
        self.multipayloadsub.configure(height=10, width=50)
        self.multipayloadsub.pack(expand="true", fill="both", side="top")
        labelframe5.pack(expand="true", fill="both", side="top")
        panedwindow3.add(labelframe5, weight="1")
        labelframe6 = ttk.Labelframe(panedwindow3)
        labelframe6.configure(height=200, text='Payload status', width=200)
        button3 = ttk.Button(frame6)
        button3.configure(text='send')
        button3.pack(side="bottom")
        button3.configure(command=self.publishmulti)
        treeview2 = ttk.Treeview(labelframe6)
        treeview2.configure(selectmode="extended")
        treeview2.pack(expand="true", fill="both", side="top")
        labelframe6.pack(side="top")
        panedwindow3.add(labelframe6, weight="1")
        panedwindow3.pack(expand="true", fill="both", side="top")
        frame6.pack(side="top")
        notebook1.add(frame6, text='Multi')
        notebook1.pack(expand="true", fill="both", side="top")
        frame1.pack(side="top")
        self.add(frame1, text='publish')
        combobox2.current(0)
        self.retain.set(0)
        ########subscribe#######
        
        frame7 = ttk.Frame(self)
        frame7.configure(height=200, width=200)
        frame7.pack(side="top")
        self.add(frame7, text='subsribe')
        self.configure(height=600, width=600)
        self.pack(expand="true", fill="both", side="top")


    ########connect excute###########

    def disabled_connect(self):
        self.clientIDentry.configure(state="disabled")
        self.hostentry.configure(state="disabled")
        self.portentry.configure(state="disabled")
        self.portentry.configure(state="disabled")
        self.userentry.configure(state="disabled")
        self.passentry.configure(state="disabled")
        self.timeentry.configure(state="disabled")
        self.keepaliveentry.configure(state="disabled")
        self.radiobutton4.configure(state="disabled")
        self.radiobutton5.configure(state="disabled")
        self.radiobutton6.configure(state="disabled")
        self.radiobutton7.configure(state="disabled")
        self.button3.configure(state="disabled")
        self.connectionstatus.set("disconnect")

    def enable_disconnect(self):
        self.clientIDentry.configure(state="normal")
        self.hostentry.configure(state="normal")
        self.portentry.configure(state="normal")
        self.portentry.configure(state="normal")
        self.userentry.configure(state="normal")
        self.passentry.configure(state="normal")
        self.timeentry.configure(state="normal")
        self.keepaliveentry.configure(state="normal")
        self.radiobutton4.configure(state="normal")
        self.radiobutton5.configure(state="normal")
        self.radiobutton6.configure(state="normal")
        self.radiobutton7.configure(state="normal")
        self.button3.configure(state="normal")
        self.connectionstatus.set("connect")
        

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connection successful")
            info = messagebox.showinfo(message="Connection successful")
            self.disabled_connect()
        else:
            print("Connection refused") 
            info = messagebox.showerror(message="Connection refused")

    def on_disconnect(self, client, userdata, rc):
        if rc == 0:
            print("Disconnect successful")
            info = messagebox.showinfo(message="Disconnect successful")
            self.enable_disconnect()

    

    def connect(self):
        if (self.connectionstatus.get() == "connect"):
            self.client = mqtt.Client(
                client_id = self.client_id.get(),
                clean_session = self.clean_session.get(),
                reconnect_on_failure = self.reconnect_on_failure.get()
            )
            self.client.username_pw_set(
                username = self.username.get(),
                password = self.password.get()
            )
            self.client._connect_timeout = int (self.connect_timeout.get())
            self.client.on_connect = self.on_connect
            try:
                self.client.connect(
                    host = self.host.get(),
                    port = int(self.port.get()),
                    keepalive = int(self.keepalive.get()),
                )
                self.client.loop(timeout= int(self.connect_timeout.get()))
            except:
                print("Connection refused") 
                info = messagebox.showerror(message="Connection refused")
        else:
            self.client.on_disconnect = self.on_disconnect
            self.client.disconnect()
            self.client.loop(timeout=1)

    def randomID(self):
        self.client_id.set(get_random_string(8))
        

    ########### publish excute #######

    def publishsigle(self):
        if (self.connectionstatus.get() != "connect"):
            if (self.topic.get() == ""): 
                info = messagebox.showerror(message="Enter topic")
                return
            if (self.payloadsub.get("1.0",'end-1c') == ""):
                info = messagebox.showerror(message="Enter payload")
                return
            if (self.qos.get() == ""):
                info = messagebox.showerror(message="Choose QoS")
                return
            self.client.publish(
                topic= self.topic.get(),
                payload= self.payloadsub.get("1.0",'end-1c'),
                qos = int(self.qos.get()),
                retain = int(self.retain.get())
            )

        else: 
            info = messagebox.showerror(message="Please connect")

    def publishmulti(self):
        if (self.connectionstatus.get() != "connect"):
            if (self.multipayloadsub.get("1.0",'end-1c') == ""):
                info = messagebox.showerror(message="Enter message")
                return
            try:
                payload_data = self.multipayloadsub.get("1.0",'end-1c')
                data = json.loads(payload_data)
                for i in data['message']:
                    print(i) 
                # print(data)
                # self.client.publish(
                #     topic= self.topic.get(),
                #     payload= self.payloadsub.get("1.0",'end-1c'),
                #     qos = int(self.qos.get()),
                #     retain = int(self.retain.get())
                # )
            except:
                pass
        else: 
            info = messagebox.showerror(message="Please connect")
        
    def callback(self, event=None):
        pass    


if __name__ == "__main__":
    root = tk.Tk()
    widget = MmtWidget(root)
    print(get_random_string(6))
    widget.pack(expand=True, fill="both")
    root.mainloop()




