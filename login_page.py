from tkinter import*
import tkinter.messagebox
root1 = Tk()
root1.geometry("1400x650+0+0")
root1.title("Login Page")
root1.configure(bg='orange red')

Label(root1,text="RESTAURANT BILLING SYSTEM",fg='white',bg='orange red',font=' algerian 40 bold italic',width=40).place(x=10,y=20)

a1=StringVar()
a2=StringVar()

def enter():
	if a1.get() == "shashank" and a2.get() == "1234":
		root1.destroy()
		import questions
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		a1.set("")
		a2.set("")
def clear():
    a1.set('')
    a2.set('')



def close():
	root1.destroy()	
Label(root1,text='USER ID',fg='white',bg='orange red',font='andalus 40 ').place(x=70,y=160)
Label(root1,text="PASSWORD",fg='white',bg='orange red',font='andalus 40 ').place(x=70,y=270)
Entry(root1,bd=10,textvariable=a1,fg='mediumblue',font='papyrus 25').place(x=450,y=170)
Entry(root1,bd=10,textvariable=a2,fg='mediumblue',font='papyrus 25',show='*').place(x=450,y=280)
Button(root1,bd=10,width=8,text='ENTER',command=enter,fg='yellow',bg='mediumblue',font='forte 20 ').place(x=70,y=430)
Button(root1,bd=10,width=8,text="CLEAR",command=clear,fg='yellow',bg='mediumblue',font='forte 20').place(x=320,y=430)
Button(root1,bd=10,width=8,text='EXIT',command=close,fg='yellow',bg='mediumblue',font='forte 20').place(x=590,y=430)
#####label for tagline###########
Label(root1,text='BE',fg='maroon2',bg='cyan',font='chiller 50 bold').place(x=10,y=700)
Label(root1,text='SURE',fg='maroon2',bg='cyan',font='chiller 70 bold').place(x=640,y=700)
Label(root1,text='BUY',fg='maroon2',bg='cyan',font='chiller 60 bold').place(x=670,y=700)
Label(root1,text='PURE!!!',fg='maroon2',bg='cyan',font='chiller 70 bold').place(x=650,y=780)
Label(root1,text='Developed by:SHASHANKSINGH',bg='red',fg='yellow',font='arial 20 bold italic').place(x=910,y=550)
