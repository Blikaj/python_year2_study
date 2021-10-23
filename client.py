#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
hostname = (input('Enter hostname: '))
sket = (input('Enter adress: '))
if (len(hostname) == 0):
	hostname = 'localhost'
if (len(sket) == 0):
	sket = "8080"
sock = socket.socket()
sock.connect((hostname, int(sket)))
while True:
	senddat = input('Enter the message: ')
	senddat = senddat.encode('utf-8')
	sock.send(senddat)

	data = sock.recv(1024)
	data = data.decode('utf-8')
	print (data)
	if data == "EXIT":
		break
sock.close()
