import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    extractedata=data.json()
    #print(extractedata)
    n=[i for i in extractedata if i["completed"]==True]
    print(n)
except:
    print("something went wrong")
