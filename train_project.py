from tkinter import *
from tkinter import ttk,font,messagebox
from PIL import ImageTk, Image
import requests
def get_live_train_status(train_no,win):
    win.destroy()
    win=Tk()    
    win.geometry("500x500")
    base_url="https://rappid.in/apis/train.php?train_no={}".format(train_no)
    response=requests.get(base_url)
    train_status=response.json()
    Label(win,text="******************************************************************").pack()
    Label (win,text="\t\t train name:"+train_status["train_name"]).pack()
    Label(win,text="*****************************************************************").pack()
    for station_info in train_status ["data"]: 
        if station_info ["is_current_station"]:
             Label(win,text="now station \t\t\t\t:"+station_info["station_name"]).pack()
             Label(win,text="distance from the starting\t:"+station_info["distance"]).pack()
             Label(win,text="timing \t\t\t\t\t\t:"+station_info["timing"]).pack()
             Label(win,text="delay \t\t\t\t\t\t:"+station_info["delay"]).pack()
             Label(win,text="platform no \t\t\t\t\t\t:"+station_info["platform"]).pack()
             Label(win,text="halt timing \t\t\t\t\t\t:"+station_info["halt"]).pack()
        else:
             Label(win,text=station_info["station_name"]).pack()
             Label(win,text="*************************************************************").pack()
             Label(win,text="\t\t message\t\t:"+train_status["message"]).pack()
             Label(win,text="\t\t message updated:"+train_status["updated_time"]).pack()
             Label(win,text="************************************************************").pack()    

def home():
    win=Tk()
    win.geometry("500x500")
    win.attributes('-fullscreen',True)
    frame=Frame(win,width=1500,height=50,bg="blue")
    frame.pack()
    f=Frame(win,width=1500,height=60,bg="blue")
    label_font=font.Font(weight="bold",family="Times New Roman",size=30)
    f=Label(win,text="METRO RAILWAY",font=label_font,bg="blue",fg="white")
    f.place(relx=0.4,rely=0.0)
    f1=Frame(win,width=1000,height=50,bg="green")
    f1.place(relx=0.35,rely=0.3)
    img=ImageTk.PhotoImage(Image.open("metros.jpg"))
    l=Label(f1,image=img)
    l.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    a=Label(win,text="train no",bg="purple",fg="white",font=label_font)
    a.place(relx=0.40,rely=0.8)
    b3=Button(win,text="Enter",bg="purple",fg="white",font=label_font,command=lambda:get_live_train_status(e1.get(),win))
    b3.place(relx=0.45,rely=0.9)
    label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    e1=Entry(win)
    e1.place(relx=0.50,rely=0.80,width=150,height=35)
    win.mainloop()
home()


