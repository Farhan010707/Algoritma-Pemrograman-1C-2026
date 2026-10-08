kode_PIN = int(input("Masukkan kode PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangannya (0-23): "))

if kode_PIN %5==0:
    if jam < 12:
        pesan = "Garasi Pagi Terbuka"
    elif jam >= 12:
        pesan = "Garasi Malam Terbuka, Lampu dinyalakan"

digit_pertama = kode_PIN // 100
digit_kedua = (kode_PIN // 10) % 10
digit_ketiga = kode_PIN % 10

if kode_PIN %2==0:
    if (digit_pertama + digit_ketiga) == digit_kedua:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"

else:
    pesan = "Akses Ditolak Sepenuhnya"

kamera_CCTV = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Digit pertama: ",digit_pertama)
print("Digit kedua: ", digit_kedua)
print("Digit ketiga: ",digit_ketiga)
print("Pesan status akses garasi: ",pesan)
print("Status kamera CCTV: ",kamera_CCTV)