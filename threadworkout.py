# import threading
# import time
# import socket
# def connect():
#     s=socket.socket()
#     host=socket.gethostname()
#     print(host)
#     port=12341
#     s.bind((host,port))
#     s.listen(5)
#     time.sleep(1)
#     while True:
#         c,addr=s.accept()
#         print("got connection from",addr)
#         a1='''Thank you for connecting,Dont compare the present with the past.
#         Be fully present each moment-be mindful and free your self from  the past.
#         Take the wisdom and love you learned from all past experiences and let the rest go.'''
#         c.send(a1.encode())
#         c.close()
# def connect1():
#     s=socket.socket()
#     host=socket.gethostname()
#     port=12341
#     s.connect((host,port))
#     a=s.recv(1024)
#     print(a.decode()+"I am a client onee")
#     time.sleep(2)
#     s.close()    
# thread1=threading.Thread(target=connect)
# thread2=threading.Thread(target=connect1)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()    



import threading
import time
def pali(d):
    a=int(input("enter the value:"))
    b=a*a
    time.sleep(1)
    while(b>0):
        r=b%10
        d=(d*10)+r
        b=b//1
        print(d)
        print(b)
    if d==b:
        print("it is adam number")
    else:
        print("it is not adam number")
        time.sleep(1)

def fact(sum):
    fact=1
    sum=int(input("enter the number"))
    for i in range(1,sum+1):
      fact=fact*i
      time.sleep(1)
    return fact
print("factorial value",fact(sum)) 
d=1
thread1=threading.Thread(target=lambda:pali(d))
thread2=threading.Thread(target=fact(sum))
thread1.start()
thread2.start()
thread1.join()
thread2.join()    

        