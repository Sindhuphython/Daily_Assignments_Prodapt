import timeit
import logging
logging.basicConfig(filename="booklog.log",level=logging.DEBUG)
l=[45,54,61,73,87,98,1,3,5,9,100,189,169,345,500,23]

try:

    #selection sort
    def selectionSort():
        length=len(l)
        for i in range(length-1):           
            minn=l[i]
            pos=i
            for j in range(i+1,length):
                if l[j]< minn:
                    minn=l[j]
                    pos=j
            l[i],l[pos]=l[pos],l[i]
        pass
    
    #insertion sort
    def insertionSort():
        length=len(l)
        for i in range(1,length):              
            item=l[i]
            j=i-1
            while(j>=0 and l[j]>item):
                l[j+1]=l[j]
                j=j-1
            l[j+1]=item
        pass
    
    #bubble sort
    def bubbleSort():
        length=len(l)
        i=l[0]
        j=l[0]
        for i in range(length-2):           
            for j in range(length-2-i):     
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
        
        pass
    
    #using sorted function
    def usingsorted():
        a=sorted(l)
        pass

    print(timeit.timeit(usingsorted,number=1000))
    print(timeit.timeit(bubbleSort,number=1000))
    print(timeit.timeit(selectionSort,number=1000))
    print(timeit.timeit(insertionSort,number=1000))
    logging.info("Sorting time of different methods printed")
except:
    
    logging.error("Some error occured during the process")
else:
    print("try block executed ")
finally:
    print("Everything executed properly")