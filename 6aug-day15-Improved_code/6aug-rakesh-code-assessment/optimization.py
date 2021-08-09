import timeit,logging
try:
    if(__name__=="__main__"):
        def sort():
            mylist=[10,21,45,1,44,34,2,23,12,11,56,33]
            sorted(mylist,key=lambda i:i,reverse=True)
            pass
        def bubble():
            def bubble_sort(nums):
                swapped = True
                while swapped:
                    swapped = False
                    for i in range(len(nums) - 1):
                        if nums[i] > nums[i + 1]:
                            nums[i], nums[i + 1] = nums[i + 1], nums[i]
                            swapped = True
            random_list_of_nums = [5, 2, 1, 8, 4]
            bubble_sort(random_list_of_nums) 
            pass
        print(timeit.timeit(sort,number=100000)) 
        print(timeit.timeit(bubble,number=100000)) 
except:
    logging.error("OOPS!! something went wrong")
finally:
    print("Thank you")    

