import timeit
try:
    def sorting():
        mylist=[2,8,1,5,9]

        a=sorted(mylist,key=lambda i:i ,reverse=True)
        return a
    def bubble():
        mylist=[2,8,1,5,9]

        for i in range(len(mylist)):
            for j in range(0,len(mylist)-i-1):
                a=mylist[j]
                b=mylist[j+1]
                if a<b:
                    mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    
    mylist=[2,8,1,5,9]
    print(timeit.timeit(sorting,number=10000))
    print(timeit.timeit(bubble,number=10000))
except:
    print("something went wrong")