from tkinter import *
from tkinter import messagebox
import mysql.connector
db=mysql.connector.connect(host='localhost',
                          user='root',
                          password='root',
                          database='library'
                          )
my_cur=db.cursor()
                          

root=Tk()
root.title('shashank')
root.geometry('2000x2000')
root.configure(bg='red')
    

def close():

    a1.set('')
    a2.set('')
    
def back():
    root.destroy()

def main_frm():
    root=Tk()
    root.title('python')
    root.geometry('1000x1000')
    root.configure(bg='red')
    Label(root,text='ALL BOOKS ARE AVAILABLE',bg='red',fg='yellow',font='arial 40 bold italic').place(x=150,y=20)
    def member_info():
        root.destroy()
        members()
    Button(root,text='Members',bg='white',font='arial 18 bold italic',command=member_info,width=20).place(x=150,y=150)
    def book_info():
        root.destroy()
        books()
    
    Button(root,text='Books',bg='white',font='arial 18 bold italic ',command=book_info,width=20).place(x=150,y=250)
    Button(root,text='Issue/deposite',bg='white',font='arial 18 bold italic',command=issue,width=20).place(x=150,y=350)
    Button(root,text='~Exit',command=root.destroy,bg='blue',font='arial 18 italic bold',width=10).place(x=200,y=550)



def members():
    root=Tk()
    root.title('python')
    root.geometry('1000x1000')
    root.configure(bg='green')
    def close():
        v1.set('')
        v2.set('')
        v3.set('')
        v4.set('')
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
    def search():
        mem_num=v1.get()
        my_cur.execute('select membername,membermobilenumber,memberaddress from member where membernumber=%s',(mem_num,))
        rec=my_cur.fetchall()
        v2.set(rec[0][0])
        v3.set(rec[0][1])
        v4.set(rec[0][2])
    def update():
        mem_num=v1.get()
        mem_name=v2.get()
        mem_mobi=v3.get()
        mem_add=v4.get()
        my_cur.execute('update member set membername=%s,membermobilenumber=%s,memberaddress=%s where membernumber=%s',(mem_name,mem_mobi,mem_add,int(mem_num)))
        db.commit()
        messagebox.showinfo('congarats','recoard updated')
    def submit():
        mem_num=v1.get()
        mem_name=v2.get()
        mem_mobi=v3.get()
        mem_add=v4.get()
        my_cur.execute('insert into member(membernumber,membername,membermobilenumber,memberaddress) values(%s,%s,%s,%s)',(int(mem_num),mem_name,int(mem_mobi),mem_add))
        db.commit()
        messagebox.showinfo('congarats','recoard updated')
    def delete():
        mem_num=v1.get()
        mem_name=v2.get()
        mem_mobi=v3.get()
        mem_add=v4.get()
        my_cur.execute('delete from member where membernumber=%s',(mem_num,))
        db.commit()
        messagebox.showinfo('congarats','recoard deleted')
    Label(root,text='ALL MEMBERS DETAILS',bg='red',fg='yellow',font='arial 40 bold italic').place(x=150,y=20)
    Label(root,text='Members number',bg='yellow',font='arial 20 bold italic').place(x=40,y=150)
    Label(root,text='Members name',bg='yellow',font='arial 20 bold italic').place(x=40,y=225)
    Label(root,text='Members mobilenumber',bg='yellow',font='arial 20 bold italic').place(x=40,y=300)
    Label(root,text='Members address',bg='yellow',font='arial 20 bold italic').place(x=40,y=375)

    Entry(root,textvariable=v1,width=15,font='arial 20 bold italic').place(x=400,y=150)
    Entry(root,textvariable=v2,width=15,font='arial 20 bold italic').place(x=400,y=225)
    Entry(root,textvariable=v3,width=15,font='arial 20 bold italic').place(x=400,y=300)
    Entry(root,textvariable=v4,width=15,font='arial 20 bold italic').place(x=400,y=375)
    Button(root,text='<--Exit',bg='orange',font='arial 15 italic bold',command=root.destroy,width=20).place(x=100,y=500)
    Button(root,text='clear',command=close,bg='orange',font='arial 15 italic bold',width=20).place(x=400,y=500)
    Button(root,text='UPDATE MEMBER',command=update,bg='black',fg='yellow',font='arial 20 bold italic').place(x=700,y=600)
    Button(root,text='DELETE MEMBER',command=delete,bg='black',fg='yellow',font='arial 20 bold italic').place(x=400,y=600)
    Button(root,text='SEARCH MEMBER',command=search,bg='black',fg='yellow',font='arial 20 bold italic').place(x=700,y=150)
    Button(root,text='SUBMIT',command=submit,bg='orange',font='arial 15 italic bold',width=20).place(x=100,y=600)

    
    
   
    

