import numpy as np

sales = np.array([
    [10000,12000,15000],
    [11000,13000,16000],
    [12000,14000,17000]
])
# print(np.sum(sales,axis=0))
# print(np.sum(sales,axis=1))
print(sales[0:2,0:2])
# print(np.max(sales[0:2,0:2],axis=1))
#  find max of first row
# find min of last row 
# find avg of first column
# find median of last column
