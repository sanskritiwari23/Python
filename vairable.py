#Vairable - It is like a container that holds the data. Creating vairable is like creating a placeholder in memory and assigning it some value
a = 12345678908653 #a is a int vairable
print(a)
b = "Harry" #if I want to print a string then using double court is imp
print(b) # b is a string vairable
c = True #C is a Boolean vairable
d= None #d is a none type vairable

print("\n")

#Datatype - Specifies the type of value a vairable holds
print("The type of a is ", type(a))#using this I can get to know the datatype of a vairable
print("The type of a is ", type(b))
print("The type of a is ", type(c))
print("The type of a is ", type(d))

print("\n")

z = complex(10, 1) #using this you can make complex numbers in the form of iota
print(z)
print(type(z))

print("\n")

list1 = [8, 2.3, [-4,5], ["apple", "Banana"]] #list is a colletion of different data elemets and a single list can contain elements of different datatypes as well
print(list1)
print(type(list1)) #list a mutable i.e. it can be changes

print("\n")

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
print(type(tuple1)) #Tuples are also a colletion of elements just like list but they are immutable i.e. it cannot change

print("\n")

dict1 = {"name":"Sakshi", "age":20, "canVote":True} #A dictionary is an unordered collections of data containing a Key:value pair. The Key:value pairs are enclosed within curly brackets
print(dict1)
print(type(dict1)) #Mappded Datatype

#In python everything is a object