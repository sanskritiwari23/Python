s1 = {1, 2, 3, 6}
s2 = {5, 6, 7}

print(s1.union(s2))
print(s2.union(s1))
#both will provide the same output no matter what

# s1.update(s2) #Using this the values of s2 gets merged into the values of s1, but s2 remains untouched
print(s1, s2)

print(s1.intersection(s2)) #Common values of both the sets will be the o/p
s1.intersection_update(s2)
print(s1) #Using this the 1st set will get updated and only the intersecting values of boht the sets will get saved in s1, s2 remains untouched

#Symmetric Difference - Deleting the common values of 2 sets
s1 = {1, 2, 3, 6}
s2 = {5, 6, 7}
print(s1.symmetric_difference(s2)) #The common value 6 is deletd from the union of this set

#difference() and difference_update()
#The basic meaning of this command is A - B
s1 = {1, 2, 3, 6}
s2 = {5, 6, 7}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)

#To check if the 2 sets are disjoint or not, i.e. they do not have anything in common
s1 = {1, 2, 3, 6}
s2 = {5, 6, 7}
print(s1.isdisjoint(s2)) #This will give answer as false
s1 = {1, 2, 3}
s2 = {5, 6, 7}
print(s1.isdisjoint(s2)) #This will give answer as True

#To check if 1 set is a super set of another set, that is both the values of the 2nd set must be there in the 1st set
s1 = {1, 2, 3, 6, 5, 7}
s2 = {5, 6, 7}
print(s1.issuperset(s2)) #This will give answer as True
print(s2.issuperset(s1))#This will give answer as False

#To check the subset
s1 = {1, 2, 3, 6, 5, 7}
s2 = {5, 6, 7}
print(s1.issubset(s2)) #This will give answer as False
print(s2.issubset(s1)) #This will give answer as True

#To add an element into the set
s1 = {1, 2, 3, 6, 5, 7}
s1.add(10)
print(s1)
#To remove/discard a particluar item in a set
s1.remove(10) #If we asked to remove an element which is not present in the set then this will raise an error
print(s1)
s1.discard(3) #If we asked to remove an element which is not present in the set then this will not raise an error
print(s1)

#Pop() - This is used to pop out any element from the set and it is not confirme that which element will get popped and give me the value that is popped out
s1 = {1, 2, 3, 6, 5, 7}
leh = s1.pop()
print(leh)
print(s1.pop())

#del - It is used to delete an entire set 
s1 = {1, 2, 3, 6, 5, 7}
del s1
# print(s1) #Here it gives error 'coz it does not exists not, after deletion

#clear - Used to clear the times of an set and then prints an empty set
s1 = {1, 2, 3, 6, 5, 7}
s1.clear()
print(s1)
