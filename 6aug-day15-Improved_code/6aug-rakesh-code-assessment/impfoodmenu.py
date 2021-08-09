import re,smtplib,logging
try:
    total_cost=0
    tea=7
    Coffee=10
    Masala_Dosa=50
    if(__name__=="__main__"):
        while True:
            print("Food menu of the restaurant")
            print("1.TEA")
            print("2.COFFEE")
            print("3.MASALA DOSA")
            print("4.VIEW BILL AND COST")
            print("5.EXIT")
            select=int(input("PLACE YOUR ORDER : "))
            if select==1:
                print("TEA : 7rs")
                total_cost=total_cost+tea
            elif select==2:
                print("COFFEE : 10rs")
                total_cost=total_cost+Coffee
            elif select==3:
                print("MASALA DOSA : 50rs")
                total_cost=total_cost+Masala_Dosa
            elif select==4:
                print("TOTAL COST :",total_cost)
                msg="Dear customer your total cost = " + str(total_cost) + "rs\nThank you! \nVISIT AGAIN. "
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("rakesh.learning.python@gmail.com","9008496668Ra@")
                connection.sendmail("rakesh.learning.python@gmail.com","90084raky@gmail.com",msg)
                print("EMAIL SENT")
                connection.quit()
                break

            else:
                print("Enter correct option")
except:
    logging.warning("OOPS!!! Something went wrong")
finally:
    print("Thank you!! Visit again")            
