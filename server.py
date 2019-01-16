# coding: utf-8

import socket
from threading import Thread

class serveur(Thread):

    def __init__(self, ip, port, client_socket):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.client_socket = client_socket
        print('nouveau thread pour {}:{}'.format(self.ip, self.port))

    def run(self):
        print("Connexion de{}:{}}" % (self.ip, self.port))
        reponse = client.recv(255)
        if reponse != "":
                print (reponse)
        client.close()
        socket.close()


host = "129.195.144.122"
port = 5555
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((host, port))
while True:
        my_socket.listen(5)
        print('en écoute...')
        client, adresse = my_socket.accept()
        ip, port = adresse
        print('info: port={} ip={}'.format(port, ip))
        reponse = client.recv(1024)
        if reponse != "b'stop'":
                print (str(reponse))
client.close()
my_socket.close()
        #new_thread = serveur(ip, port, client)
        #new_thread.start()
