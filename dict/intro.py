students = {"a":52,"b":25,"c":45}
students["d"] =85
print(students)
students.pop("b")   #delte key and its value if key is present
#otherwise errors
print(students)

print("a" in students)
# print(students.get("a1"))  #give none when key is not present
# for k,v in students.items():
#     if(v>=35):
#         print(f"name :{k} ,result :Pass, marks: {v}")
# for k,v in students.items():
#     print(f"marks of {k} : {v}")
# for s in students.values():   #for values
#     print(s)

# for s in students:   #for keys
#     print(s)

# print(students["a"])
# students["a"]=60
# print(students["a"])
# print(students)