class Film:
    def __init__(self, judul, durasi, genre):
        self.judul = judul
        self.durasi = durasi
        self.genre = genre

    def __str__(self):
        return f"{self.judul} - {self.durasi} menit - Genre: {self.genre}"

class Kursi:
    def __init__(self, nomor):
        self.nomor = nomor
        self.tersedia = True

    def pesan(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Terpesan"
        return f"Kursi {self.nomor}: {status}"

class Teater:
    def __init__(self, nama, film, jumlah_kursi):
        self.nama = nama
        self.film = film
        self.kursi = [Kursi(i+1) for i in range(jumlah_kursi)]

    def tampilkan_kursi(self):
        for kursi in self.kursi:
            print(kursi)

    def pesan_kursi(self, nomor_kursi):
        if 1 <= nomor_kursi <= len(self.kursi):
            if self.kursi[nomor_kursi-1].pesan():
                print(f"Kursi {nomor_kursi} berhasil dipesan.")
            else:
                print(f"Kursi {nomor_kursi} sudah terpesan.")
        else:
            print("Nomor kursi tidak valid.")

    def __str__(self):
        return f"Teater: {self.nama}\nFilm: {self.film}"

class Bioskop:
    def __init__(self, nama):
        self.nama = nama
        self.teater = []

    def tambah_teater(self, teater):
        self.teater.append(teater)

    def tampilkan_teater(self):
        for idx, teater in enumerate(self.teater):
            print(f"{idx + 1}. {teater}")

    def pilih_teater(self, nomor_teater):
        if 1 <= nomor_teater <= len(self.teater):
            return self.teater[nomor_teater - 1]
        else:
            print("Nomor teater tidak valid.")
            return None

def main():
    film1 = Film("Film A", 120, "Action")
    film2 = Film("Film B", 90, "Drama")

    teater1 = Teater("Teater 1", film1, 10)
    teater2 = Teater("Teater 2", film2, 8)

    bioskop = Bioskop("Bioskop ABC")
    bioskop.tambah_teater(teater1)
    bioskop.tambah_teater(teater2)

    while True:
        print("\nSelamat datang di Bioskop ABC")
        bioskop.tampilkan_teater()
        pilihan = input("Pilih teater (0 untuk keluar): ")

        if pilihan == "0":
            break

        try:
            nomor_teater = int(pilihan)
            teater = bioskop.pilih_teater(nomor_teater)
            if teater:
                print(teater)
                teater.tampilkan_kursi()
                nomor_kursi = int(input("Pilih nomor kursi untuk dipesan: "))
                teater.pesan_kursi(nomor_kursi)
        except ValueError:
            print("Input tidak valid, silakan masukkan nomor yang benar.")

if __name__ == "__main__":
    main()
