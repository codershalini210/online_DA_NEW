# c1   c2    and     or
# T    T      T       T
# T    F      F       T
# F    T      F       T    
# F    F      F       F

# age = int(input("Enter age"))
# if(age<0 or age>120):
#     print("invalid age")
# elif(age>17):
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")
# -------------------
# age = int(input("Enter age"))
# if(age>= 0 and age< 120 ):
#     if(age>=18):
#         print("Eligible to vote")
#     else:
#         print("not Eligible to vote")
# else:
#     print("invalid age")
no = int(input("Enter any no "))
if(no%2 == 0):
    print(no,"is even ")
else:
    print(no,"is odd")