def books():
    root=Tk()
    root.title('python')
    root.geometry('1000x1000')
    root.configure(bg='brown')
    def close():
        v5.set('')
        v6.set('')
        v7.set('')
        v8.set('')
        v9.set('')
        
    v5=StringVar()
    v6=StringVar()
    v7=StringVar()
    v8=StringVar()
    v9=StringVar()
    
    

    def search():
        book_num=v5.get()
        my_cur.execute('select bookname,writer,publisher,price from book where booknumber=%s',(book_num,))
        rec=my_cur.fetchall()
        v6.set(rec[0][0])
        v7.set(rec[0][1])
        v8.set(rec[0][2])
        v9.set(rec[0][3])

    def update():
        book_num=v5.get()
        book_name=v6.get()
        book_wname=v7.get()
        book_pub=v8.get()
        book_pri=v9.get()
        my_cur.execute('update book set bookname=%s,writer=%s,publisher=%s,price=%s where booknumber=%s',(book_name,book_wname,book_pub,book_pri,int(book_num)))
        db.commit()
        messagebox.showinfo('congarats','recoard updated')
    def submit():
        book_num=v5.get()
        book_name=v6.get()
        book_wname=v7.get()
        book_pub=v8.get()
        book_pri=v9.get()
        my_cur.execute('insert into book(booknumber,bookname,writer,publisher,price) values(%s,%s,%s,%s,%s)',(int(book_num),book_name,book_wname,book_pub,int(book_pri)))
        db.commit()
        messagebox.showinfo('congarats','recoard submitted')
    def delete():
        book_num=v5.get()
        book_name=v6.get()
        book_wname=v7.get()
        book_pub=v8.get()
        book_pri=v9.get()

        my_cur.execute('delete from book where booknumber=%s',(book_num,))
        db.commit()
        messagebox.showinfo('congarats','recoard deleted')
    
    Label(root,text='ALL BOOKS DETAILS',bg='red',fg='yellow',font='arial 40 bold italic').place(x=150,y=20)
    Label(root,text='writer name',bg='white',fg='red',font='arial 20 bold italic').place(x=40,y=300)

    
    Label(root,text='Book name',bg='white',fg='red',font='arial 20 bold italic').place(x=40,y=220)
    Label(root,text='ISBN number ',bg='white',fg='red',font='arial 20 bold italic').place(x=40,y=150)
    Label(root,text='Publisher',bg='white',fg='red',font='arial 20 bold italic').place(x=40,y=375)
    Label(root,text='Price',bg='white',fg='red',font='arial 20 bold italic').place(x=40,y=450)

    Entry(root,textvariable=v5,width=15,font='arial 20 bold italic').place(x=300,y=150)
    Entry(root,textvariable=v6,width=15,font='arial 20 bold italic').place(x=300,y=225)
    Entry(root,textvariable=v7,width=15,font='arial 20 bold italic').place(x=300,y=300)
    Entry(root,textvariable=v8,width=15,font='arial 20 bold italic').place(x=300,y=375)
    Entry(root,textvariable=v9,width=15,font='arial 20 bold italic').place(x=300,y=450)
    
    

    Button(root,text='Clear',command=close,bg='orange',font='arial 15 italic bold',width=20).place(x=400,y=500)
    Button(root,text='<--Exit',bg='orange',font='arial 15 italic bold',width=20,command=root.destroy).place(x=100,y=500)
    Button(root,text='UPDATE MEMBER',command=update,bg='black',fg='yellow',font='arial 20 bold italic').place(x=700,y=600)
    Button(root,text='DELETE MEMBER',command=delete,bg='black',fg='yellow',font='arial 20 bold italic').place(x=400,y=600)
    Button(root,text='SEARCH MEMBER',command=search,bg='black',fg='yellow',font='arial 20 bold italic').place(x=700,y=150)
    Button(root,text='SUBMIT',command=submit,bg='orange',font='arial 15 italic bold',width=20).place(x=100,y=600)

    
 
