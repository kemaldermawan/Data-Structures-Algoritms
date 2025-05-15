def selection_sort(arr):
    # Menjalankan loop untuk setiap elemen dalam array
    for i in range(len(arr)):
        # Asumsikan elemen saat ini adalah yang terkecil
        min_index = i
        print(f"\nProses iterasi {i + 1}:")

        # Mencari elemen terkecil dalam subarray yang belum terurut
        for j in range(i + 1, len(arr)):
            print(f"  Bandingkan {arr[j]} dengan {arr[min_index]}")
            if arr[j] < arr[min_index]:
                min_index = j

        # Geser elemen untuk menempatkan elemen terkecil pada posisi yang benar
        min_value = arr[min_index]
        for k in range(min_index, i, -1):
            arr[k] = arr[k - 1]
        arr[i] = min_value

        print(f"  Geser elemen dan tempatkan {min_value} di posisi {i}")
        print(f"  Data setelah iterasi {i + 1}: {arr}")
        print("-" * 50)

    return arr

# Program utama
def main():
    while True:
        # Meminta input dari pengguna
        user_input = input("Masukkan Data (pisahkan dengan spasi): ")
        arr = list(map(int, user_input.split()))

        print("\nData sebelum diurutkan:", arr)
        sorted_arr = selection_sort(arr)
        print("\nData setelah diurutkan:", sorted_arr)

        # Menanyakan apakah ingin mengulang program
        repeat = input("\nApakah Anda ingin mengulang program? (ya/tidak): ").strip().lower()
        if repeat != 'ya':
            print("Terima kasih! Program selesai.")
            break

# Menjalankan program utama
main()