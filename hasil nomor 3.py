jarak=100
konsumsi_motor=40
indikator_bensin_sisa=1.5
harga_bahan_bakar=10000

total_jarak=jarak + jarak

total_kebutuhan_bensin=total_jarak / konsumsi_motor

jumlah_bensin_yang_dibeli=total_kebutuhan_bensin - indikator_bensin_sisa

total_biaya_bensin=jumlah_bensin_yang_dibeli * harga_bahan_bakar

print("Total jarak pulang-pergi:",total_jarak,"km")
print("Total kebutuhan bahan bakar:",total_kebutuhan_bensin,"liter")
print("Jumlah bahan bakar yang dibeli:",jumlah_bensin_yang_dibeli,"liter")
print("Total biaya beli bahan bakar: Rp",total_biaya_bensin) 