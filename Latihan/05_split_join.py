# Latihan 5: Split dan Join
# Pertemuan 10 - Algoritma dan Pemrograman

# Membuat kalimat dengan string
kalimat = "data teks perlu dibersihkan"

print("Kalimat asli:")
print(kalimat)

# Memisahkan kalimat menjadi daftar kata
kata = kalimat.split()

print("\nHasil split():")
print(kata)

# Menghitung jumlah kata
print("\nJumlah kata:", len(kata))

# Menggabungkan kata menggunakan spasi
kalimat_spasi = " ".join(kata)

print("\nHasil join() dengan spasi:")
print(kalimat_spasi)

# Menggabungkan kata menggunakan tanda hubung
kalimat_hubung = "-".join(kata)

print("\nHasil join() dengan tanda hubung:")
print(kalimat_hubung)

# Menggabungkan kata menggunakan koma
kalimat_koma = ", ".join(kata)

print("\nHasil join() dengan koma:")
print(kalimat_koma)

# Contoh mengolah nama mahasiswa
nama = "  sri   nur   rahmawati  "

# Menghapus spasi di awal dan akhir, lalu memisahkan kata
daftar_nama = nama.strip().split()

# Menggabungkan kembali kata dengan satu spasi
nama_bersih = " ".join(daftar_nama)

print("\nNama sebelum dibersihkan:")
print(repr(nama))

print("Nama setelah dibersihkan:")
print(nama_bersih.title())

# Membuat format kode kelas
kode_kelas = "pmat f 2025"
daftar_kode = kode_kelas.upper().split()
kode_bersih = "-".join(daftar_kode)

print("\nKode kelas sebelum dibersihkan:")
print(kode_kelas)

print("Kode kelas setelah dibersihkan:")
print(kode_bersih)