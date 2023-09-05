# dict1 = {}
# b = set()
# print(dict1, type(dict1))
# print(b, type(b))

#  Both below are set because it's not containing key value pair
# dict1 = {12,212}
# print(type(dict1))
#
# b = {12, 12, 12, 2, 41}
# print(type(b))

dict1 = {"good" : "Something pleasant", "fetch": "to bring", "1": "The number 1"}

marks = {"Ashish": 62, "Rahul": 41, "Ashwin": 51}

print(dict1["good"])
print(marks["Rahul"])
marks["Priya"] = 41
print(marks)

print(marks.get("Priyanka Chopra"))
print(marks.keys())
print(marks.values())
print(marks.items())

