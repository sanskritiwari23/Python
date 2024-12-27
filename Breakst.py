#The break statemtn enables a program to skip over a part of the code. 
#A break statement terminates the very loop it lies within.
# for i in range(12):
#     print("5 x", i+1, "=", 5 * (i+1))
#     if(i==9):
#         break #Break statement will say "Iss loop ko chorr k nikal jao"

# print("Loop ko chorr k nikal gya")
#Breaking out of the loop

for i in range(12):
    if(i==9):
        print("Skip the iteration")
        continue #Continue helps us skip an iteration and let the code run in the same way
    print("5 x", i, "=", 5 * (i))
