class Person:
    def __init__(self,name,age):
        self.name1=name
        self.age=age

    def greet(self):
        print(f"Hello my name is {self.name1}, I am {self.age} years old.")
        
person1 = Person("John", 25)
print(person1.greet())

person2 = Person("Jane", 30)
print(person2.greet())