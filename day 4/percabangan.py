# Memeriksa apakah seseorang boleh mendapatkan SIM
usia = int(input("Masukkan usia: "))
memiliki_ktp = input("Apakah Anda memiliki KTP? (ya/tidak): ").lower()

if usia >= 17 and memiliki_ktp == "ya":
    print("Anda boleh mendapatkan SIM")
else:
    print("Anda tidak boleh mendapatkan SIM")
