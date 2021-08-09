import timeit
import logging
try:
    mylist=[23,56,3,4,7,8,63,45,9,11,23,45,5]

    def sort():
        sorted(mylist)

    def selection_sort():
        for idx in range(len(mylist)):
            min_idx = idx
            for j in range( idx +1, len(mylist)):
                if mylist[min_idx] > mylist[j]:
                    min_idx = j
                    mylist[idx], mylist[min_idx] = mylist[min_idx], mylist[idx]



    def shellSort():
        n=len(mylist)
        h=n//2
        while h>0:
            for i in range(h,n):
                t=mylist[i]
                j=i
                while j>=h and  mylist[j-h] >t:
                    mylist[j]=mylist[j-h]
                    j-=h
                mylist[j]=t
            h=h//2



    def insertion_sort():
        for i in range(1, len(mylist)):
            j = i-1
            nxt_element = mylist[i]

        while (mylist[j] > nxt_element) and (j >= 0):
            mylist[j+1] = mylist[j]
            j=j-1
        mylist[j+1] = nxt_element


    def mergeSort():
        if len(mylist)>1:
            mid = len(mylist)//2
            lefthalf = mylist[:mid]
            righthalf = mylist[mid:]
            i=j=k=0       
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    mylist[k]=lefthalf[i]
                    i=i+1
                else:
                    mylist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                mylist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                mylist[k]=righthalf[j]
                j=j+1
                k=k+1



    def bubblesort():
        for iter_num in range(len(mylist)-1,0,-1):
            for idx in range(iter_num):
                if mylist[idx]>mylist[idx+1]:
                    temp = mylist[idx]
                    mylist[idx] = mylist[idx+1]
                    mylist[idx+1] = temp


    if(__name__=='__main__'):

        print(timeit.timeit(sort,number=10000))
        print(timeit.timeit(selection_sort,number=10000))
        print(timeit.timeit(shellSort,number=10000))
        print(timeit.timeit(insertion_sort,number=10000))
        print(timeit.timeit(mergeSort,number=10000))
        print(timeit.timeit(bubblesort,number=10000))

except:
    logging.error("something wrong")







