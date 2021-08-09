import timeit
# By sort() funcetion 
def compareSort():
    getlist=[4,2,5,34,6,3,76,43]
    getlist.sort()
print(timeit.timeit(compareSort,number=100000))  

# By Insertion sort 
def insertion():
    def insertionSort(arr):
        for i in range(1, len(arr)):
            m = arr[i]
            j = i-1
            while j >= 0 and m< arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                arr[j + 1] = m
    arr = [4,2,5,34,6,3,76,43]
    insertionSort(arr)
print(timeit.timeit(insertion,number=100000))

# By bubble
def bubble():
    def bubbleSort(nums):            
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]> nums[j+1]:
                    temp = nums[j] 
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
    nums =[4,2,5,34,6,3,76,43]
    bubbleSort(nums)
print(timeit.timeit(bubble,number=100000))
