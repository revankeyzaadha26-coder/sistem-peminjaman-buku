from validasi import wajib_isi

class Anggota:
    def __init__(self, nama: str, id_anggota: str):
        self.__nama = wajib_isi(nama, "Nama")
        self.__id_anggota = wajib_isi(id_anggota, "ID anggota")

    @property
    def nama(self) -> str:
        return self.__nama

    @nama.setter
    def nama(self, nilai: str):
        self.__nama = wajib_isi(nilai, "Nama")

    @property
    def id_anggota(self) -> str:
        return self.__id_anggota

    def pinjam_buku(self, buku, peminjaman):
        peminjaman.proses_peminjaman(self, buku)

    def kembalikan_buku(self, buku, peminjaman):
        peminjaman.proses_pengembalian(self, buku)

    def akses_ebook(self, ebook):
        ebook.akses(self)
        print(f"Anggota {self.__nama} membuka e-book: {ebook.judul} ({ebook.file_pdf})")

    def __str__(self) -> str:
        return f"ID: {self.__id_anggota} | Nama: {self.__nama}"
