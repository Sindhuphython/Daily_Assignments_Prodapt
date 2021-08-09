import timeit,logging
try :
    if __name__ == "__main__":
     def compareSort():
       getlist=[33,11,8,45,97,25,99,1,4]
       sorted(getlist,key=lambda x:x,reverse=True)
     print(timeit.timeit(compareSort,number=100000))  
     def insertion():
        def insertionSort(arr):
         for i in range(1, len(arr)):
 
          m = arr[i]
 
        
          j = i-1
          while j >= 0 and m< arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
         arr[j + 1] = m
        arr = [33,11,8,45,97,25,99,1,4]
        insertionSort(arr)
    #for i in range(len(arr)):
      #print ("% d" % arr[i])
#insertionSort(arr,key=lambda x:x,reverse=True)
    print(timeit.timeit(insertion,number=100000)) 
except:
    logging.error("something went wrong")