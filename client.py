# coding: utf-8

import socket
boucle = True
nb = 1
host = "129.195.144.122"
port = 5555
while boucle:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, port))
    print ("Connection sur: {}:{}".format(host, port))
    message = ('message no {} '.format(nb)).encode('utf_8')
    my_socket.send(message)
    nb += 1
    close = input('stop? ')
    if close == 'o':
        boucle = False

print ("Close connection")
my_socket.close()
