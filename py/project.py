from tkinter import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

def mainwindow() :
    root = Tk()
    w = 1000
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#FFFAFA')
    #root.config(bg='#4a3933')
    root.title("Welcome to Uread")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout(root) :
    global userentry
    global pwdentry
    global loginframe

    mainlog = Frame(root,bg='white')
    mainlog.place(width=1000,height=600)
    loginframe = Frame(mainlog,bg='#8ab6d6')
    loginframe.place(width=300,height=500,x=100,y=50)
    loginframe1 = Frame(mainlog,bg='#fff9b0')
    loginframe1.place(width=500,height=500,x=400,y=50)
    #logframe
    Label(loginframe,text='Welcome',font="Garamond 30 bold",bg='#8ab6d6').place(x=70,y=50)
    Label(loginframe,text='To ',font="Garamond 30 bold",bg='#8ab6d6').place(x=130,y=130)
    Label(loginframe,text='U Read',font="Garamond 30 bold",bg='#8ab6d6').place(x=80,y=200)
    Label(loginframe,image=img6,bg='#8ab6d6').place(x=20,y=250)
    #logframe1
    Label(loginframe1,image=img1,bg='#fff9b0').place(y=30,x=50)
    Label(loginframe1,text='Login',bg='#fff9b0',font="Garamond 30 bold").place(y=60,x=200)
    #login 
    Label(loginframe1,text='Username :',bg='#fff9b0',font="Garamond 24 bold").place(y=160,x=30)
    userentry = Entry(loginframe1,bg='#faf3f3',width=20,textvariable=userinfo,font="Garamond 18 bold")
    userentry.place(y=170,x=200)
    Label(loginframe1,text='Password :',bg='#fff9b0',font="Garamond 24 bold").place(y=260,x=38)
    pwdentry = Entry(loginframe1,bg='#faf3f3',width=20,show='*',font="Garamond 18 bold",textvariable=pwdinfo)
    pwdentry.place(y=270,x=200)
    Button(loginframe1,text='Register',bg='#faf3f3',bd=4,command=regiswindow).place(y=380,x=50)
    Button(loginframe1,text='Login',bg='#faf3f3',bd=4,width=7,command=loginclick).place(y=380,x=330)
    

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('db/data.db')
    cursor = conn.cursor()


def loginclick() :
    #print("Hello from loginclick")
    if userinfo.get() == "" :
        messagebox.showwarning('Admin:','Please Enter username')
        userentry.focus_force()
    else :
        sql = 'select * from customer where USERNAME = ?'
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if pwdinfo.get() == "" :
            messagebox.showwarning('Password','Enter password first')
        else :
            if result :
                sql = 'select * from customer where USERNAME = ? and PASSWORD = ?'
                cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                result = cursor.fetchall()
                if result :
                    messagebox.showinfo('Admin :','Login Sucessfully')
                    sql = 'select * from customer where USERNAME = ? and PASSWORD = ?'
                    global db
                    cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
                    db = cursor.fetchone()
                    pwdentry.delete(0,END)
                    pwdentry.focus_force()
                    main()
                else :
                    messagebox.showwarning('Admin:','Username or Password is invaild.')
                    pwdentry.delete(0,END)
                    userentry.delete(0,END)
                    userentry.focus_force()
            else :
                messagebox.showwarning('Admin:','Username not found\nPlease Register Befor Login')
                pwdentry.delete(0,END)
                userentry.delete(0,END)
                userentry.focus_force()

def regiswindow() :
    global fullname,lastname,newuser,newpwd,cfpwd,regisframe,email

    loginframe.destroy()
    
    regisframe = Frame(root,bg='white')
    regisframe.place(width=1000,height=600)
    root.title(': Welcome to User Registration :')

    Frame(regisframe,bg='#8ab6d6').place(width=300,height=500,x=100,y=50)
    Label(regisframe,image=img12,bg='#8ab6d6').place(x=100,y=140)
    Frame(regisframe,bg='#fff9b0').place(width=500,height=500,x=400,y=50)
    Label(regisframe,text=' Registration',image=img4,bg='#fff9b0',font="Garamond 26 bold",compound=LEFT).place(x=490,y=60)
    Label(regisframe,text='      Full Name :',bg='#fff9b0',font="Garamond 12 bold",image=img7,compound=LEFT).place(x=420,y=135)
    Label(regisframe,text='      Last Name :',bg='#fff9b0',font="Garamond 12 bold",image=img7,compound=LEFT).place(x=420,y=185)
    Label(regisframe,text='     Username   :',bg='#fff9b0',font="Garamond 12 bold",image=img8,compound=LEFT).place(x=420,y=235)
    Label(regisframe,text='      Password    :',bg='#fff9b0',font="Garamond 12 bold",image=img9,compound=LEFT).place(x=420,y=285)
    Label(regisframe,text='     Comfime Password   :',bg='#fff9b0',font="Garamond 12 bold",image=img9,compound=LEFT).place(x=420,y=330)
    Label(regisframe,text='      Email   :',bg='#fff9b0',font="Garamond 12 bold",image=img10,compound=LEFT).place(x=420,y=375)
    fullname = Entry(regisframe,font="Garamond 14 bold",bg='#faf3f3',textvariable=fname)
    fullname.place(y=140,x=570)
    lastname = Entry(regisframe,font="Garamond 14 bold",bg='#faf3f3',textvariable=lname)
    lastname.place(y=190,x=570)
    newuser = Entry(regisframe,font="Garamond 14 bold",bg='#faf3f3',textvariable=newuserinfo)
    newuser.place(y=240,x=570)
    newpwd = Entry(regisframe,font="Garamond 14 bold",bg='#faf3f3',show='*',textvariable=newpwdinfo)
    newpwd.place(y=290,x=570)
    cfpwd = Entry(regisframe,font="Garamond 14 bold",bg='#faf3f3',show='*',textvariable=cfinfo)
    cfpwd.place(y=335,x=630)
    email = Entry(regisframe,font="Garamond 14 bold",bg='#faf3f3',textvariable=eminfo)
    email.place(y=380,x=570)
    #button
    Button(regisframe,text='Registration now',bd=5,bg='green',font="Garamond 18 bold",fg='white',command=registration).place(x=680,y=480)
    Button(regisframe,text='Cancel',bd=5,bg='#ce1212',font="Garamond 18 bold",fg='white',command=cancel,width=15).place(x=430,y=480)



