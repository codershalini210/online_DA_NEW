import numpy as np
sales1 = np.array([25000,63202,35000,45210,58621])
sales2=np.array([24000,56212,34000,46210,62541])
bonus = np.array([2,5,6,3,4])

print("total sales:",sales1+sales2)

print("diff",sales1-sales2)
print(sales1*bonus)
print(sales2/bonus)
print("modulus of sales1 and bonus", sales1%bonus)
print("modulus of sales2 by 4",sales2%4)
print(bonus ** 3)

# marks = np.array([35,12,18,75,85,65,25])

# increasedmarks = marks+5
# print(increasedmarks)
# # ----------------
# decreasedmarks = marks-2
# print(decreasedmarks)

# print(marks*2)
# print(marks/2)