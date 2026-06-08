# Day 3 - Python: Polymorphism

# Method Overriding (Runtime Polymorphism)
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Duck(Animal):
    def speak(self):
        print("Quack!")

# Polymorphism in action
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    animal.speak()  # same method, different behavior!

# Method Overloading (using default args)
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.add(2, 3, 4))    # 9

# Polymorphism with functions
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

# Same function call, different results
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")