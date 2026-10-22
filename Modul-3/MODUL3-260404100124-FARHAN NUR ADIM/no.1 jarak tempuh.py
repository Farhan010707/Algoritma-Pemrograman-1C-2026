jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = float(input("Masukkan jarak penumpang (0 selesai): "))
    if jarak == 0:
        print("Selesai")
        break

    if jarak < 0:
        print("Jarak tidak valid, masukkan ulang jarak penumpang")
        continue

    jumlah_penumpang += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak < 15:
        tarif = 3000+(jarak-5)*1000
    else:
        tarif = 13000+(jarak-15)*500

    if jumlah_penumpang % 5 ==0:
        besar_diskon = tarif * (50/100)
        tarif = tarif - besar_diskon
        print("Mendapat diskon 50%")

    total_pendapatan += tarif

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    if jumlah_penumpang > 0:
        rata_rata = total_jarak / jumlah_penumpang
    else:
        print("Rata-rata jarak : 0 km")

    print("Tarifnya : Rp",tarif)

print(" ", "--HASIL AKHIR---")
print("Jumlah penumpang :",jumlah_penumpang)
print("Total pendapatan : Rp",total_pendapatan)
print("Jarak terjauh    :",jarak_terjauh, "km")
print("Rata-rata jarak  :",rata_rata, "km")