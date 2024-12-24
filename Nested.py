#Nested Loops using Python

num = int(input("Enter the Number: "))
if(num < 0):
    print("Number id -ve")

#From here we started the nested loop and the statements are nested inside the elif statement
elif(num > 0):
    if(num<=10):
        print("The number is less than 10")
    elif(num >10 and num <=20):
        print("The number is between 10 and 20")
    else:
        print("The number if greater than 20")

else:
    print("The number is nither +ve nor -ve")