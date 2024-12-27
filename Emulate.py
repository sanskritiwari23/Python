#Emulate do while loop in python
i = int(input("Enter the value of i: "))
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break
#We'll i/p some number and get the numbers get increased, checked and printed again and again
#Once the number gets divide by 100, we come out of the loop