from tkinter import *
from tkinter import messagebox
import time
import mysql.connector

db=mysql.connector.connect(host='localhost',
                             user='root',
                             password='root',
                             database='bill_payment'
                             )
my_cur=db.cursor()


root5=Tk()
root5.title('update values')
root5.geometry('730x700')
root5.configure(bg='red')



v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()

def clear():
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')

def search():
    item_no=v1.get()
        
    my_cur.execute('select itemname,price,type from price where itemno=%s',(item_no,))
    rec=my_cur.fetchall()
    v2.set(rec[0][0])
    v3.set(rec[0][1])
    v4.set(rec[0][2])

def update():
    item_no=v1.get()
    item_name=v2.get()
    item_pri=v3.get()
    item_type=v4.get()
    my_cur.execute('update price set itemname=%s,price=%s,type=%s where itemno=%s',(item_name,item_pri,item_type,int(item_no)))
    db.commit()
    messagebox.showinfo('congarats','recoard updated')

def delete():
        item_no=v1.get()
        item_name=v2.get()
        item_pri=v3.get()
        item_type=v4.get()
        v1.set('')
        v2.set('')
        v3.set('')
        v4.set('')
        my_cur.execute('delete from price where itemno=%s',(item_no,))
        db.commit()
        messagebox.showinfo('congarats','recoard deleted')

def submit():
    item_no=v1.get()
    item_name=v2.get()
    item_pri=v3.get()
    item_type=v4.get()
    my_cur.execute('insert into price(itemno,itemname,price,type) values(%s,%s,%s,%s)',(int(item_no),item_name,int(item_pri),item_type))
    db.commit()
    messagebox.showinfo('congarats','recoard submitted')

def back():
    root5.destroy()
    import questions

def enter():
    root5.destroy()
    import bill_payment_systen

##### creating label of title and time ###

Label(root5,text='UPDATE RECORD',fg='black',bg='red',font='algerian 50 bold italic',width=15).place(x=50,y=20)
local_time = time.asctime(time.localtime(time.time()))
Label(root5, font = 'arial 20 bold', text = local_time, fg = "black", bd = 10,bg='red', anchor = 'w').place(x=100,y=100)



    
Label(root5,text='ITEM_NO',fg='black',bg='red',font='arial 25 bold italic').place(x=30,y=190)
Label(root5,text='ITEM_NAME',fg='black',bg='red',font='arial 25 bold italic').place(x=30,y=260)
Label(root5,text='PRICE',fg='black',bg='red',font='arial 25 bold italic').place(x=30,y=330)
Label(root5,text='TYPE',fg='black',bg='red',font='arial 25 bold italic').place(x=30,y=400)


Entry(root5,textvariable=v1,bd=10,width=20,font='arial 20 bold italic').place(x=350,y=180)
Entry(root5,textvariable=v2,bd=10,width=20,font='arial 20 bold italic').place(x=350,y=250)
Entry(root5,textvariable=v3,bd=10,width=20,font='arial 20 bold italic').place(x=350,y=320)
Entry(root5,textvariable=v4,bd=10,width=20,font='arial 20 bold italic').place(x=350,y=390)


Button(root5,text='SEARCH',fg='black',bg='linen',bd=10,font='arial 14 bold',command=search).place(x=30,y=500)
Button(root5,text='UPDATE',fg='black',bg='linen',bd=10,font='arial 14 bold',command=update).place(x=190,y=500)
Button(root5,text='DELETE',fg='black',bg='linen',bd=10,font='arial 14 bold',command=delete).place(x=350,y=500)
Button(root5,text='CLEAR',fg='black',bg='linen',bd=10,font='arial 14 bold',command=clear).place(x=520,y=500)
Button(root5,text='SUBMIT',fg='black',bg='linen',bd=10,font='arial 14 bold',command=submit).place(x=120,y=600)
Button(root5,text='BACK',fg='black',bg='linen',bd=10,font='arial 14 bold',command=back).place(x=300,y=600)
Button(root5,text='BILL',fg='black',bg='linen',bd=10,font='arial 14 bold',command=enter).place(x=450,y=600)


