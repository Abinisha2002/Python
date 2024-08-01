import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12342
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    a1='''Establish how important it is for you to eat this food.
    Carry out the really,really,want to this food?If your answer is yes'''
    c.send(a1.encode())
    c.close()