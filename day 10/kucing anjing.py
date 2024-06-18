class Anjing:
    def bersuara(self):
        print("Guk guk!")

class Kucing:
    def bersuara(self):
        print("Meong!")

def buat_suara(hewan):
    hewan.bersuara()

# Contoh penggunaan:
anjing = Anjing()
kucing = Kucing()

buat_suara(anjing)  # Output: Guk guk!
buat_suara(kucing)  # Output: Meong!
