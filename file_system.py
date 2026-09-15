
import os 

user = input("Give me something\n")
with open("something.txt","a") as f:
    f.write(user + "\n")
for i in user:
    print(i)
# myNameFiles = open("name.txt","rt")

# print(myNameFiles.read())

# with open("name.txt","rt") as myNameFiles:
#     print(myNameFiles.read())


# myNameFiles = open("name.txt","a")
# myNameFiles.write("\n German")

# with open("name.txt","a") as myNameFiles:
#     print(myNameFiles.write("\n German"))