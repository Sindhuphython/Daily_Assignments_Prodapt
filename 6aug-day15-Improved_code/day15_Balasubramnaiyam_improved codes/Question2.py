import re,smtplib
def validate(name,demaild):
    valname=re.search("^(Mr\.|Mrs\.|Ms\.)[A-Z]{1}[^A-Z]{0,25}$",name)
    valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",demaild)
    if valname and valemail:
        return True
    else:
        return False
menu=["Tea","Coffee","MasalaDosa"]
menudict=dict.fromkeys(menu,0)
try:
    class Hotel():
        def addtea(self):
            teacount=int(input("Enter the how many teas want :"))
            menudict['Tea']=menudict['Tea']+teacount
        def addcoffee(self):
            coffeecount=int(input("Enter the how many Coffee want :"))
            menudict['Coffee']=menudict['Coffee']+coffeecount
        def addmasaladosa(self):
            Masalacount=int(input("Enter the how many Masaladosa want :"))
            menudict['MasalaDosa']=menudict['MasalaDosa']+Masalacount
    obj1=Hotel()
    name=input("Enter your name :")
    demailid=input("Enter your Email id: ")
    print(validate(name,demailid))
    if validate(name,demailid)==True:
        while(True):
            print("Enter Your option: ")
            print("1)  Tea(Rs.7)")
            print("2)  Coffee(Rs.10)")
            print("3)  Masala Dosa(Rs.50)")
            print("4)  View Bill and Email")
            option=int(input())
            if option==1:
                obj1.addtea()
            elif option==2:
                obj1.addcoffee()
            elif option==3:
                obj1.addmasaladosa()
            elif option==4:
                break
            else:
                print("Enter The Correct option: ")
        print(menudict)
        message="Hi  "+ name+ "Your bill  "+"\nDish       Quantity       Price\n"
        #print("Dish       Quantity       Price")
        print(menudict["Tea"])
        if menudict['Tea']>0:
            message=message+'Tea          '+str(menudict['Tea'])+'             '+str(7*menudict['Tea'])+'Rs\n'
        if menudict['Coffee']>0:
            message=message+'Coffee       '+str(menudict['Coffee'])+'             '+str(10*menudict['Coffee'])+'Rs\n'
        if menudict['MasalaDosa']>0:
            message=message+'MasalaDosa   '+str(menudict['MasalaDosa'])+'             '+str(50*menudict['MasalaDosa'])+'Rs\n'
        message = message+'Total price                '+str(7*menudict['Tea']+10*menudict['Coffee']+50*menudict['MasalaDosa'])+'Rs\n'
        print(message)
        
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("balu08062000@gmail.com","balu@123")
        connection.sendmail("balu08062000@gmail.com",demailid,message)
        connection.quit
        print("Mail sent")
except:
    print("SomeThing went Wrong please check it")