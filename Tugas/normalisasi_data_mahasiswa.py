# Tugas 4: Normalisasi Data Mahasiswa
# Pertemuan 10 - Algoritma dan Pemrograman
# Nama: Sri Nur Rahmawati
# NIM: 2225250182
# Program Studi: Pendidikan Matematika


def normalisasi_nama(nama):
    """
    Membersihkan nama mahasiswa dari spasi berlebih
    dan mengubahnya menjadi format title case.
    """
    nama_bersih = " ".join(nama.strip().split())
    return nama_bersih.title()


def buat_inisial(nama):
    """
    Membuat inisial berdasarkan huruf pertama
    dari setiap kata dalam nama mahasiswa.
    """
    nama_bersih = normalisasi_nama(nama)
    daftar_kata = nama_bersih.split()

    inisial = "".join(kata[0] for kata in daftar_kata)

    return inisial


def normalisasi_kode(kode):
    """
    Membersihkan kode kelas, mengubahnya menjadi
    huruf besar, dan menghubungkan setiap bagian
    menggunakan tanda hubung.
    """
    daftar_kode = kode.strip().upper().split()
    kode_bersih = "-".join(daftar_kode)

    return kode_bersih


def hitung_jumlah_kata(nama):
    """
    Menghitung jumlah kata dalam nama mahasiswa
    setelah nama dibersihkan.
    """
    nama_bersih = normalisasi_nama(nama)

    if not nama_bersih:
        return 0

    return len(nama_bersih.split())


def main():
    """
    Fungsi utama untuk menerima input,
    memproses data, dan menampilkan hasil.
    """
    print("=" * 45)
    print("     NORMALISASI DATA MAHASISWA")
    print("=" * 45)

    # Meminta input dari pengguna
    nama = input("Nama: ")
    kode = input("Kode kelas: ")

    # Memproses data nama dan kode kelas
    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    jumlah_kata = hitung_jumlah_kata(nama)
    inisial = buat_inisial(nama)

    # Menampilkan hasil normalisasi
    print("\n" + "-" * 45)
    print("HASIL NORMALISASI DATA")
    print("-" * 45)

    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")

    print("-" * 45)


# Menjalankan program utama
if __name__ == "__main__":
    main()