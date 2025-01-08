s = {2, 4, 2, 6}
#There is no reoccurance in a set, a set is a unordered collection of well defined objects
#sets are unchangable, I can't change any entry for a particular index, 
print(s)

info = {"carla", 19, False, 5.9, 19}
#The elements of a list occure in random numbers, so it is not possible to print anyhting as per index
print(info)

harry = {} #If we print this, it'll become a dictionary due to similar syntax, therefore it is better to write this way
harry = set() #This refers to an empty set
print(type(harry))

#To access the values of a set
for value in info:
    print(value) #The values will be printed randomyl and only single value will be displayed