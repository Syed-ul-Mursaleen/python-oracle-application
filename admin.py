from tkinter import *
import tkinter as tk
import cx_Oracle
import CONN

from datetime import datetime
from tkinter import  ttk
from tkinter import messagebox
connection = cx_Oracle.connect('project/12345@//localhost:1522/pdborcl')
cursor = connection.cursor()
global tree2,tree3,search_field,s_var,employeeid,empid,employeename,empname,hire,hiredate,bid,window,erecords,upempwindow,sizes,itmid,udcount
global comm,commission,sal,salary,branch,phn,phone,address,empaddress,email,empemail,bid,size,price,itemid,itmname,itemid,itemname,unitprice,catid
global dealid,dealname,dealprice,dealwindow,tree4,dtree,itemsizecombo,dtreecount,itemnamescombo,updealwindow,updtree,updealname,updealprice,updealid
itemlst=[]
sizeilst=[]
v=[]
uv=[]
dtreecount=0
def dealitem():
    cursor.execute("""select item_name from items""")
    it=cursor.fetchall()
    for i in it:
        itemlst.append(i[0])
def dealisize():
    cursor.execute("""select size_name from sizes where size_id in (1,2,3)""")
    its=cursor.fetchall()
    for i in its:
        sizeilst.append(i[0])
def logout():
    window.destroy()
    import login
    login.logingui()
def viewemp():
    global ecount, erecords
    ecount=1
    cursor.execute("Select * from employees")
    erecords = cursor.fetchall()
    for records in erecords:
        z= datetime.date(records[6])
        zz= datetime.strftime(z, "%d-%b-%y")
        tree2.insert(parent='', index='end', iid=ecount, text="", values=([ecount,records[0],records[1],records[2],records[3],"0"+str(records[4]),records[5],zz, records[7],records[8]]))
        ecount=ecount+1
def delemployees():
    selected = tree2.focus()
    # grad record values
    values = tree2.item(selected, 'values')
    if len(values) == 0:
        messagebox.showerror("error", "No employee selected!")
    else:
        try:
            cursor.execute("""DELETE FROM EMPLOYEES WHERE EMP_ID = :a""", a=int(values[1]))
            cursor.execute("""commit""")
            for i in tree2.get_children():
                tree2.delete(i)
            viewemp()
        except:
            messagebox.showerror("error", "selected Employee had recieved orders")
def upemployees():
    #clear
    empid.delete(0, END)
    empname.delete(0, END)
    empemail.delete(0, END)
    phone.delete(0, END)
    empaddress.delete(0, END)
    hire.delete(0, END)
    salary.delete(0, END)
    commission.delete(0, END)
    #insert
    selected = tree2.focus()
    values = tree2.item(selected, 'values')
    empid.insert(0, values[1])
    empid.config(state="disabled")
    empid.config(disabledbackground="white")
    empname.insert(0, values[2])
    empemail.insert(0, values[3])
    empaddress.insert(0, values[4])
    phone.insert(0, values[5])
    salary.insert(0, values[6])
    hire.insert(0, values[7])
    commission.insert(0, values[8])
    bid.insert(0,values[9])
    hire.configure(state="disabled")
    hire.configure(disabledbackground = "white")
def updateemp():
    emp_id = empid.get()
    e_name = empname.get()
    e_email = empemail.get()
    cont = phone.get()
    empadd = empaddress.get()
    esal = salary.get()
    if len(e_name) > 30 or len(e_name) == 0:
        messagebox.showerror("error", "Invalid Name!")
        upempwindow.destroy()
        updateemployeegui()
    elif len(e_email) > 30 or len(e_email) == 0 or "@" not in e_email:
        messagebox.showerror("error", "Invalid Email!")
        upempwindow.destroy()
        updateemployeegui()
    elif len(cont) > 11 or len(cont) < 11 or len(cont) == 0 or cont.isdecimal() == False or "03" != cont[0:2]:
        messagebox.showerror("error", "Invalid Number!")
        upempwindow.destroy()
        updateemployeegui()
    elif len(empadd) > 40 or len(empadd) == 0:
        messagebox.showerror("error", "Invalid Address Address !")
        upempwindow.destroy()
        updateemployeegui()
    elif len(esal) > 8 or len(esal) == 0 or esal.isdecimal() == False:
        messagebox.showerror("error", "Invalid Salary")
        upempwindow.destroy()
        updateemployeegui()
    else:
        for record in tree2.get_children():
            tree2.delete(record)
    # try:
        empid.config(state="normal")
        hire.config(state="normal")
        cursor.execute("""update employees set 
            ename = :name ,
            email = :email,
            address = :address,
            phone = :phone,
            salary = :salary,
            hiredate= :hire,
            comm = :comm,
            branch_id = :b_id 
            where emp_id = :emp_id""",
                       { 'emp_id':empid.get(),
                        'name':empname.get(),
                           'email': empemail.get(),
                           'address': empaddress.get(),
                           'phone': int(phone.get()),
                           'salary': salary.get(),
                           'hire': hire.get(),
                           'comm': commission.get(),
                           'b_id': bid.get(),
                        }
                       )
        connection.commit()
        tree2.delete()
        viewemp()
        messagebox.showinfo("INFO","Successfull updated record")
        upempwindow.destroy()
def additems():
    item_name = itemname.get()
    uprice = unitprice.get()
    cid=catid.get()
    itmcombo=itemsizescombo.get()
    cursor.execute("SELECT item_id FROM ITEMS")
    allitemrecords = cursor.fetchall()
    itemids = []
    cursor.execute("""select max(item_id) from items""")
    ab = cursor.fetchall()
    item_id = int(ab[0][0]) + 1

    for record in allitemrecords:
        itemids.append(int(record[0]))
    if len(item_name) > 30 or len(item_name) == 0:
        messagebox.showerror("error", "Invalid Name!")
    elif len(uprice) > 4 or len(uprice) == 0:
        messagebox.showerror("error", "Invalid Price!")
    elif len(cid) > 2 or len(cid) == 0:
        messagebox.showerror("error", "Invalid Category ID!")
    else:
        for record in tree3.get_children():
            tree3.delete(record)
    cursor.execute("""select item_id from items where item_name=:a""",a=item_name)
    zz=cursor.fetchall()
    if len(zz)==0:
        sql = """INSERT INTO items(item_ID,item_name,cat_id) VALUES(:itemid,:itemname,:catid)"""
        cursor.execute(sql,itemid=item_id,itemname=item_name,catid=cid )
        connection.commit()
        cursor.execute("""select size_id from sizes where size_name=:sizee""",sizee=itmcombo)
        x=cursor.fetchall()
        cursor.execute("insert into price(item_id,price,size_id) values(:itemid,:price,:sizeid)",itemid=item_id,price=uprice,sizeid=int(x[0][0]))
        messagebox.showinfo("Success", "Successfully added item")
        viewitems()
    elif len(zz) != 0:
        cursor.execute("""select size_id from price where item_id =:xc""", xc=int(zz[0][0]))
        yy = cursor.fetchall()

        cursor.execute("""Select size_id from sizes where size_name=:v""", v=itmcombo)
        kk = cursor.fetchall()

        if len(yy)==0:
            cursor.execute("""select size_id from sizes where size_name=:sizee""", sizee=itmcombo)
            x = cursor.fetchall()
            cursor.execute("insert into price(item_id,price,size_id) values(:itemid,:price,:sizeid)", itemid=int(zz[0][0]),
                           price=uprice, sizeid=int(x[0][0]))
            connection.commit()
            viewitems()
            messagebox.showinfo("Success", "Successfully added item")
        elif len(yy)!=0:
            for i in yy:
                if int(i[0])==int(kk[0][0]):
                    messagebox.showerror("error", "Already exist")
                    itemwindow.destroy()
                    break
            else :
                cursor.execute("""select size_id from sizes where size_name=:sizee""", sizee=itmcombo)
                x = cursor.fetchall()
                cursor.execute("insert into price(item_id,price,size_id) values(:itemid,:price,:sizeid)", itemid=int(zz[0][0]),
                           price=uprice, sizeid=int(x[0][0]))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added item")
                viewitems()
def delitems():
    selected = tree3.focus()
    # grad record values
    values = tree3.item(selected, 'values')
    if len(values) == 0:
        messagebox.showerror("error", "No Item selected!")
    else:
        try:

            cursor.execute("""DELETE FROM PRICE WHERE ITEM_ID = :a""", a=int(values[1]))
            cursor.execute("""select item_id from price where item_id=:x""",x=int(values[1]))
            ff=cursor.fetchall()
            if len(ff)==0:
                cursor.execute("""DELETE FROM ITEMS WHERE ITEM_ID = :a""", a=int(values[1]))
                cursor.execute("""commit""")
            for i in tree3.get_children():
                tree3.delete(i)
            viewitems()
            messagebox.showerror("error", " Item deleted")

        except:
            messagebox.showerror("error", "Cannot delete This Item")
def updateitems():

    itemid.delete(0, END)
    itmname.delete(0, END)
    price.delete(0, END)
    size.delete(0, END)

    selectedz = tree3.focus()
    values = tree3.item(selectedz, 'values')
    itemid.insert(0, values[1])
    itemid.config(state="disabled")
    itemid.config(disabledbackground="white")
    itmname.insert(0, values[2])
    price.insert(0, values[4])
    size.insert(0, values[3])
    size.config(state="disabled")
    size.config(disabledbackground="white")
