from tkinter import *
import tkinter as tk
import cx_Oracle
import CONN
import random
import datetime

import admin
from tkinter import  ttk
from tkinter import messagebox
connection = cx_Oracle.connect('project/12345@//localhost:1522/pdborcl')
cursor = connection.cursor()
global top,user,pitems,count,pizzacombo,sp11,sp12,sp13,Sitems,specialcombo,tree,top1,dll,ddd,pty,regEntry3,tamount
global ss1,ss2,ss3,bitems,sb1,sb2,sb3,bevcombo,d1,dessertspin,descombo,a1,aitems,appcombo,ic1,ic2,icitems,dealcombo,totalamountlabel

acntno=0
acntname=''
tamount=0
count=1
paylst=[]
pizzalst=[]
pizzaprice=[]
speciallst=[]
spprice=[]
beveragelst=[]
bevprice=[]
dessertlst=[]
desprice=[]
deallst=[]
dp=[]
appetizerlst=[]
appiprice=[]
icecreamlst=[]
icecprice=[]

def pizza():
    cursor.execute("""SELECT i.item_name from items i inner join category c  on (i.cat_id=c.cat_id) where c.cat_name = 'Pizza'""")
    row=cursor.fetchall()
    for i in row:
        pizzalst.append(i[0])
def pizzasize():
    pp=pitems.get()
    sql= "select item_id from items where item_name= :x"
    cursor.execute(sql,x=pp)
    itemselected = cursor.fetchall()
    if str(sp11.get()) != "0":
        sql="SELECT price from price where item_id=:x and size_id=3 "
        cursor.execute(sql,x=itemselected[0][0])
        rowx=cursor.fetchall()
        pizzaprice.append(rowx)
    elif str(sp12.get()) !="0":
        cursor.execute(
        """SELECT price from price where item_id= :x and size_id = 2 """,x=itemselected[0][0])
        rowy=cursor.fetchall()
        pizzaprice.append(rowy)

    elif str(sp13.get()) !="0":
        cursor.execute(
            """SELECT price from price where item_id= :x and size_id=1 """, x=itemselected[0][0])
        rowz = cursor.fetchall()
        pizzaprice.append(rowz)
def ic():
    cursor.execute("""SELECT i.item_name from items i inner join category c  on (i.cat_id=c.cat_id) where c.cat_name = 'Icecream'""")
    row=cursor.fetchall()
    for i in row:
        icecreamlst.append(i[0])
def icasize():
    ici=icitems.get()
    sql= "select item_id from items where item_name= :x"
    cursor.execute(sql,x=ici)
    itemselected = cursor.fetchall()
    if ic1.get() > '0':
        sql="SELECT price from price where item_id=:x and size_id=4 "
        cursor.execute(sql,x=itemselected[0][0])
        rowx=cursor.fetchall()
        icecprice.append(rowx)
    elif ic2.get() >  '0':
        cursor.execute(
        """SELECT price from price where item_id= :x and size_id = 5 """,x=itemselected[0][0])
        rowy=cursor.fetchall()
        icecprice.append(rowy)
def addictotree():
    icasize()
    global count,tree, recordvalues, sp11, sp12, sp13,tamount
    recordvalues = [count, icitems.get()]
    icl = ic1.get()
    icm = ic2.get()
    if (icl =='0' and icm =='0' ):
        messagebox.showerror("Error","Select a size ")
    elif (icl !='0' and icm !='0' ):
        messagebox.showerror("Error","Select 1 size at a time")
    else:
        if icl != '0':
            recordvalues.insert(2, "245g")
            recordvalues.append(icl)
            recordvalues.insert(4, icecprice[0])
        elif icm != '0':
            recordvalues.insert(2, "475g")
            recordvalues.append(icm)
            recordvalues.insert(4, icecprice[0])
        tree.insert(parent='', index='end', iid=count, text="", values=(recordvalues))
        amo = int(recordvalues[3][0][0]) * int(recordvalues[4][0][0])

        tamount = tamount + amo
        totalamountlabel.configure(text="Rs. " + str(tamount))
        ic1.set("0")
        ic2.set("0")
        count += 1
        icecprice.clear()
def dessert():
    cursor.execute("""SELECT i.item_name from items i inner join category c  on (i.cat_id=c.cat_id) where c.cat_name = 'Desserts'""")
    row=cursor.fetchall()
    for i in row:
        dessertlst.append(i[0])
def desp():
    dd = ditems.get()
    sql = "select item_id from items where item_name= :x"
    cursor.execute(sql, x=dd)
    itemselected3 = cursor.fetchall()

    if str(d1.get()) != "0":
        cursor.execute("SELECT price from price where item_id=:x", x=itemselected3[0][0])
        rowxx = cursor.fetchall()
        desprice.append(rowxx)
def appetizerss():
    cursor.execute("""SELECT i.item_name from items i inner join category c  on (i.cat_id=c.cat_id) where c.cat_name = 'Appetizer'""")
    row=cursor.fetchall()
    for i in row:
        appetizerlst.append(i[0])
def appprice():
    aa = aitems.get()
    sql = "select item_id from items where item_name= :x"
    cursor.execute(sql, x=aa)
    itemselected4 = cursor.fetchall()
    if str(a1.get()) > "0":
        cursor.execute("SELECT price from price where item_id=:x", x=itemselected4[0][0])
        rowyx = cursor.fetchall()
        appiprice.append(rowyx)
def special():
    cursor.execute("""SELECT i.item_name from items i inner join category c  on i.cat_id=c.cat_id where c.cat_name = 'Special'""")
    row=cursor.fetchall()
    for i in row:
        speciallst.append(i[0])
def specialsize():
    ss=Sitems.get()
    sql= "select item_id from items where item_name= :x"
    cursor.execute(sql,x=ss)
    itemselected2= cursor.fetchall()
    if ss1.get() == '0' and ss2.get() == '0' and ss3.get() == '0':
        messagebox.showerror("Error","Add Quantity")
    elif (str(ss1.get()) !="0" and str(ss2.get()) !="0" and str(ss3.get()) !="0") or (str(ss1.get()) !="0" and str(ss2.get()) !="0") or (str(ss1.get()) !="0" and str(ss3.get()) !="0")  or (str(ss2.get()) !="0" and str(ss3.get()) !="0"):
        messagebox.showerror("Error","Select 1 size at a time")
    else:

        if str(ss1.get()) > "0":
            cursor.execute("SELECT price from price where item_id=:x and size_id=3 ",x=itemselected2[0][0])
            rowx=cursor.fetchall()
            spprice.append(rowx)
        elif str(ss2.get()) >"0":
            cursor.execute(
            """SELECT price from price where item_id=:x and size_id=2 """,x=itemselected2[0][0])
            rowy=cursor.fetchall()
            spprice.append(rowy)
        elif str(ss3.get()) > "0":
            cursor.execute(
                """SELECT price from price where item_id= :x and size_id=1 """, x=itemselected2[0][0])
            rowz = cursor.fetchall()
            spprice.append(rowz)
def beverage():
    cursor.execute(
        """SELECT i.item_name from items i inner join category c  on i.cat_id=c.cat_id where c.cat_name = 'Beverages'""")
    row = cursor.fetchall()
    for i in row:
        beveragelst.append(i[0])
