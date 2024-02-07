class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("The default language is Python ")

e = Employee("Rohan Das", 400)
e.showDetails()
e2 = programmer("Vikrant", 40)
e.showDetails()
e2.showLanguage()

