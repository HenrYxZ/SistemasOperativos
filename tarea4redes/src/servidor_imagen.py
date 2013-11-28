'''
Created on 10-11-2013

@author: HernaldoJesus
'''

import socket

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
        self.client_socket = 0
        self.client_address = 0
        
    def conectar(self):
        self.s.bind((self.host, self.puerto))
        self.s.listen(1)
        print("Servidor " + self.host + " establecido")
        
    def escuchar_cliente(self, conn, addr):
        copy_name = "img" + str(self.counter)
        copied_img = open(copy_name+".jpg", 'wb')
        
        # Mientras no se termine de mandar el mensaje
        while True:
            data = conn.recv(4096)
            copied_img.write(data)
            if not data:
                print("Transmission error")
                break
            if "end" in data:
                print("Transmission finished")
                break
            

        conn.send("Image loaded as " + copy_name)
        conn.close()
    
    def aceptar(self):
        self.client_socket , self.client_address = self.s.accept()
        print("Connected by ", self.client_address)
        self.escuchar_cliente(self.client_socket, self.client_address)
        
    def cerrar(self):
        self.s.close()
# ----------- MAIN -----------------------------
if __name__ == '__main__':
    server = Servidor(socket.gethostname(), 3000)
    server.conectar()
    server.aceptar()
    server.cerrar()