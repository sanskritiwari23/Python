#Good Morning Sir

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
# timestamp = time.strftime('%H')
# # print(timestamp)
# # timestamp = time.strftime('%M')
# # print(timestamp)
# # timestamp = time.strftime('%S')
# # print(timestamp)

#While comparing the time it is very imp to compare it in the form of HH:MM:SS
#There must always be '' used while comparing the time
if(timestamp < '12:00:00'):
    print("Good Morning")
elif(timestamp < '17:00:00'):
    print("Good Afternoon")
else:
    print("Good Evening")


# https://docs.python.org/3/library/time.html#time.strftime

#Another method using int!!!!
timestamp = int(time.strftime('%H'))
if(timestamp < 12):
    print("Good Morning")
elif(timestamp < 17):
    print("Good Afternoon")
else:
    print("Good Evening")
