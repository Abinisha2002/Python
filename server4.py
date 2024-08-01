import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12343
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    a1='''Connection successfuly thank you.Settle on an appropriate portion size.Decide what exactly you are craving:
    Something Salty?Sweet?Sour?Hot?Cold?Creamy? '''
    c.send(a1.encode())
    c.close()