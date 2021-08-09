import timeit
import logging
import collections
logging.basicConfig(filename="booklog.log",level=logging.DEBUG)
l=collections.deque([45,54,61,73,87,98,1,3,5,9,100,189,169,345,500,23])
#bubble sort
try:
    def usingsorted():
        a=sorted(l)
        pass

    def bubbleSort():
        length=len(l)
        i=l[0]
        j=l[0]
        for i in range(length-2):           #iteration       #treat i as index using range
            for j in range(length-2-i):     #in each iteration
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
        #l.reverse()                   #uncomment for descending order
        pass
    ###############################################

    #selection sort
    def selectionSort():
        length=len(l)
        for i in range(length-1):           #in java till length-2
            minn=l[i]
            pos=i
            for j in range(i+1,length):
                if l[j]< minn:
                    minn=l[j]
                    pos=j
            l[i],l[pos]=l[pos],l[i]
        pass
    ###################################################
    #insertion sort
    def insertionSort():
        length=len(l)
        for i in range(1,length):               #in java length-1
            item=l[i]
            j=i-1
            while(j>=0 and l[j]>item):
                l[j+1]=l[j]
                j=j-1
            l[j+1]=item
        pass
    print(timeit.timeit(usingsorted,number=100000))
    print(timeit.timeit(bubbleSort,number=100000))
    print(timeit.timeit(selectionSort,number=100000))
    print(timeit.timeit(insertionSort,number=100000))
    logging.info("Sorting time printed")
except:
    print("Something went wrong")
    logging.error("Some error occured")
finally:
    print("Everything executed properly")