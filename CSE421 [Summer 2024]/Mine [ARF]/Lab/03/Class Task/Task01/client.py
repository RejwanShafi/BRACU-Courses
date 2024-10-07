import socket
format='UTF-8'
size=16
port=5050 #server port
hostname=socket.gethostname() 
ip_add=socket.gethostbyname(hostname) #server ip add
socket_add=(ip_add,port) #server
#AF_INET denotes IPV4 and SOCK_stream denotes TCP conenction
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

message=f"From client: My host name is {hostname}.My ip address is {ip_add}"
send_msg(message)
send_msg("Disconnect")


