import timeit,logging
try:
    my_list=[12,16,16,17,18,19,18,17,25,45,56,67,89]
    if(__name__=="__main__"):     
        def f1():
            sorted(my_list)
        def f2():
            for iter_num in range(len(my_list)-1,0,-1):
                for idx in range(iter_num):
                    if my_list[idx]>my_list[idx+1]:
                        temp = my_list[idx]
                        my_list[idx] = my_list[idx+1]
                        my_list[idx+1] = temp
        print(timeit.timeit(f1,number=100000))
        print(timeit.timeit(f2,number=100000))
except:
    logging.error("unable to  process")
