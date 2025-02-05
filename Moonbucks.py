import mysql.connector as sqlc

import tkinter

import random

import tabulate

from tkinter.font import Font

cart=[['S.no','Dish Name','Dish Price','Quantity','Total Amount']]

ch=0

def logcustomer():

        window=tkinter.Tk()

        window.title('Login')

        w=435

        h=175

        sw=window.winfo_screenwidth()

        sh=window.winfo_screenheight()

        x=(sw/2)-(w/2)

        y=(sh/2)-(h/2)

        window.geometry('%dx%d+%d+%d'%(w,h,x,y))

        window.config(bg='Black')

        window.resizable(height='false',width='false')

        def click1():

            global na

            global pas

            na=''+txt1.get()

            pas=''+txt2.get()

            window.destroy()

        fontm=Font(family='Helvetica',size=22)

        bt1=tkinter.Button(window,text='Enter',font=fontm,fg='Cyan',bg='Dark Blue',command=click1,width=23)

        label1=tkinter.Label(window,text='Enter username:',font=fontm,fg='Cyan',bg='Black')

        label2=tkinter.Label(window,text='Enter password:',font=fontm,fg='Cyan',bg='Black')

        label3=tkinter.Label(window,text='Customer Login',font=fontm,fg='Cyan',bg='Black')

        txt1=tkinter.Entry(window,font=fontm,width=13)

        txt2=tkinter.Entry(window,show='*',font=fontm,width=13)

        txt1.grid(column=2,row=1)

        txt2.grid(column=2,row=2)

        bt1.grid(columnspan=3)

        label3.grid(columnspan=3,row=0)

        label1.grid(column=1,row=1)

        label2.grid(column=1,row=2)

        window.attributes('-topmost',True)

        window.mainloop()

        flag=checkuser(na,"log",pas)

        return flag