def bevsize():
    bb = bitems.get()
    sql = "select item_id from items where item_name= :x"
    cursor.execute(sql, x=bb)
    itemselected3 = cursor.fetchall()

    if str(sb1.get()) > "0":
        cursor.execute("SELECT price from price where item_id=:x and size_id=3 ", x=itemselected3[0][0])
        rowx = cursor.fetchall()
        bevprice.append(rowx)
    elif str(sb2.get()) > "0":
        cursor.execute(
            """SELECT price from price where item_id=:x and size_id=2 """, x=itemselected3[0][0])
        rowy = cursor.fetchall()
        bevprice.append(rowy)
    elif str(sb3.get()) > "0":
        cursor.execute(
            """SELECT price from price where item_id= :x and size_id=1 """, x=itemselected3[0][0])
        rowz = cursor.fetchall()
        bevprice.append(rowz)
def deall():
    cursor.execute("""SELECT dname from deals""")
    row=cursor.fetchall()
    for i in row:
        deallst.append(i[0])
def dlprice():
    de = ddd.get()
    sql = "select dprice from Deals where dname= :x"
    cursor.execute(sql, x=de)
    itemselected3 = cursor.fetchall()

    if dll.get() > '0':
        dp.append(itemselected3[0][0])
def register():
    global regEntry1,regEntry2,regEntry3
    cursor.execute("""select emp_id from employees""")
    d=cursor.fetchall()
    cursor.execute("""select max(u_id) from users""")
    uid=cursor.fetchall()
    for i in range(len(d)):

            if int(regEntry3.get()) == int(d[i][0]):
                u=int(uid[0][0])+1
                ed=int(regEntry3.get())
                sql="insert into users(u_id,username,passwords,emp_id) values(:x,:userx,:passw,:idx)"
                cursor.execute(sql,x=u,userx=regEntry1.get(),passw=regEntry2.get(),idx=ed)
                cursor.execute("""commit""")

                messagebox.showinfo("Info", "Register Successfull")
                reg.destroy()

                logingui()
            elif int(regEntry3.get()) != int(d[i][0]) and (i == len(d)-1):
                messagebox.showerror("Error","Ask admin to add employee")
def registergui():
    global  regEntry1,regEntry2,regEntry3,reg
    top1.destroy()
    reg = Tk()
    reg.geometry("610x460+519+200")
    reg.resizable(1, 1)
    reg.title("California Pizza POS")
    reg.configure(background="#ffffff")
    reg.overrideredirect(True)

    Framex = tk.Frame(reg, bg="#006400")
    Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.08)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Helvetica', 10, 'bold'),
                        command=reg.destroy)
    exitbtn.place(x=597, y=7)
    label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Helvetica', 11, 'bold'), foreground="#ffffff",
                     bg="#006400")
    label.pack(pady=13)
    Frame1 = tk.Frame(reg)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#ffffff")
    Frame1.place(relx=-0.017, rely=0.08, relheight=0.260, relwidth=1.107)
    photo = PhotoImage(file='logo.png')
    framepic = Label(Frame1, image=photo)
    framepic.pack()

    Label1 = tk.Label(reg)
    Label1.place(relx=0.327, rely=0.370, height=46, width=253)
    Label1.configure(background="#ffffff")
    Label1.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#006400")
    Label1.configure(text='''REGISTER''')

    regEntry1 = tk.Entry(reg,background="white")
    regEntry1.place(relx=0.352, rely=0.475, height=34, relwidth=0.398)
    regEntry1.configure(disabledforeground="#a3a3a3")
    regEntry1.configure(font="TkFixedFont")
    regEntry1.configure(foreground="#000000")
    regEntry1.configure(insertbackground="black")

    regEntry2 = tk.Entry(reg, show="*",background="white")
    regEntry2.place(relx=0.352, rely=0.561, height=34, relwidth=0.398)
    regEntry2.configure(disabledforeground="#a3a3a3")
    regEntry2.configure(font="TkFixedFont")
    regEntry2.configure(foreground="#000000")
    regEntry2.configure(insertbackground="black")

    regEntry3 = tk.Entry(reg, background="white")
    regEntry3.place(relx=0.352, rely=0.641, height=34, relwidth=0.398)
    regEntry3.configure(disabledforeground="#a3a3a3")
    regEntry3.configure(font="TkFixedFont")
    regEntry3.configure(foreground="#000000")
    regEntry3.configure(insertbackground="black")

    Btn = tk.Button(reg, font=('Aldhabi', 11, 'bold'), command=back)
    Btn.place(relx=0.39, rely=0.728, height=43, width=50)
    Btn.configure(activebackground="#ececec")
    Btn.configure(activeforeground="#000000")
    Btn.configure(background="#006400")
    Btn.configure(disabledforeground="#a3a3a3")
    Btn.configure(foreground="#ffffff")
    Btn.configure(highlightbackground="#d9d9d9")
    Btn.configure(highlightcolor="black")
    Btn.configure(pady="0")
    Btn.configure(text='''<-''')

    Btn = tk.Button(reg, font=('Aldhabi', 11, 'bold'), command=register)
    Btn.place(relx=0.5, rely=0.728, height=43, width=100)
    Btn.configure(activebackground="#ececec")
    Btn.configure(activeforeground="#000000")
    Btn.configure(background="#006400")
    Btn.configure(disabledforeground="#a3a3a3")
    Btn.configure(foreground="#ffffff")
    Btn.configure(highlightbackground="#d9d9d9")
    Btn.configure(highlightcolor="black")
    Btn.configure(pady="0")
    Btn.configure(text='''REGISTER''')

    Username = tk.Label(reg,text="Username",bg="white",fg="#006400" ,font=('Aldhabi', 9, 'bold'))
    Username.place(relx=0.24, rely=0.475)

    passwrd = tk.Label(reg, text="password",bg="white",font=('Aldhabi', 9, 'bold'))
    passwrd.configure(fg="#006400")
    passwrd.place(relx=0.24, rely=0.56)

    emid = tk.Label(reg, text="Emp_ID", bg="white", fg="#006400",font=('Aldhabi', 9, 'bold'))
    emid.place(relx=0.27, rely=0.65)

    reg2 = PhotoImage(file='ppp.png')
    framepic2 = Label(reg, image=reg2)
    framepic2.place(y=315, x=0)
    framepic2.configure(bd=0)

    reg.mainloop()
def back():
    reg.destroy()
    logingui()

def remove():
    global tamount
    for i in tree.get_children():
        if len(tree.item(i,'values')[0]) == 0:
            messagebox.showerror("Error","No items is selected")
        else:

            y = tree.focus()
            minus = tree.item(y, 'values')
            tamount = tamount - int(minus[4])
            totalamountlabel.configure(text="Rs ."+str(tamount))
            x= tree.selection()[0]
            tree.delete(x)
def removeall():
    global tamount
    for i in tree.get_children():
        tree.delete(i)
    totalamountlabel.configure(text="Rs. 0")
    tamount=0
def addrecordtotree():
    pizzasize()
    global count,pizzacombo,tree,recordvalues,sp11,sp12,sp13,tamount
    recordvalues = [count, pitems.get()]
    spl=sp11.get()
    spm=sp12.get()
    sps=sp13.get()
    if (len(pitems.get())==0)or(spl !='0' and spm !='0' and sps !='0') or (spl !='0' and spm !='0') or (spl !='0' and sps !='0')  or (spm !='0' and sps !='0')   :
        messagebox.showerror("Error","Empty fields")
    elif (spl == '0' and spm == '0' and sps == '0') :
        messagebox.showerror("Error", "Select 1 size ")
    else:
        if spl != "0":
            recordvalues.insert(2,"Large")
            recordvalues.append(spl)
            recordvalues.insert(4,pizzaprice[0])
        elif spm != "0":
            recordvalues.insert(2,"Medium")
            recordvalues.append(spm)
            recordvalues.insert(4, pizzaprice[0])
        elif sps != "0":
            recordvalues.insert(2,"Small")
            recordvalues.append(sps)
            recordvalues.insert(4, pizzaprice[0])
        tree.insert(parent='',index='end',iid=count,text="",values=(recordvalues))
        amo=int(recordvalues[3][0][0])*int(recordvalues[4][0][0])
        tamount= tamount+amo
        totalamountlabel.configure(text="Rs. "+str(tamount))
        sp11.set("0")
        sp12.set("0")
        sp13.set("0")
        count+=1
        pizzaprice.clear()
