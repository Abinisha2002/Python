import socket
a=socket.socket()
host=socket.gethostname()
port=12345
a.connect((host,port))
b=a.recv(1024)
print(b.decode()+" i am a client seven")
a.close()