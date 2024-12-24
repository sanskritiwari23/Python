a = int(input("Enter your age: "))
print("Your age is: ", a)

#Conditional Operators 
# >, <, >=, <=, ==, !=

# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

#These are the examples of If-Else Statements!!!
if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
#Here we have used indentations jut like in C/C++ be use {} here we use spaces to tell if the statement is written inside any command or not
print("Yay!") #This is not written with indendations which means not it cam outside the Else command

applePrice = int(input("Enter the Price of Apple: "))
budget = int(input("Input your budget: "))

# if(applePrice <= budget):
#     print("Alexa, add 1 Kg Apples to the cart.")
# else:
#     print("Alexa, do not add Apples to the cart.")


#These are the Examples of Elif statements
if(applePrice - budget == 50):
    print("Alexa, add 1 Kg Apples to the cart.")
elif(budget - applePrice >= 70): #Elif is used to add more conditions between if and else it's just like ifelse/else
    print("You can buy atmost 2 KG apples")
elif(budget - applePrice == 0):
    print("Go back home, you pooor person!!")
else:
    print("Alexa, do not add Apples to the cart.")

#REMINDER - IF ANY CONDITION OF "IF"/"ELIF" MATCHES THE I/P THEN THE CODE WILL END AND THERE WON'T BE ANY FURTHER EXECUTION

num = int(input("Enter any number: "))
if(num<0):
    print("The Number is -ve")
elif(num == 0):
    print("The number is nither +ve nor -ve")#After giving conditions in if statement to i/p extra conditions we use elif
else:
    print("The number is +ve")

