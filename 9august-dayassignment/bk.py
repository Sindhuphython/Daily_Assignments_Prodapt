import re, logging, time

booklist = []
dict1 = {}
try:
    def validate(title, author, description, price, distrubutor, publisher):
        valtitle = re.search("[a-z]{1}[^a-z]{0,25}$", dict1["title"])
        valauthor = re.search("[a-z]{1}[^a-z]{0,25}$", dict1["author"])
        valdescription1 = re.match("[a-z]{1}[^a-z]{0,25}$", dict1["description"])
        valprice = re.match("[0-9]{0,7}$", ["price"])
        valdistrubutor = re.search("[a-z]{1}[^a-z]{0,25}$", dict1["distrubutor"])
        valpublisher = re.search("([a-z]{1}[^a-z]{0,25}$)", dict1["publisher"])
        if title and author and description and price and distrubutor and publisher:
            return True
        else:
            return False


    headerContent = ["title", "author", "description", "price", "distrubutor", "publisher"]


    class BookDetails:
        def init(title, author, description, price, distrubutor, publisher, self=None):
            self.title = title
            self.author = author
            self.description = description
            self.price = price
            self.distrubutor = distrubutor
            self.publisher = publisher

        def addbookdetail(self, title, author, description, price, distrubutor, publisher):
            dict1 = {"title": title, "author": author,"description":description, "price": price, "distrubutor": distrubutor,
                     "publisher": publisher}
            booklist.append(dict1)


    obj1 = BookDetails()
    while (True):
        print("1)enter book:")
        print("2)view all books: ")
        print("3)view all books in alphabetical oder: ")
        print("4)search a book by using title filter: ")
        print("5)exit:")
        choice = int(input("Enter your choice : "))
        if choice == 1:
                title = input("Enter the book title : ")
                author = (input("Enter your author : "))
                description = (input("Enter your description : "))
                price = int(input("Enter your price : "))
                distrubutor = (input("Enter your distrubutor: "))
                publisher = (input("Enter your publisher: "))
                if validate(title,author,description,price,distrubutor,publisher):
                    obj1.addbookdetails(title, author, description, price, distrubutor,publisher)
                else:
                    logging.error("invalid data enter a valid data")

        if choice == 2:
            print(booklist)
        if choice == 3:
            title = input("Enter the book title to search : ")
            print(list(filter(lambda i: i["title"] == title, booklist)))
        
        if choice == 5:
            break


except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")