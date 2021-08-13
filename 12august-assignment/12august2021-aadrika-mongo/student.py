import pymongo
from pymongo import collection
import logging,re
logging.basicConfig(filename="stud.log",level=logging.DEBUG)
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["Studentmarkdb"]
collection_name=mydb["StudentMarks"]
class Student:
    def CreateStudent(self,name,rollnum,clas,eng,maths,social,science):
        total=eng+int(maths)+int(social)+int(science)
        dict1={"Name":name,"Rollnum":rollnum,"Class":clas,"English":eng,"Maths":maths,"Social":social,"Science":science,"total":total,"del_status":0}
        return dict1
        
obj1=Student()

def validate(name):
    name=re.match('^([a-z])( [a-z]+)([a-z])$',name)
    if name:
        return True
    else:
        return False


while(True):
    print("1. Create Students: ")
    print("2. View all students with their total marks: ")
    print("3. Search a student with class and roll number: ")
    print("4. Update student data and marks based on rollnum and class : ")
    print("5. Average marks of english based on class : ")
    print("6. Delete a student based on roll number and class : ")
    print("7. Exit: ")
    try:
        choice=int(input("Enter your choice: "))
    except:
        logging.error("User entered wrong choice")
        continue
    if choice==1:
        while(True):
            name=input("Enter your name:")
            if validate(name):
                rollnum=input("Enter your roll number:")
                clas=input("Enter your class:")
                eng=int(input("Enter your english marks:"))
                maths=input("Enter your maths marks:")
                social=input("Enter your social marks:")
                science=input("Enter your science marks:")
                new=obj1.CreateStudent(name,rollnum,clas,eng,maths,social,science)
                collection_name.insert_one(new)
            else:
                logging.error("User not enterd name in correct format")
                continue
            break
    if choice==2:
        res=collection_name.find()
        for i in res:
            print(i)
    
    if choice==3:
        clas=input("Enter your class: ")
        rollnum=input("Enter your roll number: ")
        res=collection_name.find({"$and":[{"Class":clas},{"Rollnum":rollnum},{"del_status":0}]})
        for i in res:
            print(i)

    if choice==4:
        print("Enter roll number and class whose data has to be updated :")
        rollnum=input("Enter your roll number:")
        clas=input("Enter your class:")
        print("Now enter updated data")
        name=input("Enter your name:")
        eng=int(input("Enter your english marks:"))
        maths=input("Enter your maths marks:")
        social=input("Enter your social marks:")
        science=input("Enter your science marks:")
        total=int(eng)+int(maths)+int(social)+int(science)
        res=collection_name.update_one({"$and":[{"Class":clas},{"Rollnum":rollnum},{"del_status":0}]},{"$set":{"Name":name,"English":eng,"Maths":maths,"Social":social,"Science":science,"total":total}})

    if choice==5:
        
        clas=input("Enter your class:")
        res=collection_name.aggregate([{"$match":{"Class":clas}},{"$group":{"_id":"Class","average":{"$avg":"$Englis"}}}])

        for i in res:
             print(i)
      
    if choice==6:
        rollnum=input("Enter your roll number:")
        clas=input("Enter your class:")
        res=collection_name.update_one({"$and":[{"Rollnum":rollnum},{"Class":clas}]},{"$set":{"del_status":1}})
    if choice==7:
        break