# open the file using open() command, arguments taken are file name and mode in which you want to open it. 'r' = for reading, 'w' = for writing and 'a' = for appending

#READING 
# f = open('myfile.txt', 'rb')
# #print(f)
# text = f.read()
# print(text)
# f.closed

#WRITING
# f = open('myfile.txt', 'w')
# f.write('Hello, world!')
# f.close()

#ANOTHER METHOD TO MAKE IT EASIER
with open('myfile.txt', 'a') as f:
    f.write("Hey I am inside with")
#Using this the file will close automatically and tere won't be any need of using the close statement


#1. read(r): This mode opens the file for reading only and gives an error if the file does not exists. This is the default mode if no parameters are passed
#2. write(w): This mode opens the file for writing only and creates a new file if the file does not exists
#3. append(a): This mode opens the file for appending only and creates a new file if the file if the file does not exists
#4. create(x): This mode creates a file and gives an error if the file already exists
#5. text(t): Apart from these modes we also need to specify how the files must be handed. t mode to handle in the form of text file. Default will be rt.
#6. binary(b): Used to handle binary files(images, pdfs, etc)