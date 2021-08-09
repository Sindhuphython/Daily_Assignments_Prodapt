list1=[1,23,4,5]
try:
    #print(list1[5])
    print(list1[2])
except (IndexError,NameError):
    print("IndexError occured please enter correct index")
else:                                                         #executes only when try block is error free
    print("successfully executed")
finally:
    print("done")
