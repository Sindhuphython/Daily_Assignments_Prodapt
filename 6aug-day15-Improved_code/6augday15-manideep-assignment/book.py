import re,logging
import csv

    
try:
    Booklist=[]
    class Books:
            def addbooksdetails(self,title,description,price,publisher,distributor):
                dict1={'title':title,'description':description,'price':price,'publisher':publisher,'distributor':distributor}
                Booklist.append(dict1)

            
    obj1=Books()
    def validate(bookname,price):
            valbookname=re.search("[A-Z]{1}[^A-Z]{0,25}$",title)
            valprice=re.search("[0-9]{0,7}$",price)
            if valbookname and valprice:
                return True
            else:
                return False
    while(True):
            print("1.Add book details:")
            print("2.view all Books:")
            print("3.view all books in alphabetical order by sorting ttle:")
            print("4.search a book by using title using filter function:")
            print("5.exit")
            choice=int(input("enter your choice"))
            if choice==1:
                while(True):
                    title=input("enter the Book Title:")
                    price=input("enter price :")
                    if validate(title,price):
                        description=input("enter description:")
                        publisher=input("enter a publisher name:")
                        distributor=input("enter the distributor name:")
                        obj1.addbooksdetails(title,description,price,publisher,distributor)
                    else:
                        print("Please  entered valid title and price")
                        continue
                    break
            if choice==2:
                print(Booklist)
            if choice==3:
                print(sorted(Booklist,key=lambda i:i['title']))
            if choice==4:

                title=input("enter your book title to search:")
                print(list(filter(lambda i:i["title"]==title,Booklist)))
            
            if choice==5:
                break
except:
    logging.error("opps!something went wrong")
finally:
    print("thanks")

