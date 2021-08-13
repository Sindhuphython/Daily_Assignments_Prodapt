import re,pymongo,logging

try:
    studentlist=[]
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    mydatabase=client['StudentDatabase']
    collection_name=mydatabase['students']
    class Student:
        def init(self,name,rollno,clase,section,english,maths,social,science,hindi):
            self.name=name
            self.rollno=rollno
            self.clase=clase
            self.section=section
            self.english=english
            self.maths=maths
            self.social=social
            self.science=science
            self.hindi=hindi
        def addstudentdetail(self,name,rollno,clase,section,english,maths,social,science,hindi):
            totalmarks=int(english)+int(maths)+int(social)+int(science)
            dict1={"total":totalmarks,"name":name,"rollno":rollno,"clase":clase,"section":section,"english":int(english),"maths":maths,"social":social,"science":science,"hindi":hindi,"delflag":0} 
            studentlist.append(dict1)
    obj=StudentDetails()
    def validate(name):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
          
        if name1 :
            return True
        else:
            return False  

    while True:
        print("1.Add students with marks")
        print("2.View students with marks")
        print("3.Search a student")
        print("4.update a data")
        print("5.avg marks on english based on class") 
        print("6.delete a student")
        print("7.exit")
        choice=int(input("Enter your choice : "))
        if choice==1:
            name=input("Enter the name : ")
            if validate(name):
                rollno=input("Enter the roll no : ")
                clase=input("Enter the class : ")
                section=input("enter the section")
                english=input("Enter the marks of English : ")
                maths=input("Enter the marks of maths : ")
                science=input("Enter the marks of Science : ")
                social=input("Enter the marks of Social : ")
                hindi=input("Enter the marks of hindi : ")
                obj.addstudentdetail(name,rollno,clase,section,english,maths,social,science,hindi)
                result=collection_name.insert_many(studentlist)
                print(result.inserted_ids)
        if choice==2:
            result=collection_name.find()
            for i in result:
                studentlist.append(i)
            print(i)
        if choice==3:
            name=input("enter the class - ")
            roll=input("enter the roll no - ")
            result=collection_name.find({"$and":[{"class":name},{"rollno":roll}]},{"defflag":0})
            for i in result:
                print(i)
        if choice==4:
            p=input("enter the class - ")
            q=input("enter the rollno - ")
            r=input("enter the marks to be updated - ")
            result= collection_name.update_one({"$and":[{"class":p},{"rollno":q}]},{"$set":{"maths": r }})
            print(result)
        if choice==5:
            result=collection_name.aggregate([{"$group" :{"_id":"class","Avg":{"$avg":"$english"}}}])
            for i in result:
                print(i)
        if choice==6:
            p = input('enter class ')
            q = input('enter rollno ')
            result=collection_name.update_one({"$and":[{"rollno":p},{"class":q}]},{"$set": {'delflag':1}})
            print(result)
        if choice==7:
            break
except:
    logging.error("something went wrong")