# tuples are ordered sequence of mixed data types
# tuples are writrn in comma separated elements with parenthesis

# t1 = (1,2,3,4)
# t2 = 1,2,3,4
# print(type(t1))
# print(type(t2))

# t = ('hello', 5, 5.5)
# print(len(t))
#
# print(t[0])

# Nested tuple --> tuple that have a tuple, a list at himself
# t1 = ('hello', 5, 5.5, [1,2,4])
# print(len(t1))
# print(type(t1[3]))

t2 = (1,) #--> tuple
t3 = (1) #--> int

# Indexing in tuple
t = ("Sofala", 10,"Python", 100, "Namaacha")
print(len(t))
print(t[2:])
print(t[2:4])

str = "HELLO WORLD"
print(str[6:])

# Slicing
print("Slicing")
print(t[-2:])

# Concatenation
tup1 = ("Welcome", "to", "today's")
tup2 = ("class", "on", "python")

tup3 = tup1 + tup2
print(tup3)

# min, max some sum fuctions
l1 = [2,4,6,8]
print(min(l1))
print(max(l1))
print(sum(l1))

# Immutability
t = ("Hello!!","Welcome", 5, 10, "world", "of", "Analytics!!")
t1 = ("to", "the")

new_tuple = t[0:2] + t1 + t[-3:]
print(new_tuple)
print((len(new_tuple)))

# QUESTION
t = ("disco", 12, 4.5)
print(t[0][2])

# sorting the tuples
t = (2,3,8,5,4,1)
new_var = sorted((t))
print(new_var)
print(type(new_var))

t = tuple(new_var)
print(t)
print(type(t))

# Nested tuples
t = (1,5, "Hello", "World", ("Java", "Python"))
print(t[4][0])
print(t[-1][-2])

# How to acess Java????
# QUESTION 1
t = (1,2,4,3)