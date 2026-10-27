n = int (input("Masukkan jumlah baris: "))
jarak = 2

for i in range (1, n + 1):
    for j in range (1, i + 1):
        print(j, end=" ")

    for k in range (2 * (n-i) + jarak):
        print(" ", end=" ")

    for p in range (i, 0, -1):
        print(p, end=" ")

    print()