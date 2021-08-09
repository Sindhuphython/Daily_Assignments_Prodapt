import requests
import json

try:
    data = requests.get("https://jsonplaceholder.typicode.com/todos")
    details = data.json()
    myList=[i for i in details if i['completed']==True]
    for i in myList:
        print(i)
except:
    print("Something went wrong. Please try again")
finally:
    print("Task completed")    


    

    
