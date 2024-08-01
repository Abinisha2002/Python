import socket
a=socket.socket()
host=socket.gethostname()
ports={12345,12341,12342,12343,12344}
a.connect((host,ports))
b=a.recv(1024)
print(b.decode()+" i am a client two")
for port in ports:
    a.connect((host,ports))
a.close()