import timeit,logging
the_list = [12,11,13,5,6]
logging.basicConfig(filename = "InsertionSort.log" ,level=logging.DEBUG)
def f1():
    for i in range(1, len(the_list)):
 
        key = the_list[i] 
        j = i-1
        while j >= 0 and key < the_list[j] :
                the_list[j + 1] = the_list[j]
                j -= 1
        the_list[j + 1] = key


print(timeit.timeit(f1))
logging.info(the_list)