import time
from plyer import notification

def pengingat_minum_air():
    jam_kerja = 8  # Jumlah jam kerja
    interval = 3600  # Interval waktu dalam detik (1 jam = 3600 detik)
    
    for jam in range(jam_kerja):
        # Memberi notifikasi pengingat
        notification.notify(
            title='Pengingat Minum Air',
            message='Saatnya minum air! Jangan lupa untuk tetap terhidrasi.',
            app_name='Pengingat Minum Air',
            timeout=10  # Notifikasi akan ditampilkan selama 10 detik
        )
        
        # Menunggu selama 1 jam sebelum mengingatkan lagi
        time.sleep(interval)
        
    print("Jam kerja selesai, selamat beristirahat!")

# Menjalankan fungsi pengingat
pengingat_minum_air()
