undangan = set()
webinar_A = set()
webinar_B = set()

jumlah_undangan = int(input("Masukkan jumlah undangan: "))
for undang in range(jumlah_undangan):
    nama_undangan = input(f"Masukkan nama undangan ke-{undang+1}: ")
    undangan.add(nama_undangan)

jumlah_A = int(input("\nMasukkan jumlah peserta webinar A: "))
for a in range(jumlah_A):
    nama_A = input(f"Masukkan nama peserta webinar A ke-{a+1}: ")
    webinar_A.add(nama_A)

jumlah_B = int(input("\nMasukkan jumlah peserta webinar B: "))
for b in range(jumlah_B):
    nama_B =input(f"Masukkan nama peserta webinar B ke-{b+1}: ")
    webinar_B.add(nama_B)

semua_peserta = webinar_A.union(webinar_B)
kedua_webinar = webinar_A.intersection(webinar_B)
satu_webinar = webinar_A.symmetric_difference(webinar_B)
tidak_hadir = undangan.difference(semua_peserta)

print(f"\nSemua peserta di kedua webinar: {semua_peserta}")
print(f"Peserta yg hadir di kedua webinar: {kedua_webinar}")
print(f"Peserta yg hanya hadir di salah satu webinar: {satu_webinar}")
print(f"Nama undangan yg tidak hadir di webinar mana pun: {tidak_hadir}")