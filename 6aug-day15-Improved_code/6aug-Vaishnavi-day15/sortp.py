import timeit
  

#####@@@@ Insertion sort @@@@##### 
def insertionSort():
    def insertion(arr):
        for i in range(1, len(arr)):
            l = arr[i]
            j = i-1
            while j >= 0 and l< arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                arr[j + 1] = l
    arr = [8,5,2,6,1,3,7,9]
    insertion(arr)
print(timeit.timeit(insertionSort,number=100000))

#####@@@@ BUBBLE SORT @@@@#####
def bubbleSort():
    def bubble(x):            
        for i in range(len(x)-1,0,-1):
            for j in range(i):
                if x[j]> x[j+1]:
                    temp = x[j] 
                    x[j] = x[j+1]
                    x[j+1] = temp
    x =[8,5,2,6,1,3,7,9]
    bubble(x)
print(timeit.timeit(bubbleSort,number=100000))

#####@@@@ SORT @@@@#####
def sort():
    getlist=[8,5,2,6,1,3,7,9]
    getlist.sort()
print(timeit.timeit(sort,number=100000))