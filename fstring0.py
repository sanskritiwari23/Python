#f-string is used for formatting the string in python, it has solved one of the biggest problem in python programming
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"

print(letter.format("Raji","India"))
print(letter.format(country,name))

letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country,name))

#The above code is not that convenient
print(f"Hey my name is {name} and I am from {country}")
#Here it'll take the value of name and country by it's own, without any issue

price = 49.09999
txt = f"For only {price:.2f} dollars!" #This will roundoff the value and give us the output
print(txt)

print(f"{2*30}") #Ye mujhe directly answer de dega as a string

print(f"This is how we make fstring in python: Hey my name is {{name}} and I am from {{country}}") #Ese m ye uss format m aa jyga, jisme ye actually hai mtlb jaisa likha jta h waisa, without any error