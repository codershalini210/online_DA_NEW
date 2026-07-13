import statistics
# Sort students based on marks (ascending and descending).
students = {"s1":65,"s2":23,"s3":54}
# print("variance ", statistics.stdev(students.values()))
# print(dict(sorted(students.items(),key=lambda x :x[1])))
items =list(students.items())
print(items)
n = len(items)
for i in range(n):
    for j in range(0,n-i-1):
        # print(i,"---------",items[j][0])
        # print(items[j+1][0])
        if items[j][1]> items[j+1][1]:
            items[j],items[j+1] = items[j+1],items[j]
print(items)
sorteddict = dict(items)
print(sorteddict)