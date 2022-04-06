import function
daftar_kontak = []
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")
    menu = input("Pilih Menu : ")
    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        daftar_kontak.append(function.new_kontak())
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")
print("Program selesai berjalan, sampai jumpa")