from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from tkinter import ttk
import pandas as pd
import random
import os
from PIL import ImageTk,Image
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)


conn = sqlite3.connect('B:\StudyMaterials\DBMSProject\ResDB.db')
c=conn.cursor()
print(c.execute("select * from CUSTOMER"))

def chk_conn(conn):
     try:
        conn.cursor()
        return True
     except Exception as ex:
        return False
print(chk_conn(conn))




def enter():
    try:
        screen1.destroy()
    except:
        pass
    global screen2
    screen2=Tk()
    Label(screen2,text="Enter Details",bg ="grey", font=("Calibri",15),width =500,height=1).pack()
    global CID,Cname,Address,DOB,EID,Ctoken
    CID = StringVar()
    Cname = StringVar()

    Address= StringVar()
    DOB = StringVar()
    EID = StringVar()
    Ctoken = StringVar()

    global w1,w2,w3,w4,w5,w6,w7,w8
    Label(screen2, text= "Please enter details").pack()
    Label(screen2, text= "").pack()
    Label(screen2, text= "CID").pack()
    w1=Entry(screen2, textvariable = CID).pack()
    Label(screen2, text= "Name").pack()
    w2=Entry(screen2, textvariable = Cname).pack()

    Label(screen2, text= "Address").pack()
    w4=Entry(screen2, textvariable = Address).pack()
    Label(screen2, text= "DOB").pack()
    w5=Entry(screen2, textvariable = DOB).pack()
    Label(screen2, text= "EID").pack()
    w6=Entry(screen2, textvariable = EID).pack()
    Label(screen2, text= "Ctoken").pack()
    w7=Entry(screen2, textvariable = Ctoken).pack()

    B1=Button(screen2,text="Enter Details",command=entry).pack(pady=5)


def entry():
    w1=CID.get()
    w2=Cname.get()

    w4=Address.get()
    w5=DOB.get()
    w6=EID.get()
    w7=Ctoken.get()


    x=(w1,w2,w4,w5,w6,w7)
    l1=['P','N']
    res = random.choice(l1)
    y=(res,w1)
    c.execute("insert into Customer values(?,?,?,?,?,?)",x)
    c.execute("select * from Cust_logs")
    for log in c.fetchall():
        print(log)
    conn.commit()
    screen2.destroy()
    login_admin()

def gBill():
    try:
        screen1.destroy()
    except:
        pass
    global screen61
    screen61=Tk()
    Label(screen61,text="Enter Details",bg ="grey", font=("Calibri",15),width =500,height=1).pack()
    global CID
    global d121
    CID = StringVar()
    Label(screen61, text= "Please enter details").pack()
    Label(screen61, text= "").pack()
    Label(screen61, text= "CID").pack()
    d1=Entry(screen61, textvariable = CID).pack()
    button=Button(screen61,text="Generate",command=genBill).pack(pady=5)

def genBill():
    d121=CID.get()
    c.execute(" SELECT SUM(AMOUNT),BILL.CID from BILL,CUSTOMER where BILL.CID=CUSTOMER.CID GROUP BY CUSTOMER.CID ")
    b=c.fetchall()

    c.execute("select CID,SUM(AMOUNT) from BILL where CID=(?)",[d121])
    cx=pd.DataFrame(c.fetchall())
    screen21=Tk()
    text=Text(screen21)
    text.insert(END,str(cx.iloc[:,0:]))
    text.pack(fill=BOTH, expand=1)
    screen61.destroy()
    login_admin()



def getBill():

    c.execute(" SELECT BILL.CID,SUM(AMOUNT) from BILL,CUSTOMER where BILL.CID=CUSTOMER.CID GROUP BY CUSTOMER.CID ")
    b=pd.DataFrame(c.fetchall())
    b.columns=["Customer","Price"]
    messagebox.showinfo("Bill","Bill Calculated")
    screen20=Tk()
    text=Text(screen20)
    text.insert(END,str(b.iloc[:,0:]))
    text.pack(fill=BOTH, expand=1)
    screen1.destroy()
    login_admin()


def addorder():
    try:
        screen1.destroy()
    except:
        pass
    global screen6
    screen6=Tk()
    Label(screen6,text="Enter Details",bg ="grey", font=("Calibri",15),width =500,height=1).pack()
    global OID,Oname,Ono,Price,Portion,C_ID
    global d1,d2,d3,d4,d5,d6
    OID = StringVar()
    Oname = StringVar()
    Ono = StringVar()
    Price = StringVar()
    Portion= StringVar()
    C_ID=StringVar()
    Label(screen6, text= "Please enter details").pack()
    Label(screen6, text= "").pack()
    Label(screen6, text= "OID").pack()
    d1=Entry(screen6, textvariable = OID).pack()
    Label(screen6, text= "Oname").pack()
    d2=Entry(screen6, textvariable = Oname).pack()
    Label(screen6, text= "Ono").pack()
    d3=Entry(screen6, textvariable = Ono).pack()
    Label(screen6, text= "Price").pack()
    d4=Entry(screen6, textvariable = Price).pack()
    Label(screen6, text= "Portion").pack()
    d5=Entry(screen6, textvariable = Portion).pack()
    Label(screen6, text= "CID").pack()
    d6=Entry(screen6, textvariable = C_ID).pack()

    button=Button(screen6,text="Enter Details",command=add).pack(pady=5)


