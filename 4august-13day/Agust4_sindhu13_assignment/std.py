import csv
studentlist=[]
try:
    headerContent=["total","name","rollno","admin","english","hindi","maths","science","social"]
class StudentDetails:
    # def _init_(self,name,rollno,admin,english,hindi,maths,science,social):
        # self.name=name
        # self.rollno=rollno
        # self.admin=admin
        # self.english=english
        # self.hindi=hindi
        # self.maths=maths
        # self.science=science
        # self.social=social
    def addstudentdetail(self,name,rollno,admin,english,hindi,maths,science,social):
       
        totalmarks=english+hindi+maths+science+social
        dict1 ={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social}   
        studentlist.append(dict1)
    def validate(name,rollno):
        name=re.search("[a-z]{1}[^a-z]{0,25}$",dict1["name"])
        rollno=re.search("[0-9]{0,7}$",[rollno])
        if name and rollno:
            return True
        else:
            return false
       
obj1=StudentDetails()
while(True):
    print("1)Add Student : ")
    print("2)Display students like API: ")
    print("3)Search : ")
    print("4)Ranking: ")
    print("5)Exit")
    print("6)exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        name=input("Enter the Student name : ")
        rollno=int(input("Enter your rollno : "))
        admino=int(input("Enter your admino : "))
        english=int(input("Enter your English marks : "))
        hindi=int(input("Enter your Hindi marks : "))
        maths=int(input("Enter your maths marks : "))
        science=int(input("Enter your Science marks: "))
        social=int(input("Enter your Social Marks : "))
        obj1.addstudentdetail(name,rollno,admino,english,hindi,maths,science,social)
        else:
            logging.error("check your name,description,price")

    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("Enter the rollno to search : "))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i['total'],reverse=True))
    if choice==5:
        with open("student.csv","w+",encoding="UTF8",newline='')as s:
            writer=csv.DictWriter(s,fieldnames=headerContent)
            writer.writeheader()
            writer.writerows(studentlist)
    if choice==6:
        break
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")
            
        