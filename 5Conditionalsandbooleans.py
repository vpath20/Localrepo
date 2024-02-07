language = 'Javascript'
if language == 'Python':
    print('condition was true')
elif language == 'Java':
    print('language is Java')

elif language == 'Javascript':
    print('language is Javascript')

else:
    print('no match')


#and
#or
#not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print("Admin Page")
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if not logged_in:
    print("Please log in")
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))

# False Values:
# False
# None
# Zero of numeric type
# Any empty sequence, for ex, '', (), [].
# Any empty mapping, for example, {}.

condition = 'Test'
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')

#Nested if else statement
num = 18
if (num < 0):
    print("number is negative.")
elif (num > 0):
    if (num <= 10):
        print("number is between 1-10")
    elif(num > 10 and num <= 20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")


#if else short hand

a = 330
b = 3303
print("A") if a > b else print("=") if a == b else print("B")


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


