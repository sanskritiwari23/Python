#Exception handling is the process of responding to unwanted/unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program

a = input("Enter the number: ")
print(f"Multiplixation table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid input")

#Using the code above will let us print the upcoming lines, irrespective off wrong input and occurance of error
print("Some imp lines of code")
print("End the program")

#In python we can even resolve any praticular kind of error
try:
    num = int(input("Enter and integer: "))
    a = [6, 4]
    print(a[num])
except ValueError:
    print("NUmber entered is not an integer")
except IndexError:
    print("Index Error")