def add():
    d1=OID.get()
    d2=Oname.get()
    d3=Ono.get()
    d4=Price.get()
    d5=Portion.get()
    d6=C_ID.get()
    x=(d1,d2,d3,d4,d5,d6)
    y=(d6,d4)

    c.execute("insert into ORD values(?,?,?,?,?,?)",x)
    c.execute("insert into BILL(CID,AMOUNT) values(?,?)",y)
    conn.commit()


    messagebox.showinfo("Order Added","Order Added")
    screen6.destroy()
    login_admin()


def Employee():
    global screen11
    c.execute("select * from EMPLOYEE ")
    a=pd.DataFrame(c.fetchall())
    a.columns = ['EID','Ename','Phoneno.','EXP']
    screen11=Tk()
    screen11.geometry("750x300")
    text=Text(screen11)
    text.insert(END,str(a.iloc[:,0:]))
    text.pack(fill=BOTH, expand=1)


def menu():
    try:
        screen1.destroy()
    except:
        pass
    global screen23
    screen23 =Tk()
    screen23.geometry("700x720")
    screen23.title("Restaurant Manager")
    my_img=ImageTk.PhotoImage(Image.open("menu.jpg"))


    my_canvas=Canvas(screen23,width=500,height=720)
    my_canvas.pack(fill="both",expand=True)

    my_canvas.create_image(10,10,image=my_img,anchor="nw")
    b3=Button(screen23,text="Back",command=login_admin)
    b3_window=my_canvas.create_window(600,670,anchor="nw",window=b3)

    screen23.mainloop()




def login_admin():
    try:
        screen.destroy()
        screen23.destroy()
    except:
        pass
    global screen1
    screen1=Tk()
    screen1.geometry('800x300')

    Label(screen1,text="Welcome to the Restaurant Management System",bg ="grey", font=("Calibri",15),width =500,height=1).pack()
    B1=Button(screen1,text="Get Employee Details",width =30,height=1,command=Employee).pack(pady=5)
    B2=Button(screen1,text="Enter Details",width =30,height=1,command=enter).pack(pady=5)
    B3=Button(screen1,text="MENU",width =30,height=1,command=menu).pack(pady=5)
    B4=Button(screen1,text="Get Bill",width =30,height=1,command=getBill).pack(pady=5)
    B5=Button(screen1,text="Add Order",width =30,height=1,command=addorder).pack(pady=5)
    B6=Button(screen1,text="GENERATE BILL",width =30,height=1,command=gBill).pack(pady=5)


def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()

    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    lof=os.listdir()
    if username1 in lof:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if username1=='admin':
            file2=open(username1,"r")
            verify1=file2.read().splitlines()
            if password1 in verify1 and password1=='admin':
                try:
                    messagebox.showinfo("SUCCESS","login success")
                    screen8.destroy()
                except:
                        pass
                login_admin()
        elif username1 in lof:
            file3=open(username1,"r")
            verify=file3.read().splitlines()
            if password1 in verify:
                try:
                    messagebox.showinfo("SUCCESS","login success")
                    screen8.destroy()
                except:
                    pass

                login_admin()
            else:
                messagebox.showinfo("ERROR","Password has not been Recognized")


    else:
        messagebox.showinfo("ERROR","User not found")
    file1.close()


def login1():
    try:
        screen.destroy()
    except:
        pass
    global screen8
    screen8=Tk()
    screen8.title("Login")
    screen8.geometry('500x250')
    global username_verify,password_verify,username_entry1,password_entry1
    username_verify=StringVar()
    password_verify=StringVar()
    Label(screen8,text ="Please Enter Details").pack()
    Label(screen8,text ="").pack()
    Label(screen8,text ="Username * ").pack()
    username_entry1=Entry(screen8,textvariable=username_verify)
    username_entry1.pack()
    Label(screen8,text ="Password * ").pack()
    password_entry1=Entry(screen8,textvariable=password_verify)
    password_entry1.pack()
    Label(screen8,text ="").pack()
    Button(text="Login",width =30,height=1,command=login_verify).pack()


def register_user():
    username_info=username.get()
    password_info=password.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    messagebox.showinfo("Registration Succesful","registration success")
    screen9.destroy()
    main_screen()


def register():
    try:
        screen.destroy()
    except:
        pass
    global screen9
    screen9=Tk()
    screen9.title("Register")
    screen9.geometry('500x250')
    global username,password,username_info,password_info,username_entry,password_entry
    username=StringVar()
    password=StringVar()
    Label(screen9,text ="Please Enter Details").pack()
    Label(screen9,text ="").pack()
    Label(screen9,text ="Username * ").pack()
    username_entry=Entry(screen9,textvariable=username)
    username_entry.pack()
    Label(screen9,text ="Password * ").pack()
    password_entry=Entry(screen9,textvariable=password)
    password_entry.pack()
    Label(screen9,text ="").pack()
    Button(text="Register",width =30,height=1,command=register_user).pack()


def main_screen():
    global screen
    screen =Tk()
    screen.geometry("640x540")
    screen.title("Restaurant Manager")

    # my_img1=ImageTk.PhotoImage(Image.open("Cover.jpg"))


    my_canvas=Canvas(screen,width=640,height=540)
    my_canvas.pack(fill="both")

    # my_canvas.create_image(0,0,image=my_img1,anchor="nw")

    b1=Button(screen,text="Login",width =10,height=1,command= login1)

    b2=Button(screen,text="Register",width =10,height=1,command=register)

    b3=Button(screen,text="Exit Program",width =10,height=1,command=screen.quit)


    b1_window=my_canvas.create_window(30,10,anchor="nw",window=b1)
    b2_window=my_canvas.create_window(150,10,anchor="nw",window=b2)
    b3_window=my_canvas.create_window(530,480,anchor="nw",window=b3)


    screen.mainloop()


main_screen()
