#Function - It is a block of code that performs a specific task whenever it is called. 
#This is how I created the Function
def calculateGmean(a,b): #To calculate GM
    mean = (a*b)/(a+b)
    print(mean)

def Bigger(a,b):#To check which number is greater??
    if(a>b):
        print(a, "is greater than",b)
    else:
        print(a, "is less than",b)


def isLesser(a,b):#I have made the dunction but is thinking of making the body afterwards
    #so to avoid any error in the code I'll use "pass" statement, otherwise there will be an error during execution
    pass


a = 9
b = 8
Bigger(a,b)
calculateGmean(a,b) #This is the way of calling a function
# gmean = (a*b)/(a+b) 
# print(gmean)
c = 8
d = 7
calculateGmean(c,d) #This is the way of calling a function
Bigger(c,d)

#There are 2 types of functions in Python
# 1. Builtin Functions - The functions which are already present in Python
# 2. User Defined Functions - The functions which are defined by the user by using "def" command