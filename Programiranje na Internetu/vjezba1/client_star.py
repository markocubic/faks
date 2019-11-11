import socket
import _thread

def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 50001))
    return s

def recv_message(s):
    recieved_msg=(s.recv(1024)).decode()
    print (recieved_msg)

def send_message(s):
    sent_msg = input()
    s.sendall(str.encode(sent_msg))

def send_messages(s):
    while True:
        send_message(s)

def recv_messages(s):
    while True:
        recv_message(s)


s = connect_to_server()

_thread.start_new_thread(recv_messages,(s, ))
send_messages(s)
   