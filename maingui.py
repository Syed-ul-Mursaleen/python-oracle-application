from tkinter import *
import tkinter as tk
import cx_Oracle
import CONN
from tkinter import messagebox


def maingui():
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
    label = tk.Label(Framex, text="CALIFORNIA PIZZA POS", font=('Helvetica', 11, 'bold'), foreground="#ffffff",
                     bg="#006400")
    label.pack(pady=13)

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
    Label1.place(relx=0.022, rely=0.045, height=36, width=138)
    Label1.configure(background="#ffffff")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font=18)
    Label1.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(foreground="#b90746")
    Label1.configure(text='''PIZZA''')

    L0 = tk.Label(Frame2)
    L0.place(relx=0.135, rely=0.045)
    L0.configure(background="#ffffff")
    L0.configure(disabledforeground="#a3a3a3")
    L0.configure(font=18)
    L0.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L0.configure(foreground="#b90746")
    L0.configure(text='''Q''')

    L1 = tk.Label(Frame2)
    L1.place(relx=0.172, rely=0.045)
    L1.configure(background="#ffffff")
    L1.configure(disabledforeground="#a3a3a3")
    L1.configure(font=18)
    L1.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L1.configure(foreground="#b90746")
    L1.configure(text='''L''')

    L2 = tk.Label(Frame2)
    L2.place(relx=0.202, rely=0.045)
    L2.configure(background="#ffffff")
    L2.configure(disabledforeground="#a3a3a3")
    L2.configure(font=18)
    L2.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L2.configure(foreground="#b90746")
    L2.configure(text='''M''')

    L3 = tk.Label(Frame2)
    L3.place(relx=0.234, rely=0.045)
    L3.configure(background="#ffffff")
    L3.configure(disabledforeground="#a3a3a3")
    L3.configure(font=18)
    L3.configure(font="-family {Copperplate Gothic Bold} -size 18 -weight bold -slant roman -underline 0 -overstrike 0")
    L3.configure(foreground="#b90746")
    L3.configure(text='''S''')

    PLabel1 = tk.Label(Frame2)
    PLabel1.place(relx=0.01, rely=0.116)
    PLabel1.configure(activebackground="#f9f9f9")
    PLabel1.configure(activeforeground="black")
    PLabel1.configure(background="#ffffff")
    PLabel1.configure(disabledforeground="#a3a3a3")
    PLabel1.configure(
        font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel1.configure(foreground="#008000")
    PLabel1.configure(highlightbackground="#d9d9d9")
    PLabel1.configure(highlightcolor="black")
    PLabel1.configure(text='''SUPER SUPREME''')

    Pizza1 = tk.Spinbox(Frame2,from_=0,to=30,textvariable="p1",wrap=True)
    Pizza1.place(relx=0.133, rely=0.116, height=24, relwidth=0.021)
    Pizza1.configure(background="white")
    Pizza1.configure(disabledforeground="#a3a3a3")
    Pizza1.configure(font="TkFixedFont")
    Pizza1.configure(foreground="#000000")
    Pizza1.configure(insertbackground="black")

    Sizep11 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp11", wrap=True)
    Sizep11.place(relx=0.170, rely=0.116,height=24, relwidth=0.021)
    Sizep11.configure(background="white")
    Sizep11.configure(disabledforeground="#a3a3a3")
    Sizep11.configure(font="TkFixedFont")
    Sizep11.configure(foreground="#000000")
    Sizep11.configure(insertbackground="black")

    Sizep12 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp12", wrap=True)
    Sizep12.place(relx=0.200, rely=0.116, height=24, relwidth=0.021)
    Sizep12.configure(background="white")
    Sizep12.configure(disabledforeground="#a3a3a3")
    Sizep12.configure(font="TkFixedFont")
    Sizep12.configure(foreground="#000000")
    Sizep12.configure(insertbackground="black")

    Sizep13 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp13", wrap=True)
    Sizep13.place(relx=0.230, rely=0.116, height=24, relwidth=0.021)
    Sizep13.configure(background="white")
    Sizep13.configure(disabledforeground="#a3a3a3")
    Sizep13.configure(font="TkFixedFont")
    Sizep13.configure(foreground="#000000")
    Sizep13.configure(insertbackground="black")

    PLabel2 = tk.Label(Frame2)
    PLabel2.place(relx=0.01, rely=0.179)
    PLabel2.configure(activebackground="#f9f9f9")
    PLabel2.configure(activeforeground="black")
    PLabel2.configure(background="#ffffff")
    PLabel2.configure(disabledforeground="#a3a3a3")
    PLabel2.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel2.configure(foreground="#008000")
    PLabel2.configure(highlightbackground="#d9d9d9")
    PLabel2.configure(highlightcolor="black")
    PLabel2.configure(text='''RANCH PIZZA''')

    Pizza2 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p2", wrap=True)
    Pizza2.place(relx=0.133, rely=0.177, height=24, relwidth=0.021)
    Pizza2.configure(background="white")
    Pizza2.configure(disabledforeground="#a3a3a3")
    Pizza2.configure(font="TkFixedFont")
    Pizza2.configure(foreground="#000000")
    Pizza2.configure(insertbackground="black")

    Sizep21 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp21", wrap=True)
    Sizep21.place(relx=0.170, rely=0.177, height=24, relwidth=0.021)
    Sizep21.configure(background="white")
    Sizep21.configure(disabledforeground="#a3a3a3")
    Sizep21.configure(font="TkFixedFont")
    Sizep21.configure(foreground="#000000")
    Sizep21.configure(insertbackground="black")

    Sizep22 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp22", wrap=True)
    Sizep22.place(relx=0.200, rely=0.177, height=24, relwidth=0.021)
    Sizep22.configure(background="white")
    Sizep22.configure(disabledforeground="#a3a3a3")
    Sizep22.configure(font="TkFixedFont")
    Sizep22.configure(foreground="#000000")
    Sizep22.configure(insertbackground="black")

    Sizep23 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp23", wrap=True)
    Sizep23.place(relx=0.230, rely=0.177, height=24, relwidth=0.021)
    Sizep23.configure(background="white")
    Sizep23.configure(disabledforeground="#a3a3a3")
    Sizep23.configure(font="TkFixedFont")
    Sizep23.configure(foreground="#000000")
    Sizep23.configure(insertbackground="black")

    PLabel3 = tk.Label(Frame2)
    PLabel3.place(relx=0.01, rely=0.242)
    PLabel3.configure(activebackground="#f9f9f9")
    PLabel3.configure(activeforeground="black")
    PLabel3.configure(background="#ffffff")
    PLabel3.configure(disabledforeground="#a3a3a3")
    PLabel3.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel3.configure(foreground="#008000")
    PLabel3.configure(highlightbackground="#d9d9d9")
    PLabel3.configure(highlightcolor="black")
    PLabel3.configure(text='''CREAMY TIKKA''')

    Pizza3 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p3", wrap=True)
    Pizza3.place(relx=0.133, rely=0.242,height=24, relwidth=0.021)
    Pizza3.configure(background="white")
    Pizza3.configure(disabledforeground="#a3a3a3")
    Pizza3.configure(font="TkFixedFont")
    Pizza3.configure(foreground="#000000")
    Pizza3.configure(insertbackground="black")

    Sizep31 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp31", wrap=True)
    Sizep31.place(relx=0.170, rely=0.242, height=24, relwidth=0.021)
    Sizep31.configure(background="white")
    Sizep31.configure(disabledforeground="#a3a3a3")
    Sizep31.configure(font="TkFixedFont")
    Sizep31.configure(foreground="#000000")
    Sizep31.configure(insertbackground="black")

    Sizep32 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp32", wrap=True)
    Sizep32.place(relx=0.200, rely=0.242, height=24, relwidth=0.021)
    Sizep32.configure(background="white")
    Sizep32.configure(disabledforeground="#a3a3a3")
    Sizep32.configure(font="TkFixedFont")
    Sizep32.configure(foreground="#000000")
    Sizep32.configure(insertbackground="black")

    Sizep33 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp33", wrap=True)
    Sizep33.place(relx=0.230, rely=0.242, height=24, relwidth=0.021)
    Sizep33.configure(background="white")
    Sizep33.configure(disabledforeground="#a3a3a3")
    Sizep33.configure(font="TkFixedFont")
    Sizep33.configure(foreground="#000000")
    Sizep33.configure(insertbackground="black")

    PLabel4 = tk.Label(Frame2)
    PLabel4.place(relx=0.01, rely=0.307)
    PLabel4.configure(activebackground="#f9f9f9")
    PLabel4.configure(activeforeground="black")
    PLabel4.configure(background="#ffffff")
    PLabel4.configure(disabledforeground="#a3a3a3")
    PLabel4.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel4.configure(foreground="#008000")
    PLabel4.configure(highlightbackground="#d9d9d9")
    PLabel4.configure(highlightcolor="black")
    PLabel4.configure(text='''DANCING FAJITA''')

    Pizza4 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p4", wrap=True)
    Pizza4.place(relx=0.133, rely=0.307, height=24, relwidth=0.021)
    Pizza4.configure(background="white")
    Pizza4.configure(disabledforeground="#a3a3a3")
    Pizza4.configure(font="TkFixedFont")
    Pizza4.configure(foreground="#000000")
    Pizza4.configure(insertbackground="black")

    Sizep41 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp41", wrap=True)
    Sizep41.place(relx=0.170, rely=0.307, height=24, relwidth=0.021)
    Sizep41.configure(background="white")
    Sizep41.configure(disabledforeground="#a3a3a3")
    Sizep41.configure(font="TkFixedFont")
    Sizep41.configure(foreground="#000000")
    Sizep41.configure(insertbackground="black")

    Sizep42 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp42", wrap=True)
    Sizep42.place(relx=0.200, rely=0.307, height=24, relwidth=0.021)
    Sizep42.configure(background="white")
    Sizep42.configure(disabledforeground="#a3a3a3")
    Sizep42.configure(font="TkFixedFont")
    Sizep42.configure(foreground="#000000")
    Sizep42.configure(insertbackground="black")

    Sizep43 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp43", wrap=True)
    Sizep43.place(relx=0.230, rely=0.307, height=24, relwidth=0.021)
    Sizep43.configure(background="white")
    Sizep43.configure(disabledforeground="#a3a3a3")
    Sizep43.configure(font="TkFixedFont")
    Sizep43.configure(foreground="#000000")
    Sizep43.configure(insertbackground="black")

    PLabel5 = tk.Label(Frame2)
    PLabel5.place(relx=0.01, rely=0.372)
    PLabel5.configure(activebackground="#f9f9f9")
    PLabel5.configure(activeforeground="black")
    PLabel5.configure(background="#ffffff")
    PLabel5.configure(disabledforeground="#a3a3a3")
    PLabel5.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel5.configure(foreground="#008000")
    PLabel5.configure(highlightbackground="#d9d9d9")
    PLabel5.configure(highlightcolor="black")
    PLabel5.configure(text='''CHEESE LOVER''')

    Pizza5 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p5", wrap=True)
    Pizza5.place(relx=0.133, rely=0.372, height=24, relwidth=0.021)
    Pizza5.configure(background="white")
    Pizza5.configure(disabledforeground="#a3a3a3")
    Pizza5.configure(font="TkFixedFont")
    Pizza5.configure(foreground="#000000")
    Pizza5.configure(insertbackground="black")

    Sizep51 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp51", wrap=True)
    Sizep51.place(relx=0.170, rely=0.372, height=24, relwidth=0.021)
    Sizep51.configure(background="white")
    Sizep51.configure(disabledforeground="#a3a3a3")
    Sizep51.configure(font="TkFixedFont")
    Sizep51.configure(foreground="#000000")
    Sizep51.configure(insertbackground="black")

    Sizep52 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp52", wrap=True)
    Sizep52.place(relx=0.200, rely=0.372, height=24, relwidth=0.021)
    Sizep52.configure(background="white")
    Sizep52.configure(disabledforeground="#a3a3a3")
    Sizep52.configure(font="TkFixedFont")
    Sizep52.configure(foreground="#000000")
    Sizep52.configure(insertbackground="black")

    Sizep53 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp53", wrap=True)
    Sizep53.place(relx=0.230, rely=0.372, height=24, relwidth=0.021)
    Sizep53.configure(background="white")
    Sizep53.configure(disabledforeground="#a3a3a3")
    Sizep53.configure(font="TkFixedFont")
    Sizep53.configure(foreground="#000000")
    Sizep53.configure(insertbackground="black")

    PLabel6 = tk.Label(Frame2)
    PLabel6.place(relx=0.01, rely=0.437)
    PLabel6.configure(activebackground="#f9f9f9")
    PLabel6.configure(activeforeground="black")
    PLabel6.configure(background="#ffffff")
    PLabel6.configure(disabledforeground="#a3a3a3")
    PLabel6.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel6.configure(foreground="#008000")
    PLabel6.configure(highlightbackground="#d9d9d9")
    PLabel6.configure(highlightcolor="black")
    PLabel6.configure(text='''VEGGIE LOVER''')

    Pizza6 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p6", wrap=True)
    Pizza6.place(relx=0.133, rely=0.437, height=24, relwidth=0.021)
    Pizza6.configure(background="white")
    Pizza6.configure(disabledforeground="#a3a3a3")
    Pizza6.configure(font="TkFixedFont")
    Pizza6.configure(foreground="#000000")
    Pizza6.configure(insertbackground="black")

    Sizep61 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp61", wrap=True)
    Sizep61.place(relx=0.170, rely=0.437, height=24, relwidth=0.021)
    Sizep61.configure(background="white")
    Sizep61.configure(disabledforeground="#a3a3a3")
    Sizep61.configure(font="TkFixedFont")
    Sizep61.configure(foreground="#000000")
    Sizep61.configure(insertbackground="black")

    Sizep62 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp62", wrap=True)
    Sizep62.place(relx=0.200, rely=0.437, height=24, relwidth=0.021)
    Sizep62.configure(background="white")
    Sizep62.configure(disabledforeground="#a3a3a3")
    Sizep62.configure(font="TkFixedFont")
    Sizep62.configure(foreground="#000000")
    Sizep62.configure(insertbackground="black")

    Sizep63 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp63", wrap=True)
    Sizep63.place(relx=0.230, rely=0.437, height=24, relwidth=0.021)
    Sizep63.configure(background="white")
    Sizep63.configure(disabledforeground="#a3a3a3")
    Sizep63.configure(font="TkFixedFont")
    Sizep63.configure(foreground="#000000")
    Sizep63.configure(insertbackground="black")

    PLabel7 = tk.Label(Frame2)
    PLabel7.place(relx=0.01, rely=0.502)
    PLabel7.configure(activebackground="#f9f9f9")
    PLabel7.configure(activeforeground="black")
    PLabel7.configure(background="#ffffff")
    PLabel7.configure(disabledforeground="#a3a3a3")
    PLabel7.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel7.configure(foreground="#008000")
    PLabel7.configure(highlightbackground="#d9d9d9")
    PLabel7.configure(highlightcolor="black")
    PLabel7.configure(text='''FAJTA SICILIAN''')

    Pizza7 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p7", wrap=True)
    Pizza7.place(relx=0.133, rely=0.502, height=24, relwidth=0.021)
    Pizza7.configure(background="white")
    Pizza7.configure(disabledforeground="#a3a3a3")
    Pizza7.configure(font="TkFixedFont")
    Pizza7.configure(foreground="#000000")
    Pizza7.configure(insertbackground="black")

    Sizep71 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp71", wrap=True)
    Sizep71.place(relx=0.170, rely=0.502, height=24, relwidth=0.021)
    Sizep71.configure(background="white")
    Sizep71.configure(disabledforeground="#a3a3a3")
    Sizep71.configure(font="TkFixedFont")
    Sizep71.configure(foreground="#000000")
    Sizep71.configure(insertbackground="black")

    Sizep72 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp72", wrap=True)
    Sizep72.place(relx=0.200, rely=0.502, height=24, relwidth=0.021)
    Sizep72.configure(background="white")
    Sizep72.configure(disabledforeground="#a3a3a3")
    Sizep72.configure(font="TkFixedFont")
    Sizep72.configure(foreground="#000000")
    Sizep72.configure(insertbackground="black")

    Sizep73 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp73", wrap=True)
    Sizep73.place(relx=0.230, rely=0.502, height=24, relwidth=0.021)
    Sizep73.configure(background="white")
    Sizep73.configure(disabledforeground="#a3a3a3")
    Sizep73.configure(font="TkFixedFont")
    Sizep73.configure(foreground="#000000")
    Sizep73.configure(insertbackground="black")

    PLabel8 = tk.Label(Frame2)
    PLabel8.place(relx=0.01, rely=0.567)
    PLabel8.configure(activebackground="#f9f9f9")
    PLabel8.configure(activeforeground="black")
    PLabel8.configure(background="#ffffff")
    PLabel8.configure(disabledforeground="#a3a3a3")
    PLabel8.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel8.configure(foreground="#008000")
    PLabel8.configure(highlightbackground="#d9d9d9")
    PLabel8.configure(highlightcolor="black")
    PLabel8.configure(text='''MEXICAN TREAT''')

    Pizza8 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p8", wrap=True)
    Pizza8.place(relx=0.133, rely=0.567, height=24, relwidth=0.021)
    Pizza8.configure(background="white")
    Pizza8.configure(disabledforeground="#a3a3a3")
    Pizza8.configure(font="TkFixedFont")
    Pizza8.configure(foreground="#000000")
    Pizza8.configure(insertbackground="black")

    Sizep81 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp81", wrap=True)
    Sizep81.place(relx=0.170, rely=0.567, height=24, relwidth=0.021)
    Sizep81.configure(background="white")
    Sizep81.configure(disabledforeground="#a3a3a3")
    Sizep81.configure(font="TkFixedFont")
    Sizep81.configure(foreground="#000000")
    Sizep81.configure(insertbackground="black")

    Sizep82 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp82", wrap=True)
    Sizep82.place(relx=0.200, rely=0.567, height=24, relwidth=0.021)
    Sizep82.configure(background="white")
    Sizep82.configure(disabledforeground="#a3a3a3")
    Sizep82.configure(font="TkFixedFont")
    Sizep82.configure(foreground="#000000")
    Sizep82.configure(insertbackground="black")

    Sizep83 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp83", wrap=True)
    Sizep83.place(relx=0.230, rely=0.567, height=24, relwidth=0.021)
    Sizep83.configure(background="white")
    Sizep83.configure(disabledforeground="#a3a3a3")
    Sizep83.configure(font="TkFixedFont")
    Sizep83.configure(foreground="#000000")
    Sizep83.configure(insertbackground="black")

    PLabel9 = tk.Label(Frame2)
    PLabel9.place(relx=0.01, rely=0.632)
    PLabel9.configure(activebackground="#f9f9f9")
    PLabel9.configure(activeforeground="black")
    PLabel9.configure(background="#ffffff")
    PLabel9.configure(disabledforeground="#a3a3a3")
    PLabel9.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel9.configure(foreground="#008000")
    PLabel9.configure(highlightbackground="#d9d9d9")
    PLabel9.configure(highlightcolor="black")
    PLabel9.configure(text='''MIAMI BEAST''')

    Pizza9 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p9", wrap=True)
    Pizza9.place(relx=0.133, rely=0.632, height=24, relwidth=0.021)
    Pizza9.configure(background="white")
    Pizza9.configure(disabledforeground="#a3a3a3")
    Pizza9.configure(font="TkFixedFont")
    Pizza9.configure(foreground="#000000")
    Pizza9.configure(insertbackground="black")

    Sizep91 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp91", wrap=True)
    Sizep91.place(relx=0.170, rely=0.632, height=24, relwidth=0.021)
    Sizep91.configure(background="white")
    Sizep91.configure(disabledforeground="#a3a3a3")
    Sizep91.configure(font="TkFixedFont")
    Sizep91.configure(foreground="#000000")
    Sizep91.configure(insertbackground="black")

    Sizep92 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp92", wrap=True)
    Sizep92.place(relx=0.200, rely=0.632, height=24, relwidth=0.021)
    Sizep92.configure(background="white")
    Sizep92.configure(disabledforeground="#a3a3a3")
    Sizep92.configure(font="TkFixedFont")
    Sizep92.configure(foreground="#000000")
    Sizep92.configure(insertbackground="black")

    Sizep93 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp93", wrap=True)
    Sizep93.place(relx=0.230, rely=0.632, height=24, relwidth=0.021)
    Sizep93.configure(background="white")
    Sizep93.configure(disabledforeground="#a3a3a3")
    Sizep93.configure(font="TkFixedFont")
    Sizep93.configure(foreground="#000000")
    Sizep93.configure(insertbackground="black")

    PLabel10 = tk.Label(Frame2)
    PLabel10.place(relx=0.01, rely=0.697)
    PLabel10.configure(activebackground="#f9f9f9")
    PLabel10.configure(activeforeground="black")
    PLabel10.configure(background="#ffffff")
    PLabel10.configure(disabledforeground="#a3a3a3")
    PLabel10.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel10.configure(foreground="#008000")
    PLabel10.configure(highlightbackground="#d9d9d9")
    PLabel10.configure(highlightcolor="black")
    PLabel10.configure(text='''BEEF SUPREME''')

    Pizza10 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p10", wrap=True)
    Pizza10.place(relx=0.133, rely=0.697, height=24, relwidth=0.021)
    Pizza10.configure(background="white")
    Pizza10.configure(disabledforeground="#a3a3a3")
    Pizza10.configure(font="TkFixedFont")
    Pizza10.configure(foreground="#000000")
    Pizza10.configure(insertbackground="black")

    Sizep101 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp101", wrap=True)
    Sizep101.place(relx=0.170, rely=0.697, height=24, relwidth=0.021)
    Sizep101.configure(background="white")
    Sizep101.configure(disabledforeground="#a3a3a3")
    Sizep101.configure(font="TkFixedFont")
    Sizep101.configure(foreground="#000000")
    Sizep101.configure(insertbackground="black")

    Sizep102 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp102", wrap=True)
    Sizep102.place(relx=0.200, rely=0.697, height=24, relwidth=0.021)
    Sizep102.configure(background="white")
    Sizep102.configure(disabledforeground="#a3a3a3")
    Sizep102.configure(font="TkFixedFont")
    Sizep102.configure(foreground="#000000")
    Sizep102.configure(insertbackground="black")

    Sizep103 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp103", wrap=True)
    Sizep103.place(relx=0.230, rely=0.697, height=24, relwidth=0.021)
    Sizep103.configure(background="white")
    Sizep103.configure(disabledforeground="#a3a3a3")
    Sizep103.configure(font="TkFixedFont")
    Sizep103.configure(foreground="#000000")
    Sizep103.configure(insertbackground="black")

    PLabel11 = tk.Label(Frame2)
    PLabel11.place(relx=0.01, rely=0.762)
    PLabel11.configure(activebackground="#f9f9f9")
    PLabel11.configure(activeforeground="black")
    PLabel11.configure(background="#ffffff")
    PLabel11.configure(disabledforeground="#a3a3a3")
    PLabel11.configure(
        font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel11.configure(foreground="#008000")
    PLabel11.configure(highlightbackground="#d9d9d9")
    PLabel11.configure(highlightcolor="black")
    PLabel11.configure(text='''CHIPOTLE PIZZA''')

    Pizza11 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p11", wrap=True)
    Pizza11.place(relx=0.133, rely=0.762, height=24, relwidth=0.021)
    Pizza11.configure(background="white")
    Pizza11.configure(disabledforeground="#a3a3a3")
    Pizza11.configure(font="TkFixedFont")
    Pizza11.configure(foreground="#000000")
    Pizza11.configure(insertbackground="black")

    Sizep111 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp111", wrap=True)
    Sizep111.place(relx=0.170, rely=0.762, height=24, relwidth=0.021)
    Sizep111.configure(background="white")
    Sizep111.configure(disabledforeground="#a3a3a3")
    Sizep111.configure(font="TkFixedFont")
    Sizep111.configure(foreground="#000000")
    Sizep111.configure(insertbackground="black")

    Sizep112 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp112", wrap=True)
    Sizep112.place(relx=0.200, rely=0.762, height=24, relwidth=0.021)
    Sizep112.configure(background="white")
    Sizep112.configure(disabledforeground="#a3a3a3")
    Sizep112.configure(font="TkFixedFont")
    Sizep112.configure(foreground="#000000")
    Sizep112.configure(insertbackground="black")

    Sizep113 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp113", wrap=True)
    Sizep113.place(relx=0.230, rely=0.762, height=24, relwidth=0.021)
    Sizep113.configure(background="white")
    Sizep113.configure(disabledforeground="#a3a3a3")
    Sizep113.configure(font="TkFixedFont")
    Sizep113.configure(foreground="#000000")
    Sizep113.configure(insertbackground="black")

    PLabel12 = tk.Label(Frame2)
    PLabel12.place(relx=0.01, rely=0.827)
    PLabel12.configure(activebackground="#f9f9f9")
    PLabel12.configure(activeforeground="black")
    PLabel12.configure(background="#ffffff")
    PLabel12.configure(disabledforeground="#a3a3a3")
    PLabel12.configure(font="-family {Copperplate Gothic Light} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    PLabel12.configure(foreground="#008000")
    PLabel12.configure(highlightbackground="#d9d9d9")
    PLabel12.configure(highlightcolor="black")
    PLabel12.configure(text='''CHICAGO BOLD''')

    Pizza12 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="p12", wrap=True)
    Pizza12.place(relx=0.133, rely=0.827, height=24, relwidth=0.021)
    Pizza12.configure(background="white")
    Pizza12.configure(disabledforeground="#a3a3a3")
    Pizza12.configure(font="TkFixedFont")
    Pizza12.configure(foreground="#000000")
    Pizza12.configure(insertbackground="black")

    Sizep121 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp121", wrap=True)
    Sizep121.place(relx=0.170, rely=0.827, height=24, relwidth=0.021)
    Sizep121.configure(background="white")
    Sizep121.configure(disabledforeground="#a3a3a3")
    Sizep121.configure(font="TkFixedFont")
    Sizep121.configure(foreground="#000000")
    Sizep121.configure(insertbackground="black")

    Sizep122 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp122", wrap=True)
    Sizep122.place(relx=0.200, rely=0.827, height=24, relwidth=0.021)
    Sizep122.configure(background="white")
    Sizep122.configure(disabledforeground="#a3a3a3")
    Sizep122.configure(font="TkFixedFont")
    Sizep122.configure(foreground="#000000")
    Sizep122.configure(insertbackground="black")

    Sizep123 = tk.Spinbox(Frame2, from_=0, to=30, textvariable="sp123", wrap=True)
    Sizep123.place(relx=0.230, rely=0.827, height=24, relwidth=0.021)
    Sizep123.configure(background="white")
    Sizep123.configure(disabledforeground="#a3a3a3")
    Sizep123.configure(font="TkFixedFont")
    Sizep123.configure(foreground="#000000")
    Sizep123.configure(insertbackground="black")
    # Button1_22 = tk.Button(top, command=resetobj.Reset)
    # Button1_22.place(relx=0.811, rely=0.917, height=53, width=176)
    # Button1_22.configure(activebackground="#ececec")
    # Button1_22.configure(activeforeground="#000000")
    # Button1_22.configure(background="#b90746")
    # Button1_22.configure(disabledforeground="#a3a3a3")
    # Button1_22.configure(font="-family {Cooper Black} -size 11 -weight normal -slant roman -underline 0 -overstrike 0")
    # Button1_22.configure(foreground="#ffffff")
    # Button1_22.configure(highlightbackground="#d9d9d9")
    # Button1_22.configure(highlightcolor="black")
    # Button1_22.configure(pady="0")
    # Button1_22.configure(text='''RESET''')




    top.mainloop()
maingui()