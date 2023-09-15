import socket
import sys

# instancia de socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP y puerto para la conexion
server_address = ('127.0.0.1', 10001)
#Bind del sockect a la IP y puerto
sock.bind(server_address)

# Socket en modo de escucha
sock.listen(1)

while True:
    # Socket en modo de escucha
    print('esperando conexión')
    connection, client_address = sock.accept()
    try:
        print('conexión desde:', client_address)
        while True:
            data = connection.recv(128)
            if(len(data) > 0):
                print('Mensaje recibido: {!r}'.format(data))
            if data:
                print("Respondiendo: ACK")
                connection.sendall(b'ACK')
            else:
                break

    finally:
        # Cerramos la conexión
        connection.close()