import socket
import re
import unicodedata

link_list = []

def scrap(host, page, s):
    global link_list
    temp = []
    
    if (len(link_list)>=20):
        return

    source = get_source(host, page, s)
    temp = get_links(source)

    if page not in link_list:
        link_list.append(page)
        
    if len(temp)==0:
        return

    for link in temp:
        scrap(host, link, s)

def connect_to_server(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    return s

def get_source(host, page, s):
    
    CRLF = '\r\n'
    request = 'GET /' + page +' HTTP/1.1'
    request += CRLF
    request += 'Host: ' + host + CRLF
    request += CRLF
    
    s.sendall(str.encode(request, 'cp852'))
    return s.recv(100000).decode()

def get_links(source):
    link_list = []
    beg = 0
    while True:
        beg_link = source.find('href="', beg)
        if beg_link == -1:
            return link_list
        end_link = source.find('"', beg_link + 6)
        link = source[beg_link + 6:end_link]
        beg = end_link + 1
        
        if link not in link_list:
            if 'http' not in link:
                if (link[0] == '/') and (link[0] == '#'):
                    link_list.append(link[1:])
                else:
                    link_list.append(link)
            
host="www.watchthatpage.com"

s = connect_to_server(host, 80)

scrap(host, "", s)

print(link_list)
print(len(link_list))


