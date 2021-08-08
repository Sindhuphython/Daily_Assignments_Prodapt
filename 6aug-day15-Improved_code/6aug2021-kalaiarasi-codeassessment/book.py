import re
import csv
import logging
try:
    headercontent=["title","author","description","price","publishername"]
    booklist=[]
    def validation(author):
        a=re.search("^[A-Za-z]{2,25}$",author)
        if a:
            return True
        else:
            return False
    class bookdetail:

        def addbookdetail(self,title,author,description,price,publishername):
            
            dict1={"title":title,"author":author,"description":description,"price":price,"publishername":publishername}
            booklist.append(dict1)

    if(__name__=='__main__'):

        headercontent=["title","author","description","price","publishername"]
        booklist=[]
        obj1=bookdetail()
        while(True):
            print("1. add book")
            print("2. view all book")
            print("3. view all book title in alphabetic order")
            print("4. search a book using title")
            print("5. exit")
            choice=int(input("enter ur choice:"))
            
            if choice==1:
                title=input("enter the title:")
                author=input("enter author:")
                description=input("enter the description:")
                price=int(input("enter the price:"))
                publishername=input("enter the publishername:")
            
                x=validation(author)
                if x:
                    obj1.addbookdetail(title,author,description,price,publishername)
                else:
                    logging.error("please enter valid data!")
            if choice==2:
                print(booklist)
            
            if choice==3:
                x=sorted(booklist,key=lambda i:i["title"])
                print(x)
            if choice==4:
                tit=input("enter the title:")
                print(list(filter(lambda i:i["title"]==tit,booklist)))
            
            if choice==5:
                break

    
except:
    logging.error("please enter correct data")

