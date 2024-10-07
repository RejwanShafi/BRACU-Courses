import socket,threading
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
def multi_thread(client_connection,client_add):

    # client_connection,client_add=server_socket.accept()
    connected=True
    while connected:
        msg_len=client_connection.recv(SIZE).decode(format)
        if msg_len:
            msg=client_connection.recv(int(msg_len)).decode(format)
            if msg=='Disconnect':
                connected=False
                client_connection.send(f'Terminating Connection with {client_add}'.encode(format))
            else: 
                vowel="aeiouAEIOU"
                counter=0
                for i in msg:
                    if i in vowel:
                        counter+=1
                if counter==0:
                    client_connection.send("Not enough vowels".encode("UTF-8"))
                elif counter<=2:
                    client_connection.send("Enough vowels I guess".encode("UTF-8"))
                else:
                    client_connection.send("Too many vowels".encode("UTF-8"))
                    
                print(msg)
                
    client_connection.close()
while True:
    client_connection,client_add=server_socket.accept()
    thread=threading.Thread(target=multi_thread,args=(client_connection,client_add))
    thread.start()