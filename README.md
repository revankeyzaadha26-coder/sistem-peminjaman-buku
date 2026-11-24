# Sistem Peminjaman Buku Perpustakaan

Program konsol berbasis Python (OOP) untuk mengelola buku fisik, e-book, anggota, dan peminjaman.
Proyek kelompok 5, mata kuliah Pemrograman Berorientasi Objek, Universitas Jambi.

## Cara menjalankan
```
python main.py
```
Butuh Python 3.8 atau lebih baru. Tidak ada library tambahan.

## Struktur file
| File | Fungsi |
|---|---|
| main.py | Titik masuk, menu interaktif Petugas dan Anggota |
| buku.py | Abstract class Buku, turunan BukuFisik dan EBook |
| katalog.py | Menyimpan dan menampilkan daftar buku |
| anggota.py | Class Anggota |
| daftar_anggota.py | Menyimpan dan mengelola daftar anggota |
| petugas.py | Class Petugas (tambah, ubah, hapus buku dan anggota) |
| peminjaman.py | Proses peminjaman dan pengembalian buku fisik |
| validasi.py | Fungsi validasi input |

## Data awal untuk demo
- ISBN `978-602-000-1` (buku fisik), `978-602-000-2` (e-book)
- ID anggota `F1E125002`, `F1E125010`
