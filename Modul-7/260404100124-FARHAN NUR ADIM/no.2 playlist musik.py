playlist = {}

while True:
    print("\n=== MENU ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Selesai")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Masukkan nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada")
        else:
            playlist[nama] = {}
            print(f"Playlist {nama} sudah dibuat")

    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ")
        if nama in playlist:
            judul = input("Masukkan judul lagu yg mau ditambahkan: ")
            penyanyi = input("Masukkan juga nama penyanyi nya: ")
            playlist[nama][judul] = penyanyi
            print(f"Lagu dgn judul '{judul}' oleh '{penyanyi}' sudah ditambahkan")
        else:
            print("Playlist tidak ditemukan, coba liat lagi!")

    elif pilihan == "3":
        if len(playlist)==0:
            print("Belum ada playlist. Coba buat playlist dulu")
        else:
            for nama, lagu in playlist.items():
                print(f"\nPlaylist : {nama}")
                if len(lagu)==0:
                    print("Belum ada lagu, tambahkan lagu dulu")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        judul = input("Masukkan judul lagu yg mau dicari: ")
        ketemu = False
        for nama, lagu in playlist.items():
            if judul in lagu:
                print("Lagu ditemukan")
                print(f"Di playlist  : {nama}")
                print(f"Judul lagu   : {judul}")
                print(f"Nama penyanyi: {penyanyi}")
                ketemu = True

        if ketemu == False:
            print("Lagu tidak ditemukan, coba yg bener!")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist nya: ")
        if nama in playlist:
            judul = input("Masukkan judul lagu yg mau dihapus: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu sudah berhasil dihapus")
            else:
                print("Lagu tidak ditemukan, coba yg bener!")
        else:
            print("Playlist tidak ditemukan, coba liat lagi!")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist yg mau dihapus: ")
        if nama in playlist:
            del playlist[nama]
            print(f"Playlist {nama} sudah berhasil dihapus")
        else:
            print("Playlist tidak ditemukan, coba liat lagi!")

    elif pilihan == "7":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid! Coba lagi")