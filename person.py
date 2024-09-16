class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def __str__(self):
        return f"Child - {super().__str__()}"
person = Person("Peter", 25) 
child = Child("Peter Junior", 5) 
print(person.name) 
print(person.age) 
print(child.__class__.__bases__[0].__name__)  