import logging,re
try:
    booklist=[]
    logging.basicConfig(filename='books.log',level=logging.DEBUG)
    class Book_Details:
        def add_Book(self,book_title,description,price,publisher,distributor):
            dict={"book_title":book_title,"description":description,"price":price,"publisher":publisher,"distributor":distributor}
            booklist.append(dict)
    obj=Book_Details()

    def validate(vbook_title,vdescription,vprice):
        book_title1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vbook_title)
        print(book_title1)
        description1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vdescription)
        print(description1)
        price1=re.match("[0-9]{0,7}$",vprice)
        print(price1)
        if book_title1 and description1 and price1:
            return True
        else:
            return False

    while(1):
        print("1.Add Book")
        print("2.View all Book")
        print("3.View the Order")
        print("4.Search a Book Based on Title")
        print("5.Exit")
        option=int(input("Enter your option :"))
        if __name__== "__main__":
            if option==1:
                vbook_title=input("Enter the Book Name:")
                vdescription=input("Enter the Book Description:")
                vprice=input("Enter the Book Price:")
                publisher=input("Enter the Book Publisher:")
                distributor=input("Enter the Book Distributor:")
                if validate(vbook_title,vdescription,vprice):
                    obj.add_Book(vbook_title,vdescription,vprice,publisher,distributor)
                else:
                    logging.error("Check your Book name, description and price")

            if option==2:
                print(booklist)

            if option==3:
                print(sorted(booklist,key=lambda i:i["book_title"]))
                logging.info("Successfully!!!View the Alphabetical Order")
            
            if option==4:
                sname=input("Ënter the Book Name to Search:")
                print(list(filter(lambda i:i["book_title"]==sname,booklist)))
                logging.info("Successfully!!! Search the Book Details")
            
            if option==5:
                break

except ValueError:
    logging.error("Please Check Value int or string")

except IndexError:
    logging.error("Please Check Your Index")

except Exception:
    logging.error("Something Went Wrong")

finally:
    print("Äll Block Completed Successfully")