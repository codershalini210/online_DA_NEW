# def demo():
#     x=10  #this is local
#     print("x is ",x)
# demo()
# print("x is ", x)   #this gives err
# ----------------------
# x=10  #this is global
# def demo():
   
#     print("x is ",x)
# demo()
# print("x is ", x)   
# //////////////////////
x=10  #this is global
def demo():
    global x
    x=20
    print("x is ",x)
demo()
print("x is ", x)   