def issue():
    root=Tk()
    root.title('python')
    root.geometry('1000x1000')
    root.configure(bg='orange')
    b1=StringVar()
    b2=StringVar()
    b3=StringVar()
    b4=StringVar()
    Label(root,text='ISSUE DETAILS',bg='red',fg='yellow',font='arial 40 bold italic').place(x=150,y=20)

    Label(root,text='Issue',bg='black',fg='yellow',font='arial 20 bold italic').place(x=40,y=150)
    Label(root,text='Issue date',bg='black',fg='yellow',font='arial 20 bold italic').place(x=40,y=220)
    Label(root,text='Deposite date',bg='black',fg='yellow',font='arial 20 bold italic').place(x=40,y=300)
    Label(root,text='Issuer name',bg='black',fg='yellow',font='arial 20 bold italic').place(x=40,y=370)
    
    Entry(root,textvariable=b1,width=15,font='arial 20 bold italic').place(x=240,y=150)
    Entry(root,textvariable=b2,width=15,font='arial 20 bold italic').place(x=240,y=225)
    Entry(root,textvariable=b3,width=15,font='arial 20 bold italic').place(x=240,y=300)
    Entry(root,textvariable=b4,width=15,font='arial 20 bold italic').place(x=240,y=375)
    Button(root,text='Clear',command=clear,bg='yellow',font='arial 15 italic bold',width=20).place(x=400,y=500)
    Button(root,text='<--Exit',command=root.destroy,bg='yellow',font='arial 15 italic bold',width=20).place(x=100,y=500)



a1=StringVar()
a2=StringVar()

Label(root,text='MADE BY\nSHASHANK SINGH',bg='black',fg='yellow',font='arial 22 bold italic').place(x=850,y=400)



Label(root,text='Library management System',bg='red',fg='yellow',font='arial 40 bold italic').place(x=150,y=30)
Label(root,text='User id/email',bg='red',font='arial 20 bold italic').place(x=100,y=200)
Label(root,text='Password',bg='red',font='arial 20 bold italic').place(x=100,y=300)



Entry(root,textvariable=a1,width=15,font='arial 20 bold italic').place(x=300,y=200)
Entry(root,textvariable=a2,width=15,font='arial 20 bold italic',show='x').place(x=300,y=300)


      

def login(): 
    uid=a1.get()
    pw=a2.get()
    query='select * from login'
    user='shashank'
    password='root'
    
    
    
    if uid==user and pw==password:
        root.destroy()
        main_frm()
    else:
        messagebox.showinfo('sorry','plese try again')

    
Button(root,text='Login',command=login,bg='purple',font='arial 18 italic bold',width=10).place(x=100,y=500)

Button(root,text='<--Exit',command=back,bg='sky blue',font='arial 18 italic bold',width=10).place(x=300,y=500)
    
Button(root,text='Clear',command=close,bg='indigo',font='arial 18 italic bold',width=10).place(x=500,y=500)