def addrecordtotree2():
    specialsize()
    global count,tree,Sitems,specialcombo,recordvalues,ss1,ss2,ss3,tamount
    recordvalues = [count, Sitems.get()]
    ssl=ss1.get()
    ssm=ss2.get()
    sss=ss3.get()
    if (ssl != '0' and ssm != '0' and sss != '0') or (ssl != '0' and ssm != '0') or (ssl != '0' and sss != '0') or (ssm != '0' and sss != '0'):
        messagebox.showerror("Error", "Select 1 size at a time")
    elif (ssl == '0' and ssm == '0' and sss == '0') :
        messagebox.showerror("Error", "Select size ")
    else:
        if ssl != "0":
            recordvalues.insert(2,"Large")
            recordvalues.append(ssl)
            recordvalues.insert(4, spprice[0])
        elif ssm != "0":
            recordvalues.insert(2, "Medium")
            recordvalues.append(ssm)
            recordvalues.insert(4, spprice[0])
        elif sss != "0":
            recordvalues.insert(2, "Small")
            recordvalues.append(sss)
            recordvalues.insert(4, spprice[0])
        tree.insert(parent='', index='end', iid=count, text="", values=(recordvalues))
        amo = int(recordvalues[3][0][0]) * int(recordvalues[4][0][0])

        tamount = tamount + amo
        totalamountlabel.configure(text="Rs. " + str(tamount))
        ss1.set("0")
        ss2.set("0")
        ss3.set("0")
        count += 1
        spprice.clear()
def addrecordtotree3():
    bevsize()
    global count,tree,bitems,recordvalues,sb1,sb2,sb3,tamount,bevcombo
    recordvalues = [count, bitems.get()]
    sbl = sb1.get()
    sbm = sb2.get()
    sbs = sb3.get()
    if (sbl != "0" and sbm != "0" and sbs != "0") or (sbl != "0" and sbm != "0") or (sbl != "0" and sbs != "0") or (sbm != "0" and sbs != "0"):
        messagebox.showerror("Error", "Select 1 size at a time")
    elif (sbl == '0' and sbm == '0' and sbs == '0') :
        messagebox.showerror("Error", "Select 1 size at a time")
    else:
        if sbl != "0":
            recordvalues.insert(2, "Large")
            recordvalues.append(sbl)
            recordvalues.insert(4, bevprice[0])
        elif sbm != "0":
            recordvalues.insert(2, "Medium")
            recordvalues.append(sbm)
            recordvalues.insert(4, bevprice[0])
        elif sbs != "0":
            recordvalues.insert(2, "Small")
            recordvalues.append(sbs)
            recordvalues.insert(4, bevprice[0])

        tree.insert(parent='', index='end', iid=count, text="", values=(recordvalues))
        amo = int(recordvalues[3][0][0]) * int(recordvalues[4][0][0])
        count += 1
        tamount = tamount + amo
        totalamountlabel.configure(text="Rs. " + str(tamount))
        sb1.set("0")
        sb2.set("0")
        sb3.set("0")
        bevprice.clear()
def addeserttree():
    global  count,tamount
    desp()
    recordvalues= [count,ditems.get()]
    if d1.get() == '0':
        messagebox.showerror("Error","Add Quantity")
    elif str(d1.get()) !="0":
        recordvalues.insert(2, "-")
        recordvalues.append(d1.get())
        recordvalues.insert(4, desprice[0][0])
        tree.insert(parent='', index='end', iid=count, text="", values=(recordvalues))
        amo = int(recordvalues[3][0][0]) * int(recordvalues[4][0][0])

        tamount = tamount + amo
        totalamountlabel.configure(text="Rs. " + str(tamount))
        d1.set("0")
        count+=1
        desprice.clear()
def addealltree():
    dlprice()
    global  count,tamount
    recordvalues= [count,ddd.get()]
    if dll.get() =='0':
        messagebox.showerror("Error","Select Deal Quantity")
    elif dll.get() != '0':
        recordvalues.insert(2, "-")
        recordvalues.append(dll.get())
        recordvalues.insert(4, dp[0])
        tree.insert(parent='', index='end', iid=count, text="", values=(recordvalues))
        count = count + 1
        dp.clear()
        amo = int(recordvalues[3]) * int(recordvalues[4])

        tamount = tamount + amo
        totalamountlabel.configure(text="Rs. " + str(tamount))
        dll.set("0")
def addapptree():
    global  count,tamount
    appprice()
    recordvalues= [count,aitems.get()]
    if a1.get() == "0":
        messagebox.showerror("Error","Add Quantity")
    elif a1.get() !="0":
        recordvalues.insert(2, "-")
        recordvalues.append(a1.get())
        recordvalues.insert(4, appiprice[0][0])
        tree.insert(parent='', index='end', iid=count, text="", values=(recordvalues))
        count += 1
        appiprice.clear()
        amo = int(recordvalues[3][0]) * int(recordvalues[4][0])
        tamount = tamount + amo
        totalamountlabel.configure(text="Rs. " + str(tamount))
        a1.set("0")
def logout():

    paylst.clear()
    pizzalst.clear()
    pizzaprice.clear()
    speciallst.clear()
    spprice.clear()
    beveragelst.clear()
    bevprice.clear()
    dessertlst.clear()
    desprice.clear()
    deallst.clear()
    dp.clear()
    appetizerlst.clear()
    appiprice.clear()
    icecreamlst.clear()
    icecprice.clear()
    top.destroy()
    logingui()


def logingui():
    global Entry1, Entry2, top1
    top1 = Tk()
    top1.geometry("610x460+519+200")
    top1.minsize(148, 1)
    top1.maxsize(1924, 1055)
    top1.resizable(1, 1)
    top1.title("California Pizza POS")
    top1.configure(background="#ffffff")
    top1.overrideredirect(True)

    Framex = tk.Frame(top1,bg="#006400")
    Framex.place(relx=-0.017, rely=0.0,relwidth=1.1,relheight=0.08)
    exitbtn = tk.Button(Framex, text="X",bg="#006400",foreground="white",font=('Helvetica', 10, 'bold'), command=top1.destroy)
    exitbtn.place(x=597,y=7)
    label = tk.Label(Framex,text="CALIFORNIA PIZZA POS",font=('Helvetica', 11, 'bold'),foreground="#ffffff",bg = "#006400")
    label.pack(pady=13)

    Frame1 = tk.Frame(top1)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#ffffff")
    Frame1.place(relx=-0.017, rely=0.08, relheight=0.260, relwidth=1.107)
    photo = PhotoImage(file='logo.png')
    framepic = Label(Frame1, image=photo)
    framepic.pack()

    Label1 = tk.Label(top1)
    Label1.place(relx=0.327, rely=0.370, height=46, width=253)
    Label1.configure(background="#ffffff")
    Label1.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#006400")
    Label1.configure(text='''LOGIN''')

    Entry1 = tk.Entry(top1)
    Entry1.place(relx=0.352, rely=0.475, height=34, relwidth=0.398)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    Entry2 = tk.Entry(top1,show="*")
    Entry2.place(relx=0.352, rely=0.561, height=34, relwidth=0.398)
    Entry2.configure(background="white")
    Entry2.configure(disabledforeground="#a3a3a3")
    Entry2.configure(font="TkFixedFont")
    Entry2.configure(foreground="#000000")
    Entry2.configure(insertbackground="black")

    Button1 = tk.Button(top1,font=('Aldhabi', 11, 'bold'), command=login)
    Button1.place(relx=0.380, rely=0.728, height=43, width=86)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#006400")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#ffffff")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''LOGIN''')

    Buttonreg = tk.Button(top1,text="REGISTER",font=('Aldhabi', 11, 'bold'),fg="#ffffff",bg="#006400",command=registergui)
    Buttonreg.place(relx=0.550,rely=0.728,height=43, width=95)

    photouser = PhotoImage(file='user.png')
    picu = Label(top1, image=photouser)
    picu.configure(bd=0)
    picu.place(relx=0.27,rely=0.475)

    photopass = PhotoImage(file='pass.png')
    picp = Label(top1, image=photopass)
    picp.configure(bd=0)
    picp.place(relx=0.27,rely=0.56)

    photo2 = PhotoImage(file='ppp.png')
    framepic2 = Label(top1, image=photo2)
    framepic2.place(y=315,x=0)
    framepic2.configure(bd=0)
    top1.mainloop()
