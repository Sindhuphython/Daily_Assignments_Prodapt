import logging  
try:   
    Books=[]
    class BookDetails:
    
        def addbookdetail(self,title,description,price,publisher):
            dict1={"title":title,"description":description,"price":price,"publisher":publisher}
            Books.append(dict1)
    obj1=BookDetails()        
    while(True):
        print("1.add Book:")
        print("2.display books like API:")
        print("3.sort all the books in an alphabetical order:")
        print("4.search book using title:")
        print("5.exit")
        choice =int(input("enter the choice:"))
        if choice==1:
            title=input("enter the title:")
            description=input("enter description:")
            price=int(input("enter price:"))
            publisher=input("enter publisher:")
            obj1.addbookdetail(title,description,price,publisher)
        if choice==2:
            print(Books)

        if choice==3:
            titles=list(map(lambda x:x['title'],Books))
            titles.sort()
            print(titles)

          
        if choice==4:
            btitle=input("enter the book title:")
            print(list(filter(lambda i:i["title"]==btitle,Books)))

        if choice==5:
            break
except:
    logging.error("wrong ")        