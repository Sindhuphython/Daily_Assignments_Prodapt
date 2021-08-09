#INSERTION SORT
import timeit
def insertionsort():
    def inser(arr):
        for i in range(1,len(arr)):
            l=arr[i]
            j=i-1
            while j>=0 and l<arr[j]:
                arr[j+1]=arr[j]
                j-=1
                arr[j+1]=l
    arr=[23,12,45,67,23,34]
    inser(arr)
print(timeit.timeit(insertionsort,number=1000))