# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The locatl x is {x}")
#     print("Hello Harry")

# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")

#Global vairable will be constant for all the values in the code, whereas local vairable will only be valid inside the function, outside the function it will not give the same value

x = 10 #Global Vairable

def my_function():
    global x #Using this you are creating an global vairable inside a function and will be able to make changes in it while keeping it inside the function only, irrespective of it been already created outside the function
    x = 4
    y = 5 #Local Vairable
    print(y)

my_function()
print(x)
#print(y) #This will cause an error because y is a local vairable and is not accessible outside of the function