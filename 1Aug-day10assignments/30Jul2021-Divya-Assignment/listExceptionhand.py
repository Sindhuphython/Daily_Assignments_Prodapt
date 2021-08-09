l = ["divya","kdaj",4,6]
try:
    print(l[6])
    #print(a[4])
except (IndexError,NameError):
    print("the given index out of bound")
else:
    print("Executed Successfully")
finally:
    print("end of the session")