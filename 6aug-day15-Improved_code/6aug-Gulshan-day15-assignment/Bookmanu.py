import re,sys,csv,operator
from datetime import datetime
import time
try:
    header = ["Bookname","discription","price","distributor","Publiser","Date_of_Publising","AddOn"]
    Booklist=[]
    class BookDetails:
        def addbookdetails(self,Bookname,discription,price,distributor,Publiser,Date_of_Publising):
            current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
            dict1={"Bookname":Bookname,"discription":discription,"price":price,"distributor":distributor,"Publiser":Publiser,"Date_of_Publising":Date_of_Publising,'AddOn':current_time}
            Booklist.append(dict1)
    obj1=BookDetails()
    def val(price):
        v=re.search("^[1-9]",price)
        if v:
            return int(price)
    while(True):
        # Bookname,Discription,price,Bookdistributer,Publiser,Date_of_Publising 
        print("1.Add Book")
        print("2.View all Book")
        print("3.Search a Book")
        print("4.list all the Book in sorted order")
        print("5.For CSV file")
        print("6.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            Bookname=input("enter the Book name - ")
            discription=input("enter the description of Book - ")
            price=input("enter the price - ")
            distributor=input("enter the distributor name - ")
            Publiser=input("enter the Publiser name - ")
            Date_of_Publising=input("enter date in mm-dd-yyyy format -")
            obj1.addbookdetails(Bookname,discription,val(price),distributor,Publiser,Date_of_Publising)
        if choice==2:
            print(Booklist)
        if choice==3:
            S=input("enter the book that you want to search - ")
            print(list(filter(lambda i:i["Bookname"]==S,Booklist)))
        if choice==4:
            print("list all the book that - ")
            Booklist.sort(key=operator.itemgetter('Bookname'))
            print(Booklist)
        if choice == 5:
            with open('Book.csv','w+',encoding='UTF8',newline='') as s:
                writer = csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(Booklist)
        if choice==6:
            sys.exit()
except Exception:
    print('something went wrong')
finally:
    print("Thank You!!")