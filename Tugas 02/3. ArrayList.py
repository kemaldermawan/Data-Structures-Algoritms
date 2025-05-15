class DaftarData:
    def __init__(self):
        self.data = []

    def tampilkan_data(self):
        print("\nDaftar Data:")
        for nama in self.data:
            print(nama, end=' ')
        print("\n")

    def tambah_data(self, data_baru):
        posisi = -1
        for i, nama in enumerate(self.data):
            if data_baru.lower() < nama.lower():
                posisi = i
                break
        if posisi == -1:
            self.data.append(data_baru)
        else:
            self.data.insert(posisi, data_baru)
        return True

    def hapus_data(self, data_yang_dihapus):
        try:
            self.data.remove(data_yang_dihapus)
            return True
        except ValueError:
            return False

    def tampilkan_menu(self):
        print("Menu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Daftar Data")
        print("4. Keluar")
        pilihan = input("Pilih (1 - 4): ")
        return pilihan.strip()
    
def main():
    daftar = DaftarData()

    while True:
        pilihan = daftar.tampilkan_menu()

        if pilihan == '1':
            nama_data = input("Masukkan nama data yang ingin ditambahkan: ").strip()
            daftar.tambah_data(nama_data)
            print(f"{nama_data} berhasil ditambahkan.")
        elif pilihan == '2':
            nama_data = input("Masukkan nama data yang ingin dihapus: ").strip()
            if daftar.hapus_data(nama_data):
                print(f"{nama_data} berhasil dihapus.")
            else:
                print("Data tidak ditemukan.")
        elif pilihan == '3':
            daftar.tampilkan_data()
        elif pilihan == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Loop untuk mengulang program
while True:
    main()
    ulang = input("Apakah Anda ingin mengulang program? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        print("Terima kasih telah menggunakan program.")
        break