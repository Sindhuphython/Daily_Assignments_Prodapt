import re,csv

book_list=[]
bookeheadercontent=["title","author","description","price","distributor","publisher"]
class BookDetails:
    def AddBook(self,title,author,description,price,distributor,publisher):
        dict1={"title":title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher}
        book_list.append(dict1)
obj=BookDetails()

def validation(book,price):
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",book)
    val2=re.match("^[0-9]{0,7}$",price)
    if val1 and val2:
        return True
    else:
        return False

while(True):
    print("1. add books ")
    print("2. view all books ")
    print("3. view books on basis of title with alphabetic order ")
    print("4. search book using title")
    print("5. save to file")
    print("6. exit")
    choice=int(input("Enter a choice: "))
    if choice==1:
        while(True):
            
            title=input("Enter title of book: ")
            price=input("Enter price of book: ")
            if validation(title,price):
                author=input("Enter author of book: ")
                description=input("Enter description of book: ")
                distributor=input("Enter distributor of book: ")
                publisher=input("Enter publisher of book: ")
                obj.AddBook(title,author,description,price,distributor,publisher)
            else:
                print("Please enter valid info ")
                continue
            break
    if choice==2:
        print(book_list)
    if choice==3:
        print(sorted(book_list,key=lambda i:i["title"]))
    if choice==4:
        search=input("Enter title to search product: ")
        print(list(filter(lambda a:a["title"]==search,book_list)))
    if choice==5:
        with open("student.csv","w+",encoding="UTF8",newline="") as s:
            writer=csv.DictWriter(s,fieldnames=bookeheadercontent)
            writer.writeheader()
            writer.writerows(book_list)
    if choice==6:
        break