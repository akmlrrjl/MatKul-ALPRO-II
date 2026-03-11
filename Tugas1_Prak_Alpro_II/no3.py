n = int(input("Masukkan jumlah mahasiswa: "))
semua = []
for i in range(n):
    mahasiswa = []
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    bener = False
    while bener == False:
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1} (0-100): "))
        if nilai >= 0 and nilai <= 100:
            bener = True
        else:
            print("Nilai tidak valid. Silakan masukkan ulang nilai antara 0 dan 100.")
    mahasiswa.append(nama)
    mahasiswa.append(nilai)
    semua.append(mahasiswa)

for i in range(n):
    print("Data keseluruhan mahasiswa :\n", semua[i])

list_nilai = []
for i in semua:
    list_nilai.append(i[1])
print("Rata-rata nilai:", sum(list_nilai) / len(list_nilai))

index_max = list_nilai.index(max(list_nilai))
index_min = list_nilai.index(min(list_nilai))
print("Nama dengan nilai tertinggi beserta nilainya",semua[index_max])
print("Nama dengan nilai terendah beserta nilainya",semua[index_min])

ma_lulus = []
s_lulus = 0
ma_tidak_lulus = []
s_tidak_lulus = 0
for i in semua:
    if i[1] >= 60:
        ma_lulus.append(i)
        s_lulus += 1
    else:
        ma_tidak_lulus.append(i)
        s_tidak_lulus += 1
print("Jumlah mahasiswa yang lulus beserta daftarnya:", s_lulus, ma_lulus)
print("Jumlah mahasiswa yang tidak lulus beserta daftarnya:", s_tidak_lulus, ma_tidak_lulus)

list_huruf = []
banyak_a = 0
banyak_b = 0
banyak_c = 0
banyak_d = 0
banyak_e = 0
for i in semua:
    if i[1] >= 80:
        list_huruf.append("A")
        banyak_a += 1
    elif i[1] >= 70:
        list_huruf.append("B")
        banyak_b += 1
    elif i[1] >= 60:
        list_huruf.append("C")
        banyak_c += 1
    elif i[1] >= 50:
        list_huruf.append("D")
        banyak_d += 1
    else:
        list_huruf.append("E")
        banyak_e += 1 

modus = max(list_huruf)
nama_modus = []
hitung = 0
print("Daftar mahasiswa dengan huruf terbanyak", modus)
for i in list_huruf:
    if i == modus:
        nama_modus.append(semua[hitung][0])
    hitung += 1
print(nama_modus)