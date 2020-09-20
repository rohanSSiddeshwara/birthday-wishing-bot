from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import math
import smtplib
import tkinter.scrolledtext as st
import pyautogui as pa
import datetime

root=Tk()
root.title("Email Sender")
root.configure(bg="#10031a")
root.geometry("320x400")

def submit_pressed(name_i,date_i,month_i,phno_i,root1):
    try:
        name=name_i.get()
        date=date_i.get()
        phno=phno_i.get()
        month=month_i.get()
        if int(date)>31 or int(month)>12:
                name=Label(root1,text='Enter a valid date and month',bg='#10031a',fg='white')
                name.place(x=10,y=10)
                date_i.delete(0,END)
                month_i.delete(0,END)
        elif int(month)==2:
            if int(date)>29:
                name=Label(root1,text='Enter a valid date and month',bg='#10031a',fg='white')
                name.place(x=10,y=10)
                name_i.delete(0,END)
                date_i.delete(0,END)
                month_i.delete(0,END)
        elif phno=="" or phno.isalpha():
            name=Label(root1,text='Enter a valid phone number',bg='#10031a',fg='white')
            name.place(x=10,y=10)
            phno_i.delete(0,END)
        else:
            with open('Birth_input.txt','a') as f:
                f.write(name+"="+month+"-"+date+"="+phno+"\n")
            name=Label(root1,text='added successfully',bg='#10031a',fg='white')
            name.place(x=10,y=250)
            name_i.delete(0,END)
            date_i.delete(0,END)
            phno_i.delete(0,END)
            month_i.delete(0,END)
            root1.destroy()



    except Exception as e:
        name_i.delete(0,END)
        date_i.delete(0,END)
        phno_i.delete(0,END)
        month_i.delete(0,END)
        name=Label(root1,text='Enter a valid input',bg='#10031a',fg='white')
        name.place(x=10,y=10)



def add_bd_pressed():
    root1=Tk()
    root1.title("Email Sender")
    root1.configure(bg="#10031a")
    root1.geometry("320x400")

    label=Label(root1,text='WELCOME',bg='#10031a',fg='white')
    label.place(x=137,y=50)

    name_l=Label(root1,text='Name: ',bg='#10031a',fg='white')
    name_l.place(x=77,y=80)
    name_i=Entry(root1,width=30,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
    name_i.place(x=77,y=110)


    date_l=Label(root1,text='Date: ',bg='#10031a',fg='white')
    date_l.place(x=77,y=140)
    date_i=Entry(root1,width=30,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
    date_i.place(x=77,y=170)

    month_l=Label(root1,text='month: ',bg='#10031a',fg='white')
    month_l.place(x=77,y=200)
    month_i=Entry(root1,width=30,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
    month_i.place(x=77,y=230)

    phno_l=Label(root1,text='Phone No: ',bg='#10031a',fg='white')
    phno_l.place(x=77,y=260)
    phno_i=Entry(root1,width=30,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
    phno_i.place(x=77,y=290)

    submit_b=Button(root1,text='Submit',bg='#ff6f00',fg='black',command=lambda:submit_pressed(name_i,date_i,month_i,phno_i,root1),relief='groove',borderwidth=0)
    submit_b.place(x=240,y=350)


def view_birdays():
    root2=Tk()
    root2.title("Email Sender")
    root2.configure(bg="#10031a")
    root2.geometry("320x400")
    Y=5
    with open('Birth_input.txt','r') as f:
        for line in f:
            a,b,c=line.split("=")
            label=Label(root2,text="{}            {}           {}".format(a.upper(),b,c),bg='#10031a',fg='white')
            label.place(x=10,y=Y)
            Y+=15
    submit_b=Button(root2,text='exit',bg='#ff6f00',fg='black',command=root2.destroy,relief='groove',borderwidth=0)
    submit_b.place(x=170,y=350)



def send():
    D=datetime.date.today()
    with open('Birth_input.txt','r') as f:
        Y=130
        X=10
        C=[]
        pa.moveTo(779,10,1)
        pa.click()
        pa.sleep(15)

        for line in f:
            a,b,c=line.split("=")
            month,day=b.split("-")
            if str(D.day)==day and str(D.month)==month:
                name=Label(root,text="{}  {}  {} ".format(a,b,c),bg='#10031a',fg='white')
                name.place(x=77,y=Y)
                Y +=30
                pa.moveTo(90,140,1)
                pa.click()
                pa.typewrite(c,1)
                pa.sleep(5)
                pa.press('enter')
                pa.sleep(5)
                pa.moveTo(390,740,1)
                pa.click()
                pa.sleep(5)
                pa.typewrite("happy birthday",0.1)
                pa.press('enter')


submit_a=Button(root,text='Add birthday',bg='#ff6f00',fg='black',command=add_bd_pressed,relief='groove',borderwidth=0)
submit_a.place(x=10,y=10)


submit_b=Button(root,text='view birthday',bg='#ff6f00',fg='black',command=view_birdays,relief='groove',borderwidth=0)
submit_b.place(x=10,y=50)

D=datetime.date.today()
with open('Birth_input.txt','r') as f:
    Y=130
    X=10
    C=[]
    for line in f:
        a,b,c=line.split("=")
        month,day=b.split("-")
        if str(D.day)==day and str(D.month)==month:
            name=Label(root,text="{}  {}  {} ".format(a,b,c),bg='#10031a',fg='white')
            name.place(x=77,y=Y)
            Y +=30

submit_b=Button(root,text='send birthday wish',bg='#ff6f00',fg='black',relief='groove',borderwidth=0,command=lambda:send())
submit_b.place(x=X,y=Y+50)






root.mainloop()
