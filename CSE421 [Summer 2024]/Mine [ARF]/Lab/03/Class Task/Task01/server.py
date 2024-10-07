import socket
SIZE=16
format="UTF-8"
port=5050 #server port
hostname=socket.gethostname() 
ip_add=socket.gethostbyname(hostname) #server ip add
socket_add=(ip_add,port)
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server_socket.bind(socket_add)
server_socket.listen()
print('Server is listening')
while True:

    client_connection,client_add=server_socket.accept()
    connected=True
    while connected:
        msg_len=client_connection.recv(SIZE).decode(format)
        if msg_len:
            msg=client_connection.recv(int(msg_len)).decode(format)
            if msg=='Disconnect':
                connected=False
                client_connection.send(f'Terminating Connection with {client_add}'.encode(format))
            else: 
                print(msg)
                client_connection.send('Welcome to the server. Nice to meet you client'.encode(format))
    client_connection.close()