
from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
import pymysql as mysql
def customerregister(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    top.configure(bg="white")

    frame2=Frame(top,height=1500,width=1500,bg="chocolate1")
    img=ImageTk.PhotoImage(Image.open("us.jpg"))
    l=Label(frame2,image=img) 
    l.place(relx=0.0,rely=0.1)

    f=Frame(top,width=1500,height=60,bg="chocolate1")
    ttf=font.Font(weight="bold",family="Arial Black",size=35)
    a=Label(top,text="CUSTOMER REGISTRATION",font=ttf,bg="chocolate1",fg="purple")
    a.place(relx=0.3,rely=0.00)

    ttf=font.Font(weight="bold",family="Arial Black",size=15)
    a=Label(top,text="UniqueID",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.2)
    a4=Entry(top)
    a4.place(relx=0.50,rely=0.200,width=150,height=30)

    b=Label(top,text=" PassengerName",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.3)
    b4=Entry(top)
    b4.place(relx=0.50,rely=0.3,width=150,height=30)

    c=Label(top,text="Gender",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.4)
    c4=Entry(top)
    c4.place(relx=0.50,rely=0.4,width=150,height=30)

    d=Label(top,text="Phone",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.5)
    d4=Entry(top)
    d4.place(relx=0.50,rely=0.5,width=150,height=30)

    e=Label(top,text="Address",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.6)
    e4=Entry(top)
    e4.place(relx=0.50,rely=0.6,width=150,height=30)

    f=Label(top,text="Email",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.7)
    f4=Entry(top)
    f4.place(relx=0.50,rely=0.7,width=150,height=30)
    
    g=Label(top,text="Aadharcard",font=ttf,bg="violet",fg="white").place(relx=0.354,rely=0.8)
    g4=Entry(top)
    g4.place(relx=0.50,rely=0.8,width=150,height=30)


    def insert():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="bank38")
        cursor=connection.cursor()
        s="insert into k1 (UniqueID, PassengerName,Gender,Phone,Address,Email,Aadharcard)values(%s,%s,%s,%s,%s,%s,%s)"
        t=(a4.get(),b4.get(),c4.get(),d4.get(),e4.get(),f4.get(),g4.get())
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo("registration","Insert Successfully")
    def update():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="bank34")
        cursor=connection.cursor()
        sql= "update k1 set PassengerName='"+str(b4.get())+"',Gender='"+str(c4.get())+"',Phone='"+str(d4.get())+"',Address='"+str(e4.get())+"',Email='"+str(f4.get())+"',Aadharcard='"+str(g4.get())+"' where UniqueID='"+str(a4.get())+"'"
        cursor.execute(sql)
        connection.commit()  
        messagebox.showinfo("registration","update successfully") 
    def delete():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="bank34")
        cursor=connection.cursor()
        sql="DELETE From k1 WHERE UniqueID='"+a4.get()+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("registration","delete successfully")


    a=Button(top,text="Insert",font=ttf,bg="green",fg="white",command=lambda:insert())   
    a.place(relx=0.7,rely=0.3) 
    b=Button(top,text="Update",font=ttf,bg="green",fg="white",command=lambda:update())
    b.place(relx=0.7,rely=0.4)
    c=Button(top,text="Delete",font=ttf,bg="green",fg="white",command=lambda:delete())
    c.place(relx=0.7,rely=0.5)       
    b3=Button(top,text="Submit",font=ttf,bg="sandybrown",fg="blue")
    b3.place(relx=0.450,rely=0.9)
    frame2.pack()
    top.mainloop(top)
   



