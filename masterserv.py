"""
Jamil Busari
CS50AP
MASTER PROJECT
Period 4
SCHENK
"""

import socket
from multiprocessing import Process

#Server Side

#Function for welcoming users joining
def Welcome_Client(s, clients):
    while True:
        conn, addr = s.accept()
        print("Connection from %s" %(str(addr)))
        message = 'Welcome to the J Server'
        try:
            conn.send(message.encode('ascii'))
            print("Message sent")
            clients.append(addr)
            Process(target=client_messages, args=(conn,clients)).start()
        except OSError as e:
            print(e)

def client_messages(conn, clients):
    
    while True:
        data = conn.recv(1024)

        if (data == "quit"):
            conn.close()
            
        else:   
            print("You got ", repr(data))
            for client in clients:
                print(client)
                conn.send(data)
    
#Main Function
def main():

    #Setting up host and port
    host = 'localhost'
    port = 5000

    #Creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print("Socket Binded and Created")

    clients = []
    
    p = Process(target=Welcome_Client, args=(s,clients))
    p.start()
    p.join()


if __name__ == "__main__":
    main()
