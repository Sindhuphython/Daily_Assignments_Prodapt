import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")


mydatabase =client['ProductsDB']
Collection_name = mydatabase['Products']

ProroductDetails= []
class Products:
    def adddetails(self,Productcode,Productname,Distributorname,Retailprice,Wholeprice,Productdescription,Contactnumber,Manufactureryear):
        self.Productcode = Productcode
        self.Productname = Productname
        self.Distributorname = Distributorname
        self.Retailprice = Retailprice
        self.Wholeprice = Wholeprice
        self.Productdescription = Productdescription
        self.Contactnumber = Contactnumber
        self.Manufactureryear = Manufactureryear
        Productdetails={"Productcode":Productcode,"Productname":Productname,"ProductDistributorname":Distributorname,"retail":Retailprice,"Whole":Wholeprice,"Productdescription":Productdescription,"Contact":Contactnumber,"Manufactureryear":Manufactureryear}
        ProductDetails.append(details)
Prod=Products()

while(True):
    print("1.ADD DETAILS")
    print("2.DISPLAY")
    print("3.SEARCH BY PRODUCTS CODE")
    print("4.To DELETE")
    print("5.To UPDATE")
    choice = int(input("enter your choice: "))

    if choice == 1:
        Productcode = int(input("Enter product code: "))
        Productname = input("Enter product name: ")
        Distributorname = input("Enter distributor name: ")
        Retailprice = int(input("Enter retail price: "))
        Wholeprice = int(input("Enter whole price: "))
        Productdescription = input("Enter product description: ")
        Manufactureryear = int(input("Enter manufacturer year: "))
        Contactnumber = int(input("Enter contact number: "))
        Prod.adddetails(Productcode,Productname,Distributorname,Retailprice,Wholeprice,Productdescription,Contactnumber,Manufactureryear)
    if choice == 2:
        print(Pro_details)
        Collection_name .insert_many(Pro_details)
    if choice == 3:
        n= input("enter product name: ")
        result = Collection_name.find({"Productname": n})
        for i in result:
            print(i)
    if choice == 4:
        result = Collection_name.delete_many({'Productname'})
        print(result.deleted_count)
    if choice == 5:
        result = Collection_name.update_one({'Productname'},{"$set":{"Productname"}})
        break
