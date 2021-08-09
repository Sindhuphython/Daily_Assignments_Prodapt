import pytz,csv,pandas,logging
from datetime import datetime
logging.basicConfig(filename = "Book_Entry_Details.log" ,level=logging.DEBUG)
headerContent=["Book_Title","Author","Description","Price","Publisher_Name","Time&Date"]
book_details=[ ]
class Book_store:
    def add_details(self,Book_title,Author,Description,Price,Publisher_Name,time):
        self.Book_title = Book_title
        self.Author = Author
        self.Description=Description
        self.Price=Price
        self.Publisher_Name = Publisher_Name
        self.time = time
        details = {"Book_Title":Book_title,"Author":Author,"Description":Description,"Price":Price,"Publisher_Name":Publisher_Name,"Time&Date":time}
        book_details.append(details)

    def timeDate(time_zone,td):        
        time_zone = pytz.timezone("Asia/kolkata")        
        td = (datetime.now(time_zone).strftime("%d-%h-%Y %H:%M:%S"))
        return td
BS = Book_store()
try:
    while(True):
        print("1.ADD BOOK DETAILS")
        print("2.VIEW ALL BOOKS")
        print("3.VIEW BOOKS IN ALPHABETICAL ORDER")
        print("4.SEARCH BOOK BY TITILE")
        print("5.EXIT")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Book_title = input("Enter Book Title: ")
            Author = input("Enter Author Name: ")
            Description = input("Enter Description: ")
            Price = int(input("Enter Book Price:Rs."))
            Publisher_Name = input("Enter Publisher Name: ")
            time = BS.timeDate("td")
            BS.add_details(Book_title,Author,Description,Price,Publisher_Name,time)
        if choice ==  2:
            with open('Book_Details.csv','w+',encoding='UTF8',newline='') as b:
                writer = csv.DictWriter(b,fieldnames=headerContent)
                writer.writeheader()
                writer.writerows(book_details)
            d = pandas.read_csv('Book_Details.csv')
            print(d)
        if choice == 3:
            dis = sorted(book_details,key= lambda i : i["Book_Title"])
            print(dis)
        if choice == 4:
            name = input("Enter Book Title to search: ")
            se = (list(filter(lambda j : j["Book_Title"]==name,book_details)))
            print(se)
        if choice == 5:
            logging.info("Program run successfully")
            break
except SyntaxError:
    print("Something went wrong")
finally:
    print("Thank you")
    
