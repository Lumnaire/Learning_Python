# Classes is a constructor of objects


# simple class
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)



# class with users input
class Person:
    #pass is used to bypass the execution
    def __init__(self,name,age):
      self.name = name
      self.age = age

name = input('Enter your name: ')
age = input('Enter your age: ')

x1 = Person(name, age)

print(x1.name)
print(x1.age)