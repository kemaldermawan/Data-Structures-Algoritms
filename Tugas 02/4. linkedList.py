class Node:  #Kelas yang merepresentasikan node
    def __init__(self, code, name):
        self.code = code  #Menyimpan nilai kode
        self.name = name  #Menyimpan nama
        self.next = None  #Pointer ke penunjuk berikutnya
    
    def display(self):  #Fungsi untuk menampilkan isi simpul
        print(f"{self.code} = {self.name}")

class LinkedList:  #Kelas yang merepresentasikan LinkedList
    def __init__(self):
        self.first = None  #Penunjuk ke simpul pertama (head)
        self.before = None  #Sebagai penunjuk simpul sebelumnya (Digunakan dalam pencarian)
        self.dataPosition = None  #Sebagai penunjuk ke simpul yang ditemukan saat pencarian

    def isEmpty(self):  #Mengecek data kosong
        return self.first is None

    def insert(self, code, name):  
        newNode = Node(code, name)  #Menambahkan simpul pada node
        newNode.next = self.first  #Simpul selanjutnya menunjuk simpul lama (None)
        self.first = newNode  #Meng-update head menjadi simpul baru
    
    def findX(self, x):
        self.dataPosition = self.first  #Mulai pencarian dari simpul pertama
        self.before = None  #Meng-set node sebelumnya ke none kembali
        while self.dataPosition is not None:
            if self.dataPosition.code == x:  #Ambil kode dari simpul saat ini
                return True  #Data ditemukan
            self.before = self.dataPosition  #Menyimpan simpul saat ini sebagai pendahulu
            self.dataPosition = self.dataPosition.next  #Berlanjut ke simpul berikutnya
        return False

    def find(self, x):  #Mencari simpul berdasarkan kode lalu Mengembalikan simpul yang ditemukan atau None jika tidak ditemukan.
        if self.findX(x):
            return self.dataPosition
        return None
    
    def remove(self, x):
        if not self.findX(x):  #Jika tidak ditemukan, tampilkan pesan dan kembalikan False.
            print("Data yang dihapus tidak ditemukan")
            return False
        if self.before is None:  #Jika simpul yang dihapus adalah simpul pertama, geser first ke simpul selanjutnya.
            self.first = self.first.next
        else:  #Jika simpul berada di tengah/akhir, lewati simpul yang akan dihapus dengan menyambungkan simpul sebelumnya ke simpul setelahnya.
            self.before.next = self.dataPosition.next
        return True
    
    def display(self):
        print("Isi Linked List")
        sign = self.first
        if sign is None:  #Jika sign kosong
            print("Linked List Kosong")
        while sign is not None:
            sign.display()  #Tampilkan isi simpul saat ini.
            sign = sign.next  #Geser ke simpul selanjutnya.

 #Digunakan untuk memastikan bahwa kode di bawah ini hanya dijalankan saat file ini dieksekusi langsung, bukan saat diimpor sebagai modul.
linkedList = LinkedList()  #Membuat objek LinkedList untuk menyimpan data.

while True:
    #Menampilkan pilihan menu
    print("\n===== Menu Linked List =====")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Cari data")
    print("4. Tampilkan data")
    print("5. Keluar")

    pilihan = input("Pilih Menu (1-5) : ")

    if pilihan == '1':  #Memasukkan nilai
        code = input("Masukkan kode: ").upper()
        name = input("Masukkan nama: ")
        linkedList.insert(code, name)
        print("Data berhasil ditambahkan.")

    elif pilihan == '2':  #Menghapus Nilai
        if linkedList.isEmpty():
            print("Data kosong")
        else:
            code = input("Masukkan kode yang ingin dihapus: ").upper()
            if linkedList.remove(code):
                print(f"{code} berhasil dihapus.")

    elif pilihan == '3':  #Mencari Nilai
        if linkedList.isEmpty():
            print("Data kosong")
        else:
            code = input("Masukkan kode yang ingin dicari: ").upper()
            result = linkedList.find(code)
            if result is not None:
                print("Data ditemukan:")
                result.display()
            else:
                print(f"{code} tidak ditemukan.")

    elif pilihan == '4':  #Menampilkan data
        linkedList.display()

    elif pilihan == '5':  #Mengakhiri data
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Self.first = head
#head -> None
#Jerman -> None
#Inggris -> Jerman -> Prancis -> None