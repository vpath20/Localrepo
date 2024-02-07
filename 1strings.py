# print welcome message
print ("hello world")

message = "hello world"
print (message)

message = "Bobby's world"
print (message)

message = 'Bobby\'s world'
print (message)

message = """ Bobby's world was a good
cartoon in the 90's"""
print (message)

message = "hello world"
print(len(message))

message = "hello world"
print(message[0:5])

message = "hello world"
print(message.upper())

message = "hello world"
print(message.count('hello'))

message = "hello world"
print(message.find('universe'))

message = "hello world"
print(message.replace('world' , 'universe'))

greeting = 'hello'
name = 'vikrant'
message = greeting + ', ' + name
print(message)

greeting = 'hello'
name = 'vikrant'
message = greeting + ', ' + name + '. Welcome! '
print(message)

greeting = 'hello'
name = 'vikrant'
message = '{}, {}. welcome!'.format(greeting, name)
print(message)

greeting = 'hello'
name = 'vikrant'
message = f'{greeting}, {name.upper()}. Welcome!:'
print(message)

greeting = 'hello'
name = 'vikrant'
print(dir(name))

greeting = 'hello'
name = 'vikrant'
print(help(str))

m = "Vikrant!!!!!"
print(m.rstrip("!"))

b = "vikrant pathak"
print(b.split())

blogheading = "introduction to js"
print(blogheading.capitalize())

start = "Welcome to the console!!!"
print(len(start))
print(len(start.center(50)))

start = "Welcome to the console!!!"
print(start.endswith("!!!"))

start = "Welcome to the console!!!"
print(start.endswith("to",4, 10))

str1 = "he's name is dan. he is an honest man"
print(str1.index("dan"))

start = "WelcomeToTheConsole"
print(start.isalnum())


#docstring
def square(n):

 '''Takes in a number n, returns the
    square of n'''
 print(n**2)
square(5)
print(square.__doc__)



