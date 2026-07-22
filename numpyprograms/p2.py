import numpy as np 
sales = np.array([12000,15000,13000,14000,16000,12000])
# print(sales[sales>13000])
# print(sales[(sales>13000 )& ( sales< 16000)])
# print(sales[(sales>15000 )| ( sales< 13000)])
# print(sales[[2,5,1]])
# # print(sales[0])
# # sales[0]=16000
# # print(sales)
# print(sales[0:4])
# print(sales[4:])
# print(sales[:3])
# print(sales[2:5])
# print(sales[-1])

marks = np.array([
    [35,65,52],  # 00,01,02
    [56,45,65],   #10,11,12
    [25,12,30], #20,21,22
    [85,95,78] # 30,31,32
])
print(marks[marks > 35])
# print(marks[0:2])
# print(marks[:,0:2])
# print(marks[0:2,1:3])

# print(marks[0][0])
# print(marks[2][1])
# print(marks[:,0])