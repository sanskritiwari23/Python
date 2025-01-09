# try:
#     l = [1,5,6,7]
#     i = int(input("Enter the index:" ))
#     print(l[i])
# except:
#     print("some error occured")
# finally:
#     print("I am always exeecuted")


#The need of finally statement is inside a function
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index:" ))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always exeecuted")
    # print("I am always executed")

x = func1()
print(x)

#If we'll directly try to print the statement it will not get printed, but instead if you'll use finally statement it gets printed

# NOTE: Always remember ki return statement execute hone k bd age ka function ni chlta h, or agr use hume chalana h to uske liye it is necessary ki hum finally use kre