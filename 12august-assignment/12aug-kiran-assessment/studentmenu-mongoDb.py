import pymongo
from valid import validation
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['studentdetailsDb']
collection_name=mydatabase['students']
students_list=[]
new_list=[]
class studentDetails:
    def addStudentDetails(self,name,rollno,standard,englishmarks,mathsmarks,socialmarks,sciencemark):
        totalmarks=int(englishmarks),int(mathsmarks),int(socialmarks),int(sciencemarks)
        dict={"name":name,"rollno":rollno,"standard":standard,"englishmarks":englishmarks,"mathsmarks":mathsmarks,"socialmarks":socialmarks,"sciencemarks":sciencemarks,"totalmarks":totalmarks,"delflag":0}
        students_list.append(dict)
obj=studentDetails()

while(1):
    print("1.create studentlist:")
    print("2.view all  students details:")
    print("3.search a student with class and rollno:")
    print("4.update a student data and marks based on class and rollno:")
    print("5.find avg marks of english based on class:")
    print("5.delete a student based on rollno and class:")
    print("6.Exit::")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter student name:")
        rollno=input("Enter student rollno:")
        standard=input("Enter student class:")
        englishmarks=input("Enter student english marks:")
        mathsmarks=input("Enter student maths marks:")
        socialmarks=input("Enter student social marks:")
        sciencemarks=input("Enter student science marks:")
       
        if validation(standard,rollno,englishmarks,mathsmarks,socialmarks,sciencemarks):
            obj.addStudentDetails(name,rollno,standard,englishmarks,mathsmarks,socialmarks,sciencemarks,totalmarks)
            result=collection_name.insert_many(students_list)
            print(result.inserted_ids)
        else:
            print("invalid details")
    if choice==2:
        result=collection_name.find({"delflag":0})
        for i in result:
            new_list.append(i)
            print(i)
            

    if choice==3:
        standard=input("enter the class:")
        rollno=input("enter the rollno:")
        result=collection_name.find({"standard":standard,"rollno":rollno,"delflag":0})
        for i in result:
            print(i)
    
    if choice==4:
        standard=input("Enter the class:")
        rollno=input("Enter the rollno:")
        name=input("enter the student name:")
        english=int(input("enter english marks:"))
        maths=int(input("enter maths marks:"))
        result=collection_name.update_one({"standard":standard,"rollno":rollno},{"$set":{"name":name,"englishmarks":english,"mathsmarks":maths}})
        print(result)

    if choice==5:
        standard=input("Enter the class:")
        result=collection_name.aggregate([{"$match":{"$standard":standard}},{"$group":{"_id":"$standard","avg":{"$avg":"$englishmarks"}}}])
        for i in result:
            print(i)

    if choice==6:
        rollno=input("enter the rollno:")
        std=input("enter the class:")
        result=collection_name.update_one({"$and":[{"rollno":rollno,"standard":std}]},{"$set":{"delflag":1}})
        print(result)

    if choice==7:
        break

