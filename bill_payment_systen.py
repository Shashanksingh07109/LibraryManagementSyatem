from tkinter import*
import tkinter.messagebox
import time
import random
import mysql.connector

db=mysql.connector.connect(host='localhost',
                             user='root',
                             password='root',
                             database='bill_payment'
                             )
my_cur=db.cursor()




root = Tk()
root.geometry("1600x800+0+0")
root.title("bill payment system")
root.configure(bg='salmon1')




##### creating label of title and time ###

Label(root, font = 'algerian 50 bold', text ="BILL PAYMENT", fg = "blue2",bg='salmon1', bd = 10, anchor = 'w').place(x=350,y=10)
local_time = time.asctime(time.localtime(time.time()))
Label(root, font = 'andalus 20 bold', text = local_time, fg = "blue", bd = 10,bg='salmon1', anchor = 'w').place(x=420,y=80)


###########now on left frame  enter menu ####################################################################

#rand = StringVar()
v1= StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
v9 = StringVar()
v10 = StringVar() 
v11 = StringVar()
v12=StringVar()
v13=StringVar()
v14=StringVar()
v15=StringVar()

############
a1= StringVar()
a2 = StringVar()
a3 = StringVar()
a4 = StringVar()
a5 = StringVar()
a6 = StringVar()
a7 = StringVar()
a8 = StringVar()
a9 = StringVar()
a10 = StringVar() 



def price():
        my_cur.execute('select price from price')
        rec=my_cur.fetchall()
        fries_p=rec[0][0]
        a1.set(fries_p)
        burger_p=rec[1][0]
        a2.set(burger_p)
        Sandwich_p=rec[2][0]
        a3.set(Sandwich_p)
        drinks_p=rec[3][0]
        a4.set(drinks_p)
        Tacos_p=rec[4][0]
        a5.set(Tacos_p)
        Pasta_p=rec[5][0]
        a6.set(Pasta_p)
        Pastries_p=rec[6][0]
        a7.set(Pastries_p)
        pizza_p=rec[7][0]
        a8.set(pizza_p)
        noodles_p=rec[8][0]
        a9.set(noodles_p)
        dosa_p=rec[9][0]
        a10.set(dosa_p)
        
        v1.set('0')
        v2.set('0')
        v3.set('0')
        v4.set('0')
        v5.set('0')
        v6.set('0')
        v7.set('0')
        v8.set('0')
        v9.set('0')
        v10.set('0')
        



def total():
        fries_q = v1.get()
        burger_q = v2.get()
        Sandwich_q = v3.get()
        drinks_q = v4.get()
        Tacos_q = v5.get()
        Pasta_q = v6.get()
        Pastries_q = v7.get()
        pizza_q = v8.get()
        noodles_q = v9.get()
        dosa_q=v10.get()
        tax_q=v11.get()
        total_q=v12.get()
                
        my_cur.execute('select price from price')
        rec=my_cur.fetchall()
        
        fries_p=rec[0][0]
        burger_p=rec[1][0]
        Sandwich_p=rec[2][0]
        drinks_p=rec[3][0]        
        Tacos_p=rec[4][0]        
        Pasta_p=rec[5][0]        
        Pastries_p=rec[6][0]
        pizza_p=rec[7][0]        
        noodles_p=rec[8][0]
        dosa_p=rec[9][0]

        
        t1=int(fries_q)*int(fries_p)
        t2=int(burger_q)*int(burger_p)
        t3=int(Sandwich_q)*int(Sandwich_p)
        t4=int(drinks_q)*int(drinks_p)
        t5=int(Tacos_q)*int(Tacos_p)
        t6=int(Pasta_q)*int(Pasta_p)
        t7=int(Pastries_q)*int(Pastries_p)
        t8=int(pizza_q)*int(pizza_p)
        t9=int(noodles_q)*int(noodles_p)
        t10=int(dosa_q)*int(dosa_p)
        tot=t1+t2+t3+t4+t5+t6+t7+t8+t9+t10
        v13.set(str(tot))

        gst=(tot)*0.18
        v14.set(str(gst))
        net=int(gst)+int(tot)
        v15.set(str(net))

        x=random.randint(23133,33344)
        random_total=str(x)
        v11.set(random_total)

def Print():
        root.destroy()
        print(tot)

def qexit():
        root.destroy()


def reset():
	v1.set("")
	v2.set("")
	v3.set("")
	v4.set("")
	v5.set("")
	v6.set("")
	v7.set("")
	v8.set("")
	v9.set("")
	v10.set("")
	v11.set("")
	v12.set("")
	v13.set("")
	v14.set("")
	v15.set("")

