ep1 ={122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566:90}

#This helps update all the values of ep2 into ep1
ep1.update(ep2)
print(ep1)
#This clears all the values of ep1 and makes it empty
ep1.clear()
print(ep1)
#This is how you can create an empty set
ampt = {}
print(ampt)

#This one pop any particular itme from the dict. and let the other itmens be as it is
ep1 ={122:45, 123:89, 567:69, 670:69}
ep1.pop(122)
print(ep1)

#This method will only remove the last value of the dictionary and you can input the key value in this, otherwise it'll give an error
ep1 ={122:45, 123:89, 567:69, 670:69}
ep1.popitem()
# del ep1 #This command will delete the whole dictionary, and give me an errro
del ep1[122] #This will delete only that particular entry
print(ep1)

#Keep reading python dictionary documentation - It'll keep you updated regarding what's new with python dicstionary