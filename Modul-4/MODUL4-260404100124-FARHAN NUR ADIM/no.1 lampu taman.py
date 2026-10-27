baris = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu: "))

for i in range(1,baris+1):
    print(f"\nPeriksa baris ke-{i}")
    for j in range(1,lampu+1):
        if j %3==0:
            print(f"Lampu{j}: Mengalami gangguan")
        else:
            print(f"Lampu{j}: Berfungsi normal")

print("\nPeriksa sumber listrik utama taman")