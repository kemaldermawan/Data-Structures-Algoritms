class Stack:
    def push(self, item): # Menambahkan elemen ke stack
        self.items.append(item)

    def pop(self): # Menghapus elemen teratas dari stack
        if len(self.items) == 0:
            return "Stack kosong!"
        return self.items.pop()

    def peek(self): # Melihat elemen teratas dari stack tanpa menghapusnya
        if len(self.items) == 0: 
            return "Stack kosong!"
        return self.items[-1]

    def empty(self): # Mengecek apakah stack kosong
        if len(self.items) == 0:
            return "Stack kosong."
        return "Stack tidak kosong."

    def clear(self): # Mengosongkan stack 
        self.items = []
        return "Stack telah dikosongkan."

    def tampilkan(self): # Menampilkan semua elemen dalam stack
        if len(self.items) == 0:
            return "Stack kosong."
        return "\n".join(f"- {item}" for item in reversed(self.items))

# Program utama
stack = Stack()
stack.items = [] 

while True: # Menu program
    print("\n=== Menu Stack ===")
    print("1. Push (Tambah Elemen)")
    print("2. Pop (Hapus Elemen Teratas)")
    print("3. Peek (Lihat Elemen Teratas)")
    print("4. Cek Apakah Stack Kosong")
    print("5. Clear (Kosongkan Stack)")
    print("6. Tampilkan Stack")
    print("7. Keluar Program")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Masukkan nama yang ingin ditambahkan ke stack: ")
        stack.push(nama)
        print(f"'{nama}' berhasil ditambahkan.")
    elif pilihan == "2":
        print(stack.pop())
    elif pilihan == "3":
        print(stack.peek())
    elif pilihan == "4":
        print(stack.empty())
    elif pilihan == "5":
        print(stack.clear())
    elif pilihan == "6":
        print(stack.tampilkan())
    elif pilihan == "7":
        ulang = input("Apakah Anda ingin mengulang program? (ya/tidak): ").strip().lower()
        if ulang != "ya":
            print("Terima kasih! Program selesai.")
            break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-7.")