try:
    n1=int(input("enter a numbers"))
    n2=int(input("enter a number "))
    div=n1/n2
    print(div)
except ZeroDivisionError:
    print("ArithmeticException")
except ValueError:
    print("number should be entered")
