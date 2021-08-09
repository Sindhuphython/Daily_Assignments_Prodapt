import re,logging
try:
    bookdetails=[]
    def validate(btitle,author,description,distributorname,publisher):
        btit=re.search("^[a-zA-Z]{0,25}$",btitle)
        bau=re.search("^[a-zA-Z]{0,25}$",btitle)
        bdes=re.search("^[a-zA-Z]{0,25}$",btitle)
        bdis=re.search("^[a-zA-Z]{0,25}$",btitle)
        bpub=re.search("^[a-zA-Z]{0,25}$",btitle)
        if btit and bau and bdes and bdis and bpub:
            return True
        else:
            return False
    class book:
        def addbook(self,btitle,author,description,price,distributorname,publisher):
            bdict={"btitle":btitle,"author":author,"description":description,"price":price,"distributorname":distributorname,"publisher":publisher}
            bookdetails.append(bdict)
    obj=book()
    while(True):
        print("1.Add book details")
        print("2.View all books")
        print("3.View all books in alphabetical order")
        print("4.Search a book by using title")
        print("5.exit")
        choice=int(input("Enter your choice"))
        if choice==1:
            btitle=input("Enter the book title")
            author=input("Enter the author name")
            description=input("Enter the description of the book")
            price=int(input("Enter the price of the book"))
            distributorname=input("Enter the distributor name")
            publisher=input("Enter the publisher name")
            x=validate(btitle,author,description,distributorname,publisher)
            if x:
                obj.addbook(btitle,author,description,price,distributorname,publisher)
            else:
                logging.error("enter valid details")
        if choice==2:
            print(bookdetails)
        if choice==3:
            print(sorted(bookdetails,key=lambda i:i["btitle"],reverse=False))
        if choice==4:
            booktitle=input("Enter the title of the book to search")
            print(list(filter(lambda i:i["btitle"]==booktitle,bookdetails))) 
        if choice==5:
            break
except:
    logging.error("Enter valid details")