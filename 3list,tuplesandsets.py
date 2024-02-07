courses = ['History', 'Math', 'Physics', 'Compsci']
print(courses[0])
print(courses[0:2])
print(courses[1:2:1])
print(courses[-1])

courses = ['History', 'Math', 'Physics', 'Compsci']
courses.append('Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'Compsci']
courses.insert(0,'Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'Compsci']
courses_2 = ['Chemistry', 'Civics']
courses.insert(0, courses_2)
print(courses)
print(courses[0])

courses = ['History', 'Math', 'Physics', 'Compsci']
courses_2 = ['Chemistry', 'Civics']
courses.extend(courses_2)
print(courses)

courses = ['History', 'Math', 'Physics', 'Compsci']
courses.remove('Math')
print(courses)

courses = ['History', 'Math', 'Physics', 'Compsci']
popped = courses.pop()
print(popped)
print(courses)


courses = ['History', 'Math', 'Physics', 'Compsci']
courses.reverse()
print(courses)


courses = ['History', 'Math', 'Physics', 'Compsci']
nums = [1, 5, 4, 7, 2]
nums.sort(reverse=True)
courses.sort(reverse=True)
print(nums)
print(courses)

courses = ['History', 'Math', 'Physics', 'Compsci']
print(courses.index('Compsci'))
print('Math' in courses)

courses = ['History', 'Math', 'Physics', 'Compsci']
for item in courses:
    print(item)

courses = ['History', 'Math', 'Physics', 'Compsci']
for index, course in enumerate(courses, start=1):
    print(index, course)

courses = ['History', 'Math', 'Physics', 'Compsci']
course_str = ' - '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)


#mutable
list_1 = ['History', 'Math', 'Physics', 'Compsci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

#Tuples
#immutable
#tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
#tuple_2 = tuple_1

#print(tuple_1)
#print(tuple_2)

#tuple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)

#Sets
cs_courses = {'History', 'Math', 'Physics', 'Compsci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


#Empty list
empty_list = []
empty_list = list()

#Empty tuples
empty_tuples = ()
empty_tuples = tuple()

# Empty sets
empty_sets = {} #This is not right! It's a dict
empty_sets = set()

lst = [i for i in range(5)]
print(lst)

lst = [i*i for i in range(10)]
print(lst)
for i in range(10):
    if i%2 == 0:
        print(i*i)

lst = [i*i for i in range(10) if i%2==0]
print(lst)

l = [11, 46, 67, 5, 67, 56, 78]
m = [900,800,767]
k = [700,400,79]
k = l + m
print(k)
#l.extend(m)
print(l)

v = set()
print(type(set))


cities = {"Delhi","Mumbai","Kolkata","Chennai"}
cities2 = {"Gujarat","Mumbai","Kolkata","Kerala"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Delhi","Mumbai","Kolkata","Chennai"}
cities2 = {"Gujarat","Mumbai","Kolkata","Kerala"}
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))


cities = {"Delhi","Mumbai","Kolkata","Chennai"}
cities.add("Gorakhpur")
print(cities)

