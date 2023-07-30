from tkinter import *
from tkinter import messagebox


root2=Tk()
root2.geometry('1100x800')
root2.title("Menu")
root2.configure(bg='orange red')



def enter1():
    root2.destroy()
    import bill_payment_systen
def enter2():
    root2.destroy()
    import update

Label(root2,text='YOU WANT TO --->',fg='black',bg='orange red',font='algerian 50 italic').place(x=30,y=70)

Label(root2,text='BILL',fg='blue',bg='orange red',font='forte 40 bold ').place(x=150,y=200)
Label(root2,text='CHANGE PRICES',fg='blue',bg='orange red',font='forte 40 bold ').place(x=70,y=300)

Button(root2,text='press here',fg='red',bg='bisque',font='forte 20 bold',bd=8,command=enter1).place(x=600,y=200)
Button(root2,text='press here',fg='green',bg='bisque',font='forte 20 bold',bd=10,command=enter2).place(x=600,y=300)

Label(root2,text='BE',fg='yellow',bg='orange red',font='andalus 50 bold').place(x=50,y=500)
Label(root2,text='SURE',fg='yellow',bg='orange red',font='andalus 50 bold').place(x=170,y=500)
Label(root2,text='BUY',fg='yellow',bg='orange red',font='andalus 50 bold').place(x=360,y=500)
Label(root2,text='PURE!!!',fg='yellow',bg='orange red',font='andalus 50 bold').place(x=550,y=500)


