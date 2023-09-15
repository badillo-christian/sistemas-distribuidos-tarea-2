import socket
import sys

# instancia de socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP y puerto para la conexion donde el server esta escuchando
server_address = ('127.0.0.1', 10001)
# Conexión a la IP y puerto através del socket
sock.connect(server_address)

try:
    #Mensaje a enviar
    mensaje = bytes('¡¡¡HOLA MUNDO!!!', 'utf-8')
    print('enviando mensaje: {!r}'.format(mensaje))
    #Se envia el mensaje
    sock.sendall(mensaje)
    #Se almancena la respuesta del server
    respuesta = sock.recv(128)
    print('Respuesta recibida del server: {!r}'.format(respuesta))

finally:
    #Cerramos el socket
    sock.close()