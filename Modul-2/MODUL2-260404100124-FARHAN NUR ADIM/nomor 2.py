total_belanja = int(input("Masukkan total belanja: Rp"))

if total_belanja % 100000==0:
    besar_diskon = total_belanja * (100/100)
    total_bayar = total_belanja - besar_diskon
elif total_belanja % 50000==0:
    besar_diskon = total_belanja * (50/100)
    total_bayar = total_belanja - besar_diskon
elif total_belanja % 10000==0:
    besar_diskon = total_belanja * (20/100)
    total_bayar = total_belanja - besar_diskon
elif total_belanja >= 200000:
    besar_diskon =  total_belanja * (10/100)
    total_bayar = total_belanja - besar_diskon
else:
    total_bayar = total_belanja

poin = "Poin Bertambah" if total_bayar >0 else "Tidak Ada Poin"

print("Total belanja awal sebelum diskon : " "Rp", total_belanja)
print("Total harga akhir setelah diskon : " "Rp", total_bayar)
print("Status poin : " , poin)