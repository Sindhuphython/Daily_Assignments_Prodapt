import collections as c
import re

while(True):
    print("1.Add Employee")
    print("2.View Employee")
    print("3. Exit")
    
    choice=(int(input("Enter your response: ")))

    if choice==1:
        print("Add employee selected")
        EmpName=c.defaultdict(str)
        Emp_ID=c.defaultdict(int)
        Designation=c.defaultdict(str)
        Salary=c.defaultdict(int)
        add=c.defaultdict(str)
        mob_no=c.defaultdict()
        pincode=c.defaultdict(int)

        EmpName["EmpName"] =(input("Enter Employee Name: "))
        Emp_ID["EmpID"]= (int(input("Enter Employee ID: ")))
        Designation["Designaton"] = (input("Enter Employee Designation:"))
        Salary["Salary"] = (int(input("Enter Employee Salary:")))
        add["Address"] = (input("Enter Employee add:"))

        #mob_no["Mobile"] = int(input("Enter Employee Mobile number:"))
        #val_mob=re.match("^\+91?(6-9)\d{9}$",mob_no)
        try:
            mob_no["Mobile"] = (input("Enter Employee Mobile number:"))
            valMob = re.search("^(6-9)\d{9}$",mob_no)
            #val_mob=re.match("^\+91?(6-9)\d{9}$",mob_no)
            if valMob:
                print("valid mobile no")
            else:
                print("invalid Mobile No")
        except:
            print("error in validation")
        try:
            pincode["pincode"] = (int(input("Enter Employee pincode:")))
            valPin = re.search("^6\d{5}$",pincode)
            if valMob:
                print("valid mobile no")
            else:
                print("invalid Mobile No")
        except:
            print("error in validation")
              
        print(EmpName["EmpName"])
        print(Emp_ID["EmpID"])
        print(Designation["Designaton"])
        print(Salary["Salary"])
        print(add["Address"])
        print(mob_no["Mobile"])
        print(pincode["pincode"])

        # New_Dic=c.ChainMap(EmpName,Emp_ID,Designation,Salary,add, mob_no,pincode)
        # print(New_Dic.maps)

    if choice==2:
        print("View Employee Selected")
        New_Dic=c.ChainMap(EmpName,Emp_ID,Designation,Salary,add, mob_no,pincode)
        print(list(New_Dic.maps))

    if choice==3:
        print("Exit from Menu")
        break

    else:
        print("Something went wrong, Invaid option")



