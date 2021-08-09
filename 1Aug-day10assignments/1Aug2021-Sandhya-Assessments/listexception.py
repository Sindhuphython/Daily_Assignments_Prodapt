l=[2,3,45,5]
try:
    #print(l[2])
    #print(l[5])
    print(a[2])
# except IndexError:
#     print("oops!,something went wrong")
except (IndexError,NameError):
     print("oops!,something went wrong")
else:
    print("execution completed successfully")
finally:
    print("ok done for the day") 