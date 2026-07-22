# Day 5: Exception Handling Practice

# 1. Divide two numbers - handle ZeroDivisionError
try:
    a = 10
    num = int(input("Enter a number: "))
    print(a / num)
except ZeroDivisionError:
    print("Division by zero")

# 2. Value Error
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")

# 3. Both ValueError and ZeroDivisionError
try:
    a = 10
    b = int(input("Enter a number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")

# 4. File handling
try:
    file = open("notes.txt")
except FileNotFoundError:
    print("File not found")

# 5. List index error
num = [10, 20, 30]
try:
    print(num[3])
except IndexError:
    print("Index out of range")

# 6. Dictionary key error
dic = {"a": 1, "b": 2, "c": 3, "d": 4}
try:
    print(dic["e"])
except KeyError:
    print("Key not found")

# 7. try/except/else
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print(num)

# 8. try/except/finally
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
finally:
    print("Program ends")


# Custom function with IndexError handling
def library(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Index out of range")
        return None

print(library(["a", "b", "c"], 8))