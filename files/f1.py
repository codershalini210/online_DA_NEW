file = open("data.txt","r")
# content = file.read()   #read whole file
# content = file.read(15)   #read first 15 chars of file
# print(content)
# print(file.readline())
# print(file.readline())
# print(file.readline())
lines = file.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line)
# ----------------------
# for index in range(len(lines)-1,-1,-1):
#     print(lines[index])
file.close()