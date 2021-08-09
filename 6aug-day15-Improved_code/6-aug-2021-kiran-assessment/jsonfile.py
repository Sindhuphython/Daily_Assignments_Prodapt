import requests,json
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    ExtractedData=data.json()
    completedlist=[i for i in ExtractedData if i['completed']==True]
    print(completedlist)
except:
    print("Something went Wrong")