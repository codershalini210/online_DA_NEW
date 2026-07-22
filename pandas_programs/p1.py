import pandas as pd
students =['a','b','c']
marks=[25,65,85]
data = pd.Series(marks,index = students)
print(data)
# users = pd.Series(['John','Ron','Maria','Tania'])
# users = pd.Series(['John','Ron','Maria','Tania'],
# index=['s1','s2','s3','s4'])
users = pd.Series(['John','Ron','Maria','Tania'])
users.index=['s1','s2','s3','s4']
print(users)
# print(users[0])
# print(users[-1]) #this will throw err
print(users['s1'])
print(users['s4'])