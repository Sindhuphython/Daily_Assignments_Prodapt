#BUBBLE SORT
import timeit
def bubblesort():
    def bubblesort(arr):
        n=len(arr)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
    arr=[23,87,76,77,56,65,12,13]
    bubblesort(arr)
print(timeit.timeit(bubblesort,number=1000))

    
