import re,logging,csv,datetime,time
header = ["title","author","description","price","distributor","publisher","AddOn"]
booklis=[]
class BookDetails:
    def AddBook(self,title,author,description,price,distributor,publisher):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"title":title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher,'AddOn':current_time}
        booklis.append(dict1)
k=BookDetails()

def valid_book(bookn,price):
    val=re.match("([a-z]+)([a-z]+)([a-z]+)$",bookn)
    val2=re.match("[0-9]{0,7}$",price)
    if val and val2:
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
          print("5.view in csv")
          print("6. exit")
          choice=int(input("Enter a choice: "))
          if choice==1:
             while(True):
                title=input("Enter title of book: ")
                price=input("Enter price of book: ")
                if valid_book(title,price):
                   author=input("Enter author of book: ")
                   description=input("Enter description of book: ")
                   distributor=input("Enter distributor of book: ")
                   publisher=input("Enter publisher of book: ")
                   k.AddBook(title,price,author,description,distributor,publisher)
                else:
                    print("Please enter correct infomation ")
                    continue
                break
                    
          if choice==2:
              print(booklis)
          if choice==3:
            print(sorted(booklis,key=lambda i:i["title"]))
          if choice==4:
            search1=input("Enter title to search product: ")
            print(list(filter(lambda x:x["title"]==search1,booklis)))
          if choice==5:
            with open('Bookk.csv','w+',encoding='UTF8',newline='') as b:
                writer = csv.DictWriter(b,fieldnames=header)
                writer.writeheader()
                writer.writerows(booklis)
          if choice==6:
               break
except:
    logging.error("Something went wrong")