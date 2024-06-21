# Definisikan kelas dasar (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")

# Definisikan kelas turunan (subclass)
class Dog(Animal):
    def sound(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def sound(self):
        return f"{self.name} says Moo!"

class Duck(Animal):
    def sound(self):
        return f"{self.name} says Quack!"

# Buat objek dari kelas-kelas turunan
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")
duck = Duck("Daffy")

# Cetak suara hewan
print(dog.sound())
print(cat.sound())
print(cow.sound())
print(duck.sound())
