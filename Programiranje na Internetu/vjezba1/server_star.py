import socket
import _thread

def start_server():
    IP = '127.0.0.1'
    PORT = 50001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen()
    return s

def send_message(con):
    poruka = input()
    con.sendall(str.encode(poruka))

def recv_message(connection_list, con):
    message = con.recv(1024)
    broadcasting(connection_list, message, con)

def send_messages(con):
    while True:
        send_message(con)

def recv_messages(conection_list, con):
    while True:
        recv_message(connection_list,con)

def broadcasting(connection_list, message, con):
    for connection in connection_list:
        if (connection != con):
            connection.sendall(message)

s = start_server()
connection_list = []

while True:
    con, adr = s.accept() 
    connection_list.append(con)   
    _thread.start_new_thread(recv_messages,(connection_list, con))
    
    
   