#Loops are used to execute a group of statements a certain number of times
#Types - For Loops, While Loops, Nested Loops

#EXAMPLE 1
# name = 'Abhishek'
# for i in name:
#     print(i)
#     if(i == 'b'):
#         print("This is something special!!")


#EXAMPLE 2 this one is in list
# colors = ["RED", "GREEN", "BLUE", "YELLOW"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

#EXAMPLE 3 Range Function
# for k in range(1, 101): #You can give this function and the starting number will be one but the ending number will be 101-1 = 100
#     print(k)


# for k in range(5):#In this form the python will automatically as (0,5)
#     print(k)

# for k in range(0,10):
#     print(k + 1) #0+1, 1+1, 2+1,..., 8+1, 9+1

for k in range(-10, 12, 3): # An A.P. is formed here in (x,y,z) where,  
    print(k) #x = starting term, y = max. limit, and z = difference b/w 2 terms

