# Day 1 - OOP & Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age:  {self.age}")

# Single Inheritance
class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def show_student(self):
        print(f"Roll No: {self.roll}")

# Multilevel Inheritance
class Monitor(Student):
    def monitor_info(self):
        print("Class Monitor")

# Multiple Inheritance
class Sports:
    def sport(self):
        print("Cricket")

class Scholar(Student, Sports):
    pass

# Hierarchical Inheritance
class Teacher(Person):
    def subject(self):
        print("Python")

# Tests
print("=== Class & Object ===")
p = Person("Sowmya", 18)
p.display()

print("\n=== Single Inheritance ===")
s = Student("Anu", 19, 101)
s.display()
s.show_student()

print("\n=== Multilevel Inheritance ===")
m = Monitor("Rahul", 20, 102)
m.display()
m.show_student()
m.monitor_info()

print("\n=== Multiple Inheritance ===")
sc = Scholar("Kiran", 21, 103)
sc.display()
sc.show_student()
sc.sport()

print("\n=== Hierarchical Inheritance ===")
t = Teacher("Ravi", 35)
t.display()
t.subject()