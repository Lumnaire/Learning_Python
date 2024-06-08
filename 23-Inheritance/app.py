# Inheritance allows us to define a class that inherits all the methods and properties from another class
# it inherits a value from a different file, as long as it is in the same file directory

from new import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)