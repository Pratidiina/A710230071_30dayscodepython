class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

person = Person("Abdul Hakim", 25)
print(person.get_name())
print(person.get_age())
person.set_name("Ryan Hakim")
person.set_age(30)
print(person.get_name())
print(person.get_age())
print(person.name)
