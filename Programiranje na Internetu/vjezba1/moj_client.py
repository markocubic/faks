# -*- coding: utf-8 -*-
import socket
import time
import threading
import sys

received_message=""
sending_message=""
my_message=""
send_message = False

def start_server():
    global received_message
    global sending_message
    server=socket.socket()
    host=socket.gethostname()
    port=int(sys.argv[1])

    server.bind((host,port))
    server.listen(3)

    while True:
        c,addr=server.accept()
        received_message=(c.recv(1024)).decode()
        c.close()


def connect_to_server():
    global my_message
    global received_message
    global sending_message
    global send_message
    try:
        host=socket.gethostname()
        port=int(sys.argv[2])
        
        while True:
            time.sleep(2)

            if (sending_message!=received_message and received_message!=my_message):
                print(received_message)
                c = socket.socket() 
                c.connect((host, port))
                c.send(received_message.encode())
                c.close()
                sending_message=received_message

            if (send_message == True):
                c = socket.socket()
                c.connect((host, port))
                c.send(my_message.encode())
                send_message = False
                sending_message = my_message
                c.close()
    except Exception as e:
        connect_to_server()
        
def unos_poruke():
        while True:
                global my_message
                my_message = raw_input()
                global send_message
                send_message = True



threading._start_new_thread(start_server,())
threading._start_new_thread(unos_poruke,())
connect_to_server()
