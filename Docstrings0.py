#Docstrings and PRP-8

#Docstring in python are the string literals that appear right after the definition of a function, method, class, or module. Basically provide us their description and are different from comments
#Docstrings are used just above the function defination

def square(n):
    '''Takes in a number n, returns the square of n'''
    #The above string is a doc string and is not ignored as comments, the format given above is the correct format of writing it
    print(n**2)
square(5)
print(square.__doc__) #This will print the docstring written inside the function square
#Docstring se outputs can be changed but comments se output can't be changed


def square(n):
    print(n)
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
#Ab yaha p docstring print ni hogi kyuki yaha p ye null ho chuki h, ye sift tbhi docstring rhegi jb ye just upr rhegi defination k

#Python Enhancement Proposal - PEP8
#Used for enhancing readability and consistency of python code


#Zen of Python
#Type import this in python(CMD) and you'll see the Zen of Python, it's basically a poem which tells us the ways in which we can make out coding easy