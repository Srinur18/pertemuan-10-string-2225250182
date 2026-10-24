# Latihan 4: Membersihkan Teks
# Pertemuan 10 - Algoritma dan Pemrograman


def bersihkan_teks(teks):
    """
    Menghapus spasi berlebih dan merapikan teks.
    Spasi di awal dan akhir dihapus.
    Spasi berulang di antara kata dijadikan satu spasi.
    """
    teks = teks.strip()
    kata = teks.split()
    teks_bersih = " ".join(kata)

    return teks_bersih


# Contoh teks dengan spasi berlebih
teks = " belajar    python  untuk           pendidikan       "

print("Teks sebelum dibersihkan:")
print(repr(teks))

# Membersihkan teks
teks_bersih = bersihkan_teks(teks)

print("\nTeks setelah dibersihkan:")
print(teks_bersih)

# Mengubah huruf pertama kalimat menjadi kapital
print("\nHasil capitalize():")
print(teks_bersih.capitalize())

# Menyeragamkan huruf awal setiap kata
print("\nHasil title():")
print(teks_bersih.title())

# Contoh lain dengan format huruf berbeda
teks_kedua = "   DATA   mahasiswa   TIDAK   konsisten   "

print("\nContoh teks kedua:")
print("Sebelum:", repr(teks_kedua))
print("Sesudah:", bersihkan_teks(teks_kedua))

# Menguji teks kosong atau hanya berisi spasi
teks_kosong = "     "
print("\nHasil pembersihan teks kosong:")
print(repr(bersihkan_teks(teks_kosong)))