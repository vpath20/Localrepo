class Person:
    name = "Vikrant"
    occupation = "Trainee"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")



a = Person()
b = Person()
c = Person()
a.name = "Abhay"
a.occupation = "buisness executive"

b.name = "Nitika"
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()
c.info()