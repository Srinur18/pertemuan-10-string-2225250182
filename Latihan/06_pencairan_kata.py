# Latihan 6: Pencarian Kata
# Pertemuan 10 - Algoritma dan Pemrograman

teks = "Python untuk data. Python untuk pendidikan."
kata_dicari = "python"

# Menyamakan huruf menjadi huruf kecil agar pencarian
# tidak terpengaruh perbedaan huruf besar dan kecil.
teks_bersih = teks.lower()
kata_dicari = kata_dicari.lower()

print("Teks asli:")
print(teks)

# Memeriksa apakah kata terdapat dalam teks
ditemukan = kata_dicari in teks_bersih
print("\nApakah kata ditemukan?", ditemukan)

# Menghitung jumlah kemunculan kata
jumlah = teks_bersih.count(kata_dicari)
print("Jumlah kemunculan kata:", jumlah)

# Mencari posisi kemunculan pertama kata
posisi = teks_bersih.find(kata_dicari)
print("Posisi kemunculan pertama:", posisi)

# Memeriksa kata yang tidak terdapat dalam teks
kata_lain = "matematika"
posisi_lain = teks_bersih.find(kata_lain)

print("\nKata yang dicari:", kata_lain)

if kata_lain in teks_bersih:
    print("Kata ditemukan pada posisi:", posisi_lain)
else:
    print("Kata tidak ditemukan.")

# Memeriksa awalan teks
print("\nApakah teks diawali kata Python?",
      teks_bersih.startswith("python"))

# Memeriksa akhiran teks
print("Apakah teks diakhiri tanda titik?",
      teks.strip().endswith("."))

# Menghitung jumlah kata dalam teks
daftar_kata = teks.split()
print("Jumlah seluruh kata:", len(daftar_kata))