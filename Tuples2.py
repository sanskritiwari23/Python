#Manipulating Tuples
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3) #Count the number time a particular element occured
print('Count of 3 in tuple is: ', res)

#les = tuple1.index(3)
les = tuple1.index(3, 4, 8) #Here we have to check the occurance of 3, after slicing the tiple from index 4 to 8
#In the above line, the system will interpreate indexs as [4,8)
print('Tell us the first occurance of 3: ', les) #it will tell me the 1st occurance of any number in the tuple

ces = len(tuple1)
print('Print the lenght of the tuple: ', ces)

#If you ever want to do changes in the tuple, first you need to copy it in  a list and make changes and then copy it into another list.
#Dirctly it is not at all possible to make changes in a tuple