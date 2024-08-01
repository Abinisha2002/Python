import socket
a=socket.socket()
host=socket.gethostname()
port=12341
a.connect((host,port))
b=a.recv(1024)
print(b.decode()+" i am a client six")
a.close()