def upitems():
    # try:

    itemid.config(state="normal")
    size.config(state="normal")
    si = size.get()
    itmprice=int(price.get())

    iid=int(itemid.get())
    q = """update items set item_name = :itmname where item_id = :item_id"""
    cursor.execute(q,item_id= iid,itmname=itmname.get())
    cursor.execute("""select size_id from sizes where size_name = :siz""",siz=si)
    rowss=cursor.fetchall()
    w=int(rowss[0][0])
    cursor.execute("commit")
    cursor.execute("""update price set price = :xyx where item_id = :yz and size_id= :xc""",xyx=itmprice, yz=iid, xc=w)
    cursor.execute("commit")
    messagebox.showinfo("INFO", "Successfull updated record")
    for i in tree3.get_children():
        tree3.delete(i)
    viewitems()
    itmupwindow.destroy()
def vieworders():
    global orecord,ocount
    ocount = 1
    cursor.execute("Select o.order_id,o.orderdate,o.emp_id,od.branch_id,od.reciept_id,b.amount,b.paymenttype_id from orders o inner join orderdetail od on(o.order_id=od.order_id) inner join billing b on(od.reciept_id=b.reciept_id)")
    orecord = cursor.fetchall()
    for orecords in orecord:
        yy=datetime.date(orecords[1])
        y = datetime.strftime(yy, "%d-%b-%y")
        tree.insert(parent='', index='end', iid=ocount, text="", values=(
        [ocount,orecords[0], y, orecords[2], orecords[3], orecords[4], orecords[5], orecords[6]]))
        ocount = ocount + 1
def viewitems():
    global irecord,icount
    icount = 1
    cursor.execute("Select i.item_id,i.item_name,s.size_name,p.price,i.cat_id from items i inner join price p on(i.item_id=p.item_id) full join sizes s on (p.size_id=s.size_id)  ")
    irecord = cursor.fetchall()
    for irecords in irecord:
        tree3.insert(parent='', index='end', iid=icount, text="", values=(
        [icount,irecords[0], irecords[1], irecords[2], irecords[3], irecords[4]]))
        icount = icount + 1
def viewdeals():
    global drecord,dcount
    dcount = 1
    cursor.execute("Select distinct(deal_id),dname,dprice from deals")
    drecord = cursor.fetchall()
    for drecords in drecord:
        tree4.insert(parent='', index='end', iid=dcount, text="", values=(
        [dcount,drecords[0], drecords[1], drecords[2]]))
        dcount = dcount + 1
def adddeals():
    dealid.config(state="normal")
    did=int(dealid.get())
    dn=dealname.get()
    dp=int(dealprice.get())
    cursor.execute("""insert into deals(deal_id,dname,dprice) values(:x,:y,:z)""",x=did,y=dn,z=dp)
    connection.commit()
    for i in range(0,len(v)):
        cursor.execute("""select item_id from items
        where item_name =:aa """,aa=str(v[0][0]))

        isd = cursor.fetchall()
        cursor.execute("""select size_id from sizes
                where size_name =:bb """, bb=str(v[0][1]))
        kk=cursor.fetchall()
        v.pop(0)

        cursor.execute("""insert into dealdescription(deal_id,item_id,size_id) values(:a,:b,:c)""",a=did,b=isd[0][0],c=kk[0][0])
    cursor.execute("""commit""")
    messagebox.showinfo("Success","Deal inserted ")
    dealwindow.destroy()
    for i in tree4.get_children():
        tree4.delete(i)
    viewdeals()
def deldeals():
    select=tree4.focus()
    val = tree4.item(select,'val')
    if len(val) == 0:
        messagebox.showerror("error", "No Item selected!")
    else:
        try:
            cursor.execute("""DELETE FROM DEALDESCRIPTION WHERE DEAL_ID= :a""", a=int(val[1]))
            cursor.execute("""commit""")
            cursor.execute("""DELETE FROM DEALS WHERE DEAL_ID = :a""", a=int(val[1]))
            cursor.execute("""commit""")
            messagebox.showinfo("Message", "Deal deleted ")
            for i in tree4.get_children():
                tree4.delete(i)
            viewdeals()
        except:
            messagebox.showerror("error", "Cannot delete This Item")
def updeals():
    updealid.config(state="normal")
    updid=int(updealid.get())
    updn=updealname.get()
    updp=updealprice.get()
    if len(updn) > 30 or len(updn) == 0:
        messagebox.showerror("error", "Invalid Name!")
        updealwindow.attributes("-topmost",True)
    elif len(updp) > 4 or len(updp) == 0:
        messagebox.showerror("error", "Invalid Name!")
        updealwindow.attributes("-topmost", True)
    selected = updtree.focus()
    # grad record values
    values = updtree.item(selected, 'values')
    if updtree.get_children() == []:
        messagebox.showerror("error", "No items selected for deal!")
    else:
        for record in tree4.get_children():
            tree4.delete(record)
        sql="update deals set dname = :dealname,dprice= :dp where deal_id = :did"
        cursor.execute(sql,did= updid,dealname=updn,dp=int(updp))
        connection.commit()


        tree4.delete()
        viewdeals()
        updealwindow.destroy()
        messagebox.showinfo("INFO", "Successfull updated record")

def updd():
    global udcount
    updealid.delete(0,END)
    updealname.delete(0, END)
    updealprice.delete(0, END)
    # insert
    selected = tree4.focus()
    values = tree4.item(selected, 'values')
    updealid.insert(0, values[1])
    updealid.config(state="disabled")
    updealid.config(disabledbackground="white")
    updealname.insert(0, values[2])
    updealprice.insert(0, values[3])
    cursor.execute("""select i.item_name,s.size_name from items i inner join dealdescription dd on (i.item_id=dd.item_id) 
    inner join sizes s on(dd.size_id=s.size_id) where dd.deal_id=:xx""",xx=int(values[1]))
    itm=cursor.fetchall()
    udcount=1
    for i in itm:
        uv.append([i[0],i[1]])
        updtree.insert(parent='', index='end', iid=udcount, text="", values=(
        [udcount,i[0], i[1]]))
        udcount = udcount + 1
def checkentry(e):
    typed = search_field.get()
    selected = s_var.get()
    if selected == 0 or selected == 1:
        if typed == '':
            data = erecords
        else:
            data = []
            for record in erecords:
                if selected == 0:
                    if typed in str(record[selected]):
                        data.append(record)
                else:
                    if typed.lower() in record[selected].lower():
                        data.append(record)
        for record in tree2.get_children():
            tree2.delete(record)
        ecount = 0
        for record in data:
            yy = datetime.date(record[6])

            y = datetime.strftime(yy, "%d-%b-%y")
            tree2.insert(parent='', index='end', iid=ecount, text='',
                               values=(ecount,record[0], record[1], record[2], record[3], record[4], record[5], y, record[7], record[8]))
            ecount += 1
    elif selected == 2 or selected == 3:
        if typed == '':
            data3 = irecord
        else:
            data3 = []
            for record in irecord:
                if selected == 2:
                    if typed in str(record[0]):
                        data3.append(record)
                if selected == 3:
                    if typed in record[1]:
                        data3.append(record)
        for record in tree3.get_children():
            tree3.delete(record)
        icount = 0
        for records in data3:
            tree3.insert(parent='', index='end', iid=icount, text='',
                               values=(icount,records[0], records[1], records[2], records[3], records[4]))
            icount += 1
    elif selected == 4 or selected == 5:
        if typed == '':
            data2 = orecord
        else:
            data2 = []
            for record in orecord:
                if selected == 4:
                    if typed in str(record[0]):
                        data2.append(record)
                if selected == 5:
                    yy = datetime.date(record[1])
                    y = datetime.strftime(yy, "%d-%b-%y")
                    if typed in str(y):
                        data2.append(record)
        for record in tree.get_children():
            tree.delete(record)
        ocount = 0
        for record in data2:
            yy = datetime.date(record[1])
            y = datetime.strftime(yy, "%d-%b-%y")
            tree.insert(parent='', index='end', iid=ocount, text='',
                               values=(ocount,record[0], y, record[2], record[3], record[4], record[5], record[6]))
            ocount += 1
