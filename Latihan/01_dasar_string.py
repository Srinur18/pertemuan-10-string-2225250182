# Latihan 1: Dasar String
# Pertemuan 10 - Algoritma dan Pemrograman

# Membuat string menggunakan tanda kutip ganda
teks = "Algoritma"

# Menampilkan teks asli
print("Teks asli:", teks)

# Menghitung panjang string
print("Panjang teks:", len(teks))

# Mengubah semua huruf menjadi huruf besar
print("Huruf besar:", teks.upper())

# Mengubah semua huruf menjadi huruf kecil
print("Huruf kecil:", teks.lower())

# Menggabungkan dua string
kata_pertama = "Belajar"
kata_kedua = "Python"
kalimat = kata_pertama + " " + kata_kedua

print("Hasil penggabungan:", kalimat)

# Mengulang string
print("Pengulangan teks:", "Ha" * 3)

# Memeriksa keberadaan kata dalam string
print("Apakah terdapat kata Python?", "Python" in kalimat)

# Membuat string dengan tanda kutip tunggal
mata_kuliah = 'Algoritma dan Pemrograman'
print("Mata kuliah:", mata_kuliah)

# Membuat string beberapa baris
pesan = """Belajar Python
dengan latihan
secara bertahap."""

print("Pesan beberapa baris:")
print(pesan)