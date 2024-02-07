class Person:
    def __init__(self, n, o):
        print("Hey how are you?")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Vikrant", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()