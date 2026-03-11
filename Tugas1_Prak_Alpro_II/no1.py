print("======================================================================")
print("              ANALISIS RANGKAIAN LISTRIK - YubiBot                    ")
print("======================================================================\n")
print("              SILAKAN MASUKKAN DATA PENGUKURAN                        ")
print("----------------------------------------------------------------------")

n = int(input("Masukkan jumlah titik pengukuran (minimal 2):"))
print(f"Masukkan data untuk {n} titik pengukuran:\n")
list_V = []
list_I = []
list_n = []
for i in range(n):
    print(f"- - - Titik {i} - - -")
    V = float(input(f"Tegangan di titik {i} (Volt): "))
    I = float(input(f"Arus di titik {i} (Ampere): "))
    list_V.append(V)
    list_I.append(I)
    list_n.append(i)
    dictionary_pada_titik = {"titik ke": i,"Tegangan": V,"Arus": I}
    print()

print("======================================================================")
print("                  DATA PENGUKURAN YANG TERSIMPAN                      ")
print("======================================================================")
input("Tanggal     :")
print("Jumlah titik:", n)
print("Titik ukur  :", list_n)
print("Tegangan (V):", list_V)
print("Arus (A)    :", list_I)
print("----------------------------------------------------------------------\n")

list_R = []
for i in range(n):
    R = list_V[i] / list_I[i]
    list_R.append(R)
list_P = []
sum_P = 0
for i in range(n):
    P = list_V[i] * list_I[i]
    list_P.append(P)
    sum_P += P
P_i = 0
for i in range(1,n-1):
    P_i += list_P[i]
E = 1/2 * (list_P[0] + list_P[n-1] + 2 * P_i)

print("======================================================================")
print("                      RINGKASAN HASIL ANALISIS                        ")
print("======================================================================")
print("-> Jumlah titik        :", n)
print("-> Tegangan            :", list_V, "V") 
print("-> Arus                :", list_I, "A")
print("-> Hambatan tiap titik :", list_R, "Ohm")
print("-> Daya tiap titik     :", list_P, "Watt")
print("-> Total daya          :", sum_P, "Watt")
print("-> Energi total        :", E, "J")
print("-> Minimum             :", min(list_V), "V dan", min(list_I), "A")
print("-> Maximum             :", max(list_V), "V dan", max(list_I), "A")
print("-> Rata-rata           :", sum(list_V) / len(list_V), "V dan", sum(list_I) / len(list_I), "A")