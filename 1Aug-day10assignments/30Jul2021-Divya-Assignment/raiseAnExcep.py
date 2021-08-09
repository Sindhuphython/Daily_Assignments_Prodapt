try:
    n = int(input("enter a number:"))
    if (n > 0 < 5):
        raise ValueError(n)
    else:
        print(n)
except ValueError:
    print("n is out of range")
