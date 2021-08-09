#Exception Handling error

try:
    n1 = int(input("enter a num: "))
    n2 = int(input("enter a num: "))
    div = n1/n2
    print(div)
except ZeroDivisionError:
    print("OOPS! ,Division by zero is not allowed")
except ValueError:
    print("Enter right value in integer")