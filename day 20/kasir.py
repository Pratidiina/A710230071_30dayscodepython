class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Rp {self.price} x {self.quantity})"

class Kasir:
    def __init__(self):
        self.cart = []

    def tambah_item(self, name, price, quantity):
        new_item = Item(name, price, quantity)
        self.cart.append(new_item)
        print(f"Item {name} berhasil ditambahkan ke keranjang.")

    def tampilkan_keranjang(self):
        if not self.cart:
            print("Keranjang belanja kosong.")
        else:
            print("Daftar Item di Keranjang Belanja:")
            for item in self.cart:
                print(item)

    def hitung_total(self):
        total = sum(item.price * item.quantity for item in self.cart)
        print(f"Total Harga: Rp {total}")
        return total

    def bayar(self, amount):
        total = self.hitung_total()
        if amount < total:
            print(f"Uang tidak cukup. Anda harus membayar Rp {total - amount} lagi.")
        else:
            change = amount - total
            print(f"Pembayaran berhasil. Kembalian Anda: Rp {change}")

def main():
    kasir = Kasir()

    while True:
        print("\nMenu Kasir:")
        print("1. Tambah Item")
        print("2. Tampilkan Keranjang")
        print("3. Hitung Total")
        print("4. Bayar")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            name = input("Nama item: ")
            price = int(input("Harga item: "))
            quantity = int(input("Jumlah item: "))
            kasir.tambah_item(name, price, quantity)
        elif pilihan == '2':
            kasir.tampilkan_keranjang()
        elif pilihan == '3':
            kasir.hitung_total()
        elif pilihan == '4':
            amount = int(input("Jumlah uang yang dibayarkan: "))
            kasir.bayar(amount)
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program kasir ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
