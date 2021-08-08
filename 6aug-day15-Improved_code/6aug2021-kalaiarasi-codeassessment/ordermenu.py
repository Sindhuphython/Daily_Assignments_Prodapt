import logging
import re
try:
    def validation(emailid):
        e=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",emailid)
        
        if e:
            return True
        else:
            return False

    class menu:
        def tea(self,a):
            return a*7
        def coffee(self,b):
            return b*10
        def masaladosa(self,s):
            return s*50
    c=menu()
    bill=0
    while(True):
        print("select an option:")
        print("\n")
        print("1.tea            - RS:7")
        print("2.coffee         -RS:10")
        print("3.masaladosa     -RS:50")
        print("4.View Bill and Email")
        choice=int(input("enter ur choice:"))
        
        if choice==1:
            print("tea selected")
            a=int(input("enter count of tea:"))
            ans=c.tea(a)
            bill=bill+ans

        if choice==2:
            print("coffee selected")
            b=int(input("enter count of coffee:"))
            ans=c.coffee(b)
            bill=bill+ans
        if choice==3:
            print("masala dosa selected")
            s=int(input("enter count of masaladosa:"))
            ans=c.masaladosa(s)
            bill=bill+ans
        if choice==4:
            emailid=input("enter your mailid:")
            if validation(emailid):

                message="the total amount for your order is " + str(bill)
                print(bill)
                print("email send")
            else:
                logging.error("please enter valid emailid")
            break

    
    import smtplib
    connection =smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("kalai.iprimed@gmail.com","Kalai@2404")
    connection.sendmail("kalai.iprimed@gmail.com",emailid,message)
    connection.quit()

except:
    logging.error("please enter correct data")
