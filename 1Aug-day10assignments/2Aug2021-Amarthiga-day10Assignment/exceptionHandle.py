# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# div=x/y         #maybe get zerodivision error/exceptions
# print(div)

#try block exception handling method:1
# try:                       
#     x=int(input("Enter a number:"))
#     y=int(input("Enter a number:"))
#     div=x/y
#     print(div)

# except:
#     print("Something went wrong")

#2
try:                       
    x=int(input("Enter a number:"))
    y=int(input("Enter a number:"))
    div=x/y
    print(div)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Only number should be given")
    