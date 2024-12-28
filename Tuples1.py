tup = (1, 5, 6, 76, 342, 32, "green", True)
print(type(tup), tup)

tup = (1) #If we put single element without a coma so python will take it as integer
print(type(tup), tup)
#Therefore
tup = (1,) #Put coma so it will then be a tuple
print(type(tup), tup)

#Tuples are always in () and list in [], and tuples are immutable, i.e. I can't make changes in them
#different datatype can also be used in a single tuple

#In this manner I can print the element of any particular index of the tuple
tup = (1, 5, 6, 76, 342, 32, "green", True)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(len(tup))
#Same -ve idexing concept is used as list

if 34 in tup:
    print("Yes 342 is present in this tuple")
else:
    print("Age Bhado")

#We can do slicing in the tuple as well, but here a new tuple will be formed and there will be no changes in the original tuple
tup2 = tup[1:4]
print(tup2)