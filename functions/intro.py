# def hi():
#     print("hello world ")
#     print("-----------")
#     print("how are you today")
# hi()
# print("dummy msg ")
# hi()
# -------------------------
# def greet(name):
#     print("welcome ",name)
# greet("Aman")
# greet("Raman")
# --------------------------
# def sum(x,y):
#     s = x+y
#     print("sum is ",s)
# sum(12,2)
# sum(13,5)
# --------------------
# def voting(name,age):
#     if(age>=18):
#         print(name ,"you are eligible to vote")
#     else:
#         print(name, "you are not eligible to vote")
# voting('John',25)
# voting('Maria',12)
# ---------------------
# def highest(a,b,c):
#     if(a>b and a>c):
#         print("a is highest")
#     elif(b>c):
#         print("b is highest")
#     else:
#         print("c is highest")
#     # if(b>a and b>c):
#     #     print("b is highest")
#     # if(c>b and c>a):
#     #     print("c is highest")
# highest(101,12,13)
# highest(12,11,14)
# highest(12,111,14)
# -----------------------
# def voting(name,age):
#     if(age>=18):
#         print(name ,"you are eligible to vote")
#     else:
#         print(name, "you are not eligible to vote")
# voting('John',25)
# voting(age=54,name="Aman")
# -------------------
# def nationality(name,nationality="Indian"):
#     print(name," you are ", nationality)
# nationality("ankit","American")
# nationality("Ankita")
# ---------------------------
# def sum(*args):
    
#     s = 0 
#     for n in args:
#         s=s+n
#     print("sum is ",s)
# sum(12,13)
# sum(33,44,12,42)
# sum(1,2,3,3,5,67,4,1,23,3,2,32)
# ------------
# print(10/2)
# print(10%2)
# print(13%2)
def checkeven(n):
    if(n%2 == 0):
        print(n, "is even")
    else:
        print(n, "is odd")
checkeven(12)
checkeven(15)