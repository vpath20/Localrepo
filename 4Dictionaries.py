
students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
print(students)

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
print(students['name'])
print(students.get('phone', 'Not Found'))

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
students['phone'] = '555_5555'
students['name'] = 'Jane'
#print(students.get('phone', 'Not Found'))
print(students)

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
students.update({'name': 'Jane', 'age': '23', 'phone': '555-5555', 'courses': ['Math', 'Compsci']})
print(students)

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
del students['age']
print(students)

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
age = students.pop('age')
print(students)
print(age)

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
print(len(students))
print(students.keys())
print(students.values())
print(students.items())

students = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
for key, value in students.items():
    print(key, value)


