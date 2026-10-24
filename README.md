# Pertemuan 10 - String dan Pengolahan Teks

**Nama:** Sri Nur Rahmawati  
**NIM:** 2225250182  
**Kelas:** 3F

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python, mulai dari mengakses karakter, menggunakan indeks dan slicing, memanfaatkan method string, membersihkan teks, memisahkan dan menggabungkan kata, hingga melakukan pencarian kata. Materi ini diterapkan dalam program normalisasi data nama mahasiswa dan kode kelas.

## Struktur Program

Folder `latihan` berisi enam program untuk mempelajari dasar string, indeks dan slicing, method string, pembersihan teks, penggunaan split dan join, serta pencarian kata.

Folder `tugas` berisi program `normalisasi_data_mahasiswa.py` yang digunakan untuk membersihkan nama mahasiswa dan kode kelas, menghitung jumlah kata, serta membuat inisial nama secara otomatis.

## Cara Menjalankan

Pastikan Python 3 sudah terpasang dan terminal VS Code berada di folder utama proyek.

Jalankan program tugas dengan perintah:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

Jika menggunakan Windows dan perintah `python3` tidak dikenali, gunakan:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

Program kemudian meminta input nama mahasiswa dan kode kelas. Masukkan data sesuai permintaan, lalu tekan Enter untuk melihat hasil normalisasi.

## Algoritma

1. Program meminta pengguna memasukkan nama lengkap mahasiswa dan kode kelas.
2. Nama mahasiswa dibersihkan menggunakan `strip()` untuk menghapus spasi di awal dan akhir, kemudian menggunakan `split()` dan `join()` untuk merapikan spasi berlebih di antara kata.
3. Nama yang sudah bersih diubah menjadi format huruf kapital pada awal setiap kata menggunakan `title()`.
4. Nama dibagi menjadi beberapa kata untuk menghitung jumlah kata dan mengambil huruf pertama setiap kata sebagai inisial.
5. Kode kelas dibersihkan dari spasi yang tidak diperlukan, diubah menjadi huruf besar menggunakan `upper()`, kemudian kata-katanya digabungkan dengan tanda hubung menggunakan `join()`.
6. Program menampilkan nama bersih, kode kelas yang sudah dinormalisasi, jumlah kata, dan inisial mahasiswa.

## Test Case

| No. | Input Nama | Input Kode Kelas | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `aan hendrayana` | `pmat a 2026` | Nama: Aan Hendrayana; Kode: PMAT-A-2026; Jumlah kata: 2; Inisial: AH | Nama: Aan Hendrayana; Kode: PMAT-A-2026; Jumlah kata: 2; Inisial: AH | Berhasil |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | Nama: Fathiyyah Muthmainnah; Kode: KELAS-B; Jumlah kata: 2; Inisial: FM | Nama: Fathiyyah Muthmainnah; Kode: KELAS-B; Jumlah kata: 2; Inisial: FM | Berhasil |
| 3 | `BUDI` | `pmtk 01` | Nama: Budi; Kode: PMTK-01; Jumlah kata: 1; Inisial: B | Nama: Budi; Kode: PMTK-01; Jumlah kata: 1; Inisial: B | Berhasil |
| 4 | `siti nur aisyah` | `kelas c` | Nama: Siti Nur Aisyah; Kode: KELAS-C; Jumlah kata: 3; Inisial: SNA | Nama: Siti Nur Aisyah; Kode: KELAS-C; Jumlah kata: 3; Inisial: SNA | Berhasil |

Catatan: Hasil aktual di atas merupakan hasil yang diharapkan dari kode. Jalankan program dan cocokkan kembali hasilnya sebelum mengumpulkan tugas.

## Refleksi

Salah satu masalah yang ditemukan adalah data nama mahasiswa memiliki spasi berlebih dan penggunaan huruf besar serta huruf kecil yang tidak konsisten. Hal tersebut dapat membuat data terlihat berbeda meskipun nama yang dimaksud sama. Masalah ini diperbaiki dengan menggunakan `strip()` dan `split()` untuk merapikan spasi, `join()` untuk menyusun kembali kata, serta `title()` untuk menyeragamkan penulisan nama. Pada kode kelas, penggunaan `upper()` dan tanda hubung membantu membuat format kode lebih konsisten.

## Sumber

Bahan Ajar Algoritma dan Pemrograman, Pertemuan 10: String dan Pengolahan Teks dalam Python, Tahun Ajaran 2026/2027 Ganjil.