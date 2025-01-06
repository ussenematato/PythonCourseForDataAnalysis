# creating a dictionary
d1 = {"Mozambique": "MZN", "USA": "USD", "India": "INR", "Hong Kong": "HKD"}
print(type(d1))
print(len(d1))

# Accessing the value using keys
print(d1["Mozambique"])

# Replacing the value for a key in a dictionary
d1["India"] = "NEW"
print(d1)

# Inserting a new key-vlue pair
d1["Japan"] = "YEN"
print(d1)

# deleting a key value pair
del d1["Japan"]
print(d1)

# Sorting a dictionary
print(sorted(d1))

# values() method
print(d1.values())

# keys() method
print(d1.keys())

# get method
print(d1.get("India"))

# update() method
d1.update({"India": "Rs"})
d1["India"] = "Rs"
print(d1)

# Practice Codes
# key: emp id
# values: name, age, profession
Employee_data = {101:['Shiva', 24, 'Content Strategist'] ,102:['Udit', 25, 'Content Strategist'], 103:['Ussas', 27, 'Data Analytics']}
print(type(Employee_data))
print(Employee_data)

print()
print(Employee_data[103])
print(Employee_data[103][2])

# question nr2
dict_1 = {"Python": 40, "R": 45}
print(dict_1)
del dict_1["R"]
print(dict_1)

# Question 3
d = {'Python': 40, 'R':45}
print(list(d.keys()))
print(list(d.values()))

# Question 4
input_dict = {'Name': 'Monty', 'Profession': 'Singer'}

if "Label" in input_dict.keys():
    print(input_dict.keys())
else:
    print("NA")

print()
# Question 5
input_dict = {"Jack Dorsey": "Twitter", "Tim Cook": "Apple", "Jeff Bezos": "Amazon", "Mukesh Ambani": "RJIO"}
print(sorted(input_dict.keys()))
print(sorted(input_dict.values()))

# Or convert to a list and order
new_list = (input_dict.values())
print(sorted(new_list))