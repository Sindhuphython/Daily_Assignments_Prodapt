# from Miniproject2.main import Collection_name2
import pymongo,logging
import sys,time
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['studentdataDb']
Collection_name =mydatabase['studentsdata']
try:
    student= []
    class StudentData:
        def addDetails(self,name,rollno,classes,english,hindi,maths,science,social):
            totalmarks=int(english)+int(hindi)+int(maths)+int(science)+int(social)
            current_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
            dict1 = {'total':totalmarks,'name':name,'rollno':rollno,'classes':classes,'english':english,'hindi':hindi,'maths':maths,'science':science,'social':social,'AddOn':current_time,"delflag":0}
            student.append(dict1)
        def init(self,name,rollno,classes,english,hindi,maths,science,social):
            self.name = name
            self.rollno = rollno
            self.classes = classes
            self.english=english
            self.hindi=hindi
            self.maths=maths
            self.science=science
            self.social=social

    obj1=StudentData()
    while(True):
        print("1. Add student details - ")
        print("2. Display all student details  - ")
        print("3. Search student data with class and rollno - ")
        print("4. Update student data- ")
        print("5. Delete student data - ")
        print("6. Exit - ")
        choice = int(input('enter your choice - '))
        if choice==1:
            name = input("enter the name of student - ")
            rollno=input("enter the Rollno - ")
            classes=input('enter the class -  ')
            english=input("enter the english marks: ")
            maths=input("enter the maths marks: ")
            social=input("enter the social marks: ")
            hindi=input("enter the hindi marks: ")
            science=input("enter the science marks: ")
            obj1.addDetails(name,rollno,classes,english,hindi,maths,science,social)
            result=Collection_name.insert_many(student)
            print(result.inserted_ids)
        if choice==2:

            result = Collection_name.find()
            l = []
            for i in result:
                l.append(i)
            print(l)
                
    
        if choice==3:
            classes=input("enter the class - ")
            roll=input("enter the roll no - ")
            result=Collection_name.find({"$and":[{"classes":classes},{"rollno":roll}]},{"defflag":0})
            for i in result:
                print(i)

        if choice==4:
            # name = input("\n Enter class ?")
            classes=input("enter the class - ")
            rollno=input("enter the rollno - ")
            update=input("enter the marks to be updated - ")
            result= Collection_name.update_one({"$and":[{"classes":classes},{"rollno":rollno}]},{"$set":{"maths": update }})
            print(result)
        if choice==5:
            classes = input('enter class -')
            rollno = input('enter rollno -')
            result=Collection_name.update_one({"$and":[{"rollno":rollno},{"classes":classes}]},{"$set": {'delflag':1}})
        if choice==6:
            sys. exit()
except Exception:
    print("something went wrong")
finally:
    print("Thank you!!")