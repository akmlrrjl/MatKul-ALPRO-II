P = [[10,20,30],
     [40,50,60],
     [70,80,90]]
V = [[100,70],
     [150,100],
     [200,150]]
K = [[1,0,2],
     [2,1,0],
     [0,3,1]]

T = []
for i in range(3):
    baris_profit = []
    for j in range(2):
        profit = 0
        for ij in range(3):
            profit += P[i][ij] * V[ij][j]
        baris_profit.append(profit)
    T.append(baris_profit)

bawah = 0
for i in range(3):
    i0 = i % 3
    i1 = (i + 1) % 3
    i2 = (i + 2) % 3
    bawah += K[0][i0] * K[1][i1] * K[2][i2]
atas = 0
for i in range(3):
    i0 = i % 3
    i1 = (i + 1) % 3
    i2 = (i + 2) % 3
    atas += K[0][i2] * K[1][i1] * K[2][i0]
det_K = bawah - atas

I = [[1,0,0],
     [0,1,0],
     [0,0,1]]

if det_K != 0:
    TB = []
    for i in range(3):
        TB.append(T[i][0] - T[i][1])
    print("Total profit bersih untuk setiap pabrik:", TB)
    KI = []
    for i in range(3):
        baris_KI = []
        for j in range(3):
            baris_KI.append(K[i][j] + I[i][j])
        KI.append(baris_KI)
else:
    print("Sistem Terkunci: Kunci Verifikasi Tidak Valid")