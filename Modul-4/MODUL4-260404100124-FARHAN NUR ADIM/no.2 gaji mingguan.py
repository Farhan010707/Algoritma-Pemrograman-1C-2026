gaji_pokok = 100000
total_gaji = 0

for i in range (1,8):
    print(f"\nHari ke-{i}")
    lembur = int(input("Masukkan berapa jam lembur (1-8): "))

    if lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur <= 4:
        upah_lembur = 100000
    elif lembur <= 6:
        upah_lembur = 200000
    elif lembur <= 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0
        print("Jumlah lembur melebihi batas, tidak dapat upah")

    shift = input("Apakah bekerja shift malam? (y/gak): ")

    if shift == "y":
        upah_tambahan_shift = 50000
    else:
        upah_tambahan_shift = 0

    gaji_harian = gaji_pokok + upah_lembur + upah_tambahan_shift

    total_gaji += gaji_harian

    print(f"Gaji hari ke-{i}: Rp{gaji_harian}")

print(f"\nTotal Gaji Selama Seminggu (7 hari): Rp{total_gaji}")