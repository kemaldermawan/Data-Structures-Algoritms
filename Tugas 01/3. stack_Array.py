def create_stack(capacity):  #Fungsi untuk membuat stack dengan kapasitas tertentu
    stack = []
    return stack, capacity

def is_empty(stack): #Mengecek apakah stack kosong
    return len(stack) == 0

def is_full(stack, capacity): #Mengecek apakah stack full
    return len(stack) == capacity

def push(stack, item, capacity): #Fungsi untuk menambahkan elemen ke dalam stack
    if is_full(stack, capacity): #Jika stack full
        print("Stack Overflow! Tidak bisa menambahkan elemen.")
    else:
        stack.append(item) #Jika masih tersisa ruang
        print(f"Pushed: {item}")

def pop(stack): #Fungsi untuk menghapus elemen teratas
    if is_empty(stack): #Jika tidak ada elemen
        print("Stack Underflow! Tidak ada elemen untuk di-pop.")
    else:
        removed = stack.pop() #Jika ada elemen yang diambil
        print(f"Popped : {removed}")

def display(stack, capacity): #Fungsi untuk mengecek elemen apa saja yang terdapat dalam stack
    if len(stack) == capacity: #Saat stack full
        print("Stack penuh")
        print("Stack saat ini:", stack)
    else: #Saat stack masih tersisa
        print("Stack tersisa :", capacity - len(stack)) 
        print("Stack saat ini:", stack)

#Main code untuk menjalankan program
capacity = int(input("Masukkan kapasitas stack: "))
stack, capacity = create_stack(capacity)

while True: #Pilihan menu yang dapat dipilih user
    print("\nMenu:")
    print("1. Push (Tambahkan elemen)")
    print("2. Pop (Hapus elemen teratas)")
    print("3. Tampilkan stack")
    print("4. Keluar")
    choice = int(input("Pilih menu: "))

    if choice == 1:
        item = input("Masukkan elemen yang ingin ditambahkan: ")
        push(stack, item, capacity)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        display(stack, capacity)
    elif choice == 4:
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")