import re, csv, logging

logging.basicConfig(filename="booklog.log",level=logging.DEBUG)
booklist=[]

bookeheadcontent=["title","author","description","price","distributor","publisher"]

################ class book ###############
class BookD:
    def AddBook(self,title,author,description,price,distributor,publisher):
        dict1={"title":title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher}
        booklist.append(dict1)
book=BookD()   ############## object of classs

############# validation function ###########
def validation_of_book(bookname,price):
    valid=re.match("([a-z]+)([a-z]+)(\s)([a-z]+)$",bookname)
    valid2=re.match("^[0-9]{0,7}$",price)
    try:
        if valid and valid2:
            return True
        else:
            return False
    except:
        logging.error("Validation not working")

############# menu driven program ################

while(True):
    print("1. Add book ")
    print("2. View book ")
    print("3. Sorted order of book on basis of title ")
    print("4. Search book using title")
    print("5. Save to CSV file")
    print("6. exit")
    try:
        choice=int(input("Enter your choice: "))
        logging.info("User entered correct choice")
    except ValueError:
        logging.error("CHOICE NOT CORRECT")
        continue
    if choice==1:
        while(True):
            
            title=input("Enter title of book: ")
            price=input("Enter price of book: ")
            if validation_of_book(title,price):
                author=input("Enter author of book: ")
                description=input("Enter description of book: ")
                distributor=input("Enter distributor of book: ")
                publisher=input("Enter publisher of book: ")
                book.AddBook(title,author,description,price,distributor,publisher)
            else:
                print("Please enter valid information about the book ")
                continue
            break
    if choice==2:
        print(booklist)
    if choice==3:
        print(sorted(booklist,key=lambda i:i["title"]))
    if choice==4:
        searchbook=input("Enter title to search product: ")
        print(list(filter(lambda i:i["title"]==searchbook,booklist)))
    if choice==5:
        with open("books.csv","w+",encoding="UTF8",newline="") as s:
            writer=csv.DictWriter(s,fieldnames=bookeheadcontent)
            writer.writeheader()
            writer.writerows(booklist)
            logging.info("Changes are Saved to the file")
    if choice==6:
        break