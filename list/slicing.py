# marks= [12,32,52,34,23,56]
# print(marks)
# print(marks[0:3])
# print(marks[2:5])
# print(marks[2:])
# print(marks[:4])
# print(marks[::-1])
# list1=[1,2,3,4,5,6,7,8]
# l = int(len(list1)/2)
# sub1 = list1[0:l]
# sub2 = list1[l:]
# print(list1)
# print(sub1)
# print(sub2)
# temp = list1[0]
# list1[0]=list1[-1]
# list1[-1]=temp
# print(list1)
# ----------------
students =[]
students.append("Raj")
students.append("John") #add element to the end of list
print(students)
students.extend(["MAria","Sam","Ron"])  #add multiple values at the end of list
print(students)
students.remove("Sam")  #removes first occurance of given value
print(students)
students.insert(2,"Alexa") #insert before particular index
print(students)

# students.sort() #sort list in asc order
# print(students)
# students.sort(reverse=True)   #sort list in des order
# print(students)

# students.reverse()  #reverse list 
# print(students)

students.pop()   #remove last inserted value
print(students)