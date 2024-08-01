# from tkinter import *
# from tkinter import ttk,font,messagebox
# import socket
# def connect():
#     s=socket.socket()
#     host=socket.gethostname()
#     port=12341
#     s.connect((host,port))
#     a=s.recv(1024)
#     print(a.decode()+"I am a client one")
#     s.close()  

#     win=Tk()
#     win.attributes('-fullscreen',True)
#     win.geometry("500x500")
#     label_font=font.Font(weight="bold",family="Times New Roman",size=30)
#     e1=Entry(win)
#     e1.place(relx=0.50,rely=0.24,width=150,height=30,command=lambda:connect())
#     e2=Entry(win)
#     e2.place(relx=0.50,rely=0.34,width=150,height=30,command=lambda:connect())
#     e3=Entry(win)
#     e3.place(relx=0.50,rely=0.44,width=150,height=30,command=lambda:connect())
#     e4=Entry(win)
#     e4.place(relx=0.50,rely=0.54,width=150,height=30,command=lambda:connect())
#     e5=Entry(win)
#     e5.place(relx=0.50,rely=0.64,width=150,height=30,command=lambda:connect())
#     b=Button(win,text="server",bg="pink")
#     b.place(relx=0.38,rely=0.25)
#     b1=Button(win,text="server2",bg="pink")
#     b1.place(relx=0.38,rely=0.35)
#     b2=Button(win,text="server3",bg="pink")
#     b2.place(relx=0.38,rely=0.45)
#     b3=Button(win,text="server4",bg="pink")
#     b3.place(relx=0.38,rely=0.55)
#     b4=Button(win,text="server5",bg="pink")
#     b4.place(relx=0.38,rely=0.65)
#     messagebox.showinfo("connection Successfully")
#     win.mainloop()  
# connect()    
    



# from tkinter import*
# from tkinter import ttk,font,messagebox
# import socket
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