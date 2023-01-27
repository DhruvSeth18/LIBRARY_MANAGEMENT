import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import *
import webbrowser
import random
from PIL import Image,ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


mydb = mysql.connector.connect(host='localhost', user='root', password='@Behappy12', database='librarymanagement')
cur = mydb.cursor()


# Function for random ID for Registration
def f():
    a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    bk = "REGI"
    c_ = random.choice(a)
    d_ = random.choice(a)
    e_ = random.choice(a)
    f_ = random.choice(a)
    g_ = random.choice(a)
    k = '@' + bk + str(c_) + str(d_) + str(e_) + str(f_) + str(g_)
    return k
def BookId():
    c=0
    for i in range(1,6):
        a=[1,2,3,4,5,6,7,8,9]
        c=(c*10)+random.choice(a)
    return"@BOOK"+str(c)

root = tk.Tk()
root.geometry("1000x450")
root.resizable(0,0)
root.title("MAIN LOGIN")
root.configure(bg="white")
l2=tk.Label(root,text="LIBRARY MANAGEMENT",bg="white",font=('Arial',25,'bold')).place(x=430,y=10)

image=Image.open("chitkara.png").resize((500,300))
photo=ImageTk.PhotoImage(image)

label1 = tk.Label(root,bg="white",image=photo)
label1.pack(side="left")

f1 = tk.Frame(root, height=70,bg="white", width=200)
f1.place(x=580,y=110)

def BEbook():
    win1=Toplevel(root)
    cur.execute('select Sno,book from ebooks')
    b = cur.fetchall()
    win1.geometry("480x330")
    win1.resizable(False,False)
    win1.configure(bg="orange")
    win1.title("OPEN A Ebook")

    f1=tk.Frame(win1,bg="orange")
    f1.pack(pady=20,padx=10)


    trv = ttk.Treeview(f1, selectmode='browse',height=8)
    trv.grid(row=0,column=0,sticky="ew")
    def open():
        select=trv.selection()[0]
        Sel1='select * from ebooks where Sno = %s'
        a__=[select]
        cur.execute(Sel1,a__)
        Data1=cur.fetchall()
        b__=Data1[0][2]
        print(b__)
        webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new(b__)

    b1=tk.Button(win1,text="Open",command=open).pack(pady=30)

    trv["column"] = ("1", "2")
    trv["show"] = "headings"


    trv.column("1", width=100, anchor='c')
    trv.column("2", width=340, anchor='c')
    trv.heading("1", text="Sno")
    trv.heading("2", text="NameOfBook")

    for i in b:
        trv.insert("", 'end', iid=i[0], values=(i[0], i[1]))
    trv_scroll = ttk.Scrollbar(f1, orient="vertical", command=trv.yview)
    trv_scroll.grid(row=0, column=1, sticky="ns")
    trv["yscrollcommand"] = trv_scroll.set
    win1.mainloop()


