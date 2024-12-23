#String = Anything that you enclose between single or double quotation marks is considered as string.
#A String is essentially a sequence or array of textual data.
#Strings are used when working with Unicode Characters

name = "Raji"
friend = "Rohan"
anotherfriend = 'Lavesh'

plus = '''He said,
Hi Harry
hey I am good
I want to eat and apple'''
#By using '''Sentence''' triple quots we can write multi-line string in one go
print(plus)

apple = " \"I want to eat an apple\" "
#print(apple)
print("Hello " + name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
#If I'll use another print statement for [4] it will thow an error 'coz there are no more elements in the str

print("Let's use a for loop \n")
#Looping through the Strings
for character in name:
    print(character)

print("Let's use a for loop \n")
for character in plus:
    print(character)