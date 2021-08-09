#Find  out the execution time of sorting a list by using sorted function and/or any other function.  
# Print it in a logg file as well as in the print function.
import timeit
import logging

logging.basicConfig(filename='sortings.log', level=logging.INFO)

#1
list = [1,2,56, 45, 67, 34, 90, 32]
list.sort(reverse=True)
print(list)
print(timeit.timeit(list.sort))
try:
    logging.info(("Execution time of simple sorting method",(timeit.timeit(list.sort))))
   

except:
    logging.warning("Error")


#2
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
logging.info((timeit.timeit(cars.sort)))


#3 Bubble sort
def bubble(list3):
    n = len(list3)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if list3[j] > list3[j+1] :
                list3[j], list3[j+1] = list3[j+1], list3[j]
 
# Driver code to test above
list3 = [64, 34, 25, 12, 22, 11, 90] 
bubble(list3)
 
print ("Sorted array is:")
for i in range(len(list3)):
    print ("%d" %list3[i]),

logging.info(timeit.timeit('bubble(list3)', 'from __main__ import bubble, list3' ))