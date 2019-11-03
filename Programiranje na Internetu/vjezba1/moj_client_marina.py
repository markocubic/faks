import socket
import time
import threading
import sys

previous_message=""

def start_server():
        server=socket.socket()
        host=socket.gethostname()
        port=int(sys.argv[1])
        server.bind((host,port))
        server.listen(3)
        return server
        
def connect_to_server():
    time.sleep(2)
    try:
        while True:
            message ="Unesi poruku"
            print("Message je ",message,"a previous je ",previous_message)
            if (message!=previous_message):
                print("u ifu je: ",message)
                host=socket.gethostname()
                port=int(sys.argv[2])
                c = socket.socket()
                c.connect((host, port))
                c.send(message.encode())
                c.close()
    except Exception as e:
        connect_to_server()

server = start_server()
c,addr=server.accept()
while True:        
        previous_message=(c.recv(1024)).decode()

threading._start_new_thread(start_server,())
connect_to_server()

