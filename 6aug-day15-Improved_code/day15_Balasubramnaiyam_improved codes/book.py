import re,logging

booklist=[]
class BookDetails:
    def AddBook(self,bookname,price,author,description,distributor,publisher):
        dict1={"bookname":bookname,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher}
        booklist.append(dict1)
        print(booklist)
obj1=BookDetails()

def valid_book(bookname,price,author,description):
    valname=re.match("([A-Za-z]{1,25})",bookname)
    valauthor=re.match("([A-Za-z]{1,25})",author)
    valdescription=re.match("([A-Za-z]{1,25})",description)
    valprice=re.match("([A-Za-z]{1,25})",price)
    if valname and valprice and valauthor and valdescription:
        return True
    else:
        return False

try:
    if __name__=="__main__":
        while(True):
            print("1. add book ")
            print("2. view book ")
            print("3. sorted order of book on basis of title ")
            print("4. search book using title")
            print("5. exit")
            choice=int(input("Enter a choice: "))
            if choice==1:
                bookname=input("Enter title of book: ")
                price=input("Enter price of book: ")
                author=input("Enter author of book: ")
                description=input("Enter description of book: ")
                distributor=input("Enter distributor of book: ")
                publisher=input("Enter publisher of book: ")
                if valid_book(bookname,price,author,description):
                    obj1.AddBook(bookname,price,author,description,distributor,publisher)
                else:
                    print("Please enter correct infomation ")
            
            if choice==2:
                print(booklist)
            if choice==3:
                print(sorted(booklist,key=lambda i:i["bookname"]))
            if choice==4:
                search1=input("Enter title to search product: ")
                print(list(filter(lambda x:x["bookname"]==search1,booklist)))
            if choice==5:
                break
except:
    logging.error("Something went wrong")