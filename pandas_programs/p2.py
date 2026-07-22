import pandas as pd 
# data = pd.DataFrame({
#     "month":["Jan"],
#     "sales":[25000]
# })
# print(data)
emps = pd.DataFrame({
    "names":["john","Ron","maria","Tania","sam"],
    "salary":[25000,65200,45203,45211,36222]
})
# emps["salary"] = emps["salary"]
emps["OA"] = emps["salary"] * 0.1
emps["PF"] = emps["salary"] *0.05
emps["net salary"]=emps["salary"] +emps["OA"] - emps["PF"]

# print()
# emps=emps.rename(columns={"names":"Emp name","salary":"Basic pay"})
# emps.rename(columns={"names":"Emp_name","salary":"Basic_pay"},inplace=True)
print(emps)
# print(emps["Emp_name"])
# print(emps.iloc[0]["Emp_name"])
# data = pd.DataFrame({
#     "name":['s1','s2','s3'],
#     "marks":[34,67,43]
# } ,index=['a','b','c'])
# print(data)
# print(data.loc['a'])
# print(data.iloc[0])