def registration() :
    if fname.get() == '':
        messagebox.showwarning('Admin','Please Enter First Name')
        return
    elif lname.get() == '' :
        messagebox.showwarning('Admin','Please Enter Last Name')
        return
    elif newuser.get()=='':
        messagebox.showwarning('Admin','Please Enter New Username')
        return
    elif newpwd.get()=='':
        messagebox.showwarning('Admin','Please Enter New Password')
        return
    elif cfpwd.get()=='':
        messagebox.showwarning('Admin','Please Enter Confirm Password')
        return
    else :
        sql = "select * from customer where USERNAME =?"
        cursor.execute(sql,[newuserinfo.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("Admin:","The username is already exists")
            newuser.select_range(0,END)
            newuser.focus_force()
            return
        else :
            if newpwdinfo.get() == cfinfo.get() :
                sql = "insert into customer (FIRST_NAME,LAST_NAME,USERNAME,PASSWORD,email) values (?,?,?,?,?)"
                cursor.execute(sql,[fname.get(),lname.get(),newuserinfo.get(),newpwdinfo.get(),eminfo.get()])
                conn.commit()
                messagebox.showinfo("Admin:","Registration Successfully")
                newuser.delete(0,END)
                newpwd.delete(0,END)
                cfpwd.delete(0,END)
                fullname.delete(0,END)
                lastname.delete(0,END)
                email.delete(0,END)
                fullname.focus_force()
            else :
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.selection_range(0,END)
                cfpwd.focus_force()

def setNewValue(newValue) :
    global count, lbl_amount,popup
    count = count+newValue
    lbl_amount['text'] = str(count)
    popup.destroy()
    popup = None
    messagebox.showinfo("Success", "New balance is %d THB."%count)

def showpopup(root) :
    global popup

    if popup != None :
        return None
    
    popup = Toplevel(root)
    popup.geometry('200x200+800+300')
    popup.protocol('WM_DELETE_WINDOW',(lambda:'pass'))
    popup.rowconfigure((0,2),weight = 1)
    popup.columnconfigure((0,1),weight = 1)
    popup.resizable(0,0)

    list_amt = [20,50,100,250,300,500,800,1000]

    combo1 = ttk.Combobox(popup, values = list_amt, state = 'readonly')
    combo1.current(0)
    combo1.grid(row=0,columnspan=2)

    btn_done = Button(popup, text = 'Done', command = lambda:setNewValue(list_amt[combo1.current()]))
    btn_done.grid(row=1,columnspan=2,sticky=N)


def main() :
    loginframe.destroy()
    global winmain,lbl_amount
    winmain = Frame(root,bg='#bbe1fa')
    winmain.place(width=1000,height=600)
    root.title('Welcome : '+db[1]+" "+db[2])

    Frame(winmain,bg='#f98404').place(width=120,height=110,x=850)
    Button(winmain,image=img18,bd=3,bg='#bbe1fa',text='Search',compound=LEFT,font="Garamond 14 bold",command=lambda:init_verify(root)).place(y=40,x=700)
    Label(winmain,image=img3,bg='#bbe1fa').place(y=20,x=50)
    Label(winmain,text='CUSTOMER ID :',font="Garamond 18 bold",bg='#bbe1fa').place(x=200,y=40)
    cusid = Label(winmain,text='',font="Garamond 18 bold",bg='#bbe1fa')
    cusid.place(x=400,y=40)
    Label(winmain,text='Name :',font="Garamond 18 bold",bg='#bbe1fa').place(x=200,y=80)
    name = Label(winmain,text='',font="Garamond 18 bold",bg='#bbe1fa')
    name.place(x=280,y=80)
    last = Label(winmain,text='',font="Garamond 18 bold",bg='#bbe1fa')
    last.place(x=400,y=80)
    Button(winmain,text='Proflie',font="Garamond 9 bold",bg='#faf3f3',command=log2).place(x=200,y=120)
    Button(winmain,text='  รายงานปัญหา',font="Garamond 7 bold",bg='#faf3f3',image=img37,compound=LEFT,fg='red',command=report).place(x=280,y=120)
    Label(winmain,text="Your Balance",font="Times 13 bold",bg='#f98404').place(x=860,y=10)
    lbl_amount = Label(winmain,text=str(count),font='Tahoma 16 bold',bg='#f98404')
    lbl_amount.place(y=40,x=895)
    bt = Button(winmain,text='Top Up',relief=RAISED,font="Times 15 bold",bg="lightgrey",fg="black",width=9,command=lambda:showpopup(root))
    bt.place(x=850,y=80)
    #profile
    cusid['text'] = db[0]
    name['text'] = db[1]
    last['text'] = db[2]

    Frame(winmain,bg='#fff4e1').place(width=800,height=400,x=120,y=180)
    Label(winmain,text='   Best seller',fg='red',font="Garamond 20 bold",image=img15,bg='#fff4e1',compound=LEFT).place(x=120,y=180)
    #book1
    Label(winmain,image=img13,bg='#fff4e1').place(x=190,y=250)
    Label(winmain,text='After Effects + Premier Pro',bg='#fff4e1',font="Times 13 bold").place(x=150,y=410)
    Label(winmain,text='399 Baht.',bg='#fff4e1',font="Garamond 12 bold",fg='red').place(x=220,y=440)
    Button(winmain,text='Buy',bd=3,bg='#faf3f3',font="Garamond 14 bold",width=10,command=buy_book1).place(x=195,y=480)
    #book2
    Label(winmain,image=img14,bg='#fff4e1').place(x=410,y=250)
    Label(winmain,text='พิชิต TOEIC 900++',bg='#fff4e1',font="Times 13 bold").place(x=390,y=410)
    Label(winmain,text='289 Baht.',bg='#fff4e1',font="Garamond 12 bold",fg='red').place(x=425,y=440)
    Button(winmain,text='Buy',bd=3,bg='#faf3f3',font="Garamond 14 bold",width=10,command=buy_book2).place(x=400,y=480)
    #book3
    Label(winmain,image=img16,bg='#fff4e1').place(x=590,y=250)
    Label(winmain,text='เคล็ดไม่ลับการสัมภาษณ์',bg='#fff4e1',font="Times 11 bold").place(x=560,y=410)
    Label(winmain,text='190 Baht.',bg='#fff4e1',font="Garamond 12 bold",fg='red').place(x=605,y=440)
    Button(winmain,text='Buy',bd=3,bg='#faf3f3',font="Garamond 14 bold",width=10,command=buy_book3).place(x=580,y=480)
    #book4
    Label(winmain,image=img17,bg='#fff4e1').place(x=750,y=250)
    Label(winmain,text='English Grammar',bg='#fff4e1',font="Times 11 bold").place(x=750,y=410)
    Label(winmain,text='365 Baht.',bg='#fff4e1',font="Garamond 12 bold",fg='red').place(x=770,y=440)
    Button(winmain,text='Buy',bd=3,bg='#faf3f3',font="Garamond 14 bold",width=10,command=buy_book4).place(x=750,y=480)

def report () :
    global rp
    winmain.destroy
    rp = Frame(root,bg='white')
    rp.place(width=1000,height=600)

    Frame(rp,bg='#3d84a8').place(width=1000,height=150)
    Label(rp,text='Frequently Asked Questions',bg='#3d84a8',fg='white',font="Garamond 30 bold").place(x=30,y=30)
    Label(rp,text='คำถามที่พบบ่อย: ',bg='white',font="Garamond 24 bold").place(x=40,y=160)
    Label(rp,text='Q:   เติมเงินซื้อหนังสืออย่างไร ?',bg='white',fg='red',font="Garamond 16 bold").place(x=40,y=220)
    Label(rp,text='A:   ให้ผู้ใช้งานคลิ๊กที่ปุ่ม Top Up เพื่อเติมเงิน เมื่อคลิ๊กเสร็จแล้ว',bg='white',font="Garamond 16 bold").place(x=40,y=260)
    Label(rp,text='      จะมีหน้าต่างขึ้นให้เลือกจำนวนเงินจากนั้นให้คลิ๊กที่ปุ่ม Done',bg='white',font="Garamond 16 bold").place(x=40,y=300)
    Label(rp,text='Q:   จำเป็นต้องกรอก Email ในขั้นตอนการสมัครหรือไม่ ?',bg='white',fg='red',font="Garamond 16 bold").place(x=40,y=340)
    Label(rp,text='A:   ผู้ใช้ไม่จำเป็นต้องหรอก Email ลงในขั้นตอนการสมัคร',bg='white',font="Garamond 16 bold").place(x=40,y=380)
    Label(rp,text='Q:   ถ้ามีปัญหาอื่นๆติดต่อได้ทางไหน ?',bg='white',fg='red',font="Garamond 16 bold").place(x=40,y=420)
    Label(rp,text='A:   สามารถติดต่อได้ทาง Email = nahathai.r@bumail.net',bg='white',font="Garamond 16 bold").place(x=40,y=460)
    Button(rp,text='    Back',image=img19,compound=LEFT,bg='white',font="Garamond 18 bold",command=main).place(x=40,y=520)


def buy_book1 ():
    global buy1,lbl_amount
    buy1 = Frame(root,bg='white')
    buy1.place(width=1000,height=600)
    root.title('Welcome : '+db[1]+" "+db[2])

    sql = 'SELECT * FROM ebook WHERE ID_BOOK = 600'
    global bk1 
    cursor.execute(sql)
    bk1 = cursor.fetchone()


    Frame(buy1,bg='#3d84b8').place(width=1000,height=50)
    Frame(buy1,bg='#3d84b8').place(width=1000,height=150,y=500)
    lbl_amount = Label(buy1,text=str(count),font='Tahoma 16 bold',bg='#3d84b8')
    lbl_amount.place(y=10,x=735)
    Label(buy1,text='บ.',font='Garamond 16 bold',bg='#3d84b8').place(x=790,y=13)
    Label(buy1,text='U Read',font="Times 26 bold",bg='white').place(x=50,y=60)
    Label(buy1,text='หมวดหมู่หนังสือ  -> 600 -> After Effects + Premier Pro',font="Garamond 12",bg='white').place(x=450,y=80)
    Label(buy1,image=img8,bg='#3d84b8').place(x=50,y=10)
    name = Label(buy1,text='   ',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    name.place(x=100,y=15)
    last = Label(buy1,text='',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    last.place(x=170,y=15)
    Label(buy1,image=img22,bg='#3d84b8').place(x=130,y=140)
    Label(buy1,text='ชื่อหนังสือ : ',font="Garamond 24 bold",bg='white').place(x=450,y=140)
    bkname = Label(buy1,text=' ',font="Garamond 20",bg='white')
    bkname.place(x=620,y=145)
    #ผู้แต่ง
    Label(buy1,text='ผู้แต่ง :',font="Garamond 24 bold",bg='white').place(x=450,y=200)
    aname = Label(buy1,text=' ',font="Garamond 18",bg='white')
    aname.place(x=550,y=205)
    #สำนักพิมพ์
    Label(buy1,text='สำนักพิมพ์ :',font="Garamond 24 bold",bg='white').place(x=450,y=260)
    pname = Label(buy1,text=' ',font="Garamond 18",bg='white')
    pname.place(x=645,y=265)
    #price
    Label(buy1,text='ราคา :            บ.',font="Garamond 24 bold",bg='white').place(x=450,y=320)
    price = Label(buy1,text=' ',font="Garamond 18",bg='white')
    price.place(x=555,y=325)

    btn1 = Button(buy1,text='  ซื้อหนังสือ',image=img11,font="Garamond 18",compound=LEFT,bg='#e7d4b5',command=book1)
    btn1.place(x=820,y=450)

    name['text'] = db[1]
    last['text'] = db[2]
    bkname['text'] = bk1[1]
    aname['text'] = bk1[3]
    pname['text'] = bk1[4]
    price['text'] = bk1[2]
    Button(buy1,text='    Log out',image=img21,compound=LEFT,bg='#3d84b8',fg='white',font="Garamond 10 bold",command=lambda:loginlayout(root)).place(x=900,y=10)
    Button(buy1,text='    Back',image=img19,compound=LEFT,bg='#e7d4b5',font="Garamond 18 bold",command=main).place(x=50,y=450)

def buy_book2 ():
    global buy2,lbl_amount
    buy2 = Frame(root,bg='white')
    buy2.place(width=1000,height=600)
    root.title('Welcome : '+db[1]+" "+db[2])

    sql = 'SELECT * FROM ebook WHERE ID_BOOK = 400'
    global bk2 
    cursor.execute(sql)
    bk2 = cursor.fetchone()


    Frame(buy2,bg='#3d84b8').place(width=1000,height=50)
    Frame(buy2,bg='#3d84b8').place(width=1000,height=150,y=500)
    lbl_amount = Label(buy2,text=str(count),font='Tahoma 16 bold',bg='#3d84b8')
    lbl_amount.place(y=10,x=735)
    Label(buy2,text='บ.',font='Garamond 16 bold',bg='#3d84b8').place(x=790,y=13)
    Label(buy2,text='U Read',font="Times 26 bold",bg='white').place(x=50,y=60)
    Label(buy2,text='หมวดหมู่หนังสือ  -> 400 -> พิชิต TOEIC 900++',font="Garamond 12",bg='white').place(x=450,y=80)
    Label(buy2,image=img8,bg='#3d84b8').place(x=50,y=10)
    name = Label(buy2,text='   ',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    name.place(x=100,y=15)
    last = Label(buy2,text='',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    last.place(x=170,y=15)
    Label(buy2,image=img23,bg='#3d84b8').place(x=130,y=140)
    Label(buy2,text='ชื่อหนังสือ : ',font="Garamond 24 bold",bg='white').place(x=450,y=140)
    bkname = Label(buy2,text=' ',font="Garamond 20",bg='white')
    bkname.place(x=620,y=145)
    #ผู้แต่ง
    Label(buy2,text='ผู้แต่ง :',font="Garamond 24 bold",bg='white').place(x=450,y=200)
    aname = Label(buy2,text=' ',font="Garamond 18",bg='white')
    aname.place(x=550,y=205)
    #สำนักพิมพ์
    Label(buy2,text='สำนักพิมพ์ :',font="Garamond 24 bold",bg='white').place(x=450,y=260)
    pname = Label(buy2,text=' ',font="Garamond 18",bg='white')
    pname.place(x=645,y=265)
    #price
    Label(buy2,text='ราคา :            บ.',font="Garamond 24 bold",bg='white').place(x=450,y=320)
    price = Label(buy2,text=' ',font="Garamond 18",bg='white')
    price.place(x=555,y=325)

    btn2 = Button(buy2,text='  ซื้อหนังสือ',image=img11,font="Garamond 18",compound=LEFT,bg='#e7d4b5',command=book2)
    btn2.place(x=820,y=450)

    name['text'] = db[1]
    last['text'] = db[2]
    bkname['text'] = bk2[1]
    aname['text'] = bk2[3]
    pname['text'] = bk2[4]
    price['text'] = bk2[2]
    Button(buy2,text='    Log out',image=img21,compound=LEFT,bg='#3d84b8',fg='white',font="Garamond 10 bold",command=lambda:loginlayout(root)).place(x=900,y=10)
    Button(buy2,text='    Back',image=img19,compound=LEFT,bg='#e7d4b5',font="Garamond 18 bold",command=main).place(x=50,y=450)

def buy_book3 ():
    global buy3,lbl_amount
    buy3 = Frame(root,bg='white')
    buy3.place(width=1000,height=600)
    root.title('Welcome : '+db[1]+" "+db[2])

    sql = 'SELECT * FROM ebook WHERE ID_BOOK = 130'
    global bk3 
    cursor.execute(sql)
    bk3 = cursor.fetchone()


    Frame(buy3,bg='#3d84b8').place(width=1000,height=50)
    Frame(buy3,bg='#3d84b8').place(width=1000,height=150,y=500)
    lbl_amount = Label(buy3,text=str(count),font='Tahoma 16 bold',bg='#3d84b8')
    lbl_amount.place(y=10,x=735)
    Label(buy3,text='บ.',font='Garamond 16 bold',bg='#3d84b8').place(x=790,y=13)
    Label(buy3,text='U Read',font="Times 26 bold",bg='white').place(x=50,y=60)
    Label(buy3,text='หมวดหมู่หนังสือ  -> 130 -> เคล็ดไม่ลับการสัมภาษณ์',font="Garamond 12",bg='white').place(x=450,y=80)
    Label(buy3,image=img8,bg='#3d84b8').place(x=50,y=10)
    name = Label(buy3,text='   ',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    name.place(x=100,y=15)
    last = Label(buy3,text='',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    last.place(x=170,y=15)
    Label(buy3,image=img24,bg='#3d84b8').place(x=130,y=140)
    Label(buy3,text='ชื่อหนังสือ : ',font="Garamond 24 bold",bg='white').place(x=450,y=140)
    bkname = Label(buy3,text=' ',font="Garamond 20",bg='white')
    bkname.place(x=620,y=145)
    #ผู้แต่ง
    Label(buy3,text='ผู้แต่ง :',font="Garamond 24 bold",bg='white').place(x=450,y=200)
    aname = Label(buy3,text=' ',font="Garamond 18",bg='white')
    aname.place(x=550,y=205)
    #สำนักพิมพ์
    Label(buy3,text='สำนักพิมพ์ :',font="Garamond 24 bold",bg='white').place(x=450,y=260)
    pname = Label(buy3,text=' ',font="Garamond 18",bg='white')
    pname.place(x=645,y=265)
    #price
    Label(buy3,text='ราคา :            บ.',font="Garamond 24 bold",bg='white').place(x=450,y=320)
    price = Label(buy3,text=' ',font="Garamond 18",bg='white')
    price.place(x=555,y=325)

    btn3 = Button(buy3,text='  ซื้อหนังสือ',image=img11,font="Garamond 18",compound=LEFT,bg='#e7d4b5',command=b3_1
    )
    btn3.place(x=820,y=450)

    name['text'] = db[1]
    last['text'] = db[2]
    bkname['text'] = bk3[1]
    aname['text'] = bk3[3]
    pname['text'] = bk3[4]
    price['text'] = bk3[2]
    Button(buy3,text='    Log out',image=img21,compound=LEFT,bg='#3d84b8',fg='white',font="Garamond 10 bold",command=lambda:loginlayout(root)).place(x=900,y=10)
    Button(buy3,text='    Back',image=img19,compound=LEFT,bg='#e7d4b5',font="Garamond 18 bold",command=main).place(x=50,y=450)

def buy_book4 ():
    global buy4,lbl_amount
    buy4 = Frame(root,bg='white')
    buy4.place(width=1000,height=600)
    root.title('Welcome : '+db[1]+" "+db[2])

    sql = 'SELECT * FROM ebook WHERE ID_BOOK = 130'
    global bk4 
    cursor.execute(sql)
    bk4 = cursor.fetchone()


    Frame(buy4,bg='#3d84b8').place(width=1000,height=50)
    Frame(buy4,bg='#3d84b8').place(width=1000,height=150,y=500)
    lbl_amount = Label(buy4,text=str(count),font='Tahoma 16 bold',bg='#3d84b8')
    lbl_amount.place(y=10,x=735)
    Label(buy4,text='บ.',font='Garamond 16 bold',bg='#3d84b8').place(x=790,y=13)
    Label(buy4,text='U Read',font="Times 26 bold",bg='white').place(x=50,y=60)
    Label(buy4,text='หมวดหมู่หนังสือ  -> 130 -> เคล็ดไม่ลับการสัมภาษณ์',font="Garamond 12",bg='white').place(x=450,y=80)
    Label(buy4,image=img8,bg='#3d84b8').place(x=50,y=10)
    name = Label(buy4,text='   ',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    name.place(x=100,y=15)
    last = Label(buy4,text='',font="Garamond 12 bold",bg='#3d84b8',fg='white')
    last.place(x=170,y=15)
    Label(buy4,image=img25,bg='#3d84b8').place(x=130,y=140)
    Label(buy4,text='ชื่อหนังสือ : ',font="Garamond 24 bold",bg='white').place(x=450,y=140)
    bkname = Label(buy4,text=' ',font="Garamond 20",bg='white')
    bkname.place(x=620,y=145)
    #ผู้แต่ง
    Label(buy4,text='ผู้แต่ง :',font="Garamond 24 bold",bg='white').place(x=450,y=200)
    aname = Label(buy4,text=' ',font="Garamond 18",bg='white')
    aname.place(x=550,y=205)
    #สำนักพิมพ์
    Label(buy4,text='สำนักพิมพ์ :',font="Garamond 24 bold",bg='white').place(x=450,y=260)
    pname = Label(buy4,text=' ',font="Garamond 18",bg='white')
    pname.place(x=645,y=265)
    #price
    Label(buy4,text='ราคา :            บ.',font="Garamond 24 bold",bg='white').place(x=450,y=320)
    price = Label(buy4,text=' ',font="Garamond 18",bg='white')
    price.place(x=555,y=325)

    btn4 = Button(buy4,text='  ซื้อหนังสือ',image=img11,font="Garamond 18",compound=LEFT,bg='#e7d4b5',command=book4)
    btn4.place(x=820,y=450)

    name['text'] = db[1]
    last['text'] = db[2]
    bkname['text'] = bk4[1]
    aname['text'] = bk4[3]
    pname['text'] = bk4[4]
    price['text'] = bk4[2]
    Button(buy4,text='    Log out',image=img21,compound=LEFT,bg='#3d84b8',fg='white',font="Garamond 10 bold",command=lambda:loginlayout(root)).place(x=900,y=10)
    Button(buy4,text='    Back',image=img19,compound=LEFT,bg='#e7d4b5',font="Garamond 18 bold",command=main).place(x=50,y=450)

def book1() :
    global count
    m1 = messagebox.askyesno(title='Confirm',message='Do you confirm to order a book')
    if m1 == 1 :
        if count >= 399 :
            messagebox.showinfo(title='Success',message='Thanks for purchasing.Enjoy  a book')
            count = count-399
            lbl_amount['text']=str(count)
            b1_1()
        elif count < 399 :
            messagebox.showinfo(title='Sorry',message='Your balance is not enough',icon='error')

def book2() :
    global count
    m2 = messagebox.askyesno(title='Confirm',message='Do you confirm to order a book')
    if m2 == 1 :
        if count >= 289 :
            messagebox.showinfo(title='Success',message='Thanks for purchasing.Enjoy  a book')
            count = count-289
            lbl_amount['text']=str(count)
            b2_1( )
        elif count < 289 :
            messagebox.showinfo(title='Sorry',message='Your balance is not enough',icon='error')

def book3() :
    global count
    m3 = messagebox.askyesno(title='Confirm',message='Do you confirm to order a book')
    if m3 == 1 :
        if count >= 190 :
            messagebox.showinfo(title='Success',message='Thanks for purchasing.Enjoy  a book')
            count = count-190
            lbl_amount['text']=str(count)
        elif count < 190 :
            messagebox.showinfo(title='Sorry',message='Your balance is not enough',icon='error')

def book4() :
    global count
    m4 = messagebox.askyesno(title='Confirm',message='Do you confirm to order a book')
    if m4 == 1 :
        if count >= 365 :
            messagebox.showinfo(title='Success',message='Thanks for purchasing.Enjoy  a book')
            count = count-365
            lbl_amount['text']=str(count)
            b4_1()
        elif count < 365 :
            messagebox.showinfo(title='Sorry',message='Your balance is not enough',icon='error')

def b1_1() :
    buy1.destroy()
    global book1_1
    book1_1 = Frame(root,bg='#bbe1fa')
    book1_1.place(width=1000,height=600)
    root.title('Welcome : '+bk1[1])

    Label(book1_1,text='หน้า (1/2)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book1_1,image=img26,bg='#bbe1fa').place(x=250,y=50)
    Button(book1_1,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=b1_2).place(x=850,y=250)
    Button(book1_1,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=main).place(x=50,y=250)

def b1_2() :
    book1_1.destroy()
    global book1_2
    book1_2 = Frame(root,bg='#bbe1fa')
    book1_2.place(width=1000,height=600)
    root.title('Welcome : '+bk1[1])

    Label(book1_2,text='หน้า (2/2)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book1_2,image=img28,bg='#bbe1fa').place(x=250,y=50)
    Button(book1_2,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=main).place(x=850,y=250)
    Button(book1_2,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=b1_1).place(x=50,y=250)

def b2_1() :
    buy2.destroy()
    global book2_1
    book2_1 = Frame(root,bg='#bbe1fa')
    book2_1.place(width=1000,height=600)
    root.title('Welcome : '+bk2[1])

    Label(book2_1,text='หน้า (1/3)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book2_1,image=img30,bg='#bbe1fa').place(x=250,y=50)
    Button(book2_1,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=b2_2).place(x=850,y=250)
    Button(book2_1,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=main).place(x=50,y=250)
    
def b2_2() :
    global book2_2
    book2_2 = Frame(root,bg='#bbe1fa')
    book2_2.place(width=1000,height=600)
    root.title('Welcome : '+bk2[1])

    Label(book2_2,text='หน้า (2/3)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book2_2,image=img31,bg='#bbe1fa').place(x=250,y=50)
    Button(book2_2,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=b2_3).place(x=850,y=250)
    Button(book2_2,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=b2_1).place(x=50,y=250)

def b2_3() :
    global book2_3
    book2_3 = Frame(root,bg='#bbe1fa')
    book2_3.place(width=1000,height=600)
    root.title('Welcome : '+bk2[1])

    Label(book2_3,text='หน้า (3/3)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book2_3,image=img32,bg='#bbe1fa').place(x=250,y=50)
    Button(book2_3,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=main).place(x=850,y=250)
    Button(book2_3,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=b2_2).place(x=50,y=250)

def b3_1() :
    buy3.destroy()
    global book3_1
    book3_1 = Frame(root,bg='#bbe1fa')
    book3_1.place(width=1000,height=600)
    root.title('Welcome : '+bk3[1])

    Label(book3_1,text='หน้า (1/2)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book3_1,image=img33,bg='#bbe1fa').place(x=250,y=30)
    Button(book3_1,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=b3_2).place(x=850,y=250)
    Button(book3_1,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=main).place(x=50,y=250)
    
def b3_2() :
    global book3_2
    book3_2 = Frame(root,bg='#bbe1fa')
    book3_2.place(width=1000,height=600)
    root.title('Welcome : '+bk3[1])

    Label(book3_2,text='หน้า (2/2)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book3_2,image=img34,bg='#bbe1fa').place(x=250,y=30)
    Button(book3_2,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=main).place(x=850,y=250)
    Button(book3_2,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=b3_1).place(x=50,y=250) 

def b4_1() :
    global book4_1
    book4_1 = Frame(root,bg='#bbe1fa')
    book4_1.place(width=1000,height=600)
    root.title('Welcome : '+bk4[1])

    Label(book4_1,text='หน้า (1/2)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book4_1,image=img35,bg='#bbe1fa').place(x=250,y=30)
    Button(book4_1,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=b4_2).place(x=850,y=250)
    Button(book4_1,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=main).place(x=50,y=250)

def b4_2() :
    global book4_2
    book4_2 = Frame(root,bg='#bbe1fa')
    book4_2.place(width=1000,height=600)
    root.title('Welcome : '+bk4[1])

    Label(book4_2,text='หน้า (2/2)',bg='#bbe1fa',font="Garamond 18").pack()
    Label(book4_2,image=img36,bg='#bbe1fa').place(x=250,y=30)
    Button(book4_2,image=img27,font="Garamond 18",compound=RIGHT,bg='#bbe1fa',command=main).place(x=850,y=250)
    Button(book4_2,image=img29,font="Garamond 18",compound=LEFT,bg='#bbe1fa',command=b4_1).place(x=50,y=250)      


def log2 () :
    loginframe.destroy()
    global loginframe2
    loginframe2 = Frame(root,bg='#faf1e6')
    loginframe2.place(width=1000,height=600)
    root.title('Welcome : '+db[1]+" "+db[2])

    Label(loginframe2,image = img3,compound=CENTER,bg='#faf1e6').pack()
    #CUSTOMER_ID
    Label(loginframe2,text='CUSTOMER_ID : ',font="Garamond 18 bold",bg='#faf1e6',fg='black').place(x=350,y=180)
    StudentID = Label(loginframe2,text='',font="Garamond 18 bold",bg='#faf1e6',fg='black')
    StudentID.place(x=550,y=180)
    #name
    Label(loginframe2,text='Name : ',font="Garamond 18 bold",bg='#faf1e6',fg='black').place(x=350,y=250)
    Name = Label(loginframe2,text='',font="Garamond 18 bold",bg='#faf1e6',fg='black')
    Name.place(x=502,y=250)
    LastName = Label(loginframe2,text='',font="Garamond 18 bold",bg='#faf1e6',fg='black')
    LastName.place(x=620,y=250)
    #user
    Label(loginframe2,text='Username : ',font="Garamond 18 bold",bg='#faf1e6',fg='black').place(x=350,y=320)
    Username = Label(loginframe2,text='',font="Garamond 18 bold",bg='#faf1e6',fg='black')
    Username.place(x=502,y=320)
    #password
    Label(loginframe2,text='Password : ',font="Garamond 18 bold",bg='#faf1e6',fg='black').place(x=350,y=390)
    Pwd = Label(loginframe2,text='',font="Garamond 18 bold",bg='#faf1e6',fg='black')
    Pwd.place(x=502,y=390)
    #email
    Label(loginframe2,text='Email : ',font="Garamond 18 bold",bg='#faf1e6',fg='black').place(x=350,y=460)
    mail = Label(loginframe2,text='',font="Garamond 18 bold",bg='#faf1e6',fg='black')
    mail.place(x=502,y=460)

    if db != None :
        StudentID["text"] = db[0]
        Name['text'] = db[1]
        LastName['text'] = db[2]
        Username['text'] = db[3]
        Pwd['text'] = db[4]
        if db[5] == None :
            mail['text'] = ['-']
        else :
            mail['text'] = db[5]
    
    #button
    Button(loginframe2,image=img20,bd=3,command=main,bg='#faf1e6').place(y=20,x=40)
    Button(loginframe2,text='Log out',bg='lightgrey',fg='black',font="Garamond 18 bold",command=lambda:(loginlayout(root))).place(x=800,y=520)
    Button(loginframe2,text='Change Password',bg='lightgrey',font="Garamond 18 bold",fg='black',command=change).place(x=80,y=520)

def init_verify(root):
    winmain.destroy
    fm = Frame(root,bg='tan')
    fm.place(width=1000, height=600)
    Button(fm, borderwidth=0, image=img19, font=('Tahoma', 20, 'bold'), width=100, height=100, bg='tan', command=main).place(x=0, y=0)
    Label(root, text='Search', font=('Tahoma', 20, 'bold'), bg='tan').place(x=120, y=30)
    lblid : Label = None

    def search(keyword):
        conn = sqlite3.connect('db/data.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM ebook WHERE ID_BOOK = '{keyword}' ")
        ek = cursor.fetchone()
        conn.close()

        if ek :
            lblid['text'] = ek[0]
            lblbname['text'] = ek[1]
            lblprice['text'] = ek[2]
            lblaname['text'] = ek[3]
            lblpname['text'] = ek[4]
        
        else :
            lblid['text'] = ""
            lblbname['text'] = ""
            lblprice['text'] = ""
            lblaname['text'] = ""
            lblpname['text'] = ""

    str_keyword = StringVar()

    Label(root, text='ID_BOOK', font=('Tahoma', 18, 'bold'), bg='tan').place(x = 100, y= 120)
    Entry(root, borderwidth=0, width=25, font=('Tahoma', 18, 'bold'), textvariable=str_keyword).place(x=280, y=120)
    Button(root, text='Search', font=('Tahoma', 18, 'bold'), bg='tan', command=lambda:search(str_keyword.get())).place(x=700, y=110)

    Frame(root, width=800, height=2, bg='darkgoldenrod').place(x=0, y=180)

    Label(root, text='BOOK_ID :', font=('Tahoma', 18, 'bold'), bg='tan').place(x = 100, y= 220)
    Label(root, text='Name :', font=('Tahoma', 18, 'bold'), bg='tan').place(x = 100, y= 280)
    Label(root, text='Price :', font=('Tahoma', 18, 'bold'), bg='tan').place(x = 100, y= 340)
    Label(root, text='ผู้แต่ง :', font=('Tahoma', 18, 'bold'), bg='tan').place(x = 100, y= 400)
    Label(root, text='สำนักพิมพ์ :', font=('Tahoma', 18, 'bold'), bg='tan').place(x = 100, y= 460)

    lblid = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='tan')
    lblid.place(x = 300, y= 220)
    lblbname = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='tan')
    lblbname.place(x = 300, y= 280)
    lblprice = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='tan')
    lblprice.place(x = 300, y= 340)
    lblaname = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='tan')
    lblaname.place(x = 300, y= 400)
    lblpname = Label(root, text='', font=('Tahoma', 18, 'bold'), bg='tan')
    lblpname.place(x = 300, y= 460)

    return fm


def change() :
    global old,new,conf
    loginframe2.destroy
    changeframe = Frame(root,bg='#faf1e6')
    changeframe.place(width=1000,height=600)
    
    Label(changeframe,text='    Old Password :',font="Garamond 18 bold",bg='#faf1e6',image=img9,compound=LEFT).place(x=100,y=50)
    old = Entry(changeframe,width=20,show='*',font="Garamond 20 bold",textvariable = oldpwd)
    old.place(x=550,y=50)
    Label(changeframe,text='    New Password :',font="Garamond 18 bold",bg='#faf1e6',image=img9,compound=LEFT).place(x=100,y=150)
    new = Entry(changeframe,width=20,show='*',font="Garamond 20 bold",textvariable = newpass)
    new.place(x=550,y=150)
    Label(changeframe,text='    Comfirm New Password :',font="Garamond 18 bold",bg='#faf1e6',image=img9,compound=LEFT).place(x=100,y=250)
    conf = Entry(changeframe,width=20,show='*',font="Garamond 20 bold",textvariable = conpwd)
    conf.place(x=550,y=250)
    Button(changeframe,text='Confirm',bg='lightgrey',fg='black',font="Garamond 18 bold",command=comfirmpass).place(x=150,y=500)
    Button(changeframe,text='Cancel',bg='lightgrey',fg='black',font="Garamond 18 bold",command=log2).place(x=750,y=500)

def comfirmpass() :
    if oldpwd.get() == '' :
        messagebox.showwarning("Old Password: ","Please enter Old Password.")
        oldpwd.focus_force()
        return
    elif newpass.get() == '' :
        messagebox.showwarning("New Password : ","Please enter New Password.")
        newpass.focus_force()
        return
    elif conpwd.get() == "" :
        messagebox.showwarning("Comfirm Password : ","Please enter Comfirm Password.")
        conpwd.focus_force()
        return
    else :
        sql = "SELECT * FROM customer WHERE USERNAME = ? AND PASSWORD = ?"
        cursor.execute(sql,[userinfo.get(),oldpwd.get()])
        result = cursor.fetchone()
        if result :
            sql = "SELECT * FROM customer WHERE USERNAME = ? AND PASSWORD = ?"
            cursor.execute(sql,[userinfo.get(),oldpwd.get()])
            result = cursor.fetchone()
            if newpass.get() == conpwd.get() :
                cursor.execute('UPDATE customer SET [PASSWORD] = ? WHERE CUSTOMER_ID = ?',[newpass.get(), result[0]])
                conn.commit()
                messagebox.showinfo('Successfully : ', 'Your password has changed successfully')
                old.delete(0,END)
                new.delete(0,END)
                conf.delete(0,END)
                old.focus_force()
                new.focus_force()
                conf.focus_force()
            else:
                messagebox.showwarning('Mismatch Error :', 'The new password does not match the confirm password.')
                conf.delete(0,END)
                conf.focus_force()
        else:
            messagebox.showwarning('Old Password: ','Old password invalid')
            old.delete(0,END)
            old.focus_force()
   
def cancel():
    regisframe.destroy()
    loginlayout(root)

createconnection()
root = mainwindow()
regisframe = Frame(root)
userinfo = StringVar()
pwdinfo = StringVar()
userspy = StringVar()
searchitem = ["User Name","Password","First Name","Last Name"]

radiospy = IntVar()
btn = [Button() for i in searchitem]

img1 = PhotoImage(file='images/login.png').subsample(5,5)
img2 = PhotoImage(file='images/ning.png').subsample(5,5)
img3 = PhotoImage(file='images/profile.png').subsample(2)
img4 = PhotoImage(file='images/regis.png').subsample(9)
img5 = PhotoImage(file='images/id.png').subsample(18)
img6 = PhotoImage(file='images/ebook.png').subsample(7)
img7 = PhotoImage(file='images/text.png').subsample(20)
img8 = PhotoImage(file='images/user.png').subsample(18)
img9 = PhotoImage(file='images/lock.png').subsample(20)
img10 = PhotoImage(file='images/email.png').subsample(20)
img11 = PhotoImage(file='images/cart.png').subsample(18)
img12 = PhotoImage(file='images/regis2.png').subsample(4)
img13 = PhotoImage(file='images/b1.png').subsample(4)
img14 = PhotoImage(file='images/2.png').subsample(4)
img15 = PhotoImage(file='images/best.png').subsample(8)
img16 = PhotoImage(file='images/3.png').subsample(4)
img17 = PhotoImage(file='images/4.png').subsample(2)
img18 = PhotoImage(file='images/search.png')
img19 = PhotoImage(file='images/back.png').subsample(18)
img20 = PhotoImage(file='images/home.png').subsample(18)
img21 = PhotoImage(file='images/exit.png').subsample(20)
img22 = PhotoImage(file='images/b1.png').subsample(2)
img23 = PhotoImage(file='images/2.png').subsample(2)
img24 = PhotoImage(file='images/3.png').subsample(2)
img25 = PhotoImage(file='images/4.png').subsample(2)
img26 = PhotoImage(file='images/1-1.png').subsample(4)
img27 = PhotoImage(file='images/next.png').subsample(5)
img28 = PhotoImage(file='images/1-2.png').subsample(4)
img29 = PhotoImage(file='images/back.png').subsample(5)
img30 = PhotoImage(file='images/2-1.png').subsample(3)
img31 = PhotoImage(file='images/2-2.png').subsample(3)
img32 = PhotoImage(file='images/2-3.png').subsample(3)
img33 = PhotoImage(file='images/3-1.png').subsample(2)
img34 = PhotoImage(file='images/3-2.png').subsample(2)
img35 = PhotoImage(file='images/4-1.png').subsample(4)
img36 = PhotoImage(file='images/4-2.png').subsample(4)
img37 = PhotoImage(file='images/warning.png').subsample(28)
loginlayout(root)
popup = None
count = 0
fname = StringVar()
lname = StringVar()
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
eminfo = StringVar()
oldpwd = StringVar()
newpass = StringVar()
conpwd = StringVar() 

root.mainloop()
cursor.close()
conn.close()