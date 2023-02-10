from ipaddress import ip_address
import socket
from tkinter import *
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8000
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptconnections():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        print(client, addr)

def setup():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)
    
    print("\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print('\n')

    acceptconnections()
    
thread = Thread(target = setup)
thread.start()