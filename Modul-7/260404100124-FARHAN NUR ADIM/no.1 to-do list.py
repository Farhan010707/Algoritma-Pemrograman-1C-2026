todo_list = {}

while True:
    print("\n=== MENU ===")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas yg sudah selesai")
    print("6. Jumlah tugas yg belum")
    print("7. Selesai")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")
        if nama in todo_list:
            print("Tugas sudah ada!")
        else:
            todo_list[nama] = "Belum Selesai"
            print(f"Tugas {nama} sudah ditambahkan")

    elif pilihan == "2":
        if len(todo_list) == 0:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas: ")
            for nama, status in todo_list.items():
                print(nama, ":", status)

    elif pilihan == "3":
        nama = input("Masukkan nama tugas yang selesai: ")
        if nama in todo_list:
            todo_list[nama] = "Selesai"
            print(f"Tugas {nama} sudah ditandai selesai")
        else:
            print("Tugas tidak ditemukan")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas yang mau dihapus: ")
        if nama in todo_list:
            del todo_list[nama]
            print(f"Tugas {nama} sudah dihapus")
        else:
            print("Tugas tidak ditemukan")

    elif pilihan == "5":
        selesai = 0
        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
        print("Jumlah tugas yg selesai:", selesai)

    elif pilihan == "6":
        belum = 0
        for status in todo_list.values():
            if status == "Belum Selesai":
                belum += 1
        print("Jumlah tugas yg belum selesai:", belum)

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Pilih (1-7)")
