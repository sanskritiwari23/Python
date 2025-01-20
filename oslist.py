import os

folders = os.listdir("data")

print(os.getcwd()) #Get directory
os.chdir("/Users") #change directory
print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))