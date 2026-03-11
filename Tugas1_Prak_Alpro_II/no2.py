menu_kopi = [['Nama Menu ','Stok','Harga (Rp)'],
             ['Latte     ', 8    , 22000],
             ['Red Velvet', 12   , 18000],
             ['Espresso  ', 10   , 15000],
             ['Cappuccino', 15   , 20000],
             ['Matcha    ', 6    , 25000],
             ['Americano ', 12   , 18000]]

def lihat_menu():
    print("======================================================================")
    print("                          DAFTAR MENU KOPI                            ")
    print("======================================================================")
    for i in menu_kopi:
        print(i)

def cari_menu(nama):
    for i in range(1,7):
        if menu_kopi[i][0] == nama:
            return i
    return -1

def pesan():
    global keranjang, total, banyak_cup
    lihat_menu()
    kelar = False
    total = 0
    banyak_cup = 0
    keranjang =[]
    while kelar == False:
        nama = input("Masukkan nama menu yang ingin dipesan (ketik ”selesai” untuk checkout): ")
        if nama == "selesai":
            kelar = True
        else:
            urutan_menu = cari_menu(nama)
            if urutan_menu != -1:
                jumlah = input("Masukkan jumlah pesanan: ")
                if jumlah.isdigit() and jumlah > 0:
                    if jumlah <= menu_kopi[urutan_menu][1] and menu_kopi[urutan_menu][1] > 0:
                        menu_kopi[urutan_menu][1] -= jumlah
                        total_harga_sementara = jumlah * menu_kopi[urutan_menu][2]
                        total += total_harga_sementara 
                        banyak_cup += jumlah
                        keranjang_sementara = []
                        keranjang_sementara.append(nama)
                        keranjang_sementara.append(jumlah)
                        keranjang_sementara.append(total_harga_sementara)
                        keranjang.append(keranjang_sementara)
                        print(f"Pesanan berhasil! Total harga: Rp {total_harga_sementara}")
                    else:
                        print("Maaf, stok tidak cukup.")
                else:
                    print("Masukkan jumlah pesanan yang valid.")
            else:
                print("Menu tidak ditemukan. Silakan coba lagi.")

def main():
    ulang = True
    print("======================================================================")
    print("                  WARUNG KOPI (NGOPI ASEEEKKK!!!!)                    ")
    print("======================================================================")
    while ulang:
        print("\nAda yang bisa kami bantu?\n(ketik ”selesai” jika tidak perlu)")
        print("1. Lihat menu \n2. Pesan \n3. Checkout")
        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == "selesai":
            ulang = False
            print("Terima kasih telah berkunjung! Sampai jumpa lagi!")
        elif pilihan == "1":
            lihat_menu()
        elif pilihan == "2":
            pesan()
        elif pilihan == "3":
            ulang = False
            print("Berikut adalah rincian pesanan Anda:")
            for i in keranjang:
                print(i)
            print("Total cup yang dipesan :", banyak_cup)
            print("Total harga awal :", total)
            print("Diskon(7%) :", total * 0.07)
            print("Total yang harus dibayar :", total - (total * 0.07))
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()