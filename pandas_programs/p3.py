import pandas as pd
# s1 =pd.read_excel("../dummy.xlsx")
s2 = pd.read_excel("../dummy.xlsx","Sheet2")
# print(s1)
# print(s2.info())
# print(s2.describe())
print(s2.shape)
print(s2.dtypes)
print(s2.columns)