Label(root, font=('arial',16,'bold'),text = "Order No", bg='salmon1',bd = 16, anchor = 'w').place(x=880,y=250)
Label(root, font=('arial',16,'bold'),text = "Fries",bg='salmon1', bd = 16, anchor = 'w' ).place(x=10,y=250)
Label(root, font=('arial',16,'bold'),text = "Burger", bg='salmon1',bd = 16, anchor = 'w' ).place(x=10,y=300)
Label(root, font=('arial',16,'bold'),text = "Sandwich", bg='salmon1',bd = 16, anchor = 'w' ).place(x=10,y=350)
Label(root, font=('arial',16,'bold'),text = "Drinks", bg='salmon1',bd = 16, anchor = 'w' ).place(x=10,y=400)
Label(root, font=('arial',16,'bold'),text = "Tacos", bg='salmon1',bd = 16, anchor = 'w' ).place(x=10,y=450)
Label(root, font=('arial',16,'bold'),text = "Pasta", bg='salmon1',bd = 16, anchor = 'w' ).place(x=450,y=250)
Label(root, font=('arial',16,'bold'),text = "Pastries",bg='salmon1', bd = 16, anchor = 'w' ).place(x=450,y=300)
Label(root, font=('arial',16,'bold'),text = "Pizza", bg='salmon1',bd = 16, anchor = 'w' ).place(x=450,y=350)
Label(root, font=('arial',16,'bold'),text = "Noodles", bg='salmon1',bd = 16, anchor = 'w' ).place(x=450,y=400)
Label(root, font=('arial',16,'bold'),text = "Dosa", bg='salmon1',bd = 16, anchor = 'w' ).place(x=450,y=450)
Label(root, font=('arial',16,'bold'),text = "Customer name",bg='salmon1', bd = 16, anchor = 'w' ).place(x=880,y=300)
Label(root, font=('arial',16,'bold'),text = "Total Amount", bg='salmon1',bd = 16, anchor = 'w' ).place(x=880,y=350)
Label(root, font=('arial',16,'bold'),text = "GST", bg='salmon1',bd = 16, anchor = 'w' ).place(x=880,y=400)
Label(root, font=('arial',16,'bold'),text = "Net Amount",bg='salmon1', bd = 16, anchor = 'w' ).place(x=880,y=450)


#labelingf for rate and quantity

Label(root, font=('arial',16,'bold'),text = "RATE", bg='salmon1',bd = 16, anchor = 'w').place(x=140,y=170)
Label(root, font=('arial',16,'bold'),text = "QUANTITY", bg='salmon1',bd = 16, anchor = 'w').place(x=260,y=170)
Label(root, font=('arial',16,'bold'),text = "RATE", bg='salmon1',bd = 16, anchor = 'w').place(x=580,y=170)
Label(root, font=('arial',16,'bold'),text = "QUANTITY", bg='salmon1',bd = 16, anchor = 'w').place(x=690,y=170)



#entry for price
Entry(root,font=('arial',16,'bold'), textvariable=a1, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=140,y=250)
Entry(root,font=('arial',16,'bold'), textvariable=a2, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=140,y=300)
Entry(root,font=('arial',16,'bold'), textvariable=a3, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=140,y=350)
Entry(root,font=('arial',16,'bold'), textvariable=a4, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=140,y=400)
Entry(root,font=('arial',16,'bold'), textvariable=a5, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=140,y=450)
Entry(root,font=('arial',16,'bold'), textvariable=a6, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=580,y=250)
Entry(root,font=('arial',16,'bold'), textvariable=a7, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=580,y=300)
Entry(root,font=('arial',16,'bold'), textvariable=a8, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=580,y=350)
Entry(root,font=('arial',16,'bold'), textvariable=a9, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=580,y=400)
Entry(root,font=('arial',16,'bold'), textvariable=a10, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=580,y=450)
	
#entry for quantity
Entry(root,font=('arial',16,'bold'), textvariable=v1, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=270,y=250)
Entry(root,font=('arial',16,'bold'), textvariable=v2, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=270,y=300)
Entry(root,font=('arial',16,'bold'), textvariable=v3, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=270,y=350)
Entry(root,font=('arial',16,'bold'), textvariable=v4, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=270,y=400)
Entry(root,font=('arial',16,'bold'), textvariable=v5, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=270,y=450)
Entry(root,font=('arial',16,'bold'), textvariable=v6, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=710,y=250)
Entry(root,font=('arial',16,'bold'), textvariable=v7, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=710,y=300)
Entry(root,font=('arial',16,'bold'), textvariable=v8, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=710,y=350)
Entry(root,font=('arial',16,'bold'), textvariable=v9, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=710,y=400)
Entry(root,font=('arial',16,'bold'), textvariable=v10, bd=10, insertwidth =4,width=7,bg = "linen", justify ='right').place(x=710,y=450)


#####entry for gst & total #########
Entry(root,font=('arial',16,'bold'), textvariable=v11,bd=10, insertwidth =4,width=18,bg = "linen", justify ='right').place(x=1070,y=250)
Entry(root,font=('arial',16,'bold'), textvariable=v12, bd=10, insertwidth =4,width=18,bg = "linen", justify ='right').place(x=1070,y=300)
Entry(root,font=('arial',16,'bold'), textvariable=v13, bd=10, insertwidth =4,width=18,bg = "linen", justify ='right').place(x=1070,y=350)
Entry(root,font=('arial',16,'bold'), textvariable=v14, bd=10, insertwidth =4,width=18,bg = "linen", justify ='right').place(x=1070,y=400)
Entry(root,font=('arial',16,'bold'), textvariable=v15, bd=10, insertwidth =4,width=18,bg = "linen", justify ='right').place(x=1070,y=450)


### right Frame Button ###########

Button(root,bd= 16,fg= "black", font=('arial',16,'bold'), width=10, text= "Total",command=total, bg= "aquamarine").place(x=100,y=550)
Button(root,bd= 16,fg= "black", font=('arial',16,'bold'), width=10, text= "Price",command=price, bg= "aquamarine").place(x=380,y=550)
Button(root,bd= 16,fg= "black", font=('arial',16,'bold'), width=10, text= "Reset",command=reset, bg= "aquamarine").place(x=690,y=550)
Button(root,bd= 16,fg= "black", font=('arial',16,'bold'), width=10, text= "Exit",command=qexit, bg= "aquamarine").place(x=1000,y=550)


root.mainloop()

