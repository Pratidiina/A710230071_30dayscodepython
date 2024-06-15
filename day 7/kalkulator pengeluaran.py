# Definisikan fungsi untuk menambahkan pengeluaran
def tambah_pengeluaran(pengeluaran, deskripsi, jumlah):
    pengeluaran.append({"deskripsi": deskripsi, "jumlah": jumlah})

# Definisikan fungsi untuk menghitung total pengeluaran
def hitung_total_pengeluaran(pengeluaran):
    total = 0
    for item in pengeluaran:
        total += item["jumlah"]
    return total

# Definisikan fungsi utama untuk menjalankan program kalkulator pengeluaran
def kalkulator_pengeluaran():
    pengeluaran = []
    print("Kalkulator Pengeluaran Harian")
    print("============================")
    
    while True:
        print("\nMenu:")
        print("1. Tambah pengeluaran")
        print("2. Lihat total pengeluaran")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            deskripsi = input("Masukkan deskripsi pengeluaran: ")
            jumlah = float(input("Masukkan jumlah pengeluaran: "))
            tambah_pengeluaran(pengeluaran, deskripsi, jumlah)
            print(f"Pengeluaran '{deskripsi}' sebesar {jumlah} telah ditambahkan.")
        elif pilihan == '2':
            total = hitung_total_pengeluaran(pengeluaran)
            print(f"Total pengeluaran harian Anda adalah: {total}")
        elif pilihan == '3':
            print("Terima kasih telah menggunakan kalkulator pengeluaran harian.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program kalkulator pengeluaran
kalkulator_pengeluaran()
