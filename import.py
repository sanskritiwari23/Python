# import math

# result = math.sqrt(9)
# print(result)

#instead of importing the whole package I can do one more thing
# from math import sqrt, pi
# result = sqrt(9) * pi
# print(result)

#from math import * this whole statement can also be used to import from math module, however this is not suggested as this statement will import each and everything and lead to a lot of confusion

# another way of importing
# import math as m = using this you can use the math lib. in the code by just using "m" which will make you task easy

import math
print(dir(math)) #By using this I'll get the print of all the functionalities in math

#If I'll create a file of any name in the same folder then also I can use it as a module and import it here