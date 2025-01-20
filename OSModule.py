#Data Module help us control the data from our end.

import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")



#Using the above code I have created a folder name data and inside it several other folders for upt 100 days