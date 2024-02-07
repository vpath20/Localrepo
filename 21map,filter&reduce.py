# MAP
# def cube(x):
#     return x * x * x
#
# print(cube(2))
#
# l = [1, 2, 3, 4, 5, 6, 7]
# newl = list(map(cube, l))
# print(newl)
#
# # FILTER
# def filter_func(a):
#     return a > 4
# newnewl = list(filter(filter_func, l))
# print (newnewl)

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]


# sum = reduce(lambda x, y: x + y, numbers)
# print(sum)

def mysum(x,y):
    return x + y
sum = reduce(mysum,numbers)
print(sum)



