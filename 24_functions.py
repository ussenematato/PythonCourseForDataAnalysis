from django.db.models.fields import return_None


def even_odd(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num,"is an odd number")
even_odd(2)
print()

# FACTORIAL
# 4! = 4*3*2*1
# n!= n*n-1*n-2...1

def fact_number(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return print(fact)

fact_number(5)

def func_1(name, age = 30):
    print("Name:", name)
    print("Age:", age)

func_1("Ussas")

# LAMBDA FUNCTIONS


# FIBONACCI
def fib(n):
    # if n <= 0:
    #     print("O valor de n deve ser positvo")
    # elif n == 0:

    a = 0
    b = 1
    print(a)
    print(b)
    for _ in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fib(10)

