a = "!!!Harry!! !!!!!!! Harry"
print(a)
#*******Concept of Immutability - Strings are immutable but I can copy the same string and then make the changes in it
print(a.upper())#A new string is created and all the letter of old string "a" is in uppercase
print(a.lower())
print(a.rstrip("!")) #It strips/remove the trailing characters, which are at the last
print(a.replace("Harry", "John"))#It removes all the occurances of Harry in "a" variable into John
print(a.split(" "))#This changes the str into a list and it is compulsory to have spaces in the str
#['!!!Harry!!', '!!!!!!!', 'Harry'] This will be the O/P
blogHeading = "introduction to js"
blogHeading1 = "introduction tO jS"
print(blogHeading.capitalize())#This command will capitalize the first letter of the sentence
print(blogHeading1.capitalize())#It will convert all the other characters into lower case

str1 = "Welcome to the Console!!!"
print(str1)
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))# It helps to center the heading 

print(a.count("Harry"))#It will tell us the number of times a character occured in a str

print(str1.endswith("!!!")) #It tells if the str ends with the specified character asked by us??
print(str1.endswith("to", 4, 10)) #It helps us check weather the string from 4-10 ends with to or not??

str1 = "He's name is Dan, He is an honest man."
print(str1.find("is"))#It gives us the index of the first occurance of a given character in a string
print(str1.find("ishh"))#and if it is not present then it gives "-1"

print(str1.index("is"))#This will give me the index of 1st occurance
#print(str1.index("ishh")) #If this is not present then it'll give me error

str1 = "Welcome00ToTheConsole"
print(str1.isalnum())#It tells us weather the string is alphanumeric or not,i.e. it includes A-Z, a-z and 0-9 if any other characters are prestent then it returns false
print(str1.isalpha())#This only includes A-Z and a-z any other character will return false
print(str1.islower())#True if all the characters are in lower case otherwise false

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())#If all the elements are printable then return "True" otherwise false Eg below
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())#\n is not a printable element

str1 = "         " #using spacebar
str2 = "            " # using Tab
print(str2.isspace())#This command returns true if we have allocated some space using spacebar/tab otherwise false


str1 = "World Health Organization"
print(str1.istitle())#it returns true if 1st letter of each wordis capitale otherwise false
str2 = "To kill a mocking brid"
print(str2.istitle())#will get the answer as false

str1 = "Python is a Interepreted Language"
print(str1.startswith("Pyt"))#Just like Endswith but follows the rules for the starting character
#It dosen't matter if you write the whole word or some of the starting letters to check

str1 = "Python is a Interepreted Language"
print(str1.swapcase()) #It converst Lower case to Upper Case and Upper Case to Lower Case

str1 = "python is a interepreated language"
print(str1.title())#It converts all the starting letter of all the words of the sentence to uppercase to make it as a title