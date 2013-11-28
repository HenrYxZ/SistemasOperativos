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
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.counter = 0
        # Mapea los nombres de los clientes con sus addresses
        self.name_to_addr = dict()
        # Guarda los sockets de los clientes que tiene
        self.connections = []

    def conectar(self):
        self.s.bind((self.host, self.puerto))
        self.s.listen(5)
        print("Servidor " + self.host + " establecido")
        
    def escuchar_cliente(self, conn, addr):
        # Se genera un log de las conversaciones
        number = self.counter
        copy_name = "log" + str(number)
        log = open(copy_name+".txt", 'w')
        
        # El primer mensaje que manda un cliente
        # es su nickname
        name = conn.recv(1024)
        log.write(name + " log \n")
        self.name_to_addr.update({name: self.counter})
        print(self.name_to_addr)
        
        self.counter += 1
       
        # Mientras estamos en el ciclo
        while True:
            dest = conn.recv(1024)
            data = conn.recv(4096)
            if not dest:
                print ("Transmission error")
                break
            if not data:
                print ("Transmission error")
                break
            if "quit" in data:
                print ("Transmission finished")
                break
            log.write("->" + dest)
            log.write(":\n")
            log.write(data)
            
            if self.name_to_addr.has_key(dest):
                dest_addr = self.name_to_addr[dest]
                dest_conn = self.connections[dest_addr]
                dest_conn.sendall(name)
                dest_conn.sendall(data)
            
        log.close()
        conn.send("Historial guardado como " + copy_name)
        conn.close()
        del self.name_to_addr[name]
        del self.connections[number]
    
    def aceptar(self):
        conn, addr = self.s.accept()
        self.connections.append(conn)
        print("Connected by ", addr)
        t = Thread(target=self.escuchar_cliente, args = (conn, addr,))
        t.start()
        
    def cerrar(self):
        self.s.close()
# ----------- MAIN -----------------------------
if __name__ == '__main__':
    server = Servidor(socket.gethostname(), 3000)
    server.conectar()
    while 1:
        server.aceptar()
    server.cerrar()