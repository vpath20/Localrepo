x = 4
print(x)

def hello():
    x = 5
    print(f"The local x is {x}")
    print("Hello Vikrant")

print(f"the global x is {x}")
hello()
print(f"The global x is {x}")


x = 10

def myfunction():
    global x
    x = 6
    y = 5
    print(y)

myfunction()
print(x)
# print(y)