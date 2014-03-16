#!/usr/bin/python

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, msg:
    print 'Fail to create socket. Error code: '+ str(msg[0])+', Error message :'+msg[1]
    sys.exit();


print 'SOCKET Created'
port=80
host ='www.google.com'

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    print 'hostname could not be resolve.'
    sys.exit()

print 'ip address of '+host+' is '+remote_ip

#use the ip we get to communicate.

s.connect((remote_ip,port))

print 'socket connected to '+host+' on ip '+remote_ip

#send some data use sendall() implement

message = "GET / HTTP/1.1\r\n\r\n"

try:
    s.sendall(message)
except socket.error:
    print'send message fail'
    sys.exit()
print'data have been sent'

#now get the recive data using recv()

reply = s.recv(4096)

print reply
