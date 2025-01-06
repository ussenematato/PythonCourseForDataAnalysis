# SETS
# sets are a type of collections like lists, tuples storing mixed data
# sets are enclosed within curly brackets and elements are written as comma-separated
# sets are unordered
# sets does not allow duplicates
list1 = [1,2,3,4,5,6,5,7,2,2,2,3]
print(type(list1))
print(len(list1))

set_1 = set(list1)
print(set_1)
print(len(set_1))

set_2 = {1,2,3,4,5}

# add
set_2.add("Moz")
print(set_2)

# remove
set_2.remove(1)
print(set_2)

# Set Operations
A = {0,2,4,6,8}
B = {1,2,3,4,5}

# union() --> |
print((A | B))
print(A.union(B))
print(len(A.union(B)))

# intercetion
print(A & B)
print(A.intersection(B))

# diference
print(A - B)
print(A.difference(B))

# simetric difference
print(A^B)
print()
A = [5,1,3,4,4,5,6,7]
B = [3,3,5,5,1,7,2]
list1 = set(A) & set(B)
print(sorted(list1))
print()

list1 = [5,1,3,4,4,5,6,7]
list2 = [3,3,5,5,1,7,2]
list1_as_set = set(list1)
i = list1_as_set.intersection(list2)
print(list(i))

print()

# Question 2
nums = set([1,1,2,3,3,3,4])
print(len(nums))