def main():
    global tree3,tree2,tree,tree4,search_field,s_var,window
    window = Tk()
    window.geometry("1443x1345+0+0")
    window.minsize(148, 1)
    window.maxsize(1916, 1047)
    window.state('zoomed')
    window.resizable(1, 1)
    window.title("CALIFORNIA PIZZA POS")
    window.configure(background="#ffffff")
    window.overrideredirect(True)
    Framex = tk.Frame(window, bg="#006400")
    Framex.place(relx=-0.007, rely=0.0, relwidth=1.1, relheight=0.03)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Helvetica', 10, 'bold'),
                        command=window.destroy)
    exitbtn.place(x=1523, y=1)
    labelx = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Helvetica', 11, 'bold'), foreground="#ffffff",
                      bg="#006400")
    labelx.place(x=700, y=0.4)

    Frame_1 = tk.Frame(window)
    Frame_1.place(x=-0.007, y=27, relheight=0.168, relwidth=1.002)

    Frame_1.configure(relief='groove')
    Frame_1.configure(borderwidth="2")
    Frame_1.configure(relief="groove")
    Frame_1.configure(background="#ffffff")

    photo = PhotoImage(file='logo.png')
    framepic = Label(Frame_1, image=photo)
    framepic.pack()


    Labelu = tk.Label(Frame_1)
    Labelu.place(relx=0.905, rely=0.310)
    Labelu.configure(background="#ffffff")
    Labelu.configure(disabledforeground="#a3a3a3")
    Labelu.configure(
        font="-family {Aldhabi} -size 9 -weight bold")
    Labelu.configure(foreground="#006400")
    Labelu.configure(text="ADMINISTRATOR")

    photouser = PhotoImage(file='user.png')
    picu = Label(Frame_1, image=photouser)
    picu.configure(bd=0)
    picu.place(relx=0.874, rely=0.293)

    Button1_22 = tk.Button(Frame_1, command=logout)
    Button1_22.place(relx=0.907, rely=0.442, height=25, width=69)
    Button1_22.configure(activebackground="#006400")
    Button1_22.configure(activeforeground="#ffffff")
    Button1_22.configure(background="#006400")
    Button1_22.configure(disabledforeground="#a3a3a3")
    Button1_22.configure(font="-family {Aldhabi} -size 8 -weight bold -slant roman -underline 0 -overstrike 0")
    Button1_22.configure(foreground="#ffffff")
    Button1_22.configure(highlightbackground="#006400")
    Button1_22.configure(pady="0")
    Button1_22.configure(text='''LOGOUT''')
    Frame2 = tk.Frame(window)
    Frame2.configure(bg="white")
    Frame2.place(relx=0.0, rely=0.20, relwidth=1, relheight=0.8)

    Labelorder = tk.Label(Frame2,text="ORDER DETAILS",bg="white",fg="#006400",font="-family {Aldhabi} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Labelorder.place(relx=0.56,rely=0.50)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#006400",
                    fieldbackground="#006400", foreground="white", font=('Aldhabi', 11, "bold"))
    style.map('Treeview', background=[("selected", "#006400")])

    tree = ttk.Treeview(Frame2, column=('S.no','Order ID','Orderdate', 'Emp ID', 'Branch ID','Reciept ID','Amount','Paymenttype ID'), selectmode='extended')
    scrollbarx = Scrollbar(tree, orient=HORIZONTAL)
    scrollbary = Scrollbar(tree, orient=VERTICAL)
    tree.config(yscrollcommand=scrollbary.set)
    tree.config(xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('S.no', text="S.no", anchor=CENTER)
    tree.heading('Order ID', text="Order ID", anchor=CENTER)
    tree.heading('Orderdate', text="Orderdate", anchor=CENTER)
    tree.heading('Emp ID', text="Emp ID", anchor=CENTER)
    tree.heading('Branch ID', text="Branch ID", anchor=CENTER)
    tree.heading('Reciept ID', text="Reciept ID", anchor=CENTER)
    tree.heading('Amount', text="Amount", anchor=CENTER)
    tree.heading('Paymenttype ID', text="Paymenttype ID", anchor=CENTER)
    tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree.column('#1', stretch=NO, minwidth=0, width=55, anchor=CENTER)
    tree.column('#2', stretch=NO, minwidth=0, width=105, anchor=CENTER)
    tree.column('#3', stretch=NO, minwidth=0, width=105, anchor=CENTER)
    tree.column('#4', stretch=NO, minwidth=0, width=85, anchor=CENTER)
    tree.column('#5', stretch=NO, minwidth=0, width=95, anchor=CENTER)
    tree.column('#6', stretch=NO, minwidth=0, width=105, anchor=CENTER)
    tree.column('#7', stretch=NO, minwidth=0, width=105, anchor=CENTER)
    tree.column('#8', stretch=NO, minwidth=0, width=105, anchor=CENTER)


    tree.place(relx=0.56, rely=0.55, relheight=0.388, relwidth=0.4)
    vieworders()
    Labelemp = tk.Label(Frame2, text="EMPLOYEE DETAILS", bg="white", fg="#006400",
                          font="-family {Aldhabi} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Labelemp.place(relx=0.06, rely=0.50)

    tree2 = ttk.Treeview(Frame2, column=(
    'S.no','Emp id', 'Ename', 'Email', 'Address', 'Phone', 'Salary', 'Hiredate', 'Commission', 'Branch id'),
                        selectmode='extended')
    scrollbarx2 = Scrollbar(tree2, orient=HORIZONTAL)
    scrollbary2 = Scrollbar(tree2, orient=VERTICAL)
    tree2.config(yscrollcommand=scrollbary2.set)
    tree2.config(xscrollcommand=scrollbarx2.set)
    scrollbary2.config(command=tree2.yview)
    scrollbary2.pack(side=RIGHT, fill=Y)
    scrollbarx2.config(command=tree2.xview)
    scrollbarx2.pack(side=BOTTOM, fill=X)
    tree2.heading('S.no', text="S.no", anchor=CENTER)
    tree2.heading('Emp id', text="Emp id", anchor=CENTER)
    tree2.heading('Ename', text="Ename", anchor=CENTER)
    tree2.heading('Email', text="Email", anchor=CENTER)
    tree2.heading('Address', text="Address", anchor=CENTER)
    tree2.heading('Phone', text="Phone", anchor=CENTER)
    tree2.heading('Salary', text="Salary", anchor=CENTER)
    tree2.heading('Hiredate', text="Hiredate", anchor=CENTER)
    tree2.heading('Commission', text="Commission", anchor=CENTER)
    tree2.heading('Branch id', text="Branch id", anchor=CENTER)
    tree2.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree2.column('#1', stretch=NO, minwidth=0, width=50, anchor=CENTER)
    tree2.column('#2', stretch=NO, minwidth=0, width=95, anchor=CENTER)
    tree2.column('#3', stretch=NO, minwidth=0, width=115, anchor=CENTER)
    tree2.column('#4', stretch=NO, minwidth=0, width=205, anchor=CENTER)
    tree2.column('#5', stretch=NO, minwidth=0, width=145, anchor=CENTER)
    tree2.column('#6', stretch=NO, minwidth=0, width=100, anchor=CENTER)
    tree2.column('#7', stretch=NO, minwidth=0, width=100, anchor=CENTER)
    tree2.column('#8', stretch=NO, minwidth=0, width=95, anchor=CENTER)
    tree2.column('#9', stretch=NO, minwidth=0, width=85, anchor=CENTER)
    tree2.column('#10', stretch=NO, minwidth=0, width=105, anchor=CENTER)
    tree2.place(relx=0.022, rely=0.55, relheight=0.38, relwidth=0.5)
    viewemp()

    Framebtn = tk.Frame(Frame2,bg="white",highlightbackground="#006400",highlightthickness=2)
    Framebtn.place(relx=0.022,rely=0.1,relheight=0.340,relwidth=0.5)

    managelbl = tk.Label(Frame2, bg='#ffffff', fg="#006400",
                         font="-family {Aldhabi} -size 19 -weight bold -slant roman -underline 0 -overstrike 0")
    managelbl.place(relx=0.03, rely=0.078)
    managelbl.configure(text="MANAGE")

    addemp_btn= tk.Button(Framebtn,command=addempgui)
    addemp_btn.place(relx=0.03, rely=0.12, height=35, width=188)
    addemp_btn.configure(activebackground="#006400")
    addemp_btn.configure(activeforeground="#ffffff")
    addemp_btn.configure(background="#006400")
    addemp_btn.configure(disabledforeground="#a3a3a3")
    addemp_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    addemp_btn.configure(foreground="#ffffff")
    addemp_btn.configure(highlightbackground="#006400")
    addemp_btn.configure(highlightcolor="black")
    addemp_btn.configure(pady="0")
    addemp_btn.configure(text='''ADD EMPLOYEES''')


    delemp_btn = tk.Button(Framebtn, command=delemployees)
    delemp_btn.place(relx=0.03, rely=0.67, height=35, width=188)
    delemp_btn.configure(activebackground="#006400")
    delemp_btn.configure(activeforeground="#ffffff")
    delemp_btn.configure(background="#006400")
    delemp_btn.configure(disabledforeground="#a3a3a3")
    delemp_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    delemp_btn.configure(foreground="#ffffff")
    delemp_btn.configure(highlightbackground="#006400")
    delemp_btn.configure(highlightcolor="black")
    delemp_btn.configure(pady="0")
    delemp_btn.configure(text='''DELETE EMPLOYEE''')

    upemp_btn = tk.Button(Framebtn, command=updateemployeegui)
    upemp_btn.place(relx=0.03, rely=0.4, height=35, width=188)
    upemp_btn.configure(activebackground="#006400")
    upemp_btn.configure(activeforeground="#ffffff")
    upemp_btn.configure(background="#006400")
    upemp_btn.configure(disabledforeground="#a3a3a3")
    upemp_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    upemp_btn.configure(foreground="#ffffff")
    upemp_btn.configure(highlightbackground="#006400")
    upemp_btn.configure(highlightcolor="black")
    upemp_btn.configure(pady="0")
    upemp_btn.configure(text='''UPDATE EMPLOYEE''')

    additem_btn = tk.Button(Framebtn, command=additemgui)
    additem_btn.place(relx=0.32, rely=0.12, height=35, width=188)
    additem_btn.configure(activebackground="#006400")
    additem_btn.configure(activeforeground="#ffffff")
    additem_btn.configure(background="#006400")
    additem_btn.configure(disabledforeground="#a3a3a3")
    additem_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    additem_btn.configure(foreground="#ffffff")
    additem_btn.configure(highlightbackground="#006400")
    additem_btn.configure(highlightcolor="black")
    additem_btn.configure(pady="0")
    additem_btn.configure(text='''ADD ITEM''')

    upitem_btn = tk.Button(Framebtn, command=updateitemgui)
    upitem_btn.place(relx=0.32, rely=0.4, height=35, width=188)
    upitem_btn.configure(activebackground="#006400")
    upitem_btn.configure(activeforeground="#ffffff")
    upitem_btn.configure(background="#006400")
    upitem_btn.configure(disabledforeground="#a3a3a3")
    upitem_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    upitem_btn.configure(foreground="#ffffff")
    upitem_btn.configure(highlightbackground="#006400")
    upitem_btn.configure(highlightcolor="black")
    upitem_btn.configure(pady="0")
    upitem_btn.configure(text='''UPDATE ITEM''')

    delitem_btn = tk.Button(Framebtn, command=delitems)
    delitem_btn.place(relx=0.32, rely=0.67, height=35, width=188)
    delitem_btn.configure(activebackground="#006400")
    delitem_btn.configure(activeforeground="#ffffff")
    delitem_btn.configure(background="#006400")
    delitem_btn.configure(disabledforeground="#a3a3a3")
    delitem_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    delitem_btn.configure(foreground="#ffffff")
    delitem_btn.configure(highlightbackground="#006400")
    delitem_btn.configure(highlightcolor="black")
    delitem_btn.configure(pady="0")
    delitem_btn.configure(text='''DELETE ITEM''')

    adddeal_btn = tk.Button(Framebtn, command=adddealgui)
    adddeal_btn.place(relx=0.61, rely=0.12, height=35, width=188)
    adddeal_btn.configure(activebackground="#006400")
    adddeal_btn.configure(activeforeground="#ffffff")
    adddeal_btn.configure(background="#006400")
    adddeal_btn.configure(disabledforeground="#a3a3a3")
    adddeal_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    adddeal_btn.configure(foreground="#ffffff")
    adddeal_btn.configure(highlightbackground="#006400")
    adddeal_btn.configure(highlightcolor="black")
    adddeal_btn.configure(pady="0")
    adddeal_btn.configure(text='''ADD DEALS''')

    updeal_btn = tk.Button(Framebtn, command=updealgui)
    updeal_btn.place(relx=0.61, rely=0.4, height=35, width=188)
    updeal_btn.configure(activebackground="#006400")
    updeal_btn.configure(activeforeground="#ffffff")
    updeal_btn.configure(background="#006400")
    updeal_btn.configure(disabledforeground="#a3a3a3")
    updeal_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    updeal_btn.configure(foreground="#ffffff")
    updeal_btn.configure(highlightbackground="#006400")
    updeal_btn.configure(highlightcolor="black")
    updeal_btn.configure(pady="0")
    updeal_btn.configure(text='''UPDATE DEALS''')

    deldeal_btn = tk.Button(Framebtn, command=deldeals)
    deldeal_btn.place(relx=0.61, rely=0.67, height=35, width=188)
    deldeal_btn.configure(activebackground="#006400")
    deldeal_btn.configure(activeforeground="#ffffff")
    deldeal_btn.configure(background="#006400")
    deldeal_btn.configure(disabledforeground="#a3a3a3")
    deldeal_btn.configure(font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    deldeal_btn.configure(foreground="#ffffff")
    deldeal_btn.configure(highlightbackground="#006400")
    deldeal_btn.configure(highlightcolor="black")
    deldeal_btn.configure(pady="0")
    deldeal_btn.configure(text='''DELETE DEAL''')

    #search
    s_var = IntVar()
    id_r = Radiobutton(Frame_1, text="EmpID", variable=s_var, value=0, bg='white', font="-family {Aldhabi} -size 9")
    id_r.place(relx=0.02, rely=0.68)
    name_r = Radiobutton(Frame_1, text="Emp Name", variable=s_var, value=1, bg='white',
                         font="-family {Aldhabi} -size 9")
    name_r.place(relx=0.02, rely=0.8)
    oid_r = Radiobutton(Frame_1, text="OrderID", variable=s_var, value=4, bg='white', font="-family {Aldhabi} -size 9")
    oid_r.place(relx=0.094, rely=0.68)
    odate_r = Radiobutton(Frame_1, text="Order Date", variable=s_var, value=5, bg='white',
                         font="-family {Aldhabi} -size 9")
    odate_r.place(relx=0.094, rely=0.8)
    itmid_r = Radiobutton(Frame_1, text="ItemID", variable=s_var, value=2, bg='white', font="-family {Aldhabi} -size 9")
    itmid_r.place(relx=0.155, rely=0.68)
    itmname_r = Radiobutton(Frame_1, text="Item Name", variable=s_var, value=3, bg='white',
                         font="-family {Aldhabi} -size 9")
    itmname_r.place(relx=0.155, rely=0.8)
    search_field= tk.Entry(Frame_1,highlightbackground="#006400",highlightthickness=2)
    search_field.place(relx=0.03, rely=0.42, height=35, width=260)
    search_field.bind("<KeyRelease>", checkentry)

    searchlbl = tk.Label(Frame_1,highlightbackground="#006400", bg='#ffffff', fg="#006400",
                         font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
    searchlbl.place(relx=0.038, rely=0.288)
    searchlbl.configure(text="Search")



    Labelitem = tk.Label(Frame2, text="ITEMS DETAILS", bg="white", fg="#006400",
                        font="-family {Aldhabi} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Labelitem.place(relx=0.55, rely=0.06)

    tree3 = ttk.Treeview(Frame2, column=('S.no', 'Item id', 'Item Name', 'Size', 'Unit Price', 'Cat_ID'),
                        selectmode='extended')
    scrollbarx = Scrollbar(tree3, orient=HORIZONTAL)
    scrollbary = Scrollbar(tree3, orient=VERTICAL)
    tree3.config(yscrollcommand=scrollbary.set)
    tree3.config(xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree3.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree3.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree3.heading('S.no', text="S.no", anchor=CENTER)
    tree3.heading('Item id', text="Item id", anchor=CENTER)
    tree3.heading('Item Name', text="Item Name", anchor=CENTER)
    tree3.heading('Size', text="Size", anchor=CENTER)
    tree3.heading('Unit Price', text="Unit Price", anchor=CENTER)
    tree3.heading('Cat_ID', text="Cat_ID", anchor=CENTER)
    # tree.tag_configure()
    tree3.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree3.column('#1', stretch=NO, minwidth=0, width=45, anchor=CENTER)
    tree3.column('#2', stretch=NO, minwidth=0, width=57, anchor=CENTER)
    tree3.column('#3', stretch=NO, minwidth=0, width=95, anchor=CENTER)
    tree3.column('#4', stretch=NO, minwidth=0, width=85, anchor=CENTER)
    tree3.column('#5', stretch=NO, minwidth=0, width=85, anchor=CENTER)
    tree3.column('#6', stretch=NO, minwidth=0, width=85, anchor=CENTER)
    tree3.place(relx=0.55, rely=0.10, relheight=0.35, relwidth=0.20)

    viewitems()

    Labeldeal = tk.Label(Frame2, text="DEAL DETAILS", bg="white", fg="#006400",
                         font="-family {Aldhabi} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Labeldeal.place(relx=0.782, rely=0.06)

    tree4 = ttk.Treeview(Frame2, column=('S.no', 'Deal id', 'Deal Name', 'Deal Price'),
                         selectmode='extended')
    scrollbarx = Scrollbar(tree4, orient=HORIZONTAL)
    scrollbary = Scrollbar(tree4, orient=VERTICAL)
    tree4.config(yscrollcommand=scrollbary.set)
    tree4.config(xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree4.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree4.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree4.heading('S.no', text="S.no", anchor=CENTER)
    tree4.heading('Deal id', text="Deal id", anchor=CENTER)
    tree4.heading('Deal Name', text="Deal Name", anchor=CENTER)
    tree4.heading('Deal Price', text="Deal Price", anchor=CENTER)
    # tree.tag_configure()
    tree4.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree4.column('#1', stretch=NO, minwidth=0, width=46, anchor=CENTER)
    tree4.column('#2', stretch=NO, minwidth=0, width=79, anchor=CENTER)
    tree4.column('#3', stretch=NO, minwidth=0, width=88, anchor=CENTER)
    tree4.column('#4', stretch=NO, minwidth=0, width=90, anchor=CENTER)
    tree4.place(relx=0.78, rely=0.10, relheight=0.35, relwidth=0.18)
    viewdeals()


    window.mainloop()
def updateemployeegui():
    global emloyeeid, empid, employeename, email, address, phn, comm, sal, hiredate, branch,upempwindow
    global empname, phone, commission, hire, empemail, empname, bid, empaddress, salary
    foc = tree2.focus()
    values = tree2.item(foc, 'values')
    if len(values) == 0:
        messagebox.showerror("Error", "Select an employee to update")
    else:
        upempwindow = Tk()
        upempwindow.geometry("610x560+519+200")
        upempwindow.minsize(148, 1)
        upempwindow.maxsize(1924, 1055)
        upempwindow.resizable(1, 1)
        upempwindow.title("California Pizza POS")
        upempwindow.configure(background="#ffffff")
        upempwindow.overrideredirect(True)

        Framex = tk.Frame(upempwindow, bg="#006400")
        Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.06)
        exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Helvetica', 10, 'bold'),
                            command=upempwindow.destroy)
        exitbtn.place(x=597, y=7)
        label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Aldhabi', 10, 'bold'), foreground="#ffffff",
                         bg="#006400")
        label.pack(pady=10)

        separator = ttk.Separator(upempwindow, orient='horizontal')
        separator.place(relx=0.05, rely=0.2, relwidth=0.9)

        Labelx = tk.Label(upempwindow)
        Labelx.place(relx=0.327, rely=0.117, height=46, width=253)
        Labelx.configure(background="#ffffff")
        Labelx.configure(
            font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
        Labelx.configure(foreground="#006400")
        Labelx.configure(text='''UPDATE EMPLOYEE ''')

        employeeid = StringVar()
        empid = tk.Entry(upempwindow, textvariable=employeeid, highlightbackground="#006400", highlightthickness=2)
        empid.place(relx=0.03, rely=0.280, relheight=0.07, relwidth=0.37)

        empidlable = tk.Label(upempwindow)
        empidlable.place(relx=0.041, rely=0.26)
        empidlable.configure(background="#ffffff")
        empidlable.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        empidlable.configure(disabledforeground="#a3a3a3")
        empidlable.configure(foreground="#006400")
        empidlable.configure(text='''Emp ID ''')

        employeename = StringVar()
        empname = tk.Entry(upempwindow, textvariable=employeename, highlightbackground="#006400", highlightthickness=2)
        empname.place(relx=0.03, rely=0.404, relheight=0.07, relwidth=0.37)

        enamelabel = tk.Label(upempwindow)
        enamelabel.place(relx=0.041, rely=0.377)
        enamelabel.configure(background="#ffffff")
        enamelabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        enamelabel.configure(disabledforeground="#a3a3a3")
        enamelabel.configure(foreground="#006400")
        enamelabel.configure(text='''Ename ''')

        email = StringVar()
        empemail = tk.Entry(upempwindow, textvariable=email, highlightbackground="#006400", highlightthickness=2)
        empemail.place(relx=0.03, rely=0.53, relheight=0.07, relwidth=0.37)

        emaillabel = tk.Label(upempwindow)
        emaillabel.place(relx=0.041, rely=0.507)
        emaillabel.configure(background="#ffffff")
        emaillabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        emaillabel.configure(disabledforeground="#a3a3a3")
        emaillabel.configure(foreground="#006400")
        emaillabel.configure(text='''Email ''')

        address = StringVar()
        empaddress = tk.Entry(upempwindow, textvariable=address, highlightbackground="#006400", highlightthickness=2)
        empaddress.place(relx=0.03, rely=0.67, relheight=0.07, relwidth=0.37)

        addresslabel = tk.Label(upempwindow)
        addresslabel.place(relx=0.04, rely=0.641)
        addresslabel.configure(background="#ffffff")
        addresslabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        addresslabel.configure(disabledforeground="#a3a3a3")
        addresslabel.configure(foreground="#006400")
        addresslabel.configure(text='''Address ''')

        phn = StringVar()
        phone = tk.Entry(upempwindow, textvariable=phn, highlightbackground="#006400", highlightthickness=2)
        phone.place(relx=0.03, rely=0.79, relheight=0.07, relwidth=0.37)

        phonelabel = tk.Label(upempwindow)
        phonelabel.place(relx=0.046, rely=0.767)
        phonelabel.configure(background="#ffffff")
        phonelabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        phonelabel.configure(disabledforeground="#a3a3a3")
        phonelabel.configure(foreground="#006400")
        phonelabel.configure(text='''Phone ''')

        sal = StringVar()
        salary = tk.Entry(upempwindow, textvariable=sal, highlightbackground="#006400", highlightthickness=2)
        salary.place(relx=0.53, rely=0.28, relheight=0.07, relwidth=0.37)

        sallabel = tk.Label(upempwindow)
        sallabel.place(relx=0.547, rely=0.262)
        sallabel.configure(background="#ffffff")
        sallabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        sallabel.configure(disabledforeground="#a3a3a3")
        sallabel.configure(foreground="#006400")
        sallabel.configure(text='''Salary ''')

        hiredate = StringVar()
        hire = tk.Entry(upempwindow, textvariable=hiredate, highlightbackground="#006400", highlightthickness=2)
        hire.place(relx=0.53, rely=0.404, relheight=0.07, relwidth=0.37)

        hiredatelabel = tk.Label(upempwindow)
        hiredatelabel.place(relx=0.538, rely=0.38)
        hiredatelabel.configure(background="#ffffff")
        hiredatelabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        hiredatelabel.configure(disabledforeground="#a3a3a3")
        hiredatelabel.configure(foreground="#006400")
        hiredatelabel.configure(text='''Hiredate ''')

        comm = StringVar()
        commission = tk.Entry(upempwindow, textvariable=comm, highlightbackground="#006400", highlightthickness=2)
        commission.place(relx=0.53, rely=0.53, relheight=0.07, relwidth=0.37)

        commlabel = tk.Label(upempwindow)
        commlabel.place(relx=0.539, rely=0.511)
        commlabel.configure(background="#ffffff")
        commlabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        commlabel.configure(disabledforeground="#a3a3a3")
        commlabel.configure(foreground="#006400")
        commlabel.configure(text='''Commission ''')

        branch = StringVar()
        bid = tk.Entry(upempwindow, textvariable=branch, highlightbackground="#006400", highlightthickness=2)
        bid.place(relx=0.53, rely=0.67, relheight=0.07, relwidth=0.37)

        branchlabel = tk.Label(upempwindow)
        branchlabel.place(relx=0.546, rely=0.642)
        branchlabel.configure(background="#ffffff")
        branchlabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        branchlabel.configure(disabledforeground="#a3a3a3")
        branchlabel.configure(foreground="#006400")
        branchlabel.configure(text='''Branch ID''')
        upemployees()
        up_btn = tk.Button(upempwindow, command=updateemp)
        up_btn.place(relx=0.63, rely=0.79, height=35, width=103)
        up_btn.configure(activebackground="#006400")
        up_btn.configure(activeforeground="#ffffff")
        up_btn.configure(background="#006400")
        up_btn.configure(disabledforeground="#a3a3a3")
        up_btn.configure(font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        up_btn.configure(foreground="#ffffff")
        up_btn.configure(highlightbackground="#006400")
        up_btn.configure(pady="0")
        up_btn.configure(text='''UPDATE''')

        upempwindow.mainloop()
def updateitemgui():
    global itemid, itmname, price,sizes,size,itmid,itmupwindow
    foc = tree3.focus()
    values = tree3.item(foc, 'values')
    if len(values) == 0:
        messagebox.showerror("Error", "Select an item to update")
    else:
        itmupwindow = Tk()
        itmupwindow.geometry("410x460+519+200")
        itmupwindow.minsize(148, 1)
        itmupwindow.maxsize(1924, 1055)
        itmupwindow.resizable(1, 1)
        itmupwindow.title("California Pizza POS")
        itmupwindow.configure(background="#ffffff")
        itmupwindow.overrideredirect(True)

        Framex = tk.Frame(itmupwindow, bg="#006400")
        Framex.place(relx=-0.07, rely=0.0, relwidth=1.1, relheight=0.06)
        exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Aldhabi', 10, 'bold'),
                            command=itmupwindow.destroy)
        exitbtn.place(x=418, y=3.5)
        label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Aldhabi', 10, 'bold'), foreground="#ffffff",
                         bg="#006400")
        label.pack(pady=3)

        separator = ttk.Separator(itmupwindow, orient='horizontal')
        separator.place(relx=0.05, rely=0.2, relwidth=0.9)

        Labelx = tk.Label(itmupwindow)
        Labelx.place(relx=0.19, rely=0.079, height=46, width=253)
        Labelx.configure(background="#ffffff")
        Labelx.configure(
            font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
        Labelx.configure(foreground="#006400")
        Labelx.configure(text='''UPDATE ITEM ''')

        itmid = StringVar()
        itemid = tk.Entry(itmupwindow, textvariable=itmid, highlightbackground="#006400", highlightthickness=2)
        itemid.place(relx=0.13, rely=0.280, relheight=0.07, relwidth=0.67)

        itmidlable = tk.Label(itmupwindow)
        itmidlable.place(relx=0.151, rely=0.26)
        itmidlable.configure(background="#ffffff")
        itmidlable.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        itmidlable.configure(disabledforeground="#a3a3a3")
        itmidlable.configure(foreground="#006400")
        itmidlable.configure(text='''Item ID ''')

        itemname = StringVar()
        itmname = tk.Entry(itmupwindow, textvariable=itemname, highlightbackground="#006400", highlightthickness=2)
        itmname.place(relx=0.13, rely=0.404, relheight=0.07, relwidth=0.67)

        itmnamelabel = tk.Label(itmupwindow)
        itmnamelabel.place(relx=0.151, rely=0.371)
        itmnamelabel.configure(background="#ffffff")
        itmnamelabel.configure(
            font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        itmnamelabel.configure(disabledforeground="#a3a3a3")
        itmnamelabel.configure(foreground="#006400")
        itmnamelabel.configure(text='''Item Name ''')

        pp = StringVar()
        price = tk.Entry(itmupwindow, textvariable=pp, highlightbackground="#006400", highlightthickness=2)
        price.place(relx=0.13, rely=0.525, relheight=0.07, relwidth=0.67)

        pricelabel = tk.Label(itmupwindow)
        pricelabel.place(relx=0.150, rely=0.494)
        pricelabel.configure(background="#ffffff")
        pricelabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        pricelabel.configure(disabledforeground="#a3a3a3")
        pricelabel.configure(foreground="#006400")
        pricelabel.configure(text='''Price ''')

        sizes = StringVar()
        size = tk.Entry(itmupwindow, textvariable=sizes, highlightbackground="#006400", highlightthickness=2)
        size.place(relx=0.13, rely=0.647, relheight=0.075, relwidth=0.67)

        sizeslabel = tk.Label(itmupwindow)
        sizeslabel.place(relx=0.150, rely=0.622)
        sizeslabel.configure(background="#ffffff")
        sizeslabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        sizeslabel.configure(disabledforeground="#a3a3a3")
        sizeslabel.configure(foreground="#006400")
        sizeslabel.configure(text='''Size''')

        updateitems()
        iup_btn = tk.Button(itmupwindow, command=upitems)
        iup_btn.place(relx=0.36, rely=0.79, height=35, width=103)
        iup_btn.configure(activebackground="#006400")
        iup_btn.configure(activeforeground="#ffffff")
        iup_btn.configure(background="#006400")
        iup_btn.configure(disabledforeground="#a3a3a3")
        iup_btn.configure(font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        iup_btn.configure(foreground="#ffffff")
        iup_btn.configure(highlightbackground="#006400")
        iup_btn.configure(pady="0")
        iup_btn.configure(text='''UPDATE''')

        itmupwindow.mainloop()
def addempgui():
    global emloyeeid,empid,employeename,email,address,phn,comm,sal,hiredate,branch
    global empname,phone,commission,hire,empemail,empname,bid,empaddress,salary
    empwindow = Tk()
    empwindow.geometry("610x560+519+200")
    empwindow.minsize(148, 1)
    empwindow.maxsize(1924, 1055)
    empwindow.resizable(1, 1)
    empwindow.title("California Pizza POS")
    empwindow.configure(background="#ffffff")
    empwindow.overrideredirect(True)

    Framex = tk.Frame(empwindow, bg="#006400")
    Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.06)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Helvetica', 10, 'bold'),
                        command=empwindow.destroy)
    exitbtn.place(x=597, y=7)
    label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Aldhabi', 10, 'bold'), foreground="#ffffff",
                     bg="#006400")
    label.pack(pady=10)


    separator = ttk.Separator(empwindow, orient='horizontal')
    separator.place(relx=0.05, rely=0.2, relwidth=0.9)

    Labelx = tk.Label(empwindow)
    Labelx.place(relx=0.327, rely=0.117, height=46, width=253)
    Labelx.configure(background="#ffffff")
    Labelx.configure(
        font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Labelx.configure(disabledforeground="#a3a3a3")
    Labelx.configure(foreground="#006400")
    Labelx.configure(text='''ADD EMPLOYEE ''')

    cursor.execute("select max(emp_id) from employees")
    rr=cursor.fetchall()

    employeeid = StringVar()
    empid=tk.Entry(empwindow,textvariable=employeeid,highlightbackground="#006400",highlightthickness=2)
    empid.place(relx=0.03,rely=0.280,relheight=0.07,relwidth=0.37)
    empid.insert(0,int(rr[0][0])+1)
    empid.config(state="disabled")
    empid.config(disabledbackground="white")

    empidlable = tk.Label(empwindow)
    empidlable.place(relx=0.041, rely=0.26)
    empidlable.configure(background="#ffffff")
    empidlable.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    empidlable.configure(disabledforeground="#a3a3a3")
    empidlable.configure(foreground="#006400")
    empidlable.configure(text='''Emp ID ''')

    employeename = StringVar()
    empname = tk.Entry(empwindow, textvariable=employeename, highlightbackground="#006400", highlightthickness=2)
    empname.place(relx=0.03, rely=0.404, relheight=0.07, relwidth=0.37)

    enamelabel = tk.Label(empwindow)
    enamelabel.place(relx=0.041, rely=0.377)
    enamelabel.configure(background="#ffffff")
    enamelabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    enamelabel.configure(disabledforeground="#a3a3a3")
    enamelabel.configure(foreground="#006400")
    enamelabel.configure(text='''Ename ''')



    email=StringVar()
    empemail = tk.Entry(empwindow, textvariable=email,highlightbackground="#006400",highlightthickness=2)
    empemail.place(relx=0.03, rely=0.53, relheight=0.07, relwidth=0.37)

    emaillabel = tk.Label(empwindow)
    emaillabel.place(relx=0.041, rely=0.507)
    emaillabel.configure(background="#ffffff")
    emaillabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    emaillabel.configure(disabledforeground="#a3a3a3")
    emaillabel.configure(foreground="#006400")
    emaillabel.configure(text='''Email ''')

    address=StringVar()
    empaddress = tk.Entry(empwindow, textvariable=address,highlightbackground="#006400",highlightthickness=2)
    empaddress.place(relx=0.03, rely=0.67, relheight=0.07, relwidth=0.37)


    addresslabel = tk.Label(empwindow)
    addresslabel.place(relx=0.04, rely=0.641)
    addresslabel.configure(background="#ffffff")
    addresslabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    addresslabel.configure(disabledforeground="#a3a3a3")
    addresslabel.configure(foreground="#006400")
    addresslabel.configure(text='''Address ''')

    phn = StringVar()
    phone = tk.Entry(empwindow, textvariable=phn, highlightbackground="#006400", highlightthickness=2)
    phone.place(relx=0.03, rely=0.79, relheight=0.07, relwidth=0.37)

    phonelabel = tk.Label(empwindow)
    phonelabel.place(relx=0.046  , rely=0.767)
    phonelabel.configure(background="#ffffff")
    phonelabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    phonelabel.configure(disabledforeground="#a3a3a3")
    phonelabel.configure(foreground="#006400")
    phonelabel.configure(text='''Phone ''')

    sal = StringVar()
    salary = tk.Entry(empwindow, textvariable=sal,highlightbackground="#006400",highlightthickness=2)
    salary.place(relx=0.53, rely=0.28, relheight=0.07, relwidth=0.37)

    sallabel = tk.Label(empwindow)
    sallabel.place(relx=0.547, rely=0.262)
    sallabel.configure(background="#ffffff")
    sallabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    sallabel.configure(disabledforeground="#a3a3a3")
    sallabel.configure(foreground="#006400")
    sallabel.configure(text='''Salary ''')

    hiredate = StringVar()
    hire = tk.Entry(empwindow, textvariable=hiredate,highlightbackground="#006400",highlightthickness=2)
    hire.place(relx=0.53, rely=0.404, relheight=0.07, relwidth=0.37)


    hiredatelabel = tk.Label(empwindow)
    hiredatelabel.place(relx=0.538, rely=0.38)
    hiredatelabel.configure(background="#ffffff")
    hiredatelabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    hiredatelabel.configure(disabledforeground="#a3a3a3")
    hiredatelabel.configure(foreground="#006400")
    hiredatelabel.configure(text='''Hiredate ''')

    comm = StringVar()
    commission = tk.Entry(empwindow, textvariable=comm,highlightbackground="#006400",highlightthickness=2)
    commission.place(relx=0.53, rely=0.53, relheight=0.07, relwidth=0.37)

    commlabel = tk.Label(empwindow)
    commlabel.place(relx=0.539, rely=0.511)
    commlabel.configure(background="#ffffff")
    commlabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    commlabel.configure(disabledforeground="#a3a3a3")
    commlabel.configure(foreground="#006400")
    commlabel.configure(text='''Commission ''')

    branch = StringVar()
    bid = tk.Entry(empwindow, textvariable=branch,highlightbackground="#006400",highlightthickness=2)
    bid.place(relx=0.53, rely=0.67, relheight=0.07, relwidth=0.37)

    branchlabel = tk.Label(empwindow)
    branchlabel.place(relx=0.546, rely=0.642)
    branchlabel.configure(background="#ffffff")
    branchlabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    branchlabel.configure(disabledforeground="#a3a3a3")
    branchlabel.configure(foreground="#006400")
    branchlabel.configure(text='''Branch ID''')

    ADD_btn = tk.Button(empwindow, command=addemployees)
    ADD_btn.place(relx=0.63, rely=0.79, height=35, width=103)
    ADD_btn.configure(activebackground="#006400")
    ADD_btn.configure(activeforeground="#ffffff")
    ADD_btn.configure(background="#006400")
    ADD_btn.configure(disabledforeground="#a3a3a3")
    ADD_btn.configure(font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
    ADD_btn.configure(foreground="#ffffff")
    ADD_btn.configure(highlightbackground="#006400")
    ADD_btn.configure(pady="0")
    ADD_btn.configure(text='''ADD''')



    empwindow.mainloop()
def addemployees():
    global tree2, tree3, employeeid, empid, employeename, empname, hire, hiredate, bid,branch
    global comm, commission, sal, salary, branch, phn, phone, address, empaddress, email, empemail
    e_id= empid.get()
    e_name =empname.get()
    empem= empemail.get()
    addr = empaddress.get()
    phon= phone.get()
    ss= salary.get()
    hh= hire.get()
    com = commission.get()
    br = bid.get()
    cursor.execute("SELECT * FROM EMPLOYEES")
    allemprecords = cursor.fetchall()
    empids = []
    for record in allemprecords:
        empids.append(record[0])
    if len(e_name) > 30 or len(e_name) == 0:
        messagebox.showerror("error", "Invalid Name!")
    elif len(empem) > 30 or len(empem) == 0 or "@" not in empem:
        messagebox.showerror("error", "Invalid Email!")
    elif len(phon) > 11 or len(phon) < 11 or len(phon) == 0 or phon.isdecimal() == False or "03" != phon[0:2]:
        messagebox.showerror("error", "Invalid Number!")
    elif len(addr) > 50 or len(addr) == 0:
        messagebox.showerror("error", "Invalid Address Address !")
    elif len(ss) > 8 or len(ss) == 0 or ss.isdecimal() == False:
        messagebox.showerror("error", "Invalid Salary")
    else:
        for record in tree2.get_children():
            tree2.delete(record)
    sql="""INSERT INTO employees(emp_ID,ename,email,address,phone,salary,hiredate,comm,branch_ID) VALUES(:eid,:emname,:ee,:eaddr,:ph,:sss,:h,:comm,:bb)"""
    cursor.execute(sql,eid=int(e_id),emname=e_name,ee=empem,eaddr=addr,ph=int(phon),sss=int(ss),h=hh,comm=int(com),bb=int(br))
    connection.commit()
    messagebox.showinfo("Success","Successfully added employee")
    viewemp()
    upempwindow.destroy()


def adddealgui():
    global dealid,dealname,dtree,dealprice,dealwindow,itemsizecombo,itemnamescombo
    dealwindow = Tk()
    dealwindow.geometry("610x610+519+200")
    dealwindow.minsize(148, 1)
    dealwindow.maxsize(1924, 1055)
    dealwindow.resizable(1, 1)
    dealwindow.title("California Pizza POS")
    dealwindow.configure(background="#ffffff")
    dealwindow.overrideredirect(True)

    Framex = tk.Frame(dealwindow, bg="#006400")
    Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.06)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Aldhabi', 10, 'bold'),
                        command=dealwindow.destroy)
    exitbtn.place(x=597, y=3)
    label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Aldhabi', 10, 'bold'), foreground="#ffffff",
                     bg="#006400")
    label.pack(pady=7)


    separator = ttk.Separator(dealwindow, orient='horizontal')
    separator.place(relx=0.05, rely=0.2, relwidth=0.9)

    Labelx = tk.Label(dealwindow)
    Labelx.place(relx=0.43, rely=0.097)
    Labelx.configure(background="#ffffff")
    Labelx.configure(
        font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Labelx.configure(disabledforeground="#a3a3a3")
    Labelx.configure(foreground="#006400")
    Labelx.configure(text='''ADD DEALS ''')


    D_id = StringVar()
    dealid=tk.Entry(dealwindow,textvariable=D_id,highlightbackground="#006400",highlightthickness=2)
    dealid.place(relx=0.26,rely=0.260,relheight=0.07,relwidth=0.53)
    cursor.execute("""select max(deal_id) from deals""")
    dx=cursor.fetchall()
    dealid.insert(0,int(dx[0][0])+1)
    dealid.config(state="disabled")
    dealid.config(disabledbackground="white")

    dealidlable = tk.Label(dealwindow)
    dealidlable.place(relx=0.271, rely=0.240)
    dealidlable.configure(background="#ffffff")
    dealidlable.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    dealidlable.configure(disabledforeground="#a3a3a3")
    dealidlable.configure(foreground="#006400")
    dealidlable.configure(text='''Deal ID ''')

    d_name = StringVar()
    dealname = tk.Entry(dealwindow, textvariable=d_name, highlightbackground="#006400", highlightthickness=2)
    dealname.place(relx=0.26, rely=0.390, relheight=0.07, relwidth=0.53)

    deallabel = tk.Label(dealwindow)
    deallabel.place(relx=0.271, rely=0.368)
    deallabel.configure(background="#ffffff")
    deallabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    deallabel.configure(disabledforeground="#a3a3a3")
    deallabel.configure(foreground="#006400")
    deallabel.configure(text='''Deal Name ''')

    dprice=StringVar()
    dealprice = tk.Entry(dealwindow, textvariable=dprice,highlightbackground="#006400",highlightthickness=2)
    dealprice.place(relx=0.26, rely=0.526, relheight=0.07, relwidth=0.53)

    dealplabel = tk.Label(dealwindow)
    dealplabel.place(relx=0.271, rely=0.5)
    dealplabel.configure(background="#ffffff")
    dealplabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    dealplabel.configure(disabledforeground="#a3a3a3")
    dealplabel.configure(foreground="#006400")
    dealplabel.configure(text='''Unit Price''')

    dealilabel = tk.Label(dealwindow)
    dealilabel.place(relx=0.271, rely=0.613)
    dealilabel.configure(background="#ffffff")
    dealilabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    dealilabel.configure(disabledforeground="#a3a3a3")
    dealilabel.configure(foreground="#006400")
    dealilabel.configure(text='''Items''')

    namess=StringVar()
    itemnamescombo=ttk.Combobox(dealwindow,textvariable=namess)
    itemnamescombo.place(relx=0.269,rely=0.66)
    dealitem()
    itemnamescombo['values'] = itemlst
    itemnamescombo.bind("<<ComboboxSelected>>",inserttotree)

    dealslabel = tk.Label(dealwindow)
    dealslabel.place(relx=0.532, rely=0.613)
    dealslabel.configure(background="#ffffff")
    dealslabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    dealslabel.configure(disabledforeground="#a3a3a3")
    dealslabel.configure(foreground="#006400")
    dealslabel.configure(text='''Sizes''')

    style = ttk.Style(dealwindow)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#006400",
                    fieldbackground="#006400", foreground="white", font=('Aldhabi', 11, "bold"))
    style.map('Treeview', background=[("selected", "#006400")])

    dtree = ttk.Treeview(dealwindow, column=('S.no', 'Item Name', 'Size'), selectmode='extended')
    scrollbary = Scrollbar(dtree, orient=VERTICAL)
    scrollbarx = Scrollbar(dtree, orient=HORIZONTAL)
    dtree.config(xscrollcommand=scrollbarx.set)
    scrollbarx.config(command=dtree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    dtree.config(yscrollcommand=scrollbary.set)
    scrollbary.config(command=dtree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.pack(side=BOTTOM, fill=X)
    dtree.heading('S.no', text="S.no", anchor=CENTER)
    dtree.heading('Item Name', text="Item Name", anchor=CENTER)
    dtree.heading('Size', text="Size", anchor=CENTER)
    dtree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    dtree.column('#1', stretch=NO, minwidth=0, width=55, anchor=CENTER)
    dtree.column('#2', stretch=NO, minwidth=0, width=155, anchor=CENTER)
    dtree.column('#3', stretch=NO, minwidth=0, width=110, anchor=CENTER)
    dtree.place(relx=0.251, rely=0.743, relheight=0.17, relwidth=0.54)

    sizs = StringVar()
    itemsizecombo = ttk.Combobox(dealwindow, textvariable=sizs)
    itemsizecombo.place(relx=0.531, rely=0.66)
    dealisize()
    itemsizecombo['values'] = sizeilst
    itemsizecombo.bind("<<ComboboxSelected>>",inserttotree)

    removebtn = tk.Button(dealwindow,command=remitem)
    removebtn.place(relx=0.8,rely=0.87,height=20, width=20)
    removebtn.config(activebackground="#006400")
    removebtn.config(font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    removebtn.config(foreground="#ffffff")
    removebtn.configure(text='''-''')
    removebtn.configure(background="#006400")
    removebtn.configure(highlightbackground="#006400")

    ADD_btn = tk.Button(dealwindow, command=adddeals)
    ADD_btn.place(relx=0.428, rely=0.93, height=35, width=103)
    ADD_btn.configure(activebackground="#006400")
    ADD_btn.configure(activeforeground="#ffffff")
    ADD_btn.configure(background="#006400")
    ADD_btn.configure(disabledforeground="#a3a3a3")
    ADD_btn.configure(font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
    ADD_btn.configure(foreground="#ffffff")
    ADD_btn.configure(highlightbackground="#006400")
    ADD_btn.configure(pady="0")
    ADD_btn.configure(text='''ADD''')
    dealwindow.mainloop()
dtreecount = 1
def inserttotree(event):
    global  dtreecount,v
    if len(itemnamescombo.get())>0 and len(itemsizecombo.get()) > 0:
        dtree.insert(parent='', index='end', iid=dtreecount, text="", values=([dtreecount, itemnamescombo.get(),itemsizecombo.get()]))
        dtreecount = dtreecount + 1
        v.append([itemnamescombo.get(),itemsizecombo.get()])
        itemnamescombo.set('')
        itemsizecombo.set('')
def inserttotree2(event):
    global  dtreecount,uv,udcount
    dtreecount=udcount
    if len(upitemnamescombo.get())>0 and len(upitemsizecombo.get()) > 0:
        updtree.insert(parent='', index='end', iid=dtreecount, text="", values=([dtreecount+1, upitemnamescombo.get(),upitemsizecombo.get()]))
        udcount = udcount + 1
        uv.append([upitemnamescombo.get(),upitemsizecombo.get()])
        upitemnamescombo.set('')
        upitemsizecombo.set('')
def updealgui():
    global updealid,updealname,updtree,updealprice,updealwindow,upitemsizecombo,upitemnamescombo
    foc = tree4.focus()
    values = tree4.item(foc, 'values')
    if len(values) == 0:
        messagebox.showerror("Error", "Select a deal to update")
    else:
        updealwindow = Tk()
        updealwindow.geometry("610x610+519+200")
        updealwindow.minsize(148, 1)
        updealwindow.maxsize(1924, 1055)
        updealwindow.resizable(1, 1)
        updealwindow.title("California Pizza POS")
        updealwindow.configure(background="#ffffff")
        updealwindow.overrideredirect(True)

        Framex = tk.Frame(updealwindow, bg="#006400")
        Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.06)
        exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Aldhabi', 10, 'bold'),
                            command=updealwindow.destroy)
        exitbtn.place(x=597, y=3)
        label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Aldhabi', 10, 'bold'), foreground="#ffffff",
                         bg="#006400")
        label.pack(pady=7)


        separator = ttk.Separator(updealwindow, orient='horizontal')
        separator.place(relx=0.05, rely=0.2, relwidth=0.9)

        Labelx = tk.Label(updealwindow)
        Labelx.place(relx=0.38, rely=0.097)
        Labelx.configure(background="#ffffff")
        Labelx.configure(
            font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
        Labelx.configure(disabledforeground="#a3a3a3")
        Labelx.configure(foreground="#006400")
        Labelx.configure(text='''UPDATE DEALS ''')

        upD_id = StringVar()
        updealid=tk.Entry(updealwindow,textvariable=upD_id,highlightbackground="#006400",highlightthickness=2)
        updealid.place(relx=0.26,rely=0.260,relheight=0.07,relwidth=0.53)
        updealid.config(disabledbackground="white")

        updealidlable = tk.Label(updealwindow)
        updealidlable.place(relx=0.271, rely=0.240)
        updealidlable.configure(background="#ffffff")
        updealidlable.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        updealidlable.configure(disabledforeground="#a3a3a3")
        updealidlable.configure(foreground="#006400")
        updealidlable.configure(text='''Deal ID ''')

        upd_name = StringVar()
        updealname = tk.Entry(updealwindow, textvariable=upd_name, highlightbackground="#006400", highlightthickness=2)
        updealname.place(relx=0.26, rely=0.390, relheight=0.07, relwidth=0.53)

        updeallabel = tk.Label(updealwindow)
        updeallabel.place(relx=0.271, rely=0.368)
        updeallabel.configure(background="#ffffff")
        updeallabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        updeallabel.configure(disabledforeground="#a3a3a3")
        updeallabel.configure(foreground="#006400")
        updeallabel.configure(text='''Deal Name ''')

        updprice=StringVar()
        updealprice = tk.Entry(updealwindow, textvariable=updprice,highlightbackground="#006400",highlightthickness=2)
        updealprice.place(relx=0.26, rely=0.526, relheight=0.07, relwidth=0.53)

        updealplabel = tk.Label(updealwindow)
        updealplabel.place(relx=0.271, rely=0.5)
        updealplabel.configure(background="#ffffff")
        updealplabel.configure(
            font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        updealplabel.configure(disabledforeground="#a3a3a3")
        updealplabel.configure(foreground="#006400")
        updealplabel.configure(text='''Unit Price''')

        # updealilabel = tk.Label(updealwindow)
        # updealilabel.place(relx=0.271, rely=0.613)
        # updealilabel.configure(background="#ffffff")
        # updealilabel.configure(
        #     font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        # updealilabel.configure(disabledforeground="#a3a3a3")
        # updealilabel.configure(foreground="#006400")
        # updealilabel.configure(text='''Items''')

        # upnamess=StringVar()
        # upitemnamescombo=ttk.Combobox(updealwindow,textvariable=upnamess)
        # upitemnamescombo.place(relx=0.269,rely=0.66)
        # dealitem()
        # upitemnamescombo['values'] = itemlst
        # upitemnamescombo.bind("<<ComboboxSelected>>",inserttotree2)

        # updealslabel = tk.Label(updealwindow)
        # updealslabel.place(relx=0.532, rely=0.613)
        # updealslabel.configure(background="#ffffff")
        # updealslabel.configure(
        #     font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        # updealslabel.configure(disabledforeground="#a3a3a3")
        # updealslabel.configure(foreground="#006400")
        # updealslabel.configure(text='''Sizes''')

        style = ttk.Style(updealwindow)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#006400",
                        fieldbackground="#006400", foreground="white", font=('Aldhabi', 11, "bold"))
        style.map('Treeview', background=[("selected", "#006400")])

        updtree = ttk.Treeview(updealwindow, column=('S.no', 'Item Name', 'Size'), selectmode='extended')
        scrollbary = Scrollbar(updtree, orient=VERTICAL)
        scrollbarx = Scrollbar(updtree, orient=HORIZONTAL)
        updtree.config(xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=updtree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        updtree.config(yscrollcommand=scrollbary.set)
        scrollbary.config(command=updtree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.pack(side=BOTTOM, fill=X)
        updtree.heading('S.no', text="S.no", anchor=CENTER)
        updtree.heading('Item Name', text="Item Name", anchor=CENTER)
        updtree.heading('Size', text="Size", anchor=CENTER)
        updtree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
        updtree.column('#1', stretch=NO, minwidth=0, width=55, anchor=CENTER)
        updtree.column('#2', stretch=NO, minwidth=0, width=155, anchor=CENTER)
        updtree.column('#3', stretch=NO, minwidth=0, width=110, anchor=CENTER)
        updtree.place(relx=0.251, rely=0.735, relheight=0.17, relwidth=0.54)


        updd()

        up_btn = tk.Button(updealwindow, command=updeals)
        up_btn.place(relx=0.428, rely=0.93, height=35, width=103)
        up_btn.configure(activebackground="#006400")
        up_btn.configure(activeforeground="#ffffff")
        up_btn.configure(background="#006400")
        up_btn.configure(disabledforeground="#a3a3a3")
        up_btn.configure(font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        up_btn.configure(foreground="#ffffff")
        up_btn.configure(highlightbackground="#006400")
        up_btn.configure(pady="0")
        up_btn.configure(text='''UPDATE''')

        updealwindow.mainloop()
def remitem():
    if len(dtree.selection()) ==0:
        messagebox.showerror("Error","No item selected")
        dealwindow.attributes("-topmost",True)
    else:
        x=dtree.selection()[0]
        dtree.delete(x)
def upremitem():
    global udcount
    if len(updtree.selection()) ==0:
        messagebox.showerror("Error","No item selected")
        dealwindow.attributes("-topmost",True)
    else:
        c = updtree.focus()
        h = updtree.item(c, 'values')
        uv.remove([h[1], h[2]])
        x=updtree.selection()[0]
        k = updtree.selection()[0][0]
        updtree.delete(x)
        udcount = int(k)

def additemgui():
    global itemid,itemname,unitprice,catid,itemsizescombo,itemwindow
    itemwindow = Tk()
    itemwindow.geometry("610x560+519+200")
    itemwindow.minsize(148, 1)
    itemwindow.maxsize(1924, 1055)
    itemwindow.resizable(1, 1)
    itemwindow.title("California Pizza POS")
    itemwindow.configure(background="#ffffff")
    itemwindow.overrideredirect(True)

    Framex = tk.Frame(itemwindow, bg="#006400")
    Framex.place(relx=-0.017, rely=0.0, relwidth=1.1, relheight=0.06)
    exitbtn = tk.Button(Framex, text="X", bg="#006400", foreground="white", font=('Aldhabi', 10, 'bold'),
                        command=itemwindow.destroy)
    exitbtn.place(x=597, y=7)
    label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Aldhabi', 10, 'bold'), foreground="#ffffff",
                     bg="#006400")
    label.pack(pady=10)


    separator = ttk.Separator(itemwindow, orient='horizontal')
    separator.place(relx=0.05, rely=0.2, relwidth=0.9)

    Labelx = tk.Label(itemwindow)
    Labelx.place(relx=0.3, rely=0.117, height=46, width=253)
    Labelx.configure(background="#ffffff")
    Labelx.configure(
        font="-family {Aldhabi} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Labelx.configure(disabledforeground="#a3a3a3")
    Labelx.configure(foreground="#006400")
    Labelx.configure(text='''ADD ITEMS ''')

    item_name = StringVar()
    itemname = tk.Entry(itemwindow, textvariable=item_name, highlightbackground="#006400", highlightthickness=2)
    itemname.place(relx=0.26, rely=0.320, relheight=0.07, relwidth=0.45)

    itemlabel = tk.Label(itemwindow)
    itemlabel.place(relx=0.271, rely=0.300)
    itemlabel.configure(background="#ffffff")
    itemlabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    itemlabel.configure(disabledforeground="#a3a3a3")
    itemlabel.configure(foreground="#006400")
    itemlabel.configure(text='''Item Name ''')

    uprice=StringVar()
    unitprice = tk.Entry(itemwindow, textvariable=uprice,highlightbackground="#006400",highlightthickness=2)
    unitprice.place(relx=0.26, rely=0.435, relheight=0.07, relwidth=0.45)

    upricelabel = tk.Label(itemwindow)
    upricelabel.place(relx=0.271, rely=0.42)
    upricelabel.configure(background="#ffffff")
    upricelabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    upricelabel.configure(disabledforeground="#a3a3a3")
    upricelabel.configure(foreground="#006400")
    upricelabel.configure(text='''Unit Price''')

    cid=StringVar()
    catid = tk.Entry(itemwindow, textvariable=cid,highlightbackground="#006400",highlightthickness=2)
    catid.place(relx=0.26, rely=0.57, relheight=0.07, relwidth=0.45)

    catidlabel = tk.Label(itemwindow)
    catidlabel.place(relx=0.271, rely=0.55)
    catidlabel.configure(background="#ffffff")
    catidlabel.configure(
        font="-family {Aldhabi} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    catidlabel.configure(disabledforeground="#a3a3a3")
    catidlabel.configure(foreground="#006400")
    catidlabel.configure(text='''Category ID ''')

    sxt=StringVar()
    itemsizescombo = ttk.Combobox(itemwindow,textvariable=sxt)
    itemsizescombo.place(relx=0.346, rely=0.68)
    cursor.execute("""Select size_name from sizes """)
    sss = cursor.fetchall()
    slst=[]
    for i in sss:
        slst.append((i[0]))
    itemsizescombo['values'] = slst
    itemsizescombo.bind("<<ComboboxSelected>>")



    ADD_btn = tk.Button(itemwindow, command=additems)
    ADD_btn.place(relx=0.4, rely=0.8, height=35, width=103)
    ADD_btn.configure(activebackground="#006400")
    ADD_btn.configure(activeforeground="#ffffff")
    ADD_btn.configure(background="#006400")
    ADD_btn.configure(disabledforeground="#a3a3a3")
    ADD_btn.configure(font="-family {Aldhabi} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
    ADD_btn.configure(foreground="#ffffff")
    ADD_btn.configure(highlightbackground="#006400")
    ADD_btn.configure(pady="0")
    ADD_btn.configure(text='''ADD''')



