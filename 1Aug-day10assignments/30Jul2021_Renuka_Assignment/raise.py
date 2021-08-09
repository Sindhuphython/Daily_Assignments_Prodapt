try:
    n1=int(input("enter a number"))
    if n1<0:
        raise ValueError()    #used to raise an exception explicitly by user
    else:
        print(n1)
except ValueError:
    print("n1 should be greater than zero")
