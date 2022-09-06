cars = ["honda", "BMW"]

#x = cars[1]
#print(x)
#class
x = len(cars)
print(x)
'''Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects'''
#class my:
    #x = 5

#p1 = my()
#print(p1.x)
'''The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:'''
'''class per:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = per("Char", 10)
print(p1.name)
print(p1.age)'''
#lambda
'''x = lambda a, b, c : a * b * c
print(x(5, 6, 2))'''
#a more complex way to triple an int
'''def bruh(n):
    return lambda a : a * n

mydoubler = bruh(2)
mytripler = bruh(3)

print(mydoubler(11))
print(mytripler(11))'''