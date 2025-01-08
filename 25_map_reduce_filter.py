import math
def area(r):
    return math.pi*(r**2)

radii = [1,2,3,4,5]
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

# we can use maps like this o reduce the code and have quick function
print(list(map(area, radii)))

# print(areas)

# CONVERT CELSIUS SCALE TO FARHENEIT
# F = 9/5*C + 32
temps = [("Mumbai", 35), ("Berlin", 12), ("Tokio", 25), ("Honk Kong", 31), ("Sydney", 30)]
print(type(temps))
print(len(temps))

cel_to_far = lambda data: (data[0], (9/5)*data[1]+32)
#  map(f, iterable)

map(cel_to_far, temps)
print(list(map(cel_to_far, temps)))

# FILTER FUNCTION -filter out the data
# filter(f, data)

import statistics

data = [1,2,3,4,5,8,7,12,2]

avg = statistics.mean(data)
print(avg)


filter(lambda x: x>avg, data) # filtering the number in data list > avg
print(list(filter(lambda x: x>avg, data)))

print("-"*5,"Areas > 10", "-"*5)
# print(list(map(area, radii)))
print(list(filter(lambda x: x>10,areas)))


# Getting rid of thr null/NaN values
print()
print('Getting rid of thr null/NaN values')
name = ['Satyajit', 'Neha',0, 'Namrata']
filter(None,name)
list(filter(None,name))
print(list(filter(None,name)))

print()
number = [12,19, 21, 0, 0.0, '',0, 55, 70, ""]
filter(None,number)
list(filter(None,number))
print(list(filter(None,number)))
print()

# REDUCE FUNCTIONS
# reduce(f, data)
from functools import reduce
# multiply all the items in a list
print("using reduce filter for a multiplier operator for all item in the list")
data = [1,2,3,4,5]

multiplier = lambda x,y: x*y
reduce(multiplier, data)
print(reduce(multiplier, data))

# In a traditional way could be like this:
data = [1,2,3,4,5]
prev = data[0]
for i in data:
    i = i*prev
    prev = i
print(i)

print()
print("using reduce filter for a sum_operator for all item in the list")
data = [1,2,3,4,5]
sum_op = lambda x,y: x+y
reduce(sum_op, data)
print(reduce(sum_op, data))