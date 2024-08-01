import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12344
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    a1='''vanakkam thamizha,today is new day.There is no other day like today.It is unique and special.
    It is also an opportunity to begin a new,
    To experience a clean a late,A new beginning-in this every moment.
    Living in the moment is different from living for the moment'''
    c.send(a1.encode())
    c.close()