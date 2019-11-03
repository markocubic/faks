import socket
import time
import sys

previous_message=""

def start_server():

    server=socket.socket()
    host=socket.gethostname()
    port=40101 #12345

    server.bind((host,port))
    server.listen(3)   #kod profe je prazno
    print("Started listening:")

   #print("Got connection from ",addr[0])

    while True:
        c,addr=server.accept()
        data=(c.recv(1024)).decode()
        print(data)
        if data==previous_message:
            print("Kraj")
            c.close()
start_server()
