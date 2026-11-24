from buku import BukuFisik, EBook
from anggota import Anggota
from daftar_anggota import DaftarAnggota
from petugas import Petugas
from peminjaman import Peminjaman
from katalog import Katalog


def baca_teks(prompt: str, boleh_kosong: bool = False) -> str:
    while True:
        nilai = input(prompt).strip()
        if nilai or boleh_kosong:
            return nilai
        print("Input tidak boleh kosong.")


def data_awal(katalog, daftar_anggota):
    katalog.tambah(BukuFisik("Pemrograman Berorientasi Objek", "Tim Dosen", "978-602-000-1"))
    katalog.tambah(EBook("Analisis dan Desain Sistem", "Pariyadi", "978-602-000-2", "analisis_desain.pdf"))
    daftar_anggota.tambah(Anggota("Afza Qurratu Nazifa", "F1E125002"))
    daftar_anggota.tambah(Anggota("Lintang Retno Putri", "F1E125010"))


def menu_petugas(petugas, katalog, daftar_anggota, peminjaman):
    while True:
        print("\n=== MENU PETUGAS ===")
        print("1. Lihat daftar buku")
        print("2. Tambah buku fisik")
        print("3. Tambah e-book")
        print("4. Ubah data buku")
        print("5. Hapus buku")
        print("6. Lihat daftar anggota")
        print("7. Daftarkan anggota baru")
        print("8. Ubah data anggota")
        print("9. Hapus anggota")
        print("10. Lihat riwayat akses e-book")
        print("0. Kembali")
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                katalog.tampilkan()
            elif pilihan == "2":
                judul = baca_teks("Judul: ")
                penulis = baca_teks("Penulis: ")
                isbn = baca_teks("ISBN: ")
                petugas.kelola_buku(katalog, BukuFisik(judul, penulis, isbn))
            elif pilihan == "3":
                judul = baca_teks("Judul: ")
                penulis = baca_teks("Penulis: ")
                isbn = baca_teks("ISBN: ")
                file_pdf = baca_teks("Nama file PDF: ")
                petugas.kelola_buku(katalog, EBook(judul, penulis, isbn, file_pdf))
            elif pilihan == "4":
                isbn = baca_teks("ISBN buku yang diubah: ")
                judul = baca_teks("Judul baru (kosongkan jika tidak diubah): ", True)
                penulis = baca_teks("Penulis baru (kosongkan jika tidak diubah): ", True)
                petugas.ubah_buku(katalog, isbn, judul, penulis)
            elif pilihan == "5":
                isbn = baca_teks("ISBN buku yang dihapus: ")
                petugas.hapus_buku(katalog, peminjaman, isbn)
            elif pilihan == "6":
                daftar_anggota.tampilkan()
            elif pilihan == "7":
                id_anggota = baca_teks("ID anggota: ")
                nama = baca_teks("Nama: ")
                petugas.kelola_anggota(daftar_anggota, Anggota(nama, id_anggota))
            elif pilihan == "8":
                id_anggota = baca_teks("ID anggota yang diubah: ")
                nama = baca_teks("Nama baru: ")
                petugas.ubah_anggota(daftar_anggota, id_anggota, nama)
            elif pilihan == "9":
                id_anggota = baca_teks("ID anggota yang dihapus: ")
                petugas.hapus_anggota(daftar_anggota, peminjaman, id_anggota)
            elif pilihan == "10":
                isbn = baca_teks("ISBN e-book: ")
                buku = katalog.cari(isbn)
                if isinstance(buku, EBook):
                    katalog.tampilkan_log_akses(buku)
                else:
                    print("E-book dengan ISBN tersebut tidak ditemukan.")
            elif pilihan == "0":
                return
            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Gagal: {e}")


def menu_anggota(anggota, katalog, peminjaman):
    while True:
        print(f"\n=== MENU ANGGOTA ({anggota.nama}) ===")
        print("1. Lihat daftar buku")
        print("2. Pinjam buku")
        print("3. Kembalikan buku")
        print("4. Akses e-book")
        print("0. Kembali")
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                katalog.tampilkan()
            elif pilihan in ("2", "3", "4"):
                isbn = baca_teks("ISBN buku: ")
                buku = katalog.cari(isbn)
                if buku is None:
                    print("Buku tidak ditemukan.")
                elif pilihan == "2":
                    anggota.pinjam_buku(buku, peminjaman)
                elif pilihan == "3":
                    anggota.kembalikan_buku(buku, peminjaman)
                else:
                    if isinstance(buku, EBook):
                        anggota.akses_ebook(buku)
                    else:
                        print("Buku fisik tidak diakses, silakan dipinjam.")
            elif pilihan == "0":
                return
            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Gagal: {e}")


def main():
    katalog = Katalog()
    daftar_anggota = DaftarAnggota()
    peminjaman = Peminjaman()
    petugas = Petugas("Budi", "P001")
    data_awal(katalog, daftar_anggota)

    while True:
        print("\n=== SISTEM PEMINJAMAN BUKU PERPUSTAKAAN ===")
        print("1. Masuk sebagai Petugas")
        print("2. Masuk sebagai Anggota")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            menu_petugas(petugas, katalog, daftar_anggota, peminjaman)
        elif pilihan == "2":
            id_anggota = baca_teks("Masukkan ID anggota: ")
            anggota = daftar_anggota.cari(id_anggota)
            if anggota is None:
                print("ID anggota tidak terdaftar.")
            else:
                menu_anggota(anggota, katalog, peminjaman)
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
