
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/EmployeeDb")
mydatabase=client['ProductDb']
collection_name=mydatabase['Product']
productlist=[]

    
class ProductDetails:
    def addProductDetails(self,productname,distributorname,manufactureyear,wholesaleprice,retailprice,description,contactnumber):
        self.productname=productname
        self.distributorname=distributorname
        self.manufactureyear=manufactureyear
        self.wholesaleprice=wholesaleprice
        self.retailprice=retailprice
        self.description=description
        self.contactnumber=contactnumber
                
    def addproductdetail(self,productname,distributorname,manufactureyear,wholesaleprice,retailprice,description,contactnumber):
        dict1={"productname":productname,"distributorname":distributorname,"manufactureyear":manufactureyear,"wholesaleprice":wholesaleprice,"retailprice":retailprice,"description":description,"contactnumber":contactnumber}
        productlist.append(dict1)
obj=ProductDetails()
def validate(vname,vdescription):
    name1=re.match("([a-z]+)([a-z]+)([a-z]+)$",vname)
    description1=re.match("([a-z]+)([a-z]+)([a-z]+)$",vdescription)
        
    if name1 and description1:
        return True
    else:
        return False
        # obj=ProductDetails()
while True:
    print("1.Add Product:")
    print("2.view a product:")
    print("3.search a product:")
    print("4.delete a product:")
    print("5.update a product:")
    print("6.exit")
    choice=int(input("enter your choice:"))

    if choice==1:
        vname=input("Enter the Product name : ")
        distributorname=input("Enter the distributor name:")
        vdescription=input("Enter the Description : ")
        manufactureyear=input("Enter the manufactureyear:")
        wholesaleprice=input("Enter the wholesaleprice : ")
        retailprice=input("Enter the retailprice : ")
        contactnumber=input("Enter the contactnumber:")
        if validate(vname,vdescription):
            obj.addProductDetails(vname,distributorname,manufactureyear,wholesaleprice,retailprice,vdescription,contactnumber)
            collection_name.insert_many(productlist)
        else:
            logging.error("check your name,description,price")

    if choice==2:
        result=collection_name.find({{"_id":0}})
        for i in result:
            productlist.append(i)
            print(i)
            
    if choice==3:
        productname=input("Enter the product name to search : ")
        result2=collection_name.find({"productname":productname})
        for i in result1:
            print(i)
            
    if choice==4:
        productname=input("Enter the product name that you want delete : ")
        result2=collection_name.delete_many({"productname":productname})
        print(result2.deleted_count)
    
            
    if choice==5:
        productname=input("Enter the product that you want update: ")
        description=input("Enter the description to update")
        result3=collection_name.update_one({"productname=":productname},{"$set":{"descrption":description}})
    if choice==6:
        break

