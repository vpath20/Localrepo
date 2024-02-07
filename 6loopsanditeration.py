nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

#break loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found it")
        break
    print(num)

#continue loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found it")
        continue
    print(num)


nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)


for i in range(1, 11):
    print(i)


x = 0

while x < 10:
    print(x)
    x += 1


for i in []:
    print(i)

else:
    print("Sorry no i")



#enumerate function
marks = [12, 43, 57, 54, 68, 65, 76, 77, 58]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("awesome")

marks = [12, 43, 57, 54, 68, 65, 76, 77, 58]

for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("awesome")


