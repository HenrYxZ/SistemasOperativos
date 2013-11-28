'''
Created on 20-11-2013

@author: HernaldoJesus
'''

import socket
import sys
from threading import Thread

class Cliente:
    '''
    Cliente de Socket de Python
    '''

    def __init__(self, server_address, port):
        '''
        Constructor
        '''
        self.host = server_address
        self.puerto = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Escriba su nickname en la sesion ")
        self.name = raw_input()
        self.quit = False
        
    def conectar(self):
        '''
        Conexion al servidor por el host y puerto predefinido
        '''
        self.s.connect((self.host, self.puerto))
        print("Connected to remote host " + self.host)
        
    def enviar_mensajes(self):
        '''
        Se envia un mensaje indicando el nombre del destinatario
        '''
        # Identificarse
        self.s.sendall(self.name)
        
        while True:    
            
            # Escribir destinatario y mensaje
            dest = raw_input("Send to: ")
            self.s.sendall(dest)
            
            msg = raw_input("-> ")
            self.s.sendall(msg)
            
            if msg == "quit":
                self.quit = True
                break

    def escuchar_mensajes(self):
        '''
        Funcion que escucha mensajes provenientes del server
        '''
        while True:
            src = self.s.recv(1024)
            print(src + ":")
            msg = self.s.recv(4096)
            print(msg)
            if self.quit:
                break
        
        self.cerrar()
        
    def cerrar(self):
        print("Conexion terminada")
        self.s.close()
        

# ----------- MAIN -----------------------------
if __name__ == '__main__':
    if(len(sys.argv) < 2) :
        print 'Usage : python cliente_chat.py hostname'
        sys.exit()

    client = Cliente(sys.argv[1], 3000)
    client.conectar()
    escuchador = Thread(target=client.escuchar_mensajes)
    enviador = Thread(target=client.enviar_mensajes)
    escuchador.start()
    enviador.start() 
    
    
        