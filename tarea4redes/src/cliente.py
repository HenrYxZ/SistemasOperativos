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
    global host
    global puerto
    global s
    global aknowledge

    def __init__(self, server_address, port):
        '''
        Constructor
        '''
        host = server_address
        puerto = port
        s = socket.socket
    def conectar(self):
        '''
        Conexion al servidor por el host y puerto predefinido
        '''
        try:
            s.connect((host,puerto))
        except:
            print "Unable to connect"
            sys.exit()
        print("Connected to remote host " + host)
        
    def enviar_imagen(self, image_path):
        
        '''
        Se envia una imagen indicando la direccion de esta
        '''
        file = open(image_path, 'rb')
        img = file.read()
        file.close()
        
        s.send(img)
        print("Imagen" + image_path + "enviada")
        aknowledge = s.recv(1024)
        
    def cerrar(self):
        s.close()
        print(aknowledge)

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
    
        