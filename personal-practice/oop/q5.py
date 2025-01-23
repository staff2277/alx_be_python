class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name, age):
        return cls(name, age)
    

child = Person.create_child("mustapha", 25)

print(child.age)