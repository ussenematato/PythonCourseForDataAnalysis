# x = 101
# if x % 2 == 0:
#     print(x, "is an even numaber")
# else:
#     print(x, "is an odd number")
# ----------------------------------------

# x = int(input("Enter your number"))
# if x % 2 == 0:
#     print(x, "is an even number")
# else:
#     print(x, "is an odd number")

# --------------------------------------------------
# allow: greater than 18 & less than 50 years of age
# x = int(input("Enter your age: "))
# if x < 18 or x > 50:
#     print("Sorry!! You are not allowed in the party")
# else:
#     print("Welcome to the party")

# ---------------------------------------------------

#### PROGRAM TO PROVIDE DISCOUNTS/OFFERS
# shopping_amount = int(input("Input your billed amount: "))
# if shopping_amount >= 5000:
#     print("You have won a voucher of 1000$")
# elif shopping_amount >= 2500:
#     print("You have won a voucher of 500$")
# else:
#     print("OOPS! No vouchers")
# ------------------------------------------------------

#### ITERATIONS
# Iterate over a list of integers
list_1 = [10, 20, 30, 40, 50]
for i in list_1:
    print(i)
# ------------------------------------------------------
print()
# Iterate over a list of strings
str_1 = "India"
for i in str_1:
    print(i)

# -----------------------------------------------------
print()
# Iterate over a dictionary
studant_data = {1: ["Sam", 25], 2:["Sharma", 21], 3:["Ravi", 23], 4:["Shalu", 23], 5:["Sid", 22]}
for i in studant_data.items():
    print(i)

for i,j in studant_data.items():
    print(i)

for i,j in studant_data.items():
    print(j)

# -----------------------------------------------------
print()

# Iterate over a range of values
for i in range(1,5):
    print(i)
# -----------------------------------------------------
print()

# COMPREHENSIONS
list_1 = ["Automobiles", "Honda", "Benz", "Maruti", "Kia"]
list_2 = []
for i in list_1:
    list_2.append(i)
print(list_2)
# -----------------------------------------------------
print()
list_1 = ["Automobiles", "Honda", "Benz", "Maruti", "Kia"]
list_2 = []
for i in list_1:
    list_2.append(len(i))
print(list_2)
# ---------------------or--------------------------------
print()
list_1 = ["Automobiles", "Honda", "Benz", "Maruti", "Kia"]
list_2 = [len(i) for i in list_1]
print(list_2)
# ---------------------or--------------------------------
print()
list_1 = ["Automobiles", "Honda", "Benz", "Maruti", "Kia"]
d = {i: len(i) for i in list_1}
print(d)
# ---------------------or--------------------------------
print()
list_1 = ["Automobiles", "Honda", "Benz", "Maruti", "Kia"]
d = {}
for i in list_1:
    d[i] = len(i)
print(d)