def adminlog():

        while True:

                print('''

               Welcome to admin panel

        1.View customers

        2.View hotels

        B.Exit

''')

                ch=input('Enter your choice:')

                if ch=='1':

                        while True:

                                db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

                                cs=db.cursor()

                                cs.execute('''select * from customerl''')

                                a=cs.fetchall()

                                b=[['C.Id','Name','Password']]

                                a=list(a)

                                for i in a:

                                        i=list(i)

                                        b.append(i)

                                print(tabulate.tabulate(b,headers='firstrow',tablefmt='grid'))

                                print('''

E.Edit customer details

B.Back''')

                                cho=input('Enter your choice:')

                                print(cho)

                                if cho in ('E','e'):

                                        print(cho)

                                        while True:

                                                print('''

1.Edit Customer ID

2.Edit Name

3.Edit Password

B.Back''')

                                                choi=input('Enter your choice:')

                                                db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

                                                cs=db.cursor()

                                                if choi=='1':

                                                        b=int(input('Enter the C_ID of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new C_ID:'))

                                                        if len(str(a))==3:

                                                                pass

                                                        else:

                                                                print('invalid new C_ID...C_ID must be a 3 digit number')

                                                                break

                                                        cs.execute('''update customerl set c_id=(%s) where c_id=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='2':

                                                        b=int(input('Enter the C_ID of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Name:'))

                                                        cs.execute('''update customerl set cname=(%s) where c_id=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='3':

                                                        b=int(input('Enter the C_ID of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new password:'))

                                                        f=checkpass(a)

                                                        if f==1:

                                                                pass

                                                        else:

                                                                break

                                                        cs.execute('''update customerl set passwd=(%s) where c_id=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi in ('B','b'):

                                                        break

                                                else:

                                                        print('Invalid choice')

                                elif cho in ('B','b'):

                                        break

                                else:

                                        print('invalid choice')

                                 
                                 
                         
                elif ch=='2':

                        db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

                        cs=db.cursor()

                        cs.execute('''select * from restaurant''')

                        a=cs.fetchall()

                        b=[['S.no','Restaurant ID','Restaurant Name','Contact no.','Timings','Address','Ratings']]

                        a=list(a)

                        for i in a:

                                i=list(i)

                                i.pop(1)

                                b.append(i)

                        while True:

                                print(tabulate.tabulate(b,headers='firstrow',tablefmt='grid'))

                                print('''

E.Edit customer details

B.Back''')

                                cho=input('Enter your choice:')

                                if cho in ('E','e'):

                                        print(cho)

                                        while True:

                                                print('''

1.Edit Restaurant ID

2.Edit Name

3.Edit Contact no.

4.Edit Timings

5.Edit Address

6.Edit Ratings

B.Back''')

                                                choi=input('Enter your choice:')

                                                db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

                                                cs=db.cursor()

                                                if choi=='1':

                                                        b=int(input('Enter the S.no of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Restaurant_ID:'))

                                                        cs.execute('''update customerl set Restaurant_id=(%s) where S.no=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='2':

                                                        b=int(input('Enter the S.no of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Restaurant_name:'))

                                                        cs.execute('''update customerl set Restaurant_name=(%s) where S.no=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='3':

                                                        b=int(input('Enter the S.no of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Restaurant_contact:'))

                                                        cs.execute('''update customerl set Restaurant_contact=(%s) where S.no=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='4':

                                                        b=int(input('Enter the S.no of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Restaurant_Timings:'))

                                                        cs.execute('''update customerl set Restaurant_Timings=(%s) where S.no=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='3':

                                                        b=int(input('Enter the S.no of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Restaurant_address:'))

                                                        cs.execute('''update customerl set Restaurant_address=(%s) where S.no=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi=='3':

                                                        b=int(input('Enter the S.no of the customer whose details you want to edit'))

                                                        a=int(input('Enter the new Restaurant_rating:'))

                                                        cs.execute('''update customerl set Restaurant_rating=(%s) where S.no=(%s)''',(a,b))

                                                        db.commit()

                                                elif choi in ('B','b'):

                                                        break

                                                else:

                                                        print('Invalid choice')

                                elif cho in ('B','b'):

                                        break

                                else:

                                        print('invalid choice')

                elif ch in ('B','b'):

                        break

            
def admin():

   window=tkinter.Tk()

   window.title('')

   def click1():

      global ps

      ps=''+txt2.get()

      window.destroy()

   fontm=Font(family='Helvetica',size=22)

   bt1=tkinter.Button(window,text='Enter',font=fontm,fg='Cyan',bg='Dark Blue',command=click1,width=7)

   label1=tkinter.Label(window,text='Admin login',font=fontm,fg='Cyan',bg='Black')

   label2=tkinter.Label(window,text='Enter password:',font=fontm,fg='Cyan',bg='Black')

   txt1=tkinter.Entry(window,font=fontm,width=11)

   txt2=tkinter.Entry(window,show='*',font=fontm,width=11)

   txt2.grid(column=2,row=1)

   bt1.grid(columnspan=3)

   label1.grid(columnspan=3,row=0)

   label2.grid(column=1,row=1)

   w=400

   h=135

   sw=window.winfo_screenwidth()

   sh=window.winfo_screenheight()

   x=(sw/2)-(w/2)

   y=(sh/2)-(h/2)

   window.geometry('%dx%d+%d+%d'%(w,h,x,y))

   window.resizable(height='false',width='false')

   window.config(bg='Black')

   window.attributes('-topmost',True)

   window.mainloop()

   if ps=='degchan2002':

      adminlog()

   else:

      print('Wrong password....(:/)')


def checkuser(user,type,passw='abc'):

      db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

      cs=db.cursor()

      cs.execute('''select * from customerl''')

      a=cs.fetchall()

      for i in a:

         if user==i[1]and type=="check":

            print("user already exist.try again")

            return 0

         if user==i[1]and passw==i[2] and type=="log":

            print('''

================================================================================

''',end='')

            print('Logged in successfully...')

            return 0

         else:

            print("user does not exist")

            return 1


def checkpass(pw):

       uc=False

       lc=False

       num=False

       sp=False

       if len(pw)<6:

           print("password to short.try again")

           return 0

       for a in pw:

           if a.islower():

               lc=True

           if a.isupper():

               uc=True

           if a.isdigit():

               num=True

           if a.isspace():

               print("password should not have a space.")

               return 0

           if a in'''~'!@#$%^&*()-_+={}[]|\:;"><,./?''':

               sp=True

       if lc and uc  and num and sp:

          return 1

       else:

          print("invalid password.try again")

          return 0


def adduser():

      note='''

 Note:Passwords must must be at least 6 characters in length

 and should contain a  minimum of 1 lower case letter[a,z],

 1 upper case letter[a,z],1 numeric character[0,9]and

 1 special character'''

      db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

      cs=db.cursor()

      while True:

         window=tkinter.Tk()

         window.title('Login')

         w=435

         h=175

         sw=window.winfo_screenwidth()

         sh=window.winfo_screenheight()

         x=(sw/2)-(w/2)

         y=(sh/2)-(h/2)

         window.geometry('%dx%d+%d+%d'%(w,h,x,y))

         window.config(bg='Black')

         window.resizable(height='false',width='false')

         def click1():

             global na

             global pas

             na=''+txt1.get()

             pas=''+txt2.get()

             window.destroy()

         fontm=Font(family='Helvetica',size=22)

         bt1=tkinter.Button(window,text='Enter',font=fontm,fg='Cyan',bg='Dark Blue',command=click1,width=23)

         label1=tkinter.Label(window,text='Enter username:',font=fontm,fg='Cyan',bg='Black')

         label2=tkinter.Label(window,text='Enter password:',font=fontm,fg='Cyan',bg='Black')

         label3=tkinter.Label(window,text='Customer Signin',font=fontm,fg='Cyan',bg='Black')

         txt1=tkinter.Entry(window,font=fontm,width=13)

         txt2=tkinter.Entry(window,show='*',font=fontm,width=13)

         txt1.grid(column=2,row=1)

         txt2.grid(column=2,row=2)

         bt1.grid(columnspan=3)

         label3.grid(columnspan=3,row=0)

         label1.grid(column=1,row=1)

         label2.grid(column=1,row=2)

         window.attributes('-topmost',True)

         window.mainloop()

         flag=checkuser(na,"check",pas)

         if flag==0:

                continue

         while True:

             s=checkpass(pas)

             if s==0:

                   print('0')

                   continue

             else:

                print("valid password")

                ci=random.randrange(100,1000)

                cs.execute('''select * from customerl''')

                s=cs.fetchall()

                for i in s:

                   while i==ci:

                      ci=random.randrange(100,1000)

                cs.execute('''insert into customerl values(%s,%s,%s)''',(ci,na,pas))

                db.commit()

                print('New Customer added')

                hotel()

def viewcart():

    print(tabulate.tabulate(cart,headers='firstrow',tablefmt='grid'))

    cart.remove(cart[0])

    su=0

    for i in cart:

        su=su+i[4]

    print('Grand total:',su)

    print('P.Confirm and Pay order')

    print('B.Back')

    ch=input('Enter your choice:')

    if ch=='b' or ch=='B':

        pass

    elif ch=='p' or ch=='P':

        print('Total:',su)

        print('Enter your username and password to make payment')

        flag=logcustomer()

        if flag==0:

            print('Order payment successful...')

            print('Enjoy your order')

            return

def customerm():

    global cart

    cart=[['S.no','Dish Name','Dish Price','Quantity','Total Amount']]

    while True:

        print('         WELCOME',na,)

        print('''

        1.Buy food

        2.View cart

        3.Logout''')

        ch=int(input('Enter your choice:'))

        if ch==1:

            hotel()

        elif ch==2:

            viewcart()

        elif ch==3:

            return

def customer():

    while True:

       print('''

|           Customer login                                                     |

|           ======== =====                                                     |

|           1.Sign in                                                          |

|           2.Login                                                            |

|           B.Back                                                             |

''',end='')

       choice=input('enter your choice:')

       if choice=='1':

          adduser()

       elif choice=='2':

          fl=logcustomer()

          if fl==0:

              customerm()

       elif choice in ('B','b'):

          break

       else:

          print("invalid choice,try again")

def hotel_menu():

    global ch

    db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

    cs=db.cursor()

    hotel={'7':'anjappar_chettinadu_restaurant_menu','8':'dindigul_thalapakatti_biriyani_menu','4':'dominos_menu','3':'meat_and_eat_menu','1':'smokey_station_menu','2':'sri_maheswari_lunch_home_menu','6':'srinivasa_sweets_and_restaurant_menu','5':'ss_hyderabad_biriyani_menu','10':'sss_all_dishes_menu','9':'tovo_menu'}

    h=hotel.get(ch)

    cs.execute("select * from (%s)"%(h,))

    a=cs.fetchall()

    b=[['S.no','Dish Name','Dish Price']]

    for i in a:

        i=list(i)

        b.append(i)

    while True:

        print(tabulate.tabulate(b,headers='firstrow',tablefmt='grid'))

        print('C.View cart')

        print('B.Back')

        ch=input('Enter your choice:')

        if ch=='c' or ch=='C':

            viewcart()

        elif ch=='b' or ch=='B':

            return

        else:

            cs.execute('''select * from %s where S_no=%s'''%(h,int(ch),))

            a=cs.fetchall()

            a=list(a[0])

            num=int(input('Enter the quantity:'))

            a.append(num)

            a.append(a[2]*num)

            f=0

            for i in cart:

                if i[1]==a[1]:

                        i[3]=i[3]+a[3]

                        i[4]=i[4]+a[4]

                        f=1

            if f==0:

                cart.append(a)

            print(num,a[1],'Added to cart')

def hotel():

    global cart

    global ch

    while True:

        db=sqlc.connect(user='root',passwd='aptkmns2006',database='Moonbucks')

        cs=db.cursor()

        cs.execute('''select * from restaurant''')

        a=cs.fetchall()

        b=[['S.no','Restaurant ID','Restaurant Name','Contact no.','Timings','Address','Ratings']]

        a=list(a)

        for i in a:

            i=list(i)

            i.pop(1)

            b.append(i)

        while True:

            print(tabulate.tabulate(b,headers='firstrow',tablefmt='grid'))

            print('B.Back')

          