def customerlogin(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    top.configure(bg="sandybrown")

    frame2=Frame(top,height=1500,width=1500)
    img=ImageTk.PhotoImage(Image.open("secu.jpg"))
    l=Label(frame2,image=img) 
    l.place(relx=0.0,rely=0.0)

    frame=Frame(top,width=1500,height=79,bg="indianred1").place(relx=0.0,rely=0.0)
    ttf=font.Font(weight="bold",family="Algerian",size=40)
    a=Label(top,text="CUSTOMER LOGIN",font=ttf,bg="indianred4",fg="white")
    a.place(relx=0.350,rely=0.00)
    frame2.pack()

    ttf=font.Font(weight="bold",family="Blackadder ITC",size=25)
    a1=Label(top,text="Username",font=ttf,bg="purple",fg="white").place(relx=0.650,rely=0.7)
    a4=Entry(top)
    a4.place(relx=0.8,rely=0.7,width=158,height=45)

    b=Label(top,text="Password",font=ttf,bg="purple",fg="white").place(relx=0.650,rely=0.8)
    b4=Entry(top)
    b4.place(relx=0.8,rely=0.8,width=158,height=45)

    n=Entry(top,show="*")
    n.place(relx=0.8,rely=0.8, width=158, height=45)
    
    def data(top):
            m1=a4.get()
            n1=n.get()
            f=open("file.txt","r")
            time=f.read()
            lines=time.split("\n")
            for line in lines:
                info=line.split()
                if info[0]==m1 and info[1]==n1:
                    print("login")
                    messagebox.showinfo("hello","Login successfully")
                    next(top)
                    break
                else:
                    print("invaild")
                    messagebox.showerror("hello","Invaild password")
                    break
          

    c=Button(top,text="Login",font=ttf,bg="sandybrown",fg="blue",command=lambda:data(top))
    c.place(relx=0.750,rely=0.9) 

    ttf=font.Font(weight="bold",family="Algerian",size=40)
    a=Label(top,text="CUSTOMER LOGIN",font=ttf,bg="indianred4",fg="white")
    a.place(relx=0.350,rely=0.00)
    top.mainloop(top)

def next(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    frame1=Frame(top,width=1500,height=77,bg="indianred1").place(relx=0.0,rely=0.0)
    ttf=font.Font(weight="bold",family="Algerian",size=40)
    a=Label(top,text="Royal Bus booking",font=ttf,bg="indianred1",fg="white")
    a.place(relx=0.350,rely=0.0)

    img=ImageTk.PhotoImage(Image.open("busticket2.jpg"))
    l=Label(frame1,image=img) 
    l.place(relx=0.0,rely=0.1)
    img1=ImageTk.PhotoImage(Image.open("offer1.jpg"))
    l1=Label(frame1,image=img1) 
    l1.place(relx=0.0,rely=0.666)

    ttf=font.Font(weight="bold",family="Blackadder ITC",size=15)
    course=ttk.Combobox(top,values=["Chennai","coimbator","thanjavur","mayiladuthurai","kumbakonam"])
    course.place(relx=0.07,rely=0.2,width=150,height=30)
    course.set("select your source")
    v=Label(top,text="From",font=ttf,bg="sandybrown",fg="black")
    v.place(relx=0.01,rely=0.2)
    u=Label(top,text="To",font=ttf,bg="sandybrown",fg="black")
    u.place(relx=0.2,rely=0.2)
    course1=ttk.Combobox(top,values=["Salem","Erode","Trichy","Viluppuram","Theni"])
    course1.place(relx=0.250,rely=0.2,width=150,height=30)
    course1.set("select your Destination")
    w=Label(top,text="Date",font=ttf,bg="sandybrown",fg="black")
    w.place(relx=0.4,rely=0.2)
    w1=Entry(top)
    w1.place(relx=0.470,rely=0.2,width=150,height=30)
    c=Button(top,text="Search",font=ttf,bg="orange",fg="black",command=lambda:busname(top))
    c.place(relx=0.250,rely=0.3)
    ttf=font.Font(weight="bold",family="Algerian",size=15)
    a1=Label(top,text="*Online Booking Available",font=ttf,fg="black",bg="white")
    a1.place(relx=0.3,rely=0.7)
    a2=Label(top,text="*Safe&Secure",font=ttf,fg="black",bg="white")
    a2.place(relx=0.3,rely=0.750)
    a3=Label(top,text="*Best Bus Service & Security",font=ttf,fg="black",bg="white")
    a3.place(relx=0.3,rely=0.8)
    a4=Label(top,text="*Ac/None Ac & sleeper service",font=ttf,fg="black",bg="white")
    a4.place(relx=0.3,rely=0.850)
    a5=Label(top,text="*All Facilities&Time when you need",font=ttf,fg="black",bg="white")
    a5.place(relx=0.3,rely=0.9)
    img2=ImageTk.PhotoImage(Image.open("busroute.jpg"))
    l2=Label(frame1,image=img2) 
    l2.place(relx=0.670,rely=0.666)
    b5=Label(top,text="***Routes Directory***",font=ttf,fg="black",bg="white")
    b5.place(relx=0.7,rely=0.7)
    b1=Label(top,text="BANGALORE - RAMESWARAM ",font=ttf,fg="black",bg="white")
    b1.place(relx=0.7,rely=0.8)
    b2=Label(top,text="KODAIKANAL - CHENNAI",font=ttf,fg="black",bg="white")
    b2.place(relx=0.7,rely=0.850)
    b3=Label(top,text="MUMBAI - PUNE",font=ttf,fg="black",bg="white")
    b3.place(relx=0.7,rely=0.900)
    b4=Label(top,text="HYDERABAD - COIMBATORE",font=ttf,fg="black",bg="white")
    b4.place(relx=0.7,rely=0.950)
    frame1.pack()
    top.mainloop(top)




def busname(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    top.configure(bg="skyblue")
  
    frame=Frame(top,width=1500,height=77,bg="indianred1").place(relx=0.0,rely=0.0)
    ttf=font.Font(weight="bold",family="Algerian",size=40)
    a=Label(top,text="Royal Bus booking",font=ttf,bg="indianred1",fg="white")
    a.place(relx=0.350,rely=0.0)

    img=ImageTk.PhotoImage(Image.open("visual.jpg"))
    l=Label(frame,image=img) 
    l.place(relx=0.680,rely=0.2)
   
    img4=ImageTk.PhotoImage(Image.open("decker.jpg"))
    l4=Label(frame,image=img4) 
    l4.place(relx=0.680,rely=0.4)
  
    img1=ImageTk.PhotoImage(Image.open("bus26.jpg"))
    l1=Label(frame,image=img1) 
    l1.place(relx=0.680,rely=0.6)
  
    img2=ImageTk.PhotoImage(Image.open("busbooking1.jpg"))
    l2=Label(frame,image=img2) 
    l2.place(relx=0.0,rely=0.620)

    img3=ImageTk.PhotoImage(Image.open("tq.png"))
    l3=Label(frame,image=img3) 
    l3.place(relx=0.0,rely=0.8)

    frame2=Frame(top,width=200,height=400,bg="pink")
    frame2.place(relx=0.0,rely=0.1)
    ttf=font.Font(weight="bold",family="Algerian",size=15)
    v=Label(top,text="Vehicle Type",font=ttf,bg="white",fg="black")
    v.place(relx=0.0,rely=0.1)
    var1=IntVar()
    Checkbutton(top,text="Classic",variable=var1).place(relx=0.0,rely=0.150)
    var2=IntVar()
    Checkbutton(top,text="Coach",variable=var2).place(relx=0.0,rely=0.210)
    var3=IntVar()
    Checkbutton(top,text="AC",variable=var3).place(relx=0.0,rely=0.260)

    x=Label(top,text="Schedules",font=ttf,bg="white",fg="black")
    x.place(relx=0.0,rely=0.350)
    var1=IntVar()
    Checkbutton(top,text="06.00am-03.30pm",variable=var1).place(relx=0.0,rely=0.4)
    var2=IntVar()
    Checkbutton(top,text="07.00am-04.00pm",variable=var2).place(relx=0.0,rely=0.450)
    var3=IntVar()
    Checkbutton(top,text="08.00am-12.00pm",variable=var3).place(relx=0.0,rely=0.50)

    frame1=Frame(top,width=1500,height=70,bg="skyblue").place(relx=0.146,rely=0.1)
    ttf=font.Font(weight="bold",family="Algerian",size=30)
    a=Label(top,text="Bus Id",font=ttf,bg="white",fg="black")
    a.place(relx=0.150,rely=0.110)

    b=Label(top,text="Bus Name",font=ttf,bg="white",fg="black")
    b.place(relx=0.3,rely=0.110)

    c=Label(top,text="Price",font=ttf,bg="white",fg="black")
    c.place(relx=0.490,rely=0.110)

    d=Label(top,text="Bus Image",font=ttf,bg="white",fg="black")
    d.place(relx=0.640,rely=0.110)

    ttf=font.Font(weight="bold",family="Algerian",size=15)
    a1=Label(top,text="NBS4455",font=ttf,bg="white",fg="blue")
    a1.place(relx=0.150,rely=0.250)

    a2=Label(top,text="SSX6633",font=ttf,bg="white",fg="blue")
    a2.place(relx=0.150,rely=0.460)

    a3=Label(top,text="RDH4255",font=ttf,bg="white",fg="blue")
    a3.place(relx=0.150,rely=0.660)

    a11=Label(top,text="City Hopper",font=ttf,bg="white",fg="blue")
    a11.place(relx=0.3,rely=0.250)
    a22=Label(top,text="Journey Makers",font=ttf,bg="white",fg="blue")
    a22.place(relx=0.3,rely=0.460)
    a33=Label(top,text="Happy Travels",font=ttf,bg="white",fg="blue")
    a33.place(relx=0.3,rely=0.660)

    a12=Label(top,text="$2,000",font=ttf,bg="white",fg="blue")
    a12.place(relx=0.490,rely=0.260)
    a21=Label(top,text="$4,000",font=ttf,bg="white",fg="blue")
    a21.place(relx=0.490,rely=0.460)
    a31=Label(top,text="$6,000",font=ttf,bg="white",fg="blue")
    a31.place(relx=0.490,rely=0.660)

    ttf=font.Font(weight="bold",family="Algerian",size=15)
    c1=Button(top,text=" BookNow",font=ttf,bg="orange",fg="black",borderwidth="2",command=lambda:seat(top))
    c1.place(relx=0.880,rely=0.260)
    c2=Button(top,text="BookNow",font=ttf,bg="orange",fg="black",borderwidth="2",command=lambda:seat(top))
    c2.place(relx=0.880,rely=0.460)
    c3=Button(top,text=" BookNow",font=ttf,bg="orange",fg="black",borderwidth="2",command=lambda:seat(top))
    c3.place(relx=0.880,rely=0.660)

    ttf=font.Font(weight="bold",family="Algerian",size=25)
    a29='''Royal Travels Thanking to all our Valuable Customers!
        Wish you a Happy and Comfortable Journey'''
    l=Label(top,text=a29,font=ttf,bg="pink",fg="black")
    l.place(relx=0.2,rely=0.870)
    top.mainloop(top)


def seat(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    top.configure(bg="gray")
    frame=Frame(top,height=1500,width=1500,bg="darkgoldenrod")
    ttf=font.Font(weight="bold",family="time new roman",size=30)
    f=Frame(top,width=1500,height=50,bg="yellow")
    ttf=font.Font(weight="bold",family="Arial Black",size=30)
    a=Label(top,text="Royal Bus Booking",font=ttf,bg="indianred",fg="white")
    a.place(relx=0.350,rely=0.00)
    
    img2=ImageTk.PhotoImage(Image.open("busbg4.jpg"))
    l2=Label(frame,image=img2) 
    l2.place(relx=0.0,rely=0.0)

    ttf=font.Font(weight="bold",family="time new roman",size=15)
    def seat1():
        z.insert(END,"SEAT1,")
    c1=Button(top,text="seat1",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat1())
    c1.place(relx=0.05,rely=0.2)
    def seat2():
        z.insert(END,"SEAT2,")
    c2=Button(top,text="seat2",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat2())
    c2.place(relx=0.05,rely=0.3)
    def seat3():
        z.insert(END,"SEAT3,")
    c3=Button(top,text="seat3",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat3())
    c3.place(relx=0.05,rely=0.4)
    def seat4():
        z.insert(END,"SEAT4,")
    c4=Button(top,text="seat4",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat4())
  
    c4.place(relx=0.05,rely=0.5)
    def seat5():
        z.insert(END,"SEAT5,")
    c5=Button(top,text="seat5",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat5())
    c5.place(relx=0.05,rely=0.6)
    def seat6():
        z.insert(END,"SEAT6,")
    c6=Button(top,text="seat6",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat6())
    c6.place(relx=0.150,rely=0.2)
    def seat7():
        z.insert(END,"SEAT7,")
    c7=Button(top,text="seat7",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat7())
    c7.place(relx=0.150,rely=0.3)
    def seat8():
        z.insert(END,"SEAT8,")
    c8=Button(top,text="seat8",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat8())
    c8.place(relx=0.150,rely=0.4)
    def seat9():
        z.insert(END,"SEAT9,")
    c9=Button(top,text="seat9",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat9())
    c9.place(relx=0.150,rely=0.5)
    def seat10():
        z.insert(END,"SEAT10,")
    c10=Button(top,text="seat10",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat10())
    c10.place(relx=0.150,rely=0.6)
    def seat11():
        z.insert(END,"SEAT11,")
    c11=Button(top,text="seat11",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat11())
    c11.place(relx=0.250,rely=0.2)
    def seat12():
        z.insert(END,"SEAT12,")
    c12=Button(top,text="seat12",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat12())
    c12.place(relx=0.250,rely=0.3)
    def seat13():
        z.insert(END,"SEAT13,")
    c13=Button(top,text="seat13",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat13())
    c13.place(relx=0.250,rely=0.4)
    def seat14():
        z.insert(END,"SEAT14,")
    c14=Button(top,text="seat14",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat14())
    c14.place(relx=0.250,rely=0.5)
    def seat15():
        z.insert(END,"SEAT15,")
    c15=Button(top,text="seat15",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat15())
    c15.place(relx=0.250,rely=0.6)
    def seat16():
        z.insert(END,"SEAT16,")
    c16=Button(top,text="seat16",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat16())
    c16.place(relx=0.350,rely=0.2)
    def seat17():
        z.insert(END,"SEAT17,")
    c17=Button(top,text="seat17",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat17())
    c17.place(relx=0.350,rely=0.3)
    def seat18():
        z.insert(END,"SEAT18,")
    c18=Button(top,text="seat18",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat18())
    c18.place(relx=0.350,rely=0.4)
    def seat19():
        z.insert(END,"SEAT19,")
    c19=Button(top,text="seat19",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat19())
    c19.place(relx=0.350,rely=0.5)
    def seat20():
        z.insert(END,"SEAT20,")
    c20=Button(top,text="seat20",font=ttf,bg="sandybrown",fg="blue",command=lambda:seat20())
    c20.place(relx=0.3508,rely=0.6)

    ttf=font.Font(weight="bold",family="time new roman",size=15)
    a=Label(top,text="BusName",font=ttf,bg="turquoise",fg="blue")
    a.place(relx=0.7,rely=0.2)
    a1=Entry(top)
    a1.place(relx=0.8,rely=0.2,width=150,height=30) 

    b=Label(top,text="BusId",font=ttf,bg="turquoise",fg="blue")
    b.place(relx=0.7,rely=0.3)
    b2=Entry(top)
    b2.place(relx=0.8,rely=0.3,width=150,height=30)

    c=Label(top,text="EmailId",font=ttf,bg="turquoise",fg="blue")
    c.place(relx=0.7,rely=0.4)
    c1=Entry(top)
    c1.place(relx=0.8,rely=0.4,width=150,height=30)

    d=Label(top,text="PhoneNo",font=ttf,bg="turquoise",fg="blue")
    d.place(relx=0.7,rely=0.5)
    d1=Entry(top)
    def sql():
        connection=mysql.connect(host="localhost",user="root",password="livewire",database="bus03")
        cursor=connection.cursor()
        s="insert into t1 (BusName,BusId,EmailId,PhoneNo)values(%s,%s,%s,%s)"
        t=(a1.get(),b2.get(),c1.get(),d1.get())
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo("registration Successfully")

    z=Text(top,height=5,width=35)
    z.pack()
    z.insert(END,'')
    z.place(relx=0.720,rely=0.6)
    
    def data(top):
        messagebox.showinfo("Hello","Booking sucessfully!!!")
    d1.place(relx=0.8,rely=0.5,width=150,height=30)
    c11=Button(top,text="Register",font=ttf,bg="sandybrown",fg="deeppink",command=lambda:data(top))
    c11.place(relx=0.790,rely=0.740)
    frame.pack()
    top.mainloop(top)




    
        



def DeleteBooking(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    top.title("Booking")
        
    s=Frame(top,width=1500,height=1500,bg="purple")
    ttf=font.Font(weight="bold",family="Algerian",size=40)
    a=Label(top,text="Royal Bus Booking",font=ttf,bg="purple",fg="sandybrown")
    a.place(relx=0.4,rely=0.03)
    ttf=font.Font(weight="bold",family="time new roman",size=25)
        
    frame1=Frame(top,width=413,height=800,bg="gray")
    frame1.place(relx=0.0,rely=0.149)


        


    ttf=font.Font(weight="bold",family="time new roman",size=15)
    a=Label(top,text="TicketNo",font=ttf,bg="turquoise",fg="blue")
    a.place(relx=0.0,rely=0.200)
    a1=Entry(top)
    a1.place(relx=0.130,rely=0.2,width=150,height=30)
    b=Label(top,text="PaymentID",font=ttf,bg="turquoise",fg="blue")

    b.place(relx=0.0,rely=0.3)
    b1=Entry(top)
    b1.place(relx=0.130,rely=0.3,width=150,height=30)

    c=Label(top,text="Amount",font=ttf,bg="turquoise",fg="blue")
    c.place(relx=0.0,rely=0.4)
    c1=Entry(top)
    c1.place(relx=0.130,rely=0.4,width=150,height=30)

    d=Label(top,text="DateTime",font=ttf,bg="turquoise",fg="blue")
    d.place(relx=0.0,rely=0.5)
    d1=Entry(top)
    d1.place(relx=0.130,rely=0.5,width=150,height=30)

    img=ImageTk.PhotoImage(Image.open("cancel.jpg"))
    l=Label(s,image=img) 
    l.place(relx=0.3,rely=0.150)

    e=Label(top,text="MobileNo",font=ttf,bg="turquoise",fg="blue")
    e.place(relx=0.0,rely=0.6)
    e1=Entry(top)
    e1.place(relx=0.130,rely=0.6,width=150,height=30)

    f=Label(top,text="Transactiontype",font=ttf,bg="turquoise",fg="blue")
    f.place(relx=0.0,rely=0.7)
    f1=Entry(top)
    f1.place(relx=0.130,rely=0.7,width=150,height=30)

    c=Button(top,text="CANCEL",font=ttf,bg="sandybrown",fg="blue")
    c.place(relx=0.1,rely=0.8)
    s.pack()
    top.mainloop(top)


def busdetails(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    ttf=font.Font(weight="bold",family="time new roman",size=30)
    frame2=Frame(top,height=1500,width=1500)

    img1=ImageTk.PhotoImage(Image.open("sw2.jpg"))
    l1=Label(frame2,image=img1) 
    l1.place(relx=0.0,rely=0.0)

    img=ImageTk.PhotoImage(Image.open("logo.png"))
    l=Label(frame2,image=img) 
    l.place(relx=0.4,rely=0.0)
    
    ttf=font.Font(weight="bold",family="Castellar",size=15)
    b=Label(top,text="*Luxury AC Coach",font=ttf,bg="turquoise",fg="deeppink")
    b.place(relx=0.02,rely=0.2)
    c=Label(top,text="*Medicated Seat",font=ttf,bg="turquoise",fg="deeppink")
    c.place(relx=0.830,rely=0.3)
    d=Label(top,text="*OnlineTicket",font=ttf,bg="turquoise",fg="deeppink")
    d.place(relx=0.830,rely=0.4)   
    e=Label(top,text="*ExperienceDriver",font=ttf,bg="turquoise",fg="deeppink")
    e.place(relx=0.825,rely=0.5)   
    f=Label(top,text="*WIFI",font=ttf,bg="turquoise",fg="deeppink")
    f.place(relx=0.830,rely=0.2)
    g=Label(top,text="*CCTV Monitoring",font=ttf,bg="turquoise",fg="deeppink")
    g.place(relx=0.02,rely=0.3)
    h=Label(top,text="*USB Charging Port",font=ttf,bg="turquoise",fg="deeppink")
    h.place(relx=0.02,rely=0.4)
    i=Label(top,text="*Call CenterSupport",font=ttf,bg="turquoise",fg="deeppink")
    i.place(relx=0.02,rely=0.5)
        
    ttf=font.Font(weight="bold",family="Algerian",size=15)
    a='''Royal Travels which is located in Tamil Nadu is a renowned brand in the bus operating industry. 
    Our vision is to give a new face to the bus industry. 
    Since our inception passenger comfort was our top priority.'''

    l=Label(top,text=a,font=ttf,wraplength=1000,justify="center",bg="skyblue",fg="blue")
    l.place(relx=0.2,rely=0.870)
    ttf=font.Font(weight="bold",family="Castellar",size=20)
    c=Button(top,text="Vacation place",font=ttf,bg="deeppink",fg="black",command=lambda:tour(top))
    c.place(relx=0.4,rely=0.760)
    frame2.pack()
    top.mainloop(top)



def tour(top):
    top.destroy()
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)

    f=Frame(top,width=1500,height=50,bg="deeppink")
    ttf=font.Font(weight="bold",family="Arial Black",size=30)
    a=Label(top,text="Royal Tourist Place",font=ttf,bg="deeppink",fg="white")
    a.place(relx=0.350,rely=0.00)

    frame2=Frame(top,height=1500,width=1500,bg="skyblue")  
    img1=ImageTk.PhotoImage(Image.open("tour4.jpg"))
    l1=Label(frame2,image=img1) 
    l1.place(relx=0.0,rely=0.0)

    img2=ImageTk.PhotoImage(Image.open("tour17.jpg"))
    l2=Label(frame2,image=img2) 
    l2.place(relx=0.270,rely=0.0)

    img3=ImageTk.PhotoImage(Image.open("tour9.jpg"))
    l3=Label(frame2,image=img3) 
    l3.place(relx=0.540,rely=0.0)

    img4=ImageTk.PhotoImage(Image.open("tour12.jpg"))
    l4=Label(frame2,image=img4) 
    l4.place(relx=0.790,rely=0.0)

    img5=ImageTk.PhotoImage(Image.open("tour7.jpg"))
    l5=Label(frame2,image=img5) 
    l5.place(relx=0.270,rely=0.5)

    img6=ImageTk.PhotoImage(Image.open("tour14.jpg"))
    l6=Label(frame2,image=img6) 
    l6.place(relx=0.540,rely=0.5)

    
    img7=ImageTk.PhotoImage(Image.open("tour16.jpg"))
    l7=Label(frame2,image=img7) 
    l7.place(relx=0.790,rely=0.5)


    img8=ImageTk.PhotoImage(Image.open("tour11.jpg"))
    l7=Label(frame2,image=img8) 
    l7.place(relx=0.0,rely=0.5)
    f.pack()
    frame2.pack()
    top.mainloop(top)





def home():
    top=Tk()
    top.geometry("400x300")
    top.attributes('-fullscreen', True)
    top.title("Booking")
    top.configure(bg="indianred3")

   
    frame=Frame(top,width=1500,height=50,bg="indianred3").place(relx=0.0,rely=0.0)
    img=ImageTk.PhotoImage(Image.open("n86.jpg"))
    l=Label(frame,image=img)
    l.pack()

    frame=Frame(top,width=1500,height=70,bg="indianred1").place(relx=0.0,rely=0.0)
    ttf=font.Font(weight="bold",family="Algerian",size=40)
    a=Label(top,text="Royal Bus booking",font=ttf,bg="indianred1",fg="white")
    a.place(relx=0.350,rely=0.0)
    ttf=font.Font(weight="bold",family="times new roman",size=20)
    b=Button(top,text="Customer Registration",font=ttf,bg="sandybrown",fg="blue",command=lambda:customerregister(top))
    b.place(relx=0.790,rely=0.130 )
    b1=Button(top,text="Customer login",font=ttf, bg="sandybrown",fg="blue",command=lambda:customerlogin(top))
    b1.place(relx=0.850,rely=0.3)
    b2=Button(top,text="Delete Booking",font=ttf,bg="sandybrown",fg="blue",command=lambda:DeleteBooking(top))
    b2.place(relx=0.860,rely=0.5)
        
    b3=Button(top,text="About us",font=ttf,bg="sandybrown",fg="blue",command=lambda:busdetails(top))
    b3.place(relx=0.910,rely=0.7)
    b4=Button(top,text="Quit",font=ttf,bg="sandybrown",fg="blue",command=lambda:exit())
    b4.place(relx=0.950,rely=0.9)
    ttf=font.Font(weight="bold",family="Times New Roman",size=30)
 
    top.mainloop()
home()












