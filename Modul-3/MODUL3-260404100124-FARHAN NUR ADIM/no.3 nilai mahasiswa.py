jumlah_nilai_A = 0
jumlah_nilai_B = 0
jumlah_nilai_C = 0
jumlah_nilai_D = 0
jumlah_nilai_E = 0

total_nilai = 0

nilai_tertinggi = -1
nilai_terendah = 101

nama_tertinggi = " "
nama_terendah = " "

for i in range (1,11):
    print("\nMahasiswa ke-",i)

    nama = input("Masukkan nama mahasiswa: ")
    nilai_tugas = float(input("Masukkan nilai tugasnya: "))
    nilai_UTS = float(input("Masukkan nilai UTS: "))
    nilai_UAS =float(input("Masukkan nilai UAS: "))

    nilai_akhir = nilai_tugas*(30/100) + nilai_UTS*(30/100) + nilai_UAS*(40/100)

    if nilai_akhir >=85:
        kategori = "Nilai A"
        jumlah_nilai_A += 1
    elif nilai_akhir >=75:
        kategori = "Nilai B"
        jumlah_nilai_B += 1
    elif nilai_akhir >=65:
        kategori = "Nilai C"
        jumlah_nilai_C += 1
    elif nilai_akhir >=50:
        kategori = "Nilai D"
        jumlah_nilai_D += 1
    else:
        kategori = "Nilai E"
        jumlah_nilai_E += 1

    total_nilai+= nilai_akhir 

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print("\n--Data Mahasiswa--")
    print("Nama             : ",nama)
    print("Nilai tugas      : ",nilai_tugas)
    print("Nilai UTS        : ",nilai_UTS)
    print("Nilai UAS        : ",nilai_UAS)
    print("Nilai akhir      : ",nilai_akhir)
    print("Kategori Nilai   : ",kategori)

rata_rata = total_nilai/10

print("\n==HASIL AKHIR==")
print("JUMLAH MAHASISWA NILAI A : ",jumlah_nilai_A)
print("JUMLAH MAHASISWA NILAI B : ",jumlah_nilai_B)
print("JUMLAH MAHASISWA NILAI C : ",jumlah_nilai_C)
print("JUMLAH MAHASISWA NILAI D : ",jumlah_nilai_D)
print("JUMLAH MAHASISWA NILAI E : ",jumlah_nilai_E)

print("\nNILAI TERTINGGI  : ",nilai_tertinggi)
print("NAMA MAHASISWA   : ",nama_tertinggi)
print("\nNILAI TERENDAH   : ",nilai_terendah)
print("NAMA MAHASISWA   : ",nama_terendah)
print("\nRATA-RATA NILAI AKHIR : ",rata_rata)