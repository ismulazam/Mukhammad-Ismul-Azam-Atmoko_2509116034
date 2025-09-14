# Manajemen Sepatu Berdasarkan Aktivitas

List_Sepatu = [["Nike", "Running", "Lari"],["Hoka", "Trail", "Hiking"]]

print("Manajemen Sepatu untuk Aktivitas Tertentu")
print("1. Tambah Sepatu")
print("2. Lihat Daftar Sepatu")

pilihan = input("Pilih menu (ketik 1. Untuk Tambah Sepatu / 2. Untuk Lihat Daftar Sepatu): ")

# CREATE
if pilihan == "1":
    merk = input("Masukkan merk sepatu: ")
    jenis = input("Masukkan jenis sepatu: ")
    aktivitas = input("Masukkan aktivitas sepatu: ")
    List_Sepatu.append([merk, jenis, aktivitas])
    print("Sepatu berhasil ditambahkan!")
    print(List_Sepatu)

# READ
if pilihan == "2":
    if not List_Sepatu:
        print("Belum ada data sepatu.")
    else:
        print("Daftar Sepatu:")
        print("1. Merk: " + List_Sepatu[0][0] + ", Jenis: " + List_Sepatu[0][1] + ", Aktivitas: " + List_Sepatu[0][2])
        print("2. Merk: " + List_Sepatu[1][0] + ", Jenis: " + List_Sepatu[1][1] + ", Aktivitas: " + List_Sepatu[1][2])

if not (pilihan == "1" or pilihan == "2"):
    print("Hanya Ada 2 Opsi.")