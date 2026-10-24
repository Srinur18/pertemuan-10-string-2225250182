# Latihan 3: Method String
# Pertemuan 10 - Algoritma dan Pemrograman

nama = " fATHIYYAH mUTHMAINNAH         "

print("Nama asli:", repr(nama))

# Menghapus spasi di awal dan akhir
nama_bersih = nama.strip()
print("Setelah strip():", nama_bersih)

# Mengubah huruf awal setiap kata menjadi kapital
print("Hasil title():", nama_bersih.title())

# Mengubah semua huruf menjadi huruf besar
print("Hasil upper():", nama_bersih.upper())

# Mengubah semua huruf menjadi huruf kecil
print("Hasil lower():", nama_bersih.lower())

# Mengubah huruf pertama string menjadi kapital
teks = "python dasar"
print("Hasil capitalize():", teks.capitalize())

# Mengganti karakter tertentu
tanggal = "2026-10-24"
print("Tanggal setelah replace():", tanggal.replace("-", "/"))

# Mencari posisi kata dalam string
kalimat = "Belajar Python untuk pendidikan"
posisi = kalimat.find("Python")
print("Posisi kata Python:", posisi)

# Menghitung jumlah kemunculan karakter
buah = "banana"
print("Jumlah huruf a:", buah.count("a"))

# Memeriksa awalan string
kode_kelas = "KLS-A"
print("Diawali KLS:", kode_kelas.startswith("KLS"))

# Memeriksa akhiran string
nama_file = "data.csv"
print("Diakhiri .csv:", nama_file.endswith(".csv"))

# Memastikan teks yang dinormalisasi sama
teks_pertama = " Python "
teks_kedua = "python"

print(
    "Apakah kedua teks sama setelah normalisasi?",
    teks_pertama.strip().lower() == teks_kedua.strip().lower()
)