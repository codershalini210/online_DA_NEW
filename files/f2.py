# file = open("file1.txt","w")
# file = open("file1.txt","a")
# line = input("Enter text to write in the file")
# file.write(line+"\n")
# file.close()
# print("data added successfully")
with open("file1.txt","r") as  file:
    file.seek(5)
    # file.write("New line 123\n")    
    # -------------------------------
    # print(file.tell())
    content = file.readline()
    # print(file.tell())
    print(content)