def admin():
    win1= Toplevel(root)
    win1.geometry("500x450")
    win1.resizable(False,False)
    win1.configure(bg="cyan")
    win1.title("The Admin Window")
    f1 = tk.Frame(win1,bg="cyan")
    f1.pack(side="top", expand=True, padx=20, pady=20)

    f2 = tk.Frame(win1,bg="cyan")
    f2.pack(side="top", expand=True, padx=20, pady=20)

    user_name = tk.StringVar()

    L1 = tk.Label(f1, text="Enter the Password")
    L1.pack(side="left")
    E1 = tk.Entry(f1, width=20, textvariable=user_name)
    E1.pack(side="left", padx=20, fill="x")

    def B1():
        cur.execute("select * from password where name = 'pa'")
        b__ = cur.fetchall()
        c = b__[0][1]
        d=user_name.get()
        if c==d:
            win1.destroy()
            win3 = Toplevel(root)
            win3.geometry("400x800")
            win3.title("Choose Between The ADMIN OPTIONS")
            win3.configure(bg="orange")
            def B1():
                mydb = mysql.connector.connect(host='localhost', user='root', password='@Behappy12',database='librarymanagement')
                cur = mydb.cursor()

                win5 = Toplevel(root)

                win5.geometry("900x480")
                win5.resizable(0, 0)
                win5.title("Issue Book")
                win5.configure(bg="orange")

                l2 = tk.Label(win5, text="ISSUE A BOOK", bg="orange", font=('Arial', 25, 'bold')).place(x=330, y=10)

                f1 = tk.Frame(win5)
                f1.configure(bg="orange")
                f1.pack(side="left", anchor="n", padx=30, pady=60)
                f2 = tk.Frame(win5)
                f2.configure(bg="orange")
                f2.pack(side="left", anchor="n", padx=30, pady=60)
                f3 = tk.Frame(win5)
                f3.configure(bg="orange")
                f3.pack(side="left", anchor="n", padx=30, pady=70)

                cur.execute("select * from pbooks")
                b = cur.fetchall()
                trv = ttk.Treeview(f3, selectmode='browse', height=12)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2", "3")
                trv["show"] = 'headings'

                trv.column("1", width=100, anchor='c')
                trv.column("2", width=150, anchor='c')
                trv.column("3", width=100, anchor='c')

                trv.heading("1", text="Book Number")
                trv.heading("2", text="Books")
                trv.heading("3", text="Quantity")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2]))
                trv_scroll = ttk.Scrollbar(f3, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set

                # Message Box Missing
                a__ = tk.StringVar()
                b__ = tk.StringVar()
                c__ = tk.StringVar()
                d__ = tk.StringVar()
                e__ = tk.StringVar()

                l1 = tk.Label(f1, text="Enter Registration Number ", bg="orange").pack(pady=20, side="top", anchor="w")
                l2 = tk.Label(f1, text="Enter the Book Number ", bg="orange").pack(pady=20, side="top", anchor="w")
                l3 = tk.Label(f1, text="Enter your Email ", bg="orange").pack(pady=20, side="top", anchor="w")
                l4 = tk.Label(f1, text="Issue_Date ", bg="orange").pack(pady=20, side="top", anchor="w")
                l5 = tk.Label(f1, text="Enter The Book Name ", bg="orange").pack(pady=20, side="top", anchor="w")

                E1 = tk.Entry(f2, textvariable=a__).pack(pady=20)
                E2 = tk.Entry(f2, textvariable=b__).pack(pady=20)
                E3 = tk.Entry(f2, textvariable=c__).pack(pady=20)
                E4 = tk.Entry(f2, textvariable=d__).pack(pady=20)
                E5 = tk.Entry(f2, textvariable=e__).pack(pady=20)

                def B12():
                    a_ = "@REGI" + a__.get()
                    b_ = b__.get()
                    c_ = c__.get()
                    d_ = d__.get()
                    e_ = e__.get()
                    cur.execute("select * from registration")
                    bk = cur.fetchall()
                    print(a_)
                    for i in range(len(bk)):
                        if a_ == bk[i][0]:
                            print(a_)
                            N1 = bk[i][2]
                            Id = BookId()
                            Name1 = bk[i][1]
                            print(Id, Name1, c_, N1, d_, e_, b_)
                            q1 = "insert into student(Id,Name,Email,Phone_Number,Issue_Date,Name_of_Book_issued,Book_Number) values(%s,%s,%s,%s,%s,%s,%s)"
                            V1 = [Id, Name1, c_, N1, d_, e_, b_]
                            cur.execute(q1, V1)
                            mydb.commit()
                            Check1="select * from student where Id=%s"
                            Check2=[a_]
                            cur.execute(Check1,Check2)
                            Check3=cur.fetchall()
                            print(Check3)

                            if 1:
                                q2 = "update pbooks SET quantity=quantity-1 where Sno = %s"
                                V2 = [b_]
                                cur.execute(q2, V2)
                                mydb.commit()
                                print("2")
                                break
                    mydb.commit()
                b1 = tk.Button(win5, text="Submit", width=10, command=B12).place(x=350, y=390)
                b1 = tk.Button(win5, text="Exit", width=10, command=win5.destroy).place(x=470, y=390)

                win5 = mainloop()

            def B2():
                win8 = Toplevel(root)
                win8.geometry("2100x1000")
                win8.configure(bg="White")

                f1 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=5, height=70).pack(fill="x")
                f9 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=5, height=60).pack(fill='x', pady=1)

                # The Red Box
                f12 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=7, width=710, height=460)
                f12.place(x=1220, y=130)
                f2 = Frame(win8, bg="#AAE3E2")
                f2.place(x=1290, y=210)

                # The White Box
                f15 = Frame(win8, bg="#AAE3E2", width=610, height=342, relief=RIDGE, bd=7)
                f15.place(x=610, y=650)

                # The Grey Box
                f4 = Frame(win8, bg="#AAE3E2", relief=RIDGE, bd=7, width=610, height=343)
                f4.place(x=0, y=648)

                # The Pink Box
                f13 = Frame(win8, bg="#AAE3E2", width=710, relief=RIDGE, bd=7, height=342)
                f13.place(x=1220, y=650)
                f3 = Frame(win8, bg="#AAE3E2")
                f3.place(x=1320, y=740)

                f5 = Frame(win8, bg="#AAE3E2", width=610, relief=RIDGE, bd=7, height=230).place(x=610, y=130)
                f6 = Frame(win8, bg="#AAE3E2", width=610, relief=RIDGE, bd=7, height=230).place(x=0, y=360)

                f7 = Frame(win8, bg="#AAE3E2", width=610, height=230, relief=RIDGE, bd=7, ).place(x=0, y=130)
                f8 = Frame(win8, bg="#AAE3E2", width=610, height=230, relief=RIDGE, bd=7, ).place(x=610, y=360)

                # Yhe All Box Frame
                f11 = Frame(win8, bg="#AAE3E2", width=1950, height=60, relief=RIDGE, bd=7)
                f11.place(x=0, y=590)

                l1 = Label(win8, text="CHANGE THE STOCK WINDOW", fg="Black", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l1.place(x=760, y=15)

                l2 = l1 = Label(win8, text="PHYSICAL BOOKS", fg="Black", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l2.place(x=860, y=82)

                l3 = Label(win8, text="Add a Book", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l3.place(x=210, y=140)
                l4 = Label(win8, text="Add Book Quantity", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l4.place(x=770, y=140)
                l5 = Label(win8, text="Remove a Book", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l5.place(x=180, y=370)
                l6 = Label(win8, text="Remove Book Quantity", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l6.place(x=735, y=370)
                l7 = Label(win8, text="Physical Book Records", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l7.place(x=1380, y=140)
                l8 = Label(win8, text="E-Book Records", bg="#AAE3E2", font=("Arial", 20, "bold"))
                l8.place(x=1450, y=670)
                l9 = l1 = Label(win8, text="PHYSICAL BOOKS", fg="#AAE3E2", bg="black", font=("Arial", 20, "bold"))
                l9.place(x=860, y=598)
                l10 = Label(win8, text="Add a Book", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l10.place(x=210, y=660)
                l11 = Label(win8, text="Remove a Book", font=("Arial", 20, "bold"), bg="#AAE3E2")
                l11.place(x=800, y=660)

                # Label that Work

                # The Yellow Box

                l12 = Label(win8, text="Enter Book Number", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l12.place(x=100, y=195)

                l13 = Label(win8, text="Enter Book Quantity", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l13.place(x=100, y=240)
                a__ = StringVar()
                b__ = StringVar()
                E1 = Entry(win8, textvariable=a__, width=20)
                E1.place(x=350, y=198)

                E2 = Entry(win8, textvariable=b__, width=20)
                E2.place(x=350, y=242)

                def B1():
                    a_ = a__.get().upper()
                    b_ = b__.get()
                    q1 = "insert into pbooks(books,quantity) Values(%s,%s)"
                    V1 = [a_, b_]
                    cur.execute(q1, V1)
                    mydb.commit()
                    a__.set("")
                    b__.set("")

                B1 = tk.Button(win8, text="Clic To Add A Book", command=B1).place(x=220, y=300)

                # The Orange Box

                l14 = Label(win8, text="Enter Book Number", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l14.place(x=700, y=195)

                l14 = Label(win8, text="Enter Book Quantity to Add", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l14.place(x=700, y=240)

                c__ = StringVar()
                d__ = StringVar()

                E3 = Entry(win8, textvariable=c__, width=20)
                E3.place(x=990, y=198)

                E4 = Entry(win8, textvariable=d__, width=20)
                E4.place(x=990, y=240)

                def B2():
                    c_ = c__.get()
                    d_ = d__.get()
                    q1 = "update pbooks SET quantity=quantity+%s where Sno= %s"
                    V2 = [d_, c_]
                    cur.execute(q1, V2)
                    mydb.commit()
                    print("Hello")
                    c__.set("")
                    d__.set("")

                B2 = tk.Button(win8, text="Clic To Add A Book", command=B2).place(x=840, y=300)

                # The Blue Box
                l15 = Label(win8, text="Enter Book Number", font=("Arial", 14, "bold"), bg="#AAE3E2")
                l15.place(x=100, y=435)

                e__ = StringVar()

                E5 = Entry(win8, width=20, textvariable=e__)
                E5.place(x=350, y=442)

                def B3():
                    q3 = "delete from pbooks where Sno=%s"
                    e_ = e__.get()
                    V3 = [e_]
                    cur.execute(q3, V3)
                    mydb.commit()
                    e__.set("")

                B3 = tk.Button(win8, text="Clic To Add A Book", command=B3).place(x=220, y=530)

                # The light blue Box
                l16 = Label(win8, text="Enter Book Name", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l16.place(x=700, y=435)

                l17 = Label(win8, text="Enter Book Quantity", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l17.place(x=700, y=480)

                f__ = StringVar()
                g__ = StringVar()

                E12 = Entry(win8, width=20, textvariable=f__)
                E12.place(x=990, y=440)

                E7 = Entry(win8, width=20, textvariable=g__)
                E7.place(x=990, y=480)

                def B4():
                    f_ = f__.get()
                    g_ = g__.get()
                    q4 = "update pbooks SET quantity=quantity-%s where Sno = %s"
                    V4 = [g_, f_]
                    cur.execute(q4, V4)
                    mydb.commit()
                    f__.set("")
                    g__.set("")

                B4 = tk.Button(win8, text="Clic To Add A Book", command=B4).place(x=840, y=530)

                # The Grey Box

                l18 = Label(win8, text="Name of Book", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l18.place(x=70, y=730)

                l19 = Label(win8, text="Enter Link", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l19.place(x=70, y=782)
                h__ = StringVar()
                i__ = StringVar()
                E9 = Entry(win8, width=35, textvariable=h__)
                E9.place(x=250, y=732)

                E10 = Entry(win8, width=35, textvariable=i__)
                E10.place(x=250, y=785)

                def B5():
                    h_ = h__.get().upper()
                    i_ = i__.get()
                    q5 = "insert into ebooks(book,link) values(%s,%s)"
                    V5 = [h_, i_]
                    cur.execute(q5, V5)
                    mydb.commit()
                    h__.set("")
                    i__.set("")

                B5 = tk.Button(win8, text="Clic To Add A Book", command=B5).place(x=220, y=880)

                # The white Box
                l20 = Label(win8, text="Enter Sno of Book", font=("Arial", 12, "bold"), bg="#AAE3E2")
                l20.place(x=680, y=735)

                j__ = StringVar()

                E6 = Entry(win8, width=20, textvariable=j__)
                E6.place(x=990, y=740)

                def B6():
                    j_ = j__.get()
                    q6 = "delete from ebooks where Sno = %s"
                    V6 = [j_]
                    cur.execute(q6, V6)
                    mydb.commit()
                    j__.set("")

                B6 = tk.Button(win8, text="Clic To Add A Book", command=B6).place(x=840, y=880)

                # All the entry widget

                cur.execute("select * from pbooks")
                b = cur.fetchall()
                trv = ttk.Treeview(f2, selectmode='browse', height=16)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2", "3")
                trv["show"] = 'headings'

                trv.column("1", width=100, anchor='c')
                trv.column("2", width=350, anchor='c')
                trv.column("3", width=100, anchor='c')

                trv.heading("1", text="Book Number")
                trv.heading("2", text="Books")
                trv.heading("3", text="Quantity")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2]))
                trv_scroll = ttk.Scrollbar(f3, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set

                # The E-books field

                cur.execute('select Sno,book from ebooks')
                b = cur.fetchall()

                trv = ttk.Treeview(f3, selectmode='browse', height=10)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2")
                trv["show"] = "headings"

                trv.column("1", width=150, anchor='c')
                trv.column("2", width=340, anchor='c')
                trv.heading("1", text="Sno")
                trv.heading("2", text="NameOfBook")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1]))
                trv_scroll = ttk.Scrollbar(f3, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set


            def B3():

                win13 = Toplevel(root)
                win13.geometry("550x300")
                win13.configure(bg="Orange")
                win13.resizable(0, 0)

                def B1():
                    a_ = "@BOOK" + a__.get()
                    b_ = b__.get()
                    cur.execute("select * from student")
                    bk = cur.fetchall()
                    A = 1
                    for i in range(len(bk)):
                        if a_ == bk[i][0]:
                            V1 = [bk[i][0]]
                            q1 = "delete from student where Id=%s"
                            cur.execute(q1, V1)
                            mydb.commit()
                            if 1:
                                q2 = "update pbooks SET quantity=quantity+1 where Sno = %s"
                                V2 = [bk[i][6]]
                                cur.execute(q2, V2)
                                mydb.commit()
                                A = 0
                                print("The Book is Removed")
                                break
                    if A:
                        print("Hello My name is Dhruv Seth")

                a__ = tk.StringVar()
                b__ = tk.StringVar()

                l1 = tk.Label(win13, text="Enter Your Book Number", font=("arial", 15, "bold"), bg="Orange").place(x=20,y=40)
                E1 = tk.Entry(win13, width=20, textvariable=a__).place(x=350, y=45)
                l1 = tk.Label(win13, text="Enter Return Date", font=("arial", 15, "bold"), bg="orange").place(x=20,y=120)
                E2 = tk.Entry(win13, width=20, textvariable=b__).place(x=350, y=125)
                b1 = Button(win13, text="Click to Return", command=B1, width=30)
                b1.place(x=140, y=200)


            def B4():
                win4 = Toplevel(root)
                cur.execute("select * from student")
                b = cur.fetchall()
                win4.geometry("1200x350")
                win4.resizable(False, False)
                win4.configure(bg="orange")
                win4.title("VIEW BOOK ISSUED")

                f1 = tk.Frame(win4, bg="orange")
                f1.pack(pady=20, padx=10)

                trv = ttk.Treeview(f1, selectmode='browse', height=12)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2", "3", "4", "5", "6","7")
                trv["show"] = 'headings'

                trv.column("1", width=120, anchor='c')
                trv.column("2", width=220, anchor='c')
                trv.column("3", width=250, anchor='c')
                trv.column("4", width=120, anchor='c')
                trv.column("5", width=120, anchor='c')
                trv.column("6", width=170, anchor='c')
                trv.column("7", width=140,anchor='c')
                trv.heading("1", text="Id")
                trv.heading("2", text="Name")
                trv.heading("3", text="Email")
                trv.heading("4", text="Phone_Number")
                trv.heading("5", text="Issue_Date")
                trv.heading("6", text="Name_of_Book_issued")
                trv.heading("7", text="Book_Number")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5],i[6]))
                trv_scroll = ttk.Scrollbar(f1, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set

                b1=tk.Button(win4,text="Click to Go Back",command=win4.destroy).place(x=310,y=300)

            def B5():

                win5 = Toplevel(root)
                win5.geometry("480x400")
                win5.resizable(0, 0)
                win5.title("New Registration")
                win5.configure(bg="orange")

                l2 = tk.Label(win5, text="New Registration", bg="orange", font=('Arial', 15, 'bold')).place(x=145, y=10)

                f1 = tk.Frame(win5)
                f1.configure(bg="orange")
                f1.pack(side="left", anchor="n", padx=30, pady=60)
                f2 = tk.Frame(win5)
                f2.configure(bg="orange")
                f2.pack(side="left", anchor="n", padx=30, pady=60)
                f3 = tk.Frame(win5)

                def Register():
                    a_=a__.get()
                    b_=b__.get()
                    c_=c__.get()
                    d_=d__.get()
                    if a_!='' or len(a_)>4:
                        if len(b_)==10 :
                            if b_[0] in ['9','8','7','6','5']:
                                if c_[len(c_):-5:-1][::-1]==".com" or len(c_)>7 :
                                    if len(d_)==12 or len(d_)==14 :
                                        a_a=f()
                                        sql1="insert into registration(ID,Name,Phone_No,Email,Aadhar) values(%s,%s,%s,%s,%s)"
                                        Values=[a_a,a_,b_,c_,d_]
                                        cur.execute(sql1,Values)
                                        mydb.commit()
                                        win9=Toplevel(root)
                                        win9.geometry("450x400")
                                        l1=tk.Label(text="Boom You are Registered",font=("Arial",25,"bold"))
                                    else:
                                        win2 = Toplevel(root)
                                        l1 = tk.Label(win2, text="INCORRECT AADHAR").pack()
                                        b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                                else:
                                    win2 = Toplevel(root)
                                    l1 = tk.Label(win2, text="INCORRECT Email").pack()
                                    b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                            else:
                                win2 = Toplevel(root)
                                l1 = tk.Label(win2, text="INCORRECT PHONE NUMBER").pack()
                                b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                        else:
                            win2 = Toplevel(root)
                            l1 = tk.Label(win2, text="INCORRECT PHONE NUMBER").pack()
                            b1 = tk.Button(win2, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)
                    else:
                        z1 = Toplevel(root)
                        l1 = tk.Label(z1, text="Please Enter your name").pack()
                        b1 = tk.Button(z1, text="Retry", bg="#AEE2FF", command=win2.destroy).pack(pady=10)

                b1 = tk.Button(win5, text="Register", width=10, command=Register).place(x=140, y=340)
                b1 = tk.Button(win5, text="Back", width=10, command=win5.destroy).place(x=270, y=340)
                # Message Box Missing
                a__ = tk.StringVar()
                b__ = tk.StringVar()
                c__ = tk.StringVar()
                d__ = tk.StringVar()

                l1 = tk.Label(f1, text="Enter Student Name", bg="orange").pack(pady=20, side="top", anchor="w")
                l2 = tk.Label(f1, text="Enter your Phone_No", bg="orange").pack(pady=20, side="top", anchor="w")
                l3 = tk.Label(f1, text="Enter your Email ", bg="orange").pack(pady=20, side="top", anchor="w")
                l4 = tk.Label(f1, text="AAdhar", bg="orange").pack(pady=20, side="top", anchor="w")

                E1 = tk.Entry(f2, textvariable=a__,width=30).pack(pady=20)
                E2 = tk.Entry(f2, textvariable=b__,width=30).pack(pady=20)
                E3 = tk.Entry(f2, textvariable=c__,width=30).pack(pady=20)
                E4 = tk.Entry(f2, textvariable=d__,width=30).pack(pady=20)

                #a_a is the random number generated

            def B6():

                win4 = Toplevel(root)
                cur.execute("select * from registration")
                b = cur.fetchall()
                win4.geometry("950x350")
                win4.resizable(False, False)
                win4.configure(bg="orange")
                win4.title("VIEW BOOK ISSUED")

                f1 = tk.Frame(win4, bg="orange")
                f1.pack(pady=20, padx=10)

                trv = ttk.Treeview(f1, selectmode='browse', height=12)
                trv.grid(row=0, column=0, sticky="ew")

                trv["column"] = ("1", "2", "3", "4", "5")
                trv["show"] = 'headings'

                trv.column("1", width=140, anchor='c')
                trv.column("2", width=200, anchor='c')
                trv.column("3", width=120, anchor='c')
                trv.column("4", width=250, anchor='c')
                trv.column("5", width=140, anchor='c')
                trv.heading("1", text="Id")
                trv.heading("2", text="Name")
                trv.heading("3", text="Phone_Number")
                trv.heading("4", text="Email")
                trv.heading("5", text="Aadhar")

                for i in b:
                    trv.insert("", 'end', iid=i[0], values=(i[0], i[1], i[2], i[3], i[4]))
                trv_scroll = ttk.Scrollbar(f1, orient="vertical", command=trv.yview)
                trv_scroll.grid(row=0, column=1, sticky="ns")
                trv["yscrollcommand"] = trv_scroll.set

                b1 = tk.Button(win4, text="Click to Go Back", command=win4.destroy).place(x=310, y=300)

            B1 = tk.Button(win3, text="Issue A Book",command=B1,height=3, width=20)
            B1.pack(pady=20)
            B2 = tk.Button(win3, text="Change Stock",command=B2, height=3, width=20)
            B2.pack(pady=20)
            B3 = tk.Button(win3, text="Return Book", height=3,command=B3, width=20)
            B3.pack(pady=20)
            B4 = tk.Button(win3, text="View Book Issued",command=B4, height=3, width=20)
            B4.pack(pady=20)
            B5 = tk.Button(win3, text="New Registration", height=3,width=20, command=B5)
            B5.pack(pady=20)
            B6 = tk.Button(win3, text="Registered Member", height=3, width=20, command=B6)
            B6.pack(pady=20)
            B7 = tk.Button(win3, text="Exit", height=3, width=20, command=win3.destroy)
            B7.pack(pady=20)

            win3.resizable(False, False)
            win3.configure(bg="orange")


        else:
            win2=Toplevel(root)
            l1=tk.Label(win2,text="INCORRECT PASSWORD").pack()
            b1=tk.Button(win2,text="Retry",bg="#AEE2FF",command=win2.destroy).pack(pady=10)



    B1 = tk.Button(f2, text="Submit", width=20, command=B1)
    B1.pack(side="left", padx=10)


    B2 = tk.Button(f2, text="quit", width=20, command=win1.destroy)
    B2.pack(side="left", padx=10)





# BUTTON MAIN WINDOW
b1 = tk.Button(f1, text="ADMIN", height=4, width=30, bg="#CE1212",fg="white",font=("Arial",10,"bold"), command=admin)
b1.pack(side="top", pady=10)

b2 = tk.Button(f1, text="Ebooks", height=4, width=30, bg="#CE1212",fg="white",font=("Arial",10,"bold"),command=BEbook)
b2.pack(side="left",pady=20)

root.mainloop()