name = input("Enter your name ")
marks = int(input("Enter marks "))
if(marks>100):
    print("invalid marks")
elif(marks>=60):
    print(name,"passed in Ist division")
elif(marks>=45):
    print(name,"passed in IInd division")
elif(marks>=35):
    print(name,"passed in IIIrd division")
elif(marks>=0):
    print(name,"Fail")
else:
    print("Invalid marks ")
# ----------------------------
# name = input("Enter your name ")
# age = int(input("Enter age"))
# if(age >=18):
#     if(age<120):
#         print(name,"you are eligble to vote")
#     else:
#         print("Invalid age")
# else:
#     if(age>=0):
#         print(name,"you are not eligible to vote")
#     else:
#         print("Invalid age")
# ---------------
# marks = int(input("Enter your marks "))
# if(marks>34):
#      print("Pass")
# else:
#      print("Fail")
