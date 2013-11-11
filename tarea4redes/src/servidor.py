'''
Created on 10-11-2013

@author: HernaldoJesus
'''

import socket
from threading import Thread

class Servidor:
    '''
    Servidor de Socket de Python
    '''
   
    def __init__(self, server_address, port):
        '''
        Constructor
        '''
        self.host = server_address
        self.puerto = port
        self.s = socket.socket()
        self.counter = 1
        self.client_sockets = []
        self.client_address = []
        
    def conectar(self):
        self.s.bind((self.host, self.puerto))
        self.s.listen(5)
        
    def escuchar_cliente(self, conn, addr):
        copy_name = "img" + str(self.counter)
        copied_img = open(copy_name+".jpg", 'wb')
        self.counter += 1
        
        # Mientras no se termine de mandar el mensaje
        while 1:
            data = conn.recv(1024)
            copied_img.write(data)
            if not data:
                self.client_sockets.remove(conn)
                self.client_addresses.remove(addr)
                break;
        conn.send("Image loaded as " + copy_name)
        conn.close()
    
    def aceptar(self):
        conn, addr = self.s.accept()
        print("Connected by ", addr)
        self.client_sockets.append(conn)
        self.client_addresses.append(addr)
        t = Thread(target="escuchar_cliente", args=(conn,addr))
        
    def cerrar(self):
        self.s.close()
# ----------- MAIN -----------------------------
if __name__ == '__main__':
    server = Servidor(socket.gethostname(), 52000)
    server.conectar()
    while 1:
        server.aceptar()
    server.cerrar()