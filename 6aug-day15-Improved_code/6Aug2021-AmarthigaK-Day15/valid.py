import re

class validation1:
    def valid1(name):
        val1 = re.search("", re.IGNORECASE)
       
        if val1:
            print("Name Validated")
        else:
            print("Name is invalid")
    def Valid2(val2):
        mobile= re.search("^\+91?[6-9]\d{9}$",val2)
        if mobile:
            print("Mobile Number validated")
        else:
            print("error")


for i in range(len(Book_list)):
            print("%d"%Book_list[i]),