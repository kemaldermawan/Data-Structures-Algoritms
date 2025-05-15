def merge_sort(arr, level=0):
    if len(arr) > 1:
        # Menentukan titik tengah
        mid = len(arr) // 2
        
        # Membagi array menjadi dua subarray
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Menampilkan langkah pembagian array tanpa kurung siku ganda
        print(f"{'  ' * level}{arr} -> {left_half} {right_half}")
        
        # Rekursif memanggil merge_sort pada masing-masing bagian
        merge_sort(left_half, level + 1)
        merge_sort(right_half, level + 1)

        # Indeks untuk menggabungkan subarray
        i = j = k = 0

        # Menggabungkan dua subarray ke dalam array utama
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Memeriksa jika ada elemen yang tersisa di left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Memeriksa jika ada elemen yang tersisa di right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Menampilkan hasil penggabungan dengan benar, menggunakan kurung siku tunggal
        print(f"{'  ' * level}{left_half} -> {right_half} -> {arr}")
    
    return arr

# Program utama
def main():
    while True:
        user_input = input("Masukkan Data (pisahkan dengan spasi): ")
        arr = list(map(int, user_input.split()))

        print("\nData sebelum diurutkan:", arr)
        sorted_arr = merge_sort(arr)
        print("\nData setelah diurutkan:", sorted_arr)

        # Menanyakan apakah ingin mengulang program
        repeat = input("\nApakah Anda ingin mengulang program? (ya/tidak): ").strip().lower()
        if repeat != 'ya':
            print("Terima kasih! Program selesai.")
            break

# Menjalankan program utama
main()
