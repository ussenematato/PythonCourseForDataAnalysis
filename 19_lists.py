# list1 = ["Moz", 7, "Mpt"]
# print(list1)
# print(type(list1))
#
# cust_info = ["Ussas", 29, "Mpt", 100000, 120000, "1GB"]
# print((cust_info))
# type(cust_info)
#
# list2 = [list1, cust_info]
#
# print(list2)
#
# # Indexing
#
# print(list2[0][1])
# # print(type(list2[0][1]))
#
#
# # Slizing
# print(list2[-1])
# print(list2[-1][1])

# list concat
list1 = [1,2,3,4]
list2 = [5,6,7,8]

new_list = list1 + list2
print(len(new_list))
print(new_list)

# add two elements to an existing list
list3 = [1,2,3,4]
new_list = list3 + [8,9]
print(new_list)

# Membership in lists & tuples
list3 = [1,2,3,4]

print(1 in list3)
print(5 in list3)

# Mutability
list1 = ["Maths", "Physics", "Chemistry", "Biology"]
print(list1[3])

list1[3] = "Computer Science"
print(list1)

# extend() function --> It extends the list
list1 = [1,2,3,4]
list1.extend([5,6])
print(list1)
print(len(list1))

# append() function --> Its append as new element in the list
list1 = [1,2,3,4]
list1.append([5,6])
print(list1)
print(len(list1))

# del command
print("delete command")
list1 = [1,2,3,4]
print(list1)
del list1[2]
print(list1)

# pop() - deletes the object based on the index value
# Default --> Removes the last element
print("Pop")
list1 = [11,22,33,44]
print(list1)
list1.pop(2)
print(list1)

# remove() - deletes the object based on the value
print("Remove")
list1 = [1,2,3,4]
print(list1)
list1.remove(3)
print(list1)


print()
print("Sorting")
# Sorting
A = [9,5,2]
print(A)
A.sort()
print(A)

print()
# Difference between sort & sorted
print("Sort")
A = ["Oranges", "Strawberry", "Mango"]
B = A.sort()
print(A)
print(B)
print()
A = ["Oranges", "Strawberry", "Mango"]
A.sort()
print(A)

print("Sorted")
A = ["Oranges", "Strawberry", "Mango"]
B = sorted(A)
print(A)
print(B)

# Shallow copy
A = ["Oranges", "Strawberry", "Mango"]
B = A
print(B)
print(A)

# Diferent way to copy --> Its doesn't deppends on A anymore
A = ["Oranges", "Strawberry", "Mango"]
B = A[0:3]
A.pop()

print(B)
print(A)

# Description
# Split string input_str = 'Kumar_Ravi_003' to person's second name, first name and unique
# costumer code, In this example, second_name= 'Kumar', first_name='Ravi', costumer_code='003'.
# A sample output of the input 'Kumar_Ravi_003'

input_str = 'Kumar_Ravi_003'
print(input_str)

str1 = input_str[0:5]
print(str1)
str2 = input_str[6:10]
print(str2)
str3 = input_str[11:]
print(str3)

print()
# Other way using split method
input_str = 'Kumar_Ravi_003'
list1 = input_str.split('_')
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])