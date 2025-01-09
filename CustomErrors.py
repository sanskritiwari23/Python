#In python, we can raise custom errors by using the "raise" keyword
#To check types of errors in python search "python error classes" on google and you'll be able to see various errors that can be raised

#Using classes we can make an error and then raise it as per our need
# class CustomError(Exception):
#     #code.....
#     pass
# try:
#     #code....
# except CustomError:
#     #code....
# The above is the syntax and you can raise custom error like this after creating it

a = (input("Enter any value betweeen 5 and 9: "))

if (a == "quit"):
    print("no issues")

elif (int(a)<5 or int(a)>9):
    raise ValueError("Value should be between 5 and 9")


#Another code of the same type
a = int(input("Enter any value betweeen 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
