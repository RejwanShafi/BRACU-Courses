import socket
format='UTF-8'
size=16
port=5050 #server port
hostname=socket.gethostname() 
ip_add=socket.gethostbyname(hostname) #server ip add
socket_add=(ip_add,port) #server

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(socket_add)
def send_msg(message):

    msg_length=len(message)
    msg_length=str(msg_length)
    encoded_msg=msg_length.encode(format)
    encoded_msg+=b" "*(size-len(encoded_msg))
    client_socket.send(encoded_msg)
    client_socket.send(message.encode(format))
    rcv_msg=client_socket.recv(2048).decode(format)
    print(rcv_msg)
loop=True
while loop:

    message=input('please enter a string: ')
    if message=='Disconnect':
        loop=False
    send_msg(message)



