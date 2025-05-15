def selection_sort(data, jenis_pengurutan): # Fungsi untuk melakukan pengurutan dengan metode Selection Sort

    for i in range(len(data)): # Iterasi untuk setiap elemen dalam data
        index = i # Menyimpan indeks elemen terkecil atau terbesar
        print(f"\nProses iterasi {i + 1}:") 

        for j in range(i + 1, len(data)): # Iterasi untuk membandingkan elemen
            print(f"  Bandingkan {data[j]} dengan {data[index]}")
            if jenis_pengurutan == 1: # Pengurutan naik
                if data[j] < data[index]:
                    index = j
            elif jenis_pengurutan == 2: # Pengurutan turun
                if data[j] > data[index]:
                    index = j

        if index != i: # Jika elemen terkecil atau terbesar bukan elemen pertama
            nilai = data[index]  
            for k in range(index, i, -1):
                data[k] = data[k - 1]
            data[i] = nilai
            print(f"  Geser elemen dan tempatkan {nilai} di posisi {i}")
        print(f"  Data setelah iterasi {i + 1}: {data}")
        print("-" * 50)
    return data

while True: # Program utama untuk meminta input data dari pengguna
    user_input = input("Masukkan Data (pisahkan dengan spasi): ")
    data = list(map(int, user_input.split())) # Mengubah input menjadi list integer

    print("Pilih jenis pengurutan:")
    print("1. Pengurutan naik (ascending)")
    print("2. Pengurutan turun (descending)")
    
    jenis_pengurutan = input("Masukkan pilihan (1 atau 2): ").strip()

    while jenis_pengurutan not in ['1', '2']:
        jenis_pengurutan = input("Pilihan tidak valid. Masukkan 1 untuk menaik atau 2 untuk menurun: ").strip()

    jenis_pengurutan = int(jenis_pengurutan) # Mengubah pilihan menjadi integer

    print("\nData sebelum diurutkan:", data)
    selection_sort(data, jenis_pengurutan) # Memanggil fungsi selection_sort
    print("Data setelah diurutkan:", data)

    ulang = input("\nIngin mengulang program? (ya/tidak): ").strip().lower() # Meminta konfirmasi untuk mengulang program
    if ulang != 'ya':
        print("Terima kasih! Program selesai.")
        break 