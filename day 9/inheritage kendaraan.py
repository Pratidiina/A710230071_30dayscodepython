class Kendaraan:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model

    def info(self):
        return f"Merk: {self.merk}, Model: {self.model}"

class Mobil(Kendaraan):
    def __init__(self, merk, model, jumlah_pintu):
        super().__init__(merk, model)
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        return f"Merk: {self.merk}, Model: {self.model}, Jumlah Pintu: {self.jumlah_pintu}"

# Contoh penggunaan
mobil_saya = Mobil("Toyota", "Avanza", 4)
print(mobil_saya.info_mobil())
