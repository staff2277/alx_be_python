class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old ")
    
    def __del__(self):
        print("farewell")


rich = Person("Richard", 19)
zack = Person("Zackus", 24)

zack.hello()