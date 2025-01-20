import os

for i in range(0,100):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
#To rename the files in OS we change it by using this command, bulk actions can be done