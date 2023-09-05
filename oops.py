class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)

ashish = Employee("Ashish", "2000121")
print(ashish.name)
print(ashish.salary)
ashish.getSalary()

Rohan = Employee("Rohan", "1239131")
print(Rohan.name)
print(Rohan.salary)
Rohan.getSalary()
