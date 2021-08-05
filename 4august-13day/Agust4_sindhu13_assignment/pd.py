import csv,logging,time
productlist=[]
try:
    headerContent=["productname","description","price","manufacturer","manufacturerdate","expirydate"]
    class ProductDetails:
        def addProductDetails(self,productname,description,price,manufacturer,manufacturerdate,expirydate):
            self.productname=productname
            self.description=description
            self.price=price
            self.manufacturer=manufacturer
            self.manufacturerdate=manufacturerdate
            self.expirydate=expirydate
        def addproductdetail(self,productname,description,price,manufacturer,manufacturerdate,expirydate):
            dict1={"productname":productname,"description":description,"price":price,"manufacturer":manufacturer,"manufacturerdate":manufacturerdate,"expirydate":expirydate}
            productlist.append(dict1)
    obj=ProductDetails()
    def validate(vname,vdescription,vprice):
        name1=re.match("([a-z]+)([a-z]+)([a-z]+)$",vname)
        description1=re.match("([a-z]+)([a-z]+)([a-z]+)$",vdescription)
        price1=re.match("[0-9]{0,7}$",vprice)
        if name1 and description1 and price1:
           return True
        else:
            return False
    # obj=ProductDetails()
    while True:
        print("1.Add Product")
        print("2.View Products")
        print("3.Search a product")
        print("4.List products that expire today")
        print("5.save to file")
        print("6.exit")
        choice=int(input("enter your choice:"))

        if choice==1:
            vname=input("Enter the Product name : ")
            vdescription=input("Enter the Description : ")
            vprice=int(input("Enter the Price : "))
            if validate(vname,vdescription,vprice):
                    manufacturer=input("Enter the manufacturer name : ")
                    manufacturerdate=input("Enter the manufacturing date : ")
                    expirydate=input("Enter the expiry date   YYYY-MM-DD : ")
                    obj.addproductdetail(vname,vdescription,vprice,manufacturer,manufacturerdate,expirydate)
            else:
                logging.error("check your name,description,price")

        if choice==2:
            print(productlist)
        if choice==3:
            sname=input("Enter the product name to search : ")
            print(list(filter(lambda i:i["productname"]==sname,productlist)))
        if choice==4:
    
            current_time=time.localtime()
            tday=time.strftime("%Y-%m-%d",current_time)
            expirylist=(list(filter(lambda i:i["expirydate"]==str(tday),productlist)))    
            if len(expirylist)>0:
                print(expirylist)
            else:
                print("No records found")
        if choice==5:
            with open("product.csv","w+",encoding="UTF8",newline='')as s:
                writer=csv.DictWriter(s,fieldnames=headerContent)
                writer.writeheader()
                writer.writerows(productlist)
        if choice==6:
            break

except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")

      

    