import tkinter as tk
import webbrowser
import tkinter.font as tkfont
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
def login():
    pass
class LoginPage:
    def __init__(win,window):
        win.window=window
        win.window.overrideredirect(True)
        win.window.geometry('1366x768+0+0')
        win.window.title('Login')
        btn1=Button(win.window,bg='Red',width=10).place(x=200,y=10)
        # background image
        win.bg_frame=Image.open('images\\background1.png')
        photo=ImageTk.PhotoImage(win.bg_frame)
        win.bg_panel=Label(win.window, image=photo)
        win.bg_panel.image=photo
        win.bg_panel.pack(fill='both',expand='yes')
        #Login Frame
        win.lgn_frame=Frame(win.window,bg='#040405',width=950,height=600)
        win.lgn_frame.place(x=200,y=100)
        win.txt="WELCOME"
        win.heading=Label(win.lgn_frame,text=win.txt,font=('Times New Roman',25),bg="#040405",fg='white',bd=5,relief=FLAT)
        win.heading.place(x=80,y=30,width=300,height=30)
        #Left Side Image
        win.side_image=Image.open('images\\vector.png')
        photo=ImageTk.PhotoImage(win.side_image)
        win.side_image_label=Label(win.lgn_frame,image=photo,bg='#040405')
        win.side_image_label.image=photo
        win.side_image_label.place(x=5,y=100)
        #Sign In Image
        win.sign_in_image=Image.open('images\\hyy.png')
        photo=ImageTk.PhotoImage(win.sign_in_image)
        win.sign_in_image_label=Label(win.lgn_frame,image=photo,bg='#040405')
        win.sign_in_image_label.image=photo
        win.sign_in_image_label.place(x=620,y=90)
        #username
        win.username_label=Label(win.lgn_frame,text="Username",bg="#040405",fg="#4f4e4d",font=("Times New Roman", 13, "bold"))
        win.username_label.place(x=550, y=230)
        win.username_entry=Entry(win.lgn_frame,highlightthickness=0,relief=FLAT,bg="#040405",fg="#6b6a69",font=("Times New Roman", 12))
        win.username_entry.place(x=580,y=270)
        win.username_line=Canvas(win.lgn_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
        win.username_line.place(x=550,y=294)
        win.username_icon=Image.open('images\\username_icon.png')
        photo=ImageTk.PhotoImage(win.username_icon)
        win.username_icon_label=Label(win.lgn_frame,image=photo,bg='#040405')
        win.username_icon_label.image=photo
        win.username_icon_label.place(x=550,y=267)
        #login button
        win.lgn_button=Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(win.lgn_button)
        win.lgn_button_label=Label(win.lgn_frame,image=photo,bg='#040405')
        win.lgn_button_label.image=photo
        win.lgn_button_label.place(x=550,y=450)
        win.login=Button(win.lgn_button_label, text='LOGIN',font=("#b6a69",13,"bold"),width=25,bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=login())
        win.login.place(x=20,y=10)
        #password
        win.password_label=Label(win.lgn_frame,text="Password",bg="#040405",fg="#4f4e4d",font=("Times New Roman",13,"bold"))
        win.password_label.place(x=550, y=335)
        win.password_entry=Entry(win.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("Times New Roman",12,"bold"), show="*")
        win.password_entry.place(x=580,y=371,width=244)
        win.password_line=Canvas(win.lgn_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
        win.password_line.place(x=550,y=395)
        #Password icon
        win.password_icon=Image.open('images\\password_icon.png')
        photo=ImageTk.PhotoImage(win.password_icon)
        win.password_icon_label=Label(win.lgn_frame,image=photo,bg='#040405')
        win.password_icon_label.image=photo
        win.password_icon_label.place(x=550,y=369)
        #show/hide password
        win.show_image=ImageTk.PhotoImage \
                        (file='images\\show.png')
        win.hide_image=ImageTk.PhotoImage \
                        (file='images\\hide.png')
        win.show_button=Button(win.lgn_frame,image=win.show_image,command=win.show,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
        win.show_button.place(x=860, y=375)
    def show(win):
        win.hide_button=Button(win.lgn_frame,image=win.hide_image,command=win.hide,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
        win.hide_button.place(x=860,y=420)
        win.password_entry.config(show='')
    def hide(win):
        win.show_button = Button(win.lgn_frame,image=win.show_image,command=win.show,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
        win.show_button.place(x=860,y=420)
        win.password_entry.config(show='*')
#Main Window
window = Tk()
LoginPage(window)
window.mainloop()
