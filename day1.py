# Mendefinisikan kelas 'Person'
class Person:
    # Konstruktor (__init__) digunakan untuk menginisialisasi atribut objek
    def __init__(self, name, age):
        self.name = name  # Atribut 'name'
        self.age = age    # Atribut 'age'

    # Metode untuk menampilkan informasi tentang orang tersebut
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Metode untuk menambahkan umur
    def birthday(self):
        self.age += 1
        print(f"Selamat ulang tahun {self.name}! Kamu sekarang {self.age} tahun.")

# Membuat objek dari kelas 'Person'
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Menggunakan metode 'display_info' untuk menampilkan informasi
person1.display_info()
person2.display_info()

# Menggunakan metode 'birthday' untuk menambahkan umur
person1.birthday()
person2.birthday()
