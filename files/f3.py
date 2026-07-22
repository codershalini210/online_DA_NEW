import os
# print(os.path.exists("file1.txt"))
# print(os.path.exists("file11.txt"))
if(os.path.exists("file1.txt")):
    os.remove("file1.txt")
    print("file deleted")
    # with open("file1.txt","r") as file :
    #     print(file.read())
else:
    print("file not exits")