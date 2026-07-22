# with open("data.txt","w") as
newcontent = ""
with open("data.txt","r") as file :
    content = file.read()

    for char in content:
        if(char in "aeiouAEIOU"):
            char="_"

        newcontent= newcontent+char
with open("data.txt","w") as file1:
    file1.write(newcontent)
    print("file updated")
    # print("total no of words in file ", len(words))