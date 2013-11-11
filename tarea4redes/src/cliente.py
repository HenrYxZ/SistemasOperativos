'''
Created on 09-11-2013

@author: HernaldoJesus
'''

import socket
import sys

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
        self.s = socket.socket
        self.aknowledge = 0
    def conectar(self):
        '''
        Conexion al servidor por el host y puerto predefinido
        '''
        try:
            self.s.connect((self.host, self.puerto))
        except:
            print "Unable to connect"
            sys.exit()
        print("Connected to remote host " + self.host)
        
    def enviar_imagen(self, image_path):
        
        '''
        Se envia una imagen indicando la direccion de esta
        '''
        file = open(image_path, 'rb')
        img = file.read()
        file.close()
        
        self.s.send(img)
        print("Imagen" + image_path + "enviada")
        aknowledge = self.s.recv(1024)
        
    def cerrar(self):
        self.s.close()
        print(self.aknowledge)

# ----------- MAIN -----------------------------
if __name__ == '__main__':
    if(len(sys.argv) < 2) :
        print 'Usage : python cliente.py hostname'
        sys.exit()

    client = Cliente(sys.argv[1], 52000)
    client.conectar()
    print 'Ingrese el path de la imagen (ej. avatar.jpg)'
    image_path = raw_input()
    client.enviar_imagen(image_path)
    client.cerrar()
    
        