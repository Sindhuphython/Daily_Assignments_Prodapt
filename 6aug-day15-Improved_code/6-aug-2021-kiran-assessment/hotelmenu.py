import re
import smtplib
try:
    def validate(name,mail):
        val1=re.search("^[A-Z][a-z]{2.20}$",name)
        val2=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",mail)
        if val1 and val2:
            return True
        else:
            return False

    Totalamount=0
    while(True):
        print("show Menu")
        print("1. Tea                   -Rs.7")
        print("2. Coffee                -Rs.10")
        print("3. Masala Dosa            -Rs.50")
        print("4. View bill and Email")
        choice=int(input("Enter your choise:"))
        if choice==1:
            Totalamount=Totalamount+7
        elif choice==2:
            Totalamount=Totalamount+10
        elif choice==3:
            Totalamount=Totalamount+50
        elif choice==4:
            break
    print(Totalamount)


    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("969kiran969@gmail.com","Kiran@969")
    message="dear customer your total bill "+str(Totalamount)
    connection.sendmail("969kiran969@gmail.com","rachapallikirankumar969@gmail.com",message)
    print("email sent successfully")
    connection.quit()
except:
    print("please check the details")
else:
    print("Details are correct")
finally:
    print("completed")
