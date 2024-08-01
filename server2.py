import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12341
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    a1='''The client sends a request, And the server returns a response
    dont keep food handy at all times ands within easy reach.'''
    c.send(a1.encode())
    c.close()