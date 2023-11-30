import tkinter as tk
import webbrowser
import tkinter.font as tkfont
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as pb
import sys
import random
from prettytable import from_db_cursor
import datetime
#_______________________________________________________________________________________________

db=pb.connect(host="localhost",user="root",passwd="nithin@792",database="pns")
curdb=db.cursor()

def suc_1():
    global msg1
    msg1=Toplevel(win1)
    msg1.geometry("1366x768+0+0")
    msg1.title("CONFIRM")
    msg1.state("zoomed")
    frame=Frame(msg1,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("CA.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    b1=tk.Button(msg1,text="Confirm",bg="black",fg="cyan",command=dat_acc)
    b1.configure(height=2,width=15)
    b1.place(x=700,y=650)
    b2=tk.Button(msg1,text="Back",bg="black",fg="red",command=msg1.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=500,y=650)
    msg1.mainloop()

def create_acc():
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e11,e10
    win4=Toplevel(win1)
    win4.geometry("1366x768+0+0")
    win4.title("Create Account")
    win4.state("zoomed")
    frame=Frame(win4,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("4.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e1=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e1.place(x=700,y=100)
    l1=tk.Label(win4,fg="#000000",text="Account number:",bg="white")
    l1.place(x=500,y=100)
    e2=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e2.place(x=700,y=150)
    l2=tk.Label(win4,fg="#000000",text="Full Name:",bg="white")
    l2.place(x=500,y=150)
    e3=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e3.place(x=700,y=200)
    l3=tk.Label(win4,fg="#000000",text="Account Type:",bg="white")
    l3.place(x=500,y=200)
    e4=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e4.place(x=700,y=250)
    l4=tk.Label(win4,fg="#000000",text="Birth date (YYYY-MM-DD):",bg="white")
    l4.place(x=500,y=250)
    e5=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e5.place(x=700,y=300)
    l5=tk.Label(win4,fg="#000000",text="Mobile Number:",bg="white")
    l5.place(x=500,y=300)
    e6=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e6.place(x=700,y=350)
    l6=tk.Label(win4,fg="#000000",text="Gender (MALE/FEMALE):",bg="white")
    l6.place(x=500,y=350)
    e7=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e7.place(x=700,y=400)
    l7=tk.Label(win4,fg="#000000",text="Nationality:",bg="white")
    l7.place(x=500,y=400)
    e8=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e8.place(x=700,y=450)
    l8=tk.Label(win4,fg="#000000",text="KYC Document:",bg="white")
    l8.place(x=500,y=450)
    e9=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black",show="*")
    e9.place(x=700,y=500)
    l9=tk.Label(win4,fg="#000000",text="PIN:",bg="white")
    l9.place(x=500,y=500)
    e11=tk.Entry(win4,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e11.place(x=700,y=550)
    l11=tk.Label(win4,fg="#000000",text="Initial Balance:",bg="white")
    l11.place(x=500,y=550)
    b1=tk.Button(win4,text="Confirm",bg="black",fg="cyan",borderwidth=10,command=suc_1)
    b1.configure(height=2,width=15)
    b1.place(x=700,y=650)
    b2=tk.Button(win4,text="Back",bg="black",fg="red",borderwidth=10,command=win4.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=500,y=650)
    win4.mainloop()

def deposit():
    global n1,n2
    win5=Toplevel(win1)
    win5.geometry("1366x768+0+0")
    win5.title("Deposit Amount")
    win5.state("zoomed")
    frame=Frame(win5,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("DEA1.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    n1=tk.Entry(win5,font="TkFixedFont",fg="#000000",highlightcolor="black",width=50)
    n1.place(x=800,y=280)
    n2=tk.Entry(win5,font="TkFixedFont",fg="#000000",highlightcolor="black",width=30)
    n2.place(x=500,y=430)
    b1=tk.Button(win5,text="Confirm",bg="black",fg="cyan",command=depo_sit)
    b1.configure(height=2,width=15)
    b1.place(x=1000,y=600)
    b2=tk.Button(win5,text="Back",bg="black",fg="red",command=win5.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=800,y=600)
    win5.mainloop()

def withdraw():
    global n3,n4
    win6=Toplevel(win1)
    win6.geometry("1366x768+0+0")
    win6.title("Deposit Amount")
    win6.state("zoomed")
    frame=Frame(win6,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("withd.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    n3=tk.Entry(win6,font="TkFixedFont",fg="#000000",highlightcolor="black",width=50)
    n3.place(x=800,y=255)
    n4=tk.Entry(win6,font="TkFixedFont",fg="#000000",highlightcolor="black",width=30)
    n4.place(x=450,y=400)
    b1=tk.Button(win6,text="Confirm",bg="black",fg="cyan",command=with_draw)
    b1.configure(height=2,width=15)
    b1.place(x=1000,y=550)
    b2=tk.Button(win6,text="Back",bg="black",fg="red",command=win6.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=750,y=550)
    win6.mainloop()
    
def update_acc():
    win7=Toplevel(win1)
    win7.geometry("1366x768+0+0")
    win7.title("Check Balance")
    win7.state("zoomed")
    frame=Frame(win7,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("UA1.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    wid1=tk.Button(win7,text="MOBILE NUMBER",bg="black",fg="cyan",font='comic',command=updat_mb1)
    wid1.config(height=1,width=25)
    wid1.place(x=1000,y=150)
    wid2=tk.Button(win7,text="DATE OF BIRTH",bg="black",font="comic",fg="cyan",command=updat_dob1)
    wid2.configure(height=1,width=25)
    wid2.place(x=1000,y=200)
    wid3=tk.Button(win7,text="KYC DOCUMENT",bg="black",font="comic",fg="cyan",command=updat_kyc1)
    wid3.configure(height=1,width=25)
    wid3.place(x=1000,y=250)
    wid4=tk.Button(win7,text="PIN",bg="black",font="comic",fg="cyan",command=updat_pin1)
    wid4.configure(height=1,width=25)
    wid4.place(x=1000,y=300)
    b2=tk.Button(win7,text="Back",bg="black",fg="red",command=win7.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=605,y=550)
    win7.mainloop()
    
def search_acc():
    global e14
    win8=Toplevel(win1)
    win8.geometry("1366x768+0+0")
    win8.title("Search account")
    win8.state("zoomed")
    frame=Frame(win8,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("SA1.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e14=tk.Entry(win8,font="TkFixedFont",fg="#000000",highlightcolor="black",width=50)
    e14.place(x=500,y=370)
    b1=tk.Button(win8,text="Confirm",bg="black",fg="cyan",command=search)
    b1.configure(height=2,width=25)
    b1.place(x=570,y=450)
    b2=tk.Button(win8,text="Back",bg="black",fg="red",command=win8.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=600,y=550)
    win8.mainloop()

def display_det():
    win9=Toplevel(win1)
    win9.geometry("1366x768+0+0")
    win9.title("Display account")
    win9.state("zoomed")
    frame=Frame(win9,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("P5.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    b1=tk.Button(win9,text="Confirm",bg="black",fg="cyan",command=dis_det)
    b1.configure(height=2,width=15)
    b1.place(x=1000,y=550)
    b2=tk.Button(win9,text="Back",bg="black",fg="red",command=win9.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=750,y=550)
    win9.mainloop()

def drop_acc():
    global e13
    win10=Toplevel(win1)
    win10.geometry("1366x768+0+0")
    win10.title("Drop account")
    win10.state("zoomed")
    frame=Frame(win10,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("DA2.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e13=tk.Entry(win10,font="TkFixedFont",fg="#000000",highlightcolor="black",width=50)
    e13.place(x=500,y=350)
    b1=tk.Button(win10,text="Confirm",bg="black",fg="cyan",command=statement)
    b1.configure(height=2,width=25)
    b1.place(x=570,y=450)
    b2=tk.Button(win10,text="Back",bg="black",fg="red",command=win10.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=600,y=550)
    win10.mainloop()

def view_stt():
    global e15
    win11=Toplevel(win1)
    win11.geometry("1366x768+0+0")
    win11.title("Drop account")
    win11.state("zoomed")
    frame=Frame(win11,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("SS.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e15=tk.Entry(win11,font="TkFixedFont",fg="#000000",highlightcolor="black",width=50)
    e15.place(x=500,y=350)
    b1=tk.Button(win11,text="Confirm",bg="black",fg="cyan",command=statement)
    b1.configure(height=2,width=25)
    b1.place(x=570,y=450)
    b2=tk.Button(win11,text="Back",bg="black",fg="red",command=win11.withdraw)
    b2.configure(height=2,width=15)
    b2.place(x=600,y=550)
    win11.mainloop()

def exitt():
    win12=Toplevel(win1)
    win12.geometry("1366x768+0+0")
    win12.title("Exit")
    win12.state("zoomed")
    frame=Frame(win12,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("tq2.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    b1=Button(win12,text='CREDITS',font=("Times New Roman",13,"bold"),width=5,bd=0,bg='#090a0a',cursor='hand2', activebackground='#3047ff', fg='white',command=credits)
    b1.configure(height=2,width=15)
    b1.place(x=1200,y=600)
    b2=Button(win12,text='EXIT PORTAL',font=("Times New Roman",13,"bold"),width=5,bd=0,bg='#090a0a',cursor='hand2', activebackground='#3047ff', fg='white',command=win1.destroy)
    b2.configure(height=2,width=15)
    b2.place(x=1200,y=650)
    win12.mainloop()

def credits():
    win13=Toplevel(win1)
    win13.geometry("1366x768+0+0")
    win13.title("Credits")
    win13.state("zoomed")
    frame=Frame(win13,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("credits.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    b2=Button(win13,text='EXIT PORTAL',font=("Times New Roman",13,"bold"),width=5,bd=0,bg='#090a0a',cursor='hand2', activebackground='#3047ff', fg='white',command=win1.destroy)
    b2.configure(height=2,width=15)
    b2.place(x=1200,y=650)
    win13.mainloop()
    
def dat_acc():
    global curdb
    ano=e1.get()
    hn=e2.get()
    typ=e3.get()
    dob=e4.get()
    ph=e5.get()
    ge=e6.get()
    nat=e7.get()
    kyc=e8.get()
    pin=e9.get()
    bal=e11.get()

    
    if not validDate(dob):
        messagebox.showinfo(' ',"Invalid date format, re-enter it")
    elif not above18(dob):
        messagebox.showinfo(' ',"You must be atleast 18 years to create a bank account")
    elif not (len(ph)==10 and ph.isdigit()):
        messagebox.showinfo(' ',"Enter 10 digit phone number")
    
    q="insert into holdet values({},'{}','{}','{}',{},'{}','{}','{}')".format(ano,hn,typ,dob,ph,ge,nat,kyc)
    q2="insert into balance values('{}',{},{})".format(hn,ano,bal)
    q3="create table {} (date date,Balance int)".format(hn)
    q4="insert into {} values('{}',{})".format(hn,datetime.datetime.today().strftime("%Y-%m-%d"),bal)
    curdb.execute(q)
    curdb.execute(q2)
    curdb.execute(q3)
    curdb.execute(q4)
    db.commit()
    messagebox.showinfo(' ','ACCOUNT CREATED SUCCESSFULLY')
    
def validDate(date):
    return (len(date)==10 and
        date[0:4].isdigit() and
        date[4]=='-' and
        date[5:7].isdigit() and
        date[7]=='-' and
        date[8:10].isdigit())

def above18(date, _format='%Y-%m-%d'):
    dateobj=datetime.datetime.strptime(date, _format)
    today=datetime.date.today()
    today_datetime=datetime.datetime(today.year, today.month, today.day)
    x=(today_datetime-dateobj)
    return (x>=datetime.timedelta(days=18*365))

def depo_sit():
    me=n1.get()
    r=n2.get()
    l=[]
    q4='select * from holdet'
    curdb.execute(q4)
    data=curdb.fetchall()
    h=True
    if h==True:
        for row in data:
            if row[1]==me:
                q9="insert into {} values('{}',{})".format(me,datetime.datetime.today().strftime("%Y-%m-%d"),r)
                curdb.execute(q9)
                db.commit()
                messagebox.showinfo(' ','AMOUNT DEPOSITED SUCCESSFULLY')
    else:
        messagebox.showinfo(' ','ENTER VALID ACCOUNT HOLDER NAME')

def with_draw():
    me=n3.get()
    r=int(n4.get())
    l=[]
    q4='select * from holdet'
    fl=True
    curdb.execute(q4)
    data=curdb.fetchall()
    h=check_bal(r)
    if h==True:
        for row in data:
            if row[1]==me:
                q9="insert into {} values('{}',-{})".format(me,datetime.datetime.today().strftime("%Y-%m-%d"),r)
                curdb.execute(q9)
                db.commit()
                messagebox.showinfo(' ','AMOUNT WITHDRAW SUCCESSFULLY')
                fla=False
    elif h==False:
        if fl==False:
            messagebox.showinfo(' ','ENTER VALID ACCOUNT HOLDER NAME')
    
def check_bal(q: int):
    me=n3.get()
    q5='select sum(balance) from {}'.format(me)
    curdb.execute(q5)
    data=curdb.fetchall()[0][0]
    if q<int(data):
        return True
    elif q>int(data):
        messagebox.showinfo(' ','INSUFFICIENT BALANCE')
        return False
       
def dis_det():
    f2=tk.Tk()
    f2.title('DISPLAY RECORD')
    f2.geometry("1366x768+0+0")
    curdb=db.cursor()
    curdb.execute("SELECT * FROM holdet")
    i=0 
    for holdet in curdb:
        for j in range(len(holdet)):
            e=Entry(f2,width=20,fg='black',bg='white')
            e.grid(row=i,column=j) 
            e.insert(END,holdet[j])
        i=i+1
    f2.mainloop()
    
def drop():
    flag=0
    a=e13.get()
    l=[]
    q4='select * from holdet'
    curdb.execute(q4)
    data=curdb.fetchall()
    
    for i in data:
        l.append(i[0])
    
    #if a in l:
     #   print("s")
    for row in data:
            print("a")
            if row[1]==a:
                print("Q")
                ch=tk.messagebox.askquestion(message='Do You Want To Delete Record YES/NO')
                if ch=="yes":
                    q7='delete from holdet where full_name=("{}")'.format(a)
                    q8='drop table {}'.format(row[1])
                    curdb.execute(q7)
                    curdb.execute(q8)
                    db.commit()
                    flag=1
                    messagebox.showinfo(' ','ACCOUNT DELETED SUCCESSFULLY')
                    
                else:
                    if flag==0:
                        messagebox.showinfo(' ','RECORD NOT FOUND')
   
def search():
    flag=0
    a=int(e14.get())
    l=[]
    q='select * from holdet'
    curdb.execute(q)
    data=curdb.fetchall()
    
    for i in data:
        l.append(i[0])
    

    if a in l:
        for row in data:
            if row[0]==a:
                ch=tk.messagebox.askquestion(message='Do You Want To Search Record YES/NO')
                if ch=="yes":
                    s2=tk.Tk()
                    s2.title('SEARCH RECORD')
                    s2.geometry("1366x768")
                    for j in range(len(row)):
                            e=Entry(s2,width=20,fg='black',bg='white')
                            e.grid(row=0,column=j) 
                            e.insert(END,row[j])
                        
                    flag=1
                    messagebox.showinfo(' ','RECORD FOUND')
                    
                      


                elif ch.upper()=='no':
                    s2.destroy()
    else:
        if flag==0:
            messagebox.showinfo(' ','RECORD NOT FOUND')
def statement():
    na=e15.get()
    f2=tk.Tk()
    f2.title('DISPLAY RECORD')
    f2.geometry("1366x768+0+0")
    curdb=db.cursor()
    curdb.execute("SELECT * FROM {}".format(na))
    i=0 
    for holdet in curdb:
        for j in range(len(holdet)):
            e=Entry(f2,width=20,fg='black',bg='white')
            e.grid(row=i,column=j) 
            e.insert(END,holdet[j])
        i=i+1
    f2.mainloop()
        
def updat_mb1():
    global e19,e20,e21
    s1=Toplevel(win1)
    s1.geometry("1366x768+0+0")
    s1.title("Update Mobile Number")
    s1.state("zoomed")
    frame=Frame(s1,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("U1.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e21=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e21.place(x=720,y=190)
    e19=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e19.place(x=700,y=320)
    e20=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e20.place(x=700,y=450)
    btn=tk.Button(s1,text="SUBMIT",fg="cyan",bg="black",command=updat_mb2)
    btn.configure(width=15,height=2)
    btn.place(x=850,y=600)
    btn2=tk.Button(s1,text="BACK",fg="red",bg="black",command=s1.withdraw)
    btn2.configure(width=15,height=2)
    btn2.place(x=650,y=600)
    s1.mainloop()

def updat_mb2():
    print('w')
    mb1=int(e19.get())
    mb2=int(e20.get())
    mb3=e21.get()
    flag=0
    l=[]
    q='select * from holdet'
    curdb.execute(q)
    data=curdb.fetchall()
    
    for i in data:
        l.append(i[1])
        
    if mb3 in l:
        for row in data:
            if row[1]==mb3:
                flag=1
                q1="update holdet set mob_no='{}' where full_name='{}'".format(mb2,mb3)
                curdb.execute(q1)
                db.commit()
                tk.messagebox.showinfo(' ','DATA UPDATED')
        
    else:
        tk.messagebox.showinfo(' ','ENTER VALID DETAILS')

def updat_dob1():
    global e22,e23,e24
    s1=Toplevel(win1)
    s1.geometry("1366x768+0+0")
    s1.title("Update Mobile Number")
    s1.state("zoomed")
    frame=Frame(s1,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("U2.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e22=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e22.place(x=750,y=215)
    e23=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e23.place(x=470,y=340)
    e24=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e24.place(x=500,y=460)
    btn=tk.Button(s1,text="SUBMIT",fg="cyan",bg="black",command=updat_dob2)
    btn.configure(width=15,height=2)
    btn.place(x=850,y=600)
    btn2=tk.Button(s1,text="BACK",fg="red",bg="black",command=s1.withdraw)
    btn2.configure(width=15,height=2)
    btn2.place(x=650,y=600)
    s1.mainloop()

def updat_dob2():
    
    dob1=int(e23.get())
    dob2=int(e24.get())
    dob3=e22.get()
    flag=0
    l=[]
    q='select * from holdet'
    curdb.execute(q)
    data=curdb.fetchall()
    
    for i in data:
        l.append(i[1])
        
    if dob3 in l:
       for row in data:
            if row[1]==dob3:
                flag=1
                q1="update holdet set dob='{}' where full_name='{}'".format(dob2,dob3)
                curdb.execute(q1)
                db.commit()
                tk.messagebox.showinfo(' ','DATA UPDATED')
        
    else:
        tk.messagebox.showinfo(' ','ENTER VALID DETAILS')

def updat_kyc1():
    global e25,e26,e27
    s1=Toplevel(win1)
    s1.geometry("1366x768+0+0")
    s1.title("Update Mobile Number")
    s1.state("zoomed")
    frame=Frame(s1,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("U3.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e25=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e25.place(x=750,y=210)
    e26=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e26.place(x=680,y=330)
    e27=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e27.place(x=700,y=450)
    btn=tk.Button(s1,text="SUBMIT",fg="cyan",bg="black",command=updat_kyc2)
    btn.configure(width=15,height=2)
    btn.place(x=850,y=600)
    btn2=tk.Button(s1,text="BACK",fg="red",bg="black",command=s1.withdraw)
    btn2.configure(width=15,height=2)
    btn2.place(x=650,y=600)
    s1.mainloop()

def updat_kyc2():
    
    kyc1=int(e26.get())
    kyc2=int(e27.get())
    kyc3=e25.get()
    flag=0
    l=[]
    q='select * from holdet'
    curdb.execute(q)
    data=curdb.fetchall()
    
    for i in data:
        l.append(i[1])
        
    if kyc3 in l:
       for row in data:
            if row[1]==kyc3:
                flag=1
                q1="update holdet set kyc='{}' where full_name='{}'".format(kyc2,kyc3)
                curdb.execute(q1)
                db.commit()
                tk.messagebox.showinfo(' ','DATA UPDATED')
        
    else:
        tk.messagebox.showinfo(' ','ENTER VALID DETAILS')

def updat_pin1():
    global e28,e29,e30
    s1=Toplevel(win1)
    s1.geometry("1366x768+0+0")
    s1.title("Update Mobile Number")
    s1.state("zoomed")
    frame=Frame(s1,width=1920,height=1080)
    frame.place(x=0,y=0)
    i=Image.open("U4.JPG")
    i=ImageTk.PhotoImage(i)
    label=Label(frame,image=i)
    label.pack()
    e28=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e28.place(x=750,y=200)
    e29=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e29.place(x=450,y=320)
    e30=tk.Entry(s1,font="TkFixedFont",fg="#000000",highlightcolor="black")
    e30.place(x=460,y=440)
    btn=tk.Button(s1,text="SUBMIT",fg="cyan",bg="black",command=updat_pin2)
    btn.configure(width=15,height=2)
    btn.place(x=850,y=600)
    btn2=tk.Button(s1,text="BACK",fg="red",bg="black",command=s1.withdraw)
    btn2.configure(width=15,height=2)
    btn2.place(x=650,y=600)
    s1.mainloop()

def updat_pin2():
    
    pin1=e29.get()
    pin2=e30.get()
    pin3=e28.get()
    flag=0
    l=[]
    q='select * from holdet'
    curdb.execute(q)
    data=curdb.fetchall()
    
    for i in data:
        l.append(i[1])
        
    if pin3 in l:
       for row in data:
            if row[1]==pin3:
                flag=1
                q1="update holdet set pin='{}' where full_name='{}'".format(pin2,pin3)
                curdb.execute(q1)
                db.commit()
                tk.messagebox.showinfo(' ','DATA UPDATED')
        
    else:
        tk.messagebox.showinfo(' ','ENTER VALID DETAILS')



#TKINTER______________________________________________________________________________________________________________________________________________________________________________

db=pb.connect(host="localhost",user="root",passwd="nithin@792",database="pns")
curdb=db.cursor()

win1=Tk()
win1.geometry("1366x768+0+0")
win1.state("zoomed")
win1.title("Home page")
win1.config(bg="black")
box=Frame(win1,width=1920,height=1080)
box.place(x=0,y=0)
#LOGIN
def login():
    global img3
    win3=Toplevel(win1)
    win3.geometry("1366x768+0+0")
    win3.state("zoomed")
    win3.title("Login Page")
    win3.config(bg="black")
    #MAINMENU
    def mainmenu():
         global img2
         win2=Toplevel(win3)
         win2.geometry("1366x768+0+0")
         win2.title("Main Menu")
         win2.state("zoomed")
         frame=Frame(win2,width=1920,height=1080)
         frame.place(x=0,y=0)
         img2=Image.open("5.JPG")
         img2=ImageTk.PhotoImage(img2)
         label=Label(frame,image=img2)
         label.pack()
         wid1=tk.Button(win2,text="CREATE A BANK ACCOUNT",bg="black",fg="cyan",font='comic',command= create_acc)
         wid1.config(height=1,width=25)
         wid1.place(x=1000,y=150)
         wid2=tk.Button(win2,text="DEPOSIT AMOUNT",bg="black",font="comic",fg="cyan",command=deposit)
         wid2.configure(height=1,width=25)
         wid2.place(x=1000,y=200)
         wid3=tk.Button(win2,text="WITHDRAW AMOUNT",bg="black",font="comic",fg="cyan",command=withdraw)
         wid3.configure(height=1,width=25)
         wid3.place(x=1000,y=250)
         wid4=tk.Button(win2,text="UPDATE ACCOUNT DETAILS",bg="black",font="comic",fg="cyan",command=update_acc)
         wid4.configure(height=1,width=25)
         wid4.place(x=1000,y=300)
         wid5=tk.Button(win2,text="SEARCH ACCOUNT",bg="black",font="comic",fg="cyan",command=search_acc)
         wid5.configure(height=1,width=25)
         wid5.place(x=1000,y=350)
         wid6=tk.Button(win2,text="DISPLAY DETAILS",bg="black",font="comic",fg="cyan",command=dis_det)
         wid6.configure(height=1,width=25)
         wid6.place(x=1000,y=400)
         wid7=tk.Button(win2,text="DROP ACCOUNT",bg="black",font="comic",fg="cyan",command=drop_acc)
         wid7.configure(height=1,width=25)
         wid7.place(x=1000,y=450)
         wid8=tk.Button(win2,text="VIEW STATEMENT",bg="black",font="comic",fg="cyan",command=view_stt)
         wid8.config(height=1,width=25)
         wid8.place(x=1000,y=500)
         wid9=tk.Button(win2,text="EXIT PAGE",bg="black",font="comic",fg="cyan",command=exitt)
         wid9.configure(height=1,width=25)
         wid9.place(x=1000,y=550)
         win2.mainloop()
    
    def login():
        pass
    class LoginPage:
        def __init__(win,window):
            win3.window=window
            win3.state("zoomed")
            win3.window.geometry('1366x768+0+0')
            win3.window.title('Login')
            btn1=Button(win3.window,bg='Red',width=10).place(x=200,y=0)
            # background image
            win3.bg_frame=Image.open('images\\background1.png')
            photo=ImageTk.PhotoImage(win3.bg_frame)
            win3.bg_panel=Label(win3.window, image=photo)
            win3.bg_panel.image=photo
            win3.bg_panel.pack(fill='both',expand='yes')
            #Login Frame
            win3.lgn_frame=Frame(win3.window,bg='#040405',width=950,height=600)
            win3.lgn_frame.place(x=200,y=100)
            win3.heading=Label(win3.lgn_frame,text="WELCOME",font=('Times New Roman',25),bg="#040405",fg='white',bd=5,relief=FLAT)
            win3.heading.place(x=80,y=30,width=300,height=30)
            #Left Side Image
            win3.side_image=Image.open('images\\vector.png')
            photo=ImageTk.PhotoImage(win3.side_image)
            win3.side_image_label=Label(win3.lgn_frame,image=photo,bg='#040405')
            win3.side_image_label.image=photo
            win3.side_image_label.place(x=5,y=100)
            #Sign In Image
            win3.sign_in_image=Image.open('images\\hyy.png')
            photo=ImageTk.PhotoImage(win3.sign_in_image)
            win3.sign_in_image_label=Label(win3.lgn_frame,image=photo,bg='#040405')
            win3.sign_in_image_label.image=photo
            win3.sign_in_image_label.place(x=620,y=90)
            #username
            win3.username_label=Label(win3.lgn_frame,text="Username",bg="#040405",fg="#4f4e4d",font=("Times New Roman", 13, "bold"))
            win3.username_label.place(x=550, y=230)
            win3.username_entry=Entry(win3.lgn_frame,highlightthickness=0,relief=FLAT,bg="#040405",fg="#6b6a69",font=("Times New Roman",15,"bold"))
            win3.username_entry.place(x=580,y=270)
            win3.username_entry.insert(0,'admin')
            win3.username_line=Canvas(win3.lgn_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            win3.username_line.place(x=550,y=294)
            win3.username_icon=Image.open('images\\username_icon.png')
            photo=ImageTk.PhotoImage(win3.username_icon)
            win3.username_icon_label=Label(win3.lgn_frame,image=photo,bg='#040405')
            win3.username_icon_label.image=photo
            win3.username_icon_label.place(x=550,y=267)
            #login button
            win3.lgn_button=Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(win3.lgn_button)
            win3.lgn_button_label=Label(win3.lgn_frame,image=photo,bg='#040405')
            win3.lgn_button_label.image=photo
            win3.lgn_button_label.place(x=550,y=450)
            win3.login=Button(win3.lgn_button_label, text='LOGIN',font=("#b6a69",13,"bold"),width=25,bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=mainmenu)
            win3.login.place(x=20,y=10)
            #password
            win3.password_label=Label(win3.lgn_frame,text="Password",bg="#040405",fg="#4f4e4d",font=("Times New Roman",13,"bold"))
            win3.password_label.place(x=550, y=335)
            win3.password_entry=Entry(win3.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("Times New Roman",15,"bold"), show="*")
            win3.password_entry.place(x=580,y=371,width=244)
            win3.password_entry.insert(0,'admin@123')
            win3.password_line=Canvas(win3.lgn_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
            win3.password_line.place(x=550,y=395)
            #Password icon
            win3.password_icon=Image.open('images\\password_icon.png')
            photo=ImageTk.PhotoImage(win3.password_icon)
            win3.password_icon_label=Label(win3.lgn_frame,image=photo,bg='#040405')
            win3.password_icon_label.image=photo
            win3.password_icon_label.place(x=550,y=369)
            #show/hide password
            win3.show_image=ImageTk.PhotoImage \
                        (file='images\\show.png')
            win3.hide_image=ImageTk.PhotoImage \
                            (file='images\\hide.png')
            win3.show_button=Button(win3.lgn_frame,image=win3.show_image,command=win3.show,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
            win3.show_button.place(x=860, y=375)
        def show():
            win3.hide_button=Button(win3.lgn_frame,image=win3.hide_image,command=win3.hide,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
            win3.hide_button.place(x=860,y=420)
            win3.password_entry.config(show='')
        def hide():
            win3.show_button = Button(win3.lgn_frame,image=win3.show_image,command=win3.show,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
            win3.show_button.place(x=860,y=420)
            win3.password_entry.config(show='*')
           
    #Main Window
    LoginPage(win3)
    win3.mainloop()



img=Image.open("S1.JPG")
img=ImageTk.PhotoImage(img)
lab=Label(box,image=img)
lab.pack()
wid1=tk.Button(text="Enter Portal",fg="cyan",bg="black",font='helvetica',command=login)
wid1.config(height=2,width=15)
wid1.place(x=1100,y=550)
wid2=tk.Button(text="Exit Portal",fg="red",bg="black",font="comic",command=win1.destroy)
wid2.config(height=2,width=15)
wid2.place(x=1100,y=650)
win1.mainloop()

#______________________________________________________________________________________________________________________________________________________________________________________
