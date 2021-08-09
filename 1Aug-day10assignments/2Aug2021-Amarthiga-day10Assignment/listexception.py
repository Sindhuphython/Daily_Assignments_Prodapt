list =[34,56,567,980]
try:
    print(list[4])
    # print(a[3])
except (IndexError,NameError):
    print("give correct index")

else:                     #else part works only when try part doesn't have error
    print("Process completed successfully")

#irrsecpective of try block, 'Finally' will work

finally:
    print("Try, after sometimes")

