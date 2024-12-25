#MatchCase = It is just like switch case statements in C/C++

x = int(input("Enter the value of x: "))
match x: #This statement tells us about the entity we will be matching
    case 0: #This checks weather x == 1
        print("x is zero")
    case 4: #This checks weather x == 4
        print("x is 4")
    # case _:#This one is default, i.e. this will execute when other cases does not match
# NOTE - If any particular case got matched with the I/P it will stop executing and give us the O/P
    #We can also use if statements inside the matchcase
    case _ if x!=90:
        print(x, "it is not 90")
    case _ if x!=80:
        print(x, "It is not equal to 80")
    case _:
        print("Ignore")



print("HEllo") #This statement is outside the match-case