def login():
    cursor.execute("""SELECT username,passwords FROM USERS where username='admin'""")
    rowadmin = cursor.fetchall()
    global user
    ID = Entry1.get()
    Password = Entry2.get()

    for i,j in rowadmin:
        if ID == i and Password == j:
            user = i
            messagebox.showinfo("Login", "Logged In Successfully")
            top1.destroy()
            admin.main()
        else:
            cursor.execute("""SELECT username,passwords FROM USERS""")
            row = cursor.fetchall()
            for i in range(len(row)):
                if ID == row[i][0] and Password == row[i][1]:
                    user = row[i][0]
                    messagebox.showinfo("Login", "Logged In Successfully")
                    top1.destroy()
                    maingui()
                elif (ID != row[i][0] and Password != row[i][1]) and (i==len(row)-1) :
                    messagebox.showerror("error", "Invalid User or password")
def maingui():
    global pitems,pizzacombo,bitems,sb1,sb2,sb3,tree,specialcombo,bevcombo,tree,sp11,sp12,sp13,Sitems,ss1,ss2,ss3,top
    global dessertcombo,ditems,d1,dessertspin,a1,aitems,ic1,ic2,icitems,dll,ddd,totalamountlabel,tamount
    top = Tk()
    top.geometry("1443x1345+0+0")
    top.minsize(148, 1)
    top.maxsize(1916, 1047)
    top.state('zoomed')
    top.resizable(1, 1)
    top.title("CALIFORNIA PIZZA POS")
    top.configure(background="#ffffff")
    top.overrideredirect(True)
    Framex = tk.Frame(top, bg="#006400")
    Framex.place(relx=-0.007, rely=0.0, relwidth=1.1, relheight=0.03)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Helvetica', 10, 'bold'),
                        command=top.destroy)
    exitbtn.place(x=1523, y=1)
    labelx = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Helvetica', 11, 'bold'), foreground="#ffffff",
                     bg="#006400")
    labelx.place(x=700,y=0.4)

    Frame_1 = tk.Frame(top)
    Frame_1.place(x=-0.007, y=27, relheight=0.168, relwidth=1.002)

    Frame_1.configure(relief='groove')
    Frame_1.configure(borderwidth="2")
    Frame_1.configure(relief="groove")
    Frame_1.configure(background="#ffffff")

    photo = PhotoImage(file='logo.png')
    framepic = Label(Frame_1, image=photo)
    framepic.pack()
    Frame2= tk.Frame(top)
    Frame2.configure(bg="white")
    Frame2.place(relx=0.0,rely=0.20,relwidth=1,relheight=0.8)

    Label1 = tk.Label(Frame2)
    Label1.place(relx=0.012, rely=0.045)
    Label1.configure(background="#ffffff")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font=18)
    Label1.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(foreground="#006400")
    Label1.configure(text='''PIZZA''')

    L1 = tk.Label(Frame2)
    L1.place(relx=0.165, rely=0.045)
    L1.configure(background="#ffffff")
    L1.configure(disabledforeground="#a3a3a3")
    L1.configure(font=18)
    L1.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L1.configure(foreground="#006400")
    L1.configure(text='''L''')

    L2 = tk.Label(Frame2)
    L2.place(relx=0.202, rely=0.045)
    L2.configure(background="#ffffff")
    L2.configure(disabledforeground="#a3a3a3")
    L2.configure(font=18)
    L2.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L2.configure(foreground="#006400")
    L2.configure(text='''M''')

    L3 = tk.Label(Frame2)
    L3.place(relx=0.232, rely=0.045)
    L3.configure(background="#ffffff")
    L3.configure(disabledforeground="#a3a3a3")
    L3.configure(font=18)
    L3.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L3.configure(foreground="#006400")
    L3.configure(text='''S''')

    pitems = StringVar()
    pizzacombo = ttk.Combobox(Frame2,textvariable=pitems)
    pizza()
    pizzacombo['values'] = pizzalst
    pizzacombo.place(relx=0.011, rely=0.115, height=37, width=200)
    pizzacombo.bind("<<ComboboxSelected>>")
    #buttom

    padd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addrecordtotree)
    padd_btn.configure(activebackground="#006400")
    padd_btn.configure(activeforeground="#ffffff")
    padd_btn.place(relx=0.260, rely=0.120, height=24, relwidth=0.015)



    sp11 = StringVar()
    Sizep11 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=sp11, wrap=True)
    Sizep11.place(relx=0.163, rely=0.120,height=24, relwidth=0.021)
    Sizep11.configure(background="white")
    Sizep11.configure(disabledforeground="#a3a3a3")
    Sizep11.configure(font="TkFixedFont")
    Sizep11.configure(foreground="#000000")
    Sizep11.configure(insertbackground="black")

    sp12 = StringVar()
    Sizep12 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=sp12, wrap=True)
    Sizep12.place(relx=0.200, rely=0.120, height=24, relwidth=0.021)
    Sizep12.configure(background="white")
    Sizep12.configure(disabledforeground="#a3a3a3")
    Sizep12.configure(font="TkFixedFont")
    Sizep12.configure(foreground="#000000")
    Sizep12.configure(insertbackground="black")

    sp13 = StringVar()
    Sizep13 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=sp13, wrap=True)
    Sizep13.place(relx=0.230, rely=0.120, height=24, relwidth=0.021)
    Sizep13.configure(background="white")
    Sizep13.configure(disabledforeground="#a3a3a3")
    Sizep13.configure(font="TkFixedFont")
    Sizep13.configure(foreground="#000000")
    Sizep13.configure(insertbackground="black")



    Label2 = tk.Label(Frame2)
    Label2.place(relx=0.012, rely=0.189)
    Label2.configure(background="#ffffff")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font=18)
    Label2.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label2.configure(foreground="#006400")
    Label2.configure(text='''SPECIAL''')

    Sitems = StringVar()
    specialcombo = ttk.Combobox(Frame2, textvariable=Sitems)
    special()
    specialcombo['values'] = speciallst
    specialcombo.place(relx=0.011, rely=0.248, height=37, width=200)
    specialcombo.bind("<<ComboboxSelected>>")

    ss1=StringVar()
    Sizes1 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=ss1, wrap=True)
    Sizes1.place(relx=0.163, rely=0.247, height=24, relwidth=0.021)
    Sizes1.configure(background="white")
    Sizes1.configure(disabledforeground="#a3a3a3")
    Sizes1.configure(font="TkFixedFont")
    Sizes1.configure(foreground="#000000")
    Sizes1.configure(insertbackground="black")

    ss2=StringVar()
    Sizes2 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=ss2, wrap=True)
    Sizes2.place(relx=0.200, rely=0.247, height=24, relwidth=0.021)
    Sizes2.configure(background="white")
    Sizes2.configure(disabledforeground="#a3a3a3")
    Sizes2.configure(font="TkFixedFont")
    Sizes2.configure(foreground="#000000")
    Sizes2.configure(insertbackground="black")

    ss3=StringVar()
    Sizes3 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=ss3, wrap=True)
    Sizes3.place(relx=0.230, rely=0.247, height=24, relwidth=0.021)
    Sizes3.configure(background="white")
    Sizes3.configure(disabledforeground="#a3a3a3")
    Sizes3.configure(font="TkFixedFont")
    Sizes3.configure(foreground="#000000")
    Sizes3.configure(insertbackground="black")

    spadd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addrecordtotree2)
    spadd_btn.configure(activebackground="#006400")
    spadd_btn.configure(activeforeground="#ffffff")
    spadd_btn.place(relx=0.260, rely=0.247, height=24, relwidth=0.015)

    Label3 = tk.Label(Frame2)
    Label3.place(relx=0.012, rely=0.330)
    Label3.configure(background="#ffffff")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font=18)
    Label3.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label3.configure(foreground="#006400")
    Label3.configure(text='''BEVERAGES''')

    bitems=StringVar()
    bevcombo = ttk.Combobox(Frame2, textvariable=bitems)
    beverage()
    bevcombo.place(relx=0.011, rely=0.380, height=37, width=200)
    bevcombo['values'] = beveragelst
    bevcombo.bind("<<ComboboxSelected>>")

    sb1=StringVar()
    Sizeb1 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=sb1, wrap=True)
    Sizeb1.place(relx=0.163, rely=0.380, height=24, relwidth=0.021)
    Sizeb1.configure(background="white")
    Sizeb1.configure(disabledforeground="#a3a3a3")
    Sizeb1.configure(font="TkFixedFont")
    Sizeb1.configure(foreground="#000000")
    Sizeb1.configure(insertbackground="black")

    sb2=StringVar()
    Sizeb2 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=sb2, wrap=True)
    Sizeb2.place(relx=0.200, rely=0.380, height=24, relwidth=0.021)
    Sizeb2.configure(background="white")
    Sizeb2.configure(disabledforeground="#a3a3a3")
    Sizeb2.configure(font="TkFixedFont")
    Sizeb2.configure(foreground="#000000")
    Sizeb2.configure(insertbackground="black")

    sb3=StringVar()
    Sizeb3 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=sb3, wrap=True)
    Sizeb3.place(relx=0.230, rely=0.380, height=24, relwidth=0.021)
    Sizeb3.configure(background="white")
    Sizeb3.configure(disabledforeground="#a3a3a3")
    Sizeb3.configure(font="TkFixedFont")
    Sizeb3.configure(foreground="#000000")
    Sizeb3.configure(insertbackground="black")

    bevadd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addrecordtotree3)
    bevadd_btn.configure(activebackground="#006400")
    bevadd_btn.configure(activeforeground="#ffffff")
    bevadd_btn.place(relx=0.260, rely=0.380, height=24, relwidth=0.015)

    Label4 = tk.Label(Frame2)
    Label4.place(relx=0.012, rely=0.465)
    Label4.configure(background="#ffffff")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font=18)
    Label4.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label4.configure(foreground="#006400")
    Label4.configure(text='''DESSERTS''')

    Lx1 = tk.Label(Frame2)
    Lx1.place(relx=0.165, rely=0.465)
    Lx1.configure(background="#ffffff")
    Lx1.configure(disabledforeground="#a3a3a3")
    Lx1.configure(font=18)
    Lx1.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Lx1.configure(foreground="#006400")
    Lx1.configure(text='''Q''')
    ditems=StringVar()
    descombo = ttk.Combobox(Frame2, textvariable=ditems)
    dessert()
    descombo.place(relx=0.012, rely=0.520, height=37, width=200)
    descombo['values'] = dessertlst
    descombo.bind("<<ComboboxSelected>>")

    d1= StringVar()
    dessertspin = tk.Spinbox(Frame2, from_=0, to=30, textvariable=d1, wrap=True)
    dessertspin.place(relx=0.163, rely=0.523, height=24, relwidth=0.021)
    dessertspin.configure(background="white")
    dessertspin.configure(disabledforeground="#a3a3a3")
    dessertspin.configure(font="TkFixedFont")
    dessertspin.configure(foreground="#000000")
    dessertspin.configure(insertbackground="black")

    dadd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addeserttree)
    dadd_btn.configure(activebackground="#006400")
    dadd_btn.configure(activeforeground="#ffffff")
    dadd_btn.place(relx=0.200, rely=0.520, height=24, relwidth=0.015)

    Label5 = tk.Label(Frame2)
    Label5.place(relx=0.012, rely=0.597)
    Label5.configure(background="#ffffff")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(font=18)
    Label5.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label5.configure(foreground="#006400")
    Label5.configure(text='''APPETIZERS''')

    aitems=StringVar()
    appcombo = ttk.Combobox(Frame2, textvariable=aitems)
    appetizerss()
    appcombo['values'] = appetizerlst
    appcombo.bind("<<ComboboxSelected>>")
    appcombo.place(relx=0.011, rely=0.655, height=37, width=200)

    a1=StringVar()
    appetizer = tk.Spinbox(Frame2, from_=0, to=30, textvariable=a1, wrap=True)
    appetizer.place(relx=0.163, rely=0.665, height=24, relwidth=0.021)
    appetizer.configure(background="white")
    appetizer.configure(disabledforeground="#a3a3a3")
    appetizer.configure(font="TkFixedFont")
    appetizer.configure(foreground="#000000")
    appetizer.configure(insertbackground="black")

    apadd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addapptree)
    apadd_btn.configure(activebackground="#006400")
    apadd_btn.configure(activeforeground="#ffffff")
    apadd_btn.place(relx=0.200, rely=0.665, height=24, relwidth=0.015)

    Label6 = tk.Label(Frame2)
    Label6.place(relx=0.358, rely=0.045)
    Label6.configure(background="#ffffff")
    Label6.configure(disabledforeground="#a3a3a3")
    Label6.configure(font=18)
    Label6.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label6.configure(foreground="#006400")
    Label6.configure(text='''DEALS''')

    Label7 = tk.Label(Frame2)
    Label7.place(relx=0.505, rely=0.045)
    Label7.configure(background="#ffffff")
    Label7.configure(disabledforeground="#a3a3a3")
    Label7.configure(font=18)
    Label7.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label7.configure(foreground="#006400")
    Label7.configure(text='''Q''')

    ddd=StringVar()
    dealcombo = ttk.Combobox(Frame2, textvariable=ddd)
    dealcombo.place(relx=0.360, rely=0.115, height=37, width=200)
    deall()
    dealcombo['values']=deallst
    dealcombo.bind("<<ComboboxSelected>>")

    dll=StringVar()
    deal = tk.Spinbox(Frame2, from_=0, to=30, textvariable=dll, wrap=True)
    deal.place(relx=0.503, rely=0.115, height=24, relwidth=0.021)
    deal.configure(background="white")
    deal.configure(disabledforeground="#a3a3a3")
    deal.configure(font="TkFixedFont")
    deal.configure(foreground="#000000")
    deal.configure(insertbackground="black")

    dealadd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addealltree)
    dealadd_btn.configure(activebackground="#006400")
    dealadd_btn.configure(activeforeground="#ffffff")
    dealadd_btn.place(relx=0.545, rely=0.111, height=24, relwidth=0.015)

    Label8 = tk.Label(Frame2)
    Label8.place(relx=0.358, rely=0.189)
    Label8.configure(background="#ffffff")
    Label8.configure(disabledforeground="#a3a3a3")
    Label8.configure(font=18)
    Label8.configure(
        font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label8.configure(foreground="#006400")
    Label8.configure(text='''ICE CREAM''')

    Label9 = tk.Label(Frame2)
    Label9.place(relx=0.498, rely=0.187)
    Label9.configure(background="#ffffff")
    Label9.configure(disabledforeground="#a3a3a3")
    Label9.configure(
        font="-family {Copperplate Gothic Bold} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
    Label9.configure(foreground="#006400")
    Label9.configure(text='''245\ngram''')

    Label10 = tk.Label(Frame2)
    Label10.place(relx=0.541, rely=0.187)
    Label10.configure(background="#ffffff")
    Label10.configure(disabledforeground="#a3a3a3")
    Label10.configure(
        font="-family {Copperplate Gothic Bold} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
    Label10.configure(foreground="#006400")
    Label10.configure(text='''475\ngram''')

    icitems=StringVar()
    iccombo = ttk.Combobox(Frame2, textvariable=icitems)
    iccombo.place(relx=0.360, rely=0.248, height=37, width=200)
    ic()
    iccombo['values']= icecreamlst
    iccombo.bind("<<ComboboxSelected>>")

    ic1=StringVar()
    Sizeic1 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=ic1, wrap=True)
    Sizeic1.place(relx=0.503, rely=0.247, height=24, relwidth=0.021)
    Sizeic1.configure(background="white")
    Sizeic1.configure(disabledforeground="#a3a3a3")
    Sizeic1.configure(font="TkFixedFont")
    Sizeic1.configure(foreground="#000000")
    Sizeic1.configure(insertbackground="black")

    ic2=StringVar()
    Sizeic2 = tk.Spinbox(Frame2, from_=0, to=30, textvariable=ic2, wrap=True)
    Sizeic2.place(relx=0.545, rely=0.247, height=24, relwidth=0.021)
    Sizeic2.configure(background="white")
    Sizeic2.configure(disabledforeground="#a3a3a3")
    Sizeic2.configure(font="TkFixedFont")
    Sizeic2.configure(foreground="#000000")
    Sizeic2.configure(insertbackground="black")

    icadd_btn = tk.Button(Frame2, text="+", font="-family {Arial} -size 21 -weight bold", bg="#006400",
                         foreground="#FFFFFF", command=addictotree)
    icadd_btn.configure(activebackground="#006400")
    icadd_btn.configure(activeforeground="#ffffff")
    icadd_btn.place(relx=0.575, rely=0.247, height=24, relwidth=0.015)


    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", background="#006400",
                     foreground="white",font=('Helvetica',11,"bold"))
    style.map('Treeview', background=[("selected", "#006400")])

    tree = ttk.Treeview(Frame2,column=('S.no','Item name','Size','Item Qty','Price'),selectmode='extended')
    scrollbarx = Scrollbar(tree, orient=HORIZONTAL)
    scrollbary = Scrollbar(tree, orient=VERTICAL)
    tree.config(yscrollcommand=scrollbary.set)
    tree.config(xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('S.no', text="S.no", anchor=CENTER)
    tree.heading('Item name', text="Item name", anchor=CENTER)
    tree.heading('Size', text="Size", anchor=CENTER)
    tree.heading('Item Qty', text="Item Qty", anchor=CENTER)
    tree.heading('Price', text="Price", anchor=CENTER)
    # tree.tag_configure()
    tree.column('#0', stretch=NO, minwidth=0, width=0,anchor=CENTER)
    tree.column('#1', stretch=NO, minwidth=0, width=45,anchor=CENTER)
    tree.column('#2', stretch=NO, minwidth=0, width=155,anchor=CENTER)
    tree.column('#3', stretch=NO, minwidth=0, width=115,anchor=CENTER)
    tree.column('#4', stretch=NO, minwidth=0, width=85,anchor=CENTER)
    tree.column('#5', stretch=NO, minwidth=0, width=105,anchor=CENTER)
    tree.place(relx=0.61, rely=0.05,relheight=0.77,relwidth=0.34)

    Labelu = tk.Label(Frame_1)
    Labelu.place(relx=0.905, rely=0.310)
    Labelu.configure(background="#ffffff")
    Labelu.configure(disabledforeground="#a3a3a3")
    Labelu.configure(
        font="-family {Prototype} -size 10 -weight bold")
    Labelu.configure(foreground="#006400")
    Labelu.configure(text=user.upper())

    photouser = PhotoImage(file='user.png')
    picu = Label(Frame_1, image=photouser)
    picu.configure(bd=0)
    picu.place(relx=0.874, rely=0.293)

    logoutemp = tk.Button(Frame_1, command=logout)
    logoutemp.place(relx=0.907, rely=0.442, height=25, width=69)
    logoutemp.configure(activebackground="#ececec")
    logoutemp.configure(activeforeground="#000000")
    logoutemp.configure(background="#006400")
    logoutemp.configure(disabledforeground="#a3a3a3")
    logoutemp.configure(font="-family {Cooper Black} -size 8 -weight bold -slant roman -underline 0 -overstrike 0")
    logoutemp.configure(foreground="#ffffff")
    logoutemp.configure(highlightbackground="#d9d9d9")
    logoutemp.configure(highlightcolor="black")
    logoutemp.configure(pady="0")
    logoutemp.configure(text='''LOGOUT''')

    totallabel=tk.Label(Frame2,fg="#006400",bg="#ffffff")
    totallabel.place(relx=0.627,rely=0.758)
    totallabel.configure(text="TOTAL")
    totallabel.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")

    totalamountlabel = tk.Label(Frame2, fg="#006400", bg="#ffffff")
    totalamountlabel.place(relx=0.87, rely=0.758)
    totalamountlabel.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    totalamountlabel.configure(text="Rs. 0")
    tamount  = 0

    removeitmbtn= tk.Button(Frame2,bg="#006400",fg="#ffffff",command=remove)
    removeitmbtn.place(relx=0.61,rely=0.84,height=35,width=130)
    removeitmbtn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    removeitmbtn.configure(text="Remove item")

    removeallbtn = tk.Button(Frame2, bg="#006400", fg="#ffffff",command=removeall)
    removeallbtn.place(relx=0.73, rely=0.84, height=35, width=130)
    removeallbtn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    removeallbtn.configure(text="Remove all item")

    billbtn = tk.Button(Frame2, bg="#006400", fg="#ffffff",command=billgui)
    billbtn.place(relx=0.86, rely=0.84, height=35, width=130)
    billbtn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    billbtn.configure(text="Generate Bill")

    top.mainloop()
def accgui():
    global accwindow,accno,accname
    accwindow = Tk()
    accwindow.geometry("610x560+419+200")
    accwindow.minsize(148, 1)
    accwindow.maxsize(1924, 1055)
    accwindow.resizable(1, 1)
    accwindow.title("California Pizza POS")
    accwindow.configure(background="#ffffff")
    accwindow.overrideredirect(True)

    Framex = tk.Frame(accwindow,bg="#006400")
    Framex.place(relx=-0.017, rely=0.0,relwidth=1.1,relheight=0.08)
    exitbtn = tk.Button(Framex, text="X",bg="#006400",foreground="white",font=('Helvetica', 10, 'bold'), command=accwindow.destroy)
    exitbtn.place(x=597,y=7)
    label = tk.Label(Framex,text="CALIFORNIA PIZZA POS",font=('Helvetica', 11, 'bold'),foreground="#ffffff",bg = "#006400")
    label.pack(pady=10)


    Label1 = tk.Label(accwindow)
    Label1.place(relx=0.22, rely=0.280, height=46, width=253)
    Label1.configure(background="#ffffff")
    Label1.configure(font="-family {Prototype -size 18 -weight bold -slant roman -underline 0 -overstrike 0}")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#006400")
    Label1.configure(text='''ACCOUNT DETAILS''')

    accname = tk.Entry(accwindow)
    accname.place(relx=0.372, rely=0.475, height=34, relwidth=0.448)
    accname.configure(background="white")
    accname.configure(disabledforeground="#a3a3a3")
    accname.configure(font="TkFixedFont")
    accname.configure(foreground="#000000")
    accname.configure(insertbackground="black")

    accno= tk.Entry(accwindow)
    accno.place(relx=0.372, rely=0.561, height=34, relwidth=0.448)
    accno.configure(background="white")
    accno.configure(disabledforeground="#a3a3a3")
    accno.configure(font="TkFixedFont")
    accno.configure(foreground="#000000")
    accno.configure(insertbackground="black")

    addaccbtn = tk.Button(accwindow,font=('Aldhabi', 11, 'bold'), command=addacc)
    addaccbtn.place(relx=0.420, rely=0.728, height=43, width=86)
    addaccbtn.configure(activebackground="#ececec")
    addaccbtn.configure(activeforeground="#000000")
    addaccbtn.configure(background="#006400")
    addaccbtn.configure(disabledforeground="#a3a3a3")
    addaccbtn.configure(foreground="#ffffff")
    addaccbtn.configure(highlightbackground="#d9d9d9")
    addaccbtn.configure(highlightcolor="black")
    addaccbtn.configure(pady="0")
    addaccbtn.configure(text='''Add''')

    Accountname=tk.Label(accwindow)
    Accountname.configure(background="#ffffff")
    Accountname.configure(font="-family {Aldhabi -size 8 -weight bold -slant roman -underline 0 -overstrike 0}")
    Accountname.configure(disabledforeground="#a3a3a3")
    Accountname.configure(foreground="#006400")
    Accountname.configure(text="Account Name")
    Accountname.place(relx=0.06,rely=0.475)

    Accountno = tk.Label(accwindow)
    Accountno.configure(background="#ffffff")
    Accountno.configure(font="-family {Aldhabi -size 8 -weight bold -slant roman -underline 0 -overstrike 0}")
    Accountno.configure(disabledforeground="#a3a3a3")
    Accountno.configure(foreground="#006400")
    Accountno.configure(text="Account No")
    Accountno.place(relx=0.08, rely=0.56)

    accwindow.mainloop()
def addacc():
    global acntname,acntno
    acn=accno.get()
    acname=accname.get()
    acntname = acntname+ acname
    acntno = acntno +int(acn)
    accwindow.destroy()
def payinsert(event):
    if paytype.get() == "card":
        accgui()

def payy():
    global b
    cursor.execute("select paymenttype_name from paymenttype")
    zz= cursor.fetchall()
    b=0
    for i in zz:
        paylst.append(i[0])
        b+=1
def billgui():
    global pty,billwindow,billtree,paytype,number,tamount
    billwindow = Tk()
    billwindow.geometry("610x560+419+200")
    billwindow.minsize(148, 1)
    billwindow.maxsize(1924, 1055)
    billwindow.resizable(1, 1)
    billwindow.title("California Pizza POS")
    billwindow.configure(background="#ffffff")
    billwindow.overrideredirect(True)

    Framex = tk.Frame(billwindow, bg="#006400")
    Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.06)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Helvetica', 10, 'bold'),
                        command=billwindow.destroy)
    exitbtn.place(x=597, y=7)
    label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Helvetica', 11, 'bold'), foreground="#ffffff",
                     bg="#006400")
    label.pack(pady=8)

    Label1 = tk.Label(billwindow)
    Label1.place(relx=0.027, rely=0.095)
    Label1.configure(background="#ffffff")
    Label1.configure(
        font="-family {ALDHABI Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#006400")
    Label1.configure(text='''BILL''')

    empnamelbl = tk.Label(billwindow)
    empnamelbl .place(relx=0.79, rely=0.1)
    empnamelbl .configure(background="white")
    empnamelbl .configure(disabledforeground="#a3a3a3")
    empnamelbl .configure(font="TkFixedFont")
    empnamelbl .configure(foreground="#000000")
    empnamelbl .configure(text="EMP: "+user.upper())

    recplbl = tk.Label(billwindow)
    recplbl.place(relx=0.027, rely=0.166)
    recplbl.configure(background="white")
    recplbl.configure(disabledforeground="#a3a3a3")
    recplbl.configure(font="TkFixedFont")
    recplbl.configure(foreground="#000000")
    recplbl.configure(text="RECIEPT NO: ")

    recpno = tk.Label(billwindow)
    recpno.place(relx=0.21, rely=0.166)
    recpno.configure(background="white")
    recpno.configure(disabledforeground="#a3a3a3")
    recpno.configure(font="TkFixedFont")
    recpno.configure(foreground="#000000")
    cursor.execute("select max(reciept_id) from billing")
    number = cursor.fetchall()
    recpno.configure(text=number[0][0]+1)

    orddatelbl = tk.Label(billwindow)
    orddatelbl.place(relx=0.027, rely=0.2)
    orddatelbl.configure(background="white")
    orddatelbl.configure(disabledforeground="#a3a3a3")
    orddatelbl.configure(font="TkFixedFont")
    orddatelbl.configure(foreground="#000000")
    orddatelbl.configure(text="Date: ")

    orddate = tk.Label(billwindow)
    orddate.place(relx=0.21, rely=0.2)
    orddate.configure(background="white")
    orddate.configure(disabledforeground="#a3a3a3")
    orddate.configure(font="TkFixedFont")
    orddate.configure(foreground="#000000")
    date= datetime.date.today()
    orddate.configure(text=date)

    orddatelbl = tk.Label(billwindow)
    orddatelbl.place(relx=0.027, rely=0.2)
    orddatelbl.configure(background="white")
    orddatelbl.configure(disabledforeground="#a3a3a3")
    orddatelbl.configure(font="TkFixedFont")
    orddatelbl.configure(foreground="#000000")
    orddatelbl.configure(text="Date: ")

    separator = ttk.Separator(billwindow, orient='horizontal')
    separator.place(relx=0.021, rely=0.25, relwidth=0.95)

    # separator2 = ttk.Separator(billwindow, orient='horizontal')
    # separator2.place(relx=0.021, rely=0.29, relwidth=0.95)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", background="#006400",
                    foreground="white", font=('Helvetica', 11, "bold"))
    style.map('Treeview', background=[("selected", "#006400")])

    billtree = ttk.Treeview(billwindow, column=('S.no', 'Item name', 'Size', 'Item Qty', 'Price'), selectmode='extended')
    scrollbarx = Scrollbar(billtree, orient=HORIZONTAL)
    scrollbary = Scrollbar(billtree, orient=VERTICAL)
    billtree.config(yscrollcommand=scrollbary.set)
    billtree.config(xscrollcommand=scrollbarx.set)
    scrollbary.config(command=billtree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=billtree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    billtree.heading('S.no', text="S.no", anchor=CENTER)
    billtree.heading('Item name', text="Item name", anchor=CENTER)
    billtree.heading('Size', text="Size", anchor=CENTER)
    billtree.heading('Item Qty', text="Item Qty", anchor=CENTER)
    billtree.heading('Price', text="Price", anchor=CENTER)
    # tree.tag_configure()
    billtree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    billtree.column('#1', stretch=NO, minwidth=0, width=45, anchor=CENTER)
    billtree.column('#2', stretch=NO, minwidth=0, width=155, anchor=CENTER)
    billtree.column('#3', stretch=NO, minwidth=0, width=115, anchor=CENTER)
    billtree.column('#4', stretch=NO, minwidth=0, width=145, anchor=CENTER)
    billtree.column('#5', stretch=NO, minwidth=0, width=105, anchor=CENTER)
    billtree.place(relx=0.021, rely=0.26, relheight=0.57, relwidth=0.976)

    paytypelabel = tk.Label(billwindow, fg="#006400", bg="#ffffff")
    paytypelabel.place(relx=0.04, rely=0.858)
    paytypelabel.configure(text="Payment Type")

    totallabel = tk.Label(billwindow, fg="#006400", bg="#ffffff")
    totallabel.place(relx=0.78, rely=0.858)
    totallabel.configure(text="TOTAL")

    totallabel.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    billamountlabel = tk.Label(billwindow, fg="#006400", bg="#ffffff")
    billamountlabel.place(relx=0.87, rely=0.858)
    billamountlabel.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    billamountlabel.configure(text="Rs. "+str(tamount))

    pty=StringVar()
    paytype = ttk.Combobox(billwindow,textvariable=pty)
    paytype.place(relx=0.04,rely=0.899)
    payy()
    paytype['values'] = paylst
    paytype.bind("<<ComboboxSelected>>",payinsert)

    ordinsert = tk.Button(billwindow, font=('Aldhabi', 11, 'bold'), command=getbill)
    ordinsert.place(relx=0.440, rely=0.899, height=43, width=100)
    ordinsert.configure(activebackground="#ececec")
    ordinsert.configure(activeforeground="#000000")
    ordinsert.configure(background="#006400")
    ordinsert.configure(disabledforeground="#a3a3a3")
    ordinsert.configure(foreground="#ffffff")
    ordinsert.configure(highlightbackground="#d9d9d9")
    ordinsert.configure(highlightcolor="black")
    ordinsert.configure(pady="0")
    ordinsert.configure(text='''PRINT''')
    cx = 0
    orderlst = []
    for i in tree.get_children():
        x = tree.item(i, 'values')
        billtree.insert(parent='', index='end', iid=cx, text="", values=(x[0], x[1], x[2], x[3], x[4]))
        cx += 1
        orderlst.append([x])
    billwindow.mainloop()
def getbill():
    global tamount
    cursor.execute("select max(order_id) from orders")
    ordid = cursor.fetchall()
    cursor.execute("select emp_id from employees where ename=:xz",xz=user)
    em=cursor.fetchall()
    dd=str(datetime.date.today())
    yy =datetime.datetime.strptime(dd, '%Y-%m-%d').strftime('%d-%b-%y')
    od=ordid[0][0]+1
    cursor.execute("""select branch_id from employees where ename=:g""",g=user)
    bd=cursor.fetchall()

    if paytype.get() == 'card':
        cursor.execute("insert into orders(order_id,orderdate,emp_id) values(:a,:b,:c) ", a=od, b=yy, c=em[0][0])

        for i in billtree.get_children():
            x = billtree.item(i, 'values')
            cursor.execute("""select item_id from items where item_name=:n""", n=x[1])
            itid = cursor.fetchall()
            if len(itid)==0:
                cursor.execute("""select deal_id from deals where dname=:e""",e=x[1])
                mn = cursor.fetchall()
                cursor.execute("insert into dealdetails(deal_qty,deal_id,order_id) values(:dq,:didd,:ood)",dq=int(x[3]),didd=str(mn[0][0]),ood=od)
                cursor.execute("""commit""")
            else:
                cursor.execute("""select size_id from sizes where size_name=:j""", j=str(x[2]).lower())
                sst = cursor.fetchall()
                if len(sst) == 0:
                    cursor.execute(
                    "insert into itemdetails(item_qty,item_id,size_id,order_id) values(:iq,:iid,Null,:odi) ", iq=x[3],
                    iid=itid[0][0], odi=od)

                else:
                    cursor.execute("insert into itemdetails(item_qty,item_id,size_id,order_id) values(:iq,:iid,:sid,:odi) ", iq=x[3],iid=itid[0][0], sid=sst[0][0], odi=od)

                cursor.execute("""insert into billing(reciept_id,order_id,amount,paymenttype_id) values(:ix,:iy,:iz,:izz)""",
                           ix=int(number[0][0] + 1),
                           iy=od, iz=tamount, izz=112)
                cursor.execute("insert into orderdetail(order_id,branch_id,reciept_id) values(:d,:e,:f)", d=od, e=bd[0][0],
                           f=number[0][0] + 1)
                cursor.execute("insert into accountdetail(accountno,accountname,reciept_id) values(:an,:aa,:rid)", an=acntno,aa=acntname, rid=int(number[0][0]+1))
                cursor.execute("commit")
            for i in tree.get_children():
                tree.delete(i)
            totalamountlabel.configure(text = "Rs. 0")
            billwindow.destroy()
            messagebox.showinfo("Success","Thank you for ordering")

    else:
        cursor.execute("insert into orders(order_id,orderdate,emp_id) values(:a,:b,:c) ", a=od, b=yy, c=em[0][0])
        for i in billtree.get_children():
            x = billtree.item(i, 'values')
            cursor.execute("""select item_id from items where item_name=:n""", n=x[1])
            itid = cursor.fetchall()
            if len(itid) == 0:
                cursor.execute("""select deal_id from deals where dname=:e""", e=x[1])
                mn = cursor.fetchall()
                cursor.execute("insert into dealdetails(deal_qty,deal_id,order_id) values(:dq,:didd,:ood)",
                               dq=int(x[3]), didd=str(mn[0][0]), ood=od)
                cursor.execute("""commit""")
            else:
                cursor.execute("""select size_id from sizes where size_name=:j""", j=str(x[2]).lower())
                sst=cursor.fetchall()
                if len(sst) == 0:
                    cursor.execute(
                    "insert into itemdetails(item_qty,item_id,size_id,order_id) values(:iq,:iid,Null,:odi) ", iq=x[3],
                    iid=itid[0][0], odi=od)
                else:
                    cursor.execute(
                    "insert into itemdetails(item_qty,item_id,size_id,order_id) values(:iq,:iid,:sid,:odi) ", iq=x[3],
                    iid=itid[0][0], sid=sst[0][0], odi=od)

        cursor.execute("""insert into billing(reciept_id,order_id,amount,paymenttype_id) values(:ix,:iy,:iz,:izz)""", ix=int(number[0][0]+1),
                           iy=od, iz=tamount, izz=111)
        cursor.execute("insert into orderdetail(order_id,branch_id,reciept_id) values(:d,:e,:f)", d=od, e=bd[0][0],
                           f=number[0][0]+1)
        cursor.execute("commit")
        messagebox.showinfo("Successfull","Thank you for ordering")

        for i in tree.get_children():
            tree.delete(i)
        totalamountlabel.configure(text="Rs. 0")

        billwindow.destroy()

logingui()