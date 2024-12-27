#List are mutable, I can make changes in a list after creating a list
# l = [3,5,6, "Harry", True]
# print(l)
# print(type(l)) #Just like strind, ordered collection of datatypes
# print(l[0])
# print(l[1])
# print(l[2])
# print(len(l))
# print(l[-3]) #-ve Indexing 
# print(l[len(l)-3]) #+ve indexing
# print(l[5-3]) #+ve indexing
# print(l[2]) #+ve indexing

#How to check weather an element is present in a list or not
# if 7 in l:
#     print("Yes")
# else:
#     print("NO")

# #Same thing applies for strings as well!!
# if "Ha" in "Harry":
#     print("Yes")

# print(l)#All the elements could be printed
# print(l[:])#All elements gets printed
# print(l[1:])#Element starting from index 1 will be printed
# print(l[:3]) #Elements till indexing 3 will be printed
# print(l[1:-1])
# print(l[1:4]) #4th indexing  element will not be included


#Jump Index
# l = [3,5,6, "Harry", True, 6, 7, 2, 32, 345, 53]
# print(l[1:8])
# print(l[1:8:2])

#List Comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
