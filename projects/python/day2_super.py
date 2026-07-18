# Day 2 - Python: super() in Inheritance

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

# Without super() - manual way
class Dog1(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Woof")  # old way

# With super() - clean way
class Dog2(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")  # modern way

# Multi-level super()
class Puppy(Dog2):
    def __init__(self, name, age):
        super().__init__(name)  # calls Dog2 -> Animal automatically
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} months old")

# Tests
print("=== Without super() ===")
d1 = Dog1("Tommy")
d1.speak()

print("\n=== With super() ===")
d2 = Dog2("Bruno")
d2.speak()

print("\n=== Multi-level super() ===")
p = Puppy("Max", 3)
p.speak()
p.info()