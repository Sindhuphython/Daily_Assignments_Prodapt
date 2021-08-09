import timeit,logging
try:
    sorting_list=[45,67,3,69,43,23,1,2,89]

    #########BUBBLE SORT
    def bubbleSort():
        for i in range(len(sorting_list)-1,0,-1):
            for j in range(i):
                if sorting_list[i]>sorting_list[j+1]:
                    temp = sorting_list[j]
                    sorting_list[j] = sorting_list[j+1]
                    sorting_list[j+1] = temp

    ##########SELECTION SORT
    def selectionSort():
        for i in range(len(sorting_list)):
            min = i
            for j in range( i+1, len(sorting_list)):
                if sorting_list[min] > sorting_list[j]:
                    min_idx = j
                    sorting_list[i], sorting_list[min_idx] = sorting_list[min_idx],sorting_list[i]

    ###########INSERTION SORT

    def insertionSort():
        for i in range(1, len(sorting_list)):
            j = i-1
            sort = sorting_list[i]
            while (sorting_list[j] > sort) and (j >= 0):
                sorting_list[j+1] = sorting_list[j]
                j=j-1
            sorting_list[j+1] = sort

    if __name__== "__main__":
        print(timeit.timeit(bubbleSort,number=10000))
        print(timeit.timeit(selectionSort,number=10000))
        print(timeit.timeit(insertionSort,number=10000))

except Exception:
    logging.error("Something Went Wrong")

finally:
    print("Äll Block Completed Successfully")