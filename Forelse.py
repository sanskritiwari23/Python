#Python allows else keyword to be used with the for and while loop too. 
# for i in range(5):
#     print(i)
# else:
#     print("Sorry no i")

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")
#This this loop else will not be printed, else means that the loop has executed successfully, but after taking a break it justifys that the loop ended in between and will not run now
i = 0
while i<7:
    print(i)
    i = i + 1
    if i == 4:
        break
else:
    print("Sorry no i")
#Same thing will be done with while loop as well in the same manner