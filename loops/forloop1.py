# for i in [12,25,54,45]:
#     print(i)
# names = ["Anit","Geeta","Meet","Maria"]
# for name in names:
#     print("Welcome ", name)
# --------------
# for i in range(1,11):
#     print(i)
# ---------------
# print(list(range(1,11)))
# print(list(range(1,11,3)))
# print(list(range(10,0,-2)))
# --------------
# n = int(input("enter any no "))
# for i in range(1,11):
#     print(i*n)
# ----------------
# for char in "Promise":
#     print(char)
# -----------------
# username = input("Enter your name ")
# vowelcount = 0 
# for ch in username:
#     if ch in "aeiouAEIOU":
#         vowelcount = vowelcount+1

# print("total no of vowels in ", username ,"is ",vowelcount)
# sals = [23000,54000,23400,76500,43650]
# lowsal = 0
# highsal = 0 
# for sal in sals:
#     if(sal>=50000):
#         highsal=highsal+1
#     else:
#         lowsal= lowsal+1
# # print("no of persons with high salary ", highsal,"no of persons with low salary",lowsal)
# print(f"no of persons with high salary {highsal} no of persons with low salary {lowsal}")
names =["sam","Ron","Maria","oxana"]
marks = [ [33,65,45],
         [44,55,66],
         [76,26,77],
         [76,54,87]]
avgmarks = []
passstudents =[]  
failstudents=[]
for i in range(0,len(names)):
    m = marks[i]
    P = True
    avg=sum(m)/len(m)
    avgmarks.append(avg)
    for mark in m :
        if(mark<35):
            P=False
    if(P):
        passstudents.append(names[i])
    else:
        failstudents.append(names[i])
print("all students", names)
print("pass students",passstudents)
print("fail students",failstudents)
print("avg marks",avgmarks)
