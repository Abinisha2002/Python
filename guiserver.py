from tkinter import *
from tkinter import ttk,font,messagebox
import threading
import socket

def connect():
    s=socket.socket()
    host=socket.gethostname()
    print(host)
    reply=s.recv(1024).decode("utf-8")
    print("client:"+reply)
    Message=input("server:")
    s.send(str(Message).encode("utf-8"))
    s.bind(("0,0,0,0",7777))
    s.listen(5)
    i=0
    while True:
        i+=1
        c,addr=s.accept()
        t=threading(target=connect,args=(c,i))
        t.start()  
def gui():
    win=Tk()
    win.geometry("500x500")
    win.title("server side")  
    button=Button(win,text="send",bg="orange",fg="red",command=lambda:connect())
    button.place(relx=0.25,rely=0.1)
    e1=Entry(win)
    e1.place(relx=0.10,rely=0.1)
    win.mainloop()
gui()     


thread1=threading.Thread(target=lambda:connect())
thread1.start()
thread1.join()



# from tkinter import*
# from tkinter import ttk,font,messagebox
# import socket
# import threading
# root=Tk()
# root.geometry("500x500")
# label_font=font.Font(weight="bold",family="times New Roman",size=20)
# label=Label(root,text="port number:",font=label_font)
# label.place(relx=0.20,rely=0.24)
# e1=Entry(root)
# e1.place(relx=0.40,rely=0.24,width=150,height=50)
# def connect():
#     s=socket.socket()
#     host=socket.gethostname()
#     port=12341
#     s.connect((host,port))
#     a=s.recv(1024)
#     print(a.decode()+"I am a client onee")
#     s.close()
# # label_font=font.Font(weight="bold",family="times New Roman",size=20)
# b1=Button(root,text="connect",bg="green",font=label_font,command=lambda:connect())
# b1.place(relx=0.40,rely=0.34)
# root.mainloop()
# thread1=threading.Thread(target=connect())
# thread1.start()
# thread1.join()  
  
