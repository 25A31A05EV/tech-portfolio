# Day 4 - Python: Duck Typing

# "If it walks like a duck and quacks like a duck, it's a duck!"
# Object type matter kaadu — behavior matter avutundi

class Dog:
    def speak(self):
        print("Woof!")
    def walk(self):
        print("Dog is walking")

class Cat:
    def speak(self):
        print("Meow!")
    def walk(self):
        print("Cat is walking")

class Robot:
    def speak(self):
        print("Beep Boop!")
    def walk(self):
        print("Robot is walking")

# Duck Typing — type check cheyyatledu, just method call chesthaam
def make_it_speak(obj):
    obj.speak()  # doesn't care what obj is!

def make_it_walk(obj):
    obj.walk()

# All work — even though different classes!
animals = [Dog(), Cat(), Robot()]
for a in animals:
    make_it_speak(a)
    make_it_walk(a)
    print("---")

# Real world example — File-like objects
class PDFReader:
    def read(self):
        print("Reading PDF...")

class ExcelReader:
    def read(self):
        print("Reading Excel...")

class JSONReader:
    def read(self):
        print("Reading JSON...")

def process_file(reader):
    reader.read()  # duck typing — just needs .read() method

process_file(PDFReader())
process_file(ExcelReader())
process_file(JSONReader())