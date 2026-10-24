# Latihan 2: Indeks dan Slicing
# Pertemuan 10 - Algoritma dan Pemrograman

teks = "Pemrograman"

print("Teks asli:", teks)
print("Karakter pertama:", teks[0])
print("Karakter ketiga:", teks[2])
print("Karakter terakhir:", teks[-1])

# Mengambil karakter dari indeks 0 sampai sebelum indeks 4
print("Empat karakter pertama:", teks[:4])

# Mengambil karakter mulai indeks 4 sampai akhir
print("Karakter mulai indeks 4:", teks[4:])

# Mengambil sebagian teks menggunakan rentang indeks
print("Potongan teks indeks 2 sampai 6:", teks[2:7])

# Mengambil karakter dengan langkah dua
print("Karakter dengan langkah dua:", teks[::2])

# Membalik urutan karakter
print("Teks terbalik:", teks[::-1])

# Menampilkan panjang string
print("Panjang teks:", len(teks))

# Menampilkan setiap karakter menggunakan perulangan
print("Karakter satu per satu:")

for indeks, karakter in enumerate(teks):
    print(f"Indeks {indeks}: {karakter}")