import re,csv,logging
try:

    header=["btitle","author","description","price","distributer","publisher"]
    booklist=[]
    class BookDetails:
        def init(self,btitle,author,description,price,distributer,publisher):
            self.btitle=btitle
            self.author=author
            self.description=description
            self.price=price
            self.distributer=distributer
            self.publisher=publisher
        def addbookdetail(self,btitle,author,description,price,distributer,publisher):
            dict1={"btitle":btitle,"author":author,"description":description,"price":price,"distributer":distributer,"publisher":publisher} 
            booklist.append(dict1)
    def validate(btitle,author,description,price,distributer,publisher):
        valbtitle=re.search("[A-Z]{1}[^A-Z]{0,25}$",btitle)
        valauthor=re.search("[A-Z]{1}[A-Z]{0,25}$",author)
        valdescription=re.search("[A-Z]{1}[A-Z]{0,250}$",description)
        valprice=re.search("[0-9]{1,5}$",price)
        valdistributer=re.search("[A-Z]{1}[A-Z]{0,50}$",distributer)
        valpublisher=re.search("[A-Z]{1}[A-Z]{0,50}$",publisher)
        if valbtitle and valauthor and valdescription and valprice and valdistributer and valpublisher:
            return True
        else:
            return False
    obj=BookDetails()
    if(__name__=="__main__"):     
        while True:
            print("1.Add Book")
            print("2.View all books")
            print("3.View all books in alphabetical order")
            print("4.Search a book by Title")
            print("5.Exit") 
            choice=int(input("Enter your choice : "))
            if choice==1:
                btitle=input("Enter the Book title : ")
                author=input("Enter the Author name : ")
                description=input("Enter the descripton : ")
                price=input("Enter the price of the book : ")
                distributer=input("Enter the Distributer name : ")
                publisher=input("Enter the Publisher name : ")
                if validate(btitle,author,description,price,distributer,publisher)==True:
                    obj.addbookdetail(btitle,author,description,price,distributer,publisher)
                else:
                    logging.warning("VALIDATION ERROR !!!!")
                    break
            if choice==2:
                print(booklist)
            if choice==4:
                title=input("Enter the Book title to search : ")
                print(list(filter(lambda i:i["btitle"]==title,booklist)))
            if choice==3:  
                book=sorted(booklist,key=lambda x:x['btitle'])
                print(book)
            if choice==5:
                break
except:
    logging.error("Something went wrong")      
finally:
    print("THANK YOU")          