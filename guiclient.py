from tkinter import *
from tkinter import ttk,font,messagebox
import threading
import socket
def client():
    while True:
        a=socket.socket()
        a.connect(("127.0.0.1",7777))
        Message=input("client:")
        a.send(str(Message).encode())
        reply=a.recv(1024).decode("utf-8")
        print("server:"+reply)
def gui():
    win=Tk()
    win.geometry("500x500")
    win.title("client side")  
    button=Button(win,text="send",bg="orange",fg="red",command=lambda:client())
    button.place(relx=0.25,rely=0.1)
    e1=Entry(win)
    e1.place(relx=0.10,rely=0.1)
    win.mainloop()
gui()            
thread1=threading.Thread(target=client())
thread1.start()
thread1.join()  
