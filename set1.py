# # cities = {"Ahmedabad","Vapi","Rajkot","Vapi","Ahmedabad"}
# # print(cities)
# lst = ["Ahmedabad","Vapi","Rajkot","Vapi","Ahmedabad"]
# cities_set = set(lst)
# print(cities_set)
# cities_set.add("Mumbai")
# cities_set.add("Vapi")
# print(cities_set)
# cities_set.update(["Dwarka","Gir"])
# print(cities_set)
# cities_set.remove("Mumbai")
# print(cities_set)

# # cities_set.remove("Mumbai123")   #throws err
# # print(cities_set)

# cities_set.discard("Mumbai123")  #no err 
# print(cities_set)

# for city in cities_set:
#     print(city)

s1 = {1,2,3}
s2 = {3,4,5}
print(s1|s2)
print(s1.union(s2))
print(s1& s2)
print(s1.intersection(s2))

print(s1-s2)
print(s1.symmetric_difference(s2))