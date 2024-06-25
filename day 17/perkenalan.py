def perkenalan_mahasiswa():
    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: ")
    nim = input("Masukkan NIM Anda: ")
    jurusan = input("Masukkan jurusan Anda: ")
    fakultas = input("Masukkan fakultas Anda: ")
    angkatan = input("Masukkan angkatan Anda: ")

    # Menampilkan informasi mahasiswa
    print("\n=== Perkenalan Mahasiswa ===")
    print(f"Nama     : {nama}")
    print(f"NIM      : {nim}")
    print(f"Jurusan  : {jurusan}")
    print(f"Fakultas : {fakultas}")
    print(f"Angkatan : {angkatan}")

# Memanggil fungsi perkenalan_mahasiswa
perkenalan_mahasiswa()
