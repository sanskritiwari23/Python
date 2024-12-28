#List Method
l = [11,45,1,2,4,6,1,1]
# print(l)
# l.append(7) #Using this we can add an element in the given list

#l.sort() #This helps arranging the list in assending order

# l.sort(reverse=True) #This halps arranging the list in decending order

# l.reverse()#Reverse the original list

# print(l.index(1))#It provides me the index of the element "1" in the list 
#If we won't give the element inside index it'll give us error
#It is also imp to remeber taht it'll provide the index of 1st occurance of the list item

# print(l.count(1)) #It helps me get the numer of time a particular element occured in the list

# m = l
# m[0] = 0
# print(l) 
#By using this there will be changes in the 'l' list as well, which we do not want
# we want to copy the list, therefor below should be used

# m = l.copy()
# m[0] = 0
# print(l)
# print(m)
#Using this there will be no changes in the list l and a new copied list m will be created
#Which is same as l and the changes then will be in m not l

#To insert a particular element in any given index
# l.insert(1,899) #899 gets insert at index 1
# print(l)

#ISka mtlb h ki m ko kholo or l k age waisa ka waise extend krdo
m = [900,1000,1100]
# I can even use one more method to merge the 2 lists, wrna there will be changes in l list
k = m + l #Concinating the list
print(k)
# l.extend(m)
print(l)
print(m)