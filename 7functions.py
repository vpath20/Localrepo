def hello_func():
    return 'Hello Function.'
print(hello_func())

def hello_func():
    return 'Hello Function.'
print(hello_func().upper())

def hello_func(greeting,name = 'you'):
    return '{}, {}'.format(greeting,name)
print(hello_func('Hi'))

def hello_func(greeting,name = 'you'):
    return '{}, {}'.format(greeting,name)
print(hello_func('Hi', name = 'Vikrant'))


def students_info(*args, **kwargs):
    print(args)
    print(kwargs)
course = ['Math', 'Science']
info = {'name' : 'John', 'age' :22}
students_info(*course, **info)

#numbers of days per month. first value placeholder
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print( is_leap(2004))


def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

a = 9
b = 5

if (a > b):
    print("first number is greater")
else:
    print("second number is greater or equal")

calculategmean(a, b)
c = 5
d = 9
if (c > d):
    print("first number is greater")
else:
    print("second number is greater or equal")

calculategmean(c, d)

def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a ,b):
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

a = 9
b = 8
isGreater(a,b)
calculategmean(a, b)

c = 8
d = 7
isGreater(c, d)
calculategmean(c, d)

def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a ,b):
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

def isLesser(a, b):
    pass

def average(a = 5, b = 5):
    print("The average is", (a+b)/2)

average(8, )

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))

average(5, 6)

def name(**name):
    print(type(name))
    print("Hello,", name["fname"],name["mname"], name["lname"])

name(mname = ".Buchanan", lname = "Barnes", fname = "James")

#calculating average using return
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(5,6,7)
print(c)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


# fibonacci sequence
#f1 = 1
#f2 = 2
#f3 = f1 + f2
#fn = fn-1 + fn-2

def fibonacci(n):
  



