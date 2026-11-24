from buku import BukuFisik, EBook, format_tanggal

class Katalog:
    def __init__(self):
        self.__daftar = []

    def tambah(self, buku):
        if self.cari(buku.isbn) is not None:
            raise ValueError(f"ISBN {buku.isbn} sudah terdaftar.")
        self.__daftar.append(buku)

    def cari(self, isbn: str):
        for b in self.__daftar:
            if b.isbn == isbn:
                return b
        return None

    def hapus(self, isbn: str):
        buku = self.cari(isbn)
        if buku is None:
            raise ValueError(f"Buku dengan ISBN {isbn} tidak ditemukan.")
        self.__daftar.remove(buku)
        return buku

    def semua(self) -> list:
        return list(self.__daftar)

    def tampilkan(self):
        print("\n========== DAFTAR BUKU ==========")
        fisik = [b for b in self.__daftar if isinstance(b, BukuFisik)]
        ebook = [b for b in self.__daftar if isinstance(b, EBook)]

        print("\n[Buku Fisik]")
        if not fisik:
            print("(kosong)")
        for i, b in enumerate(fisik, 1):
            print(f"{i}. {b}")

        print("\n[E-Book]")
        if not ebook:
            print("(kosong)")
        for i, b in enumerate(ebook, 1):
            print(f"{i}. {b}")

    def tampilkan_log_akses(self, ebook: EBook):
        print(f"\nRiwayat akses '{ebook.judul}':")
        if not ebook.log_akses:
            print("(belum ada yang mengakses)")
        for anggota, tgl in ebook.log_akses:
            print(f"- {anggota.nama} mengakses pada tanggal {format_tanggal(tgl)}")
