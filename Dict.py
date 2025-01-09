#Used for mapping, dictionary are ordered
dic = {
    344: "Harry", #Key value: Pair
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}

# print(dic["Harry"]) This will give an error
print(dic[344])

info = {'name' : 'karan', 'age' : 19, 'eligible' : True}
print(info) #Using this I'll get the whole dictionary as it is
print(info['name']) #Value corresponding to name will be the O/P
#If the key doesn't exists then info['name'] will give an error
print(info.get('name')) #whereas info.get('name') will give us O/p as none, so it totally depends if you want to generate an error or let the code run smoothly
print(info.keys()) #Using this I'll get all the key values of the dictionary
print(info.values()) #Using this I'll get all the values corresponding to keys in an ordered manner

for key in info.keys():
    print(info[key]) #using this loop I'll get all  the pair values of the dictionary, corresponding to each key

for key in info.keys():
    print(f"The value correponding to the key {key} is {info[key]}")

print(info.items()) #Using this also key:value will get printed
for key, value in info.items():
    print(f"The value correponding to the key {key} is {info[key]}")
    print(f"The value correponding to the key {key} is {value}")
#Both the above lines will give the same output