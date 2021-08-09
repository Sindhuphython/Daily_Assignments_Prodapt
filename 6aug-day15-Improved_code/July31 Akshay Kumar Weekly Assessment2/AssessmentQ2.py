import re,smtplib,logging
logging.basicConfig(filename='restaurant.log',level=logging.DEBUG)

class Tea:
        def tea_price(self):
            self.tea_p=7
            return self.tea_p

class Coffee:
    def coffee_price(self):
        self.coffe_p=10 
        return self.coffe_p
        
class Masala_Dosa:
    def dosa_price(self):
        self.dosa_p=50
        return self.dosa_p


class Order(Coffee,Tea,Masala_Dosa):
    pass
bill=Order()
cost=0
try:
    if __name__ == "__main__":
        while(True):
            Name=input("Please Enter your Name :")
            Email=input("Please Enter the Email Id :")
            regex = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
            val=re.match(regex,Email)
            if val:
                while(True):

                    print("\n Select an option from menu ")
                    print("1.Tea (Rs.7)")
                    print("2.Coffee (Rs.10)")
                    print("3.Masala Dosa (Rs.50)")
                    print("4.View Bill and send mail to user")
                    try:
                        choice=int(input("Enter your choice: "))
                    except ValueError:
                        logging.error("User pressed wrong input")
                        
                    if choice==1:
                        print("\nTea selected")
                        tea1=bill.tea_price()
                        cost+=tea1
                                

                    if choice==2:
                        print("\nCoffee selected")
                        coffee1=bill.coffee_price()
                        cost+=coffee1
                        

                    if choice==3:
                        print("\nMasala Dosa Selected")
                        mdosa1=bill.dosa_price()
                        cost+=mdosa1
                            
                    if choice==4:
                        print(f'Your Bill is {cost}')
                        message=str(f'Hi {Name}, Total amount of your order is {cost}')
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("sureshbannur6@gmail.com","aks.1513")
                        connection.sendmail("sureshbannur6@gmail.com",Email,message)

                        print("Email for your Bill has successfully send")
                        logging.info("Transaction Successful")
                        connection.quit()
                        break
                break
except Exception:
    print("Something went wrong. Please try again")

finally:
    print("Thank You!!")
