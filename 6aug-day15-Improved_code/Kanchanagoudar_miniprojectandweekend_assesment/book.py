import csv
import re
import json,logging
try:
    booklist=[]
    headerContent=["book_title","author","description","price","distributor","publisher"]
    class BookDetails:
        def _init_(self,book_title,author,description,price,distributor,publisher):
            self.book_title=''
            self.author_title=''
            self.description=''
            self=distributor=''
            self.publisher=''
        def addbookdetail(self,book_title,author,description,price,distributor,publisher):
            dict1={"book_title":book_title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher}
            booklist.append(dict1)
            
    def validate(author,distributor,publisher): 
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",author)  
        valdistributor=re.search("[A-Z]{1}[^A-Z]{0,25}$",distributor)  
        valpublisher=re.search("[A-Z]{1}[^A-Z]{0,25}$",publisher)  
        if valname and valdistributor and valpublisher:
            return True
        else:
            return False

    ordered_list=[]
    obj=BookDetails() 
    if(__name__=="__main__"):       
        while True:
            print("1.add book details")
            print("2.view all book")
            print("3.search a book")
            print("4.view all bokks in alphanumerical order")
            print("5 to store data csv in file")
            print("6 to store data json in file")
            print("7.exit") 
            choice=int(input("Enter your choice : "))
            if choice==1:
                book_title=input("Enter the book_title : ")
                author=input("Enter the author : ")
                description=input("Enter the description : ")
                price=int(input("Enter the price:"))
                distributor=input("Enter the distributor : ")
                publisher=input("Enter the publisher : ")
                a=validate(author,distributor,publisher)
                if a:
                    obj.addbookdetail(book_title,author,description,price,distributor,publisher)
                else:
                    logging.error("invalid data enter a valid data")
            if choice==2:
                print(json.dumps(booklist))
            if choice==3:
                name=input("Enter the booktitle to search : ")
                print(list(filter(lambda i:i["book_title"]==name,booklist)))
            if choice==4:
                orderd_list=sorted(booklist,key=lambda i:i["book_title"])
                print(orderd_list)
            if choice==5:
                with open("book.csv","w+",encoding="UTF8",newline='')as s:
                    writer=csv.DictWriter(s,fieldnames=headerContent)
                    writer.writeheader()
                    writer.writerows(booklist)
            if choice==6:
                myjson=json.dumps(booklist) 
                with open("book.json","w+",encoding="utf-8")as s:
                    s.write(myjson)
            if choice==8:
                break
except:
    logging.error("unable to process")

