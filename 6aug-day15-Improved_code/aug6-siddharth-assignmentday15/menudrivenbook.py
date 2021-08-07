import re
import csv
import logging
import collections
logging.basicConfig(filename="booklog.log",level=logging.DEBUG)
booklist=[]

x=collections.deque(booklist)
bookeheadercontent=["title","author","description","price","distributor","publisher"]
class BookDetails:
    def AddBook(self,title,author,description,price,distributor,publisher):
        dict1={"title":title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher}
        x.append(dict1)
        return x
obj1=BookDetails()

def validation_book(title,price):
    val=re.match("([a-z]+)([a-z]+)([a-z]+)$",title)
    val2=re.match("^[0-9]{0,7}$",price)
    if val and val2:
        return True
    else:
        return False
    

while(True):
    print("1. add book ")
    print("2. view book ")
    print("3. sorted order of book on basis of title ")
    print("4. search book using title")
    print("5. save to file")
    print("6. exit")
    try:
        choice=int(input("Enter your choice: "))
        logging.info("User enterd correct choice")
    except ValueError:
        logging.error("something went wrong")
        continue
    if choice==1:
        while(True):
            
            title=input("Enter title of book: ")
            price=input("Enter price of book: ")
            if validation_book(title,price):
                author=input("Enter author of book: ")
                description=input("Enter description of book: ")
                #price=input("Enter price of book: ")
                distributor=input("Enter distributor of book: ")
                publisher=input("Enter publisher of book: ")
                obj1.AddBook(title,author,description,price,distributor,publisher)
            else:
                print("Please enter valid info ")
                continue
            break
    if choice==2:
        print(x)
    if choice==3:
        print(sorted(x,key=lambda i:i["title"]))
    if choice==4:
        searchmee=input("Enter title to search product: ")
        print(list(filter(lambda a:a["title"]==searchmee,x)))
    if choice==5:
        with open("student.csv","w+",encoding="UTF8",newline="") as s:
            writer=csv.DictWriter(s,fieldnames=bookeheadercontent)
            writer.writeheader()
            writer.writerows(x)
            logging.info("Saved to file")
    if choice==6:
        break