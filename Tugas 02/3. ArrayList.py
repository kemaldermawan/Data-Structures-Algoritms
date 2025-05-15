def tampilkan(data): # Menampilkan isi array
    if not data: 
        print("Array kosong.")
    else:
        print("Isi array:", ", ".join(data))

def tambah(data): # Menambah data ke dalam array
    nama = input("Masukkan data yang ingin ditambah: ").strip()
    i = 0
    while i < len(data) and nama.lower() > data[i].lower():
        i += 1
    data.insert(i, nama)
    print(f"'{nama}' ditambahkan.")

def hapus(data): # Menghapus data dari array
    nama = input("Masukkan data yang ingin dihapus: ").strip()
    if nama in data:
        data.remove(nama)
        print(f"'{nama}' dihapus.")
    else:
        print("Data tidak ditemukan.")

def main(): # Fungsi utama untuk menjalankan program
    daftar = []
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data")
        print("4. Selesai")
        pilihan = input("Pilih (1-4): ").strip()

        if pilihan == '1':
            tambah(daftar)
        elif pilihan == '2':
            hapus(daftar)
        elif pilihan == '3':
            tampilkan(daftar)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")

while True: # Loop untuk mengulang program
    main()
    ulang = input("\nApakah ingin mengulang program? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        print("Terima kasih! Program selesai.")
        break