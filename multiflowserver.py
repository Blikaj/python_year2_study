#!/usr/bin/env python

import socket, threading

class ClientThread(threading.Thread):

    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("[+] New thread started for "+ip+":"+str(port)


    def run(self):    
        print ("Connection from : "+ip+":"+str(port)

        clientsock.send("\nWelcome to the server\n\n")

        data = "emptydat"

        while len(data):
            data = clientsock.recv(1024)
            print "Client sent : "+data
            clientsock.send("You sent me : "+data)

        print ("Client disconnected...")

host = "0.0.0.0"
port = 8080

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print ("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
