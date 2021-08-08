import timeit,logging
the_list = [2,4,9,1]
logging.basicConfig(filename = "BubbleSort.log" ,level=logging.DEBUG)
def f1():
    length = len(the_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if the_list[i] > the_list[i+1]:
                #print ("sorting")
                sorted = False
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i]

print(timeit.timeit(f1))
logging.info(the_list)