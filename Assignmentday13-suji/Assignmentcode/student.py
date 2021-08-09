import csv
header=['total','name','rollno','admin','english','hindi','chemistry','maths','telugu']
studentlist=[]
class StudentDetails:
   
    def addstudentdetail(self,name,rollno,admin,enlish,hindi,chemistry,maths,telugu):
        totalmarks=enlish+hindi+chemistry+maths+telugu
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"chemistry":chemistry,"maths":maths,"telugu":telugu}
        studentlist.append(dict1)
obj1=StudentDetails()        
while(True):
    print("1.add student:")
    print("2.display student like API:")
    print("3.search student using rollno:")
    print("4.ranking:")
    print("5.exit")
    print("6.save data to file:")
    choice =int(input("enter the choice:"))
    if choice==1:
        name=input("enter the name:")
        rollno=int(input("enter rollno:"))
        admin=int(input("enter admin:"))
        english=int(input("enter english marks:"))
        hindi=int(input("enter hindi marks:"))
        chemistry=int(input("enter chemistry marks:"))
        maths=int(input("enter maths marks:"))
        telugu=int(input("enter telugu marks:"))
        obj1.addstudentdetail(name,rollno,admin,english,hindi,chemistry,maths,telugu)
    if choice==2:
        print(studentlist) 
    if choice==3:
        srollno=int(input("enter the rollno:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
       print(sorted(studentlist,key=lambda i:i["total"],reverse=True))     


    if choice==5:
        break
    if choice==6:
        with open('file.csv','w+',encoding='UTF8',newline='') as x:
            writer=csv.DictWriter(x,fieldnames=header)
            writer.writeheader()
            writer.writerows(studentlist)    