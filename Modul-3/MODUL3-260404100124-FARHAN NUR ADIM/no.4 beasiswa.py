jumlah_beasiswa_penuh = 0

for i in range (1, 11):
    print("Mahasiswa ke-",i)

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))
    
    if ipk < 3 :
        print("Tidak memenuhi syarat")
        continue

    penghasilan = float(input("Penghasilan ortu per bulan: "))

    if penghasilan <= 3000000:
        print("Beasiswa penuh")
        jumlah_beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        print("Beasiswa sebagian")
    else:
        print("Tidak dapat beasiswa")

    if jumlah_beasiswa_penuh == 3:
        print("Proses seleksi dihentikan")
        break