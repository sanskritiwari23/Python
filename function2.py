#Function Arguments and return statements
# def avg(a,b):
#     print("The ave is ", (a+b)/2)

# #default Agruments
# def avg(a = 1,b = 9):
#     print("The ave is ", (a+b)/2)
# avg() #Isme it'll take the defined values of a and b
# avg(1,5) #Isme it'll overwrite the values of a and b
# avg(1) #This is how I'll give the value of a and default value of b will be used
# avg(b =9) #This is how we'll give value of b and default value of a will be used

# #Key Agruments
# avg( b = 10, a = 21) #Ese I don't have to take care of the order of the argument, wrna dhyan rkhna pdta

# #Req. Arguments
# def avg(a, b = 10):
#     print("The ave is ", (a+b)/2)

# avg(10) #In this senario it's not imp for me to give the value of b as it is already defined, but necessary to give the value of a
# #Otherwise it will give an error


#In this manner I can print the avg of n numbers without any constraint
#Here a tuppel of numbers will be made
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    #print("Average is: ", sum/len(numbers)) #This statement will be outside the for loop
     #otherwise it'll print the avg of each and every value of sum
    return sum/len(numbers) #using return you can save the value in a particular variable and then print that variable
# Jo bhi return value phele likhi hoti h bs whi ati h baki age ki values ko ignore kr diya jta h

# average(5,6)
# average(5,6,7)
c = average(5,6,7,8,9)
print(c)


#This is in the form of Dictionary, refer to this again after studying dict. 
# def name(**name):
#     #print(type(name))
#     print("Hello, ", name["fname"], name["mname"], name["lname"])
# name(mname = "Buchanan", lname = "Barnes", fname = "James")