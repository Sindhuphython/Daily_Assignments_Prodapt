from datetime import datetime 
import csv    
header=['name','description','price','manufacturer','mfgdate','expdate']
productlist=[]
class ProductDetails:
    
    def addproductdetail(self,name,description,price,manufacturer,mfgdate,expdate):
        dict1={"name":name,"description":description,"price":price,"manufacturer":manufacturer,"mfgdate":mfgdate,"expdate":expdate}
        productlist.append(dict1)
obj1=ProductDetails()        
while(True):
    print("1.add product:")
    print("2.display product like API:")
    print("3.search product using name:")
    print("4.list all the products that expire today:")
    print("5.exit")
    choice =int(input("enter the choice:"))
    if choice==1:
        name=input("enter the name:")
        description=input("enter description:")
        price=int(input("enter price:"))
        manufacturer=input("enter manufacturer:")
        
 
        mfgdate = str(input('Enter mfgdate(yyyy-mm-dd): '))
        expdate = str(input('Enter expdate(yyyy-mm-dd): '))
        
        obj1.addproductdetail(name,description,price,manufacturer,mfgdate,expdate)
    if choice==2:
        print(productlist) 
    if choice==3:
        pname=input("enter the name:")
        print(list(filter(lambda i:i["name"]==pname,productlist)))
    
    if choice==4:
        today_date=str(input("enter today date(yyyy-mm-dd):"))
        print(list(filter(lambda i:i["expdate"]==str(today_date),productlist)))

    if choice==5:
        break

    if choice==6:
        with open('pro.csv','w+',encoding='UTF8',newline='') as p:
            writer=csv.DictWriter(p,fieldnames=header)  
            writer.writeheader()
            writer.writerows(productlist)
