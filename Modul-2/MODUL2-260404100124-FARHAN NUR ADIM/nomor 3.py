suhu = float(input("Masukkan suhu reaktor (C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    if tekanan <= 50:
        status = "(Bahaya Suhu: Segera Turunkan Daya!)"
        
elif suhu > 500 and suhu < 1000: 
    if tekanan > 30:
        status = "Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Suhu:",suhu,"C")
print("Tekanan:",tekanan,"Bar")
print("Status bahaya reaktor:",status)
print("Status pompa air:", status_pompa)