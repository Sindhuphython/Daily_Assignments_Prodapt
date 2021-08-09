import re,time,sys

try:
    header=["bookname","discription","price","book_distributer","publisher","publisher_date","AddOn"]
    booklist=[]
    class BookDetails:
        def addbookdetails(self,bookname,discription,price,book_distributer,publisher,publisher_date):
            current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
            dict1={"bookname":bookname,"discription":discription,"price":price,"book_distributer":book_distributer,"publisher":publisher,"publisher_date":publisher_date,'AddOn':current_time}
            booklist.append(dict1)
    obj1=BookDetails()
    while(True):
        print("1.Add book :")
        print("2.View all book :")
        print("3.Search a book :")
        print("4.list all the book in alphabet order :")
        print("5.exit :")
        choice=int(input("Enter your choice:"))
        if choice==1:
            bookname=input("Enter the book name - ")
            discription=input("Enter the description of book - ")
            price=input("Enter price - ")
            book_distributer=input("Enter the book distributer name - ")
            publisher=input("Enter the publisher name -")
            publisher_date=input("Enter the published date - ")
            def val(price):
                v=re.search("^[1-9]",price)
                if v:
                    return int(price)
            obj1.addbookdetails(bookname,discription,val(price),book_distributer,publisher,publisher_date)
        if choice==2:
            print(booklist)
        if choice==3:
            S=input("Enter the book to search - ")
            print(list(filter(lambda i:i["bookname"]==S,booklist)))
        if choice==4:
            print("View all the book in alphabetic order - ")
            print(sorted(booklist,key=lambda i:i["bookname"],reverse=False))
            # booklist.sort(key=lambda x: x.split()[2][1],reverse=True)
        if choice ==5:
            sys.exit()

except Exception:
    print('something went wrong')
finally:
    print("Thank You!!")
