n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
try:
    div=n1/n2
    print(div)
except ZeroDivisionError:
    print("Something went wrong")
except ValueError:
    print("only number should be entered") 
    