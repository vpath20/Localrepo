import my_module
print('imported my_module')

test = 'Test String'


def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1

courses = ['History', 'Math', 'Physics', 'Compsci']

index = my_module.find_index(courses,"Math")
print(index)



import time
t = time.strftime("%H:%M:%S")
hour = int(input("Enter the hour:"))
(print(hour))

if(hour>=0 and hour<=12):
    print("Good morning")
elif(hour>12 and hour<=15):
    print("Good Afternoon")
if(hour>15 and hour<=24):
    print("Good Evening")

