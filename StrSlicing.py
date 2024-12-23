name = "harry,Shubham"
print(name[0:5])
#It is written in inclusive manner but it is interepreated as [0:5)
#We can find the lenght of a string using len() functions
print(len(name))

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])
print(fruit[:4]) #Python will automatically take "0"
print(fruit[0:]) #By dafault it will print all the letters

# print(fruit[]) = This will give error
print(fruit[0:-3]) #Here it will take the whole lenght of the str and then subtract is
#i.e. it will become [0:len(fruit)-3] => [0:2]

print(fruit[-1:-3])#This will become [len(fruit)-1:len(fruit)-3] => [4:2] jo bina sar pair ki bt h therefore no o/p
print(fruit[-3:-1])#This will become [len(fruit)-3:len(fruit)-1] => [2:4] which is a valid syntax

#Quick Quiz:
nm = "Harry"
print(nm[-4:-2]) #This will become [len(nm)-4:len(nm)-2] => [1:3]
#Output will be "ar"