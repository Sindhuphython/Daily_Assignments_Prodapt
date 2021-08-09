try:
    n1=int(input("enter a number:"))
    if n1<0:
        raise ValueError()
    else:
        print(n1)
except ValueError:
    print("n1 is out of range")