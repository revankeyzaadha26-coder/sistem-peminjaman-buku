from abc import ABC, abstractmethod
from datetime import date
from validasi import wajib_isi

BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]

def format_tanggal(tgl: date) -> str:
    return f"{tgl.day} {BULAN[tgl.month - 1]} {tgl.year}"


class Buku(ABC):
    def __init__(self, judul: str, penulis: str, isbn: str):
        self.__judul = wajib_isi(judul, "Judul")
        self.__penulis = wajib_isi(penulis, "Penulis")
        self.__isbn = wajib_isi(isbn, "ISBN")

    @property
    def judul(self) -> str:
        return self.__judul

    @judul.setter
    def judul(self, nilai: str):
        self.__judul = wajib_isi(nilai, "Judul")

    @property
    def penulis(self) -> str:
        return self.__penulis

    @penulis.setter
    def penulis(self, nilai: str):
        self.__penulis = wajib_isi(nilai, "Penulis")

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    @abstractmethod
    def jenis(self) -> str:
        pass

    @abstractmethod
    def tersedia(self) -> bool:
        pass

    def __str__(self) -> str:
        return f"[{self.__isbn}] {self.__judul} oleh {self.__penulis}"


class BukuFisik(Buku):
    def __init__(self, judul: str, penulis: str, isbn: str, status: str = "Tersedia"):
        super().__init__(judul, penulis, isbn)
        if status not in ["Tersedia", "Dipinjam"]:
            raise ValueError("Status buku harus 'Tersedia' atau 'Dipinjam'")
        self.__status = status

    @property
    def jenis(self) -> str:
        return "Fisik"

    @property
    def status(self) -> str:
        return self.__status

    def tersedia(self) -> bool:
        return self.__status == "Tersedia"

    def pinjam(self):
        if not self.tersedia():
            raise ValueError(f"Buku '{self.judul}' sedang tidak tersedia.")
        self.__status = "Dipinjam"

    def kembalikan(self):
        if self.tersedia():
            raise ValueError(f"Buku '{self.judul}' tidak sedang dipinjam.")
        self.__status = "Tersedia"

    def __str__(self) -> str:
        return f"{super().__str__()} - Status: {self.__status}"


class EBook(Buku):
    def __init__(self, judul: str, penulis: str, isbn: str, file_pdf: str):
        super().__init__(judul, penulis, isbn)
        self.__file_pdf = wajib_isi(file_pdf, "Nama file PDF")
        self.__log_akses = []  # list of (anggota, tanggal)

    @property
    def jenis(self) -> str:
        return "E-Book"

    @property
    def file_pdf(self) -> str:
        return self.__file_pdf

    @property
    def log_akses(self) -> list:
        return list(self.__log_akses)

    def tersedia(self) -> bool:
        return True

    def akses(self, anggota, tanggal: date = None) -> str:
        tanggal = tanggal or date.today()
        self.__log_akses.append((anggota, tanggal))
        return self.__file_pdf

    def __str__(self) -> str:
        return f"{super().__str__()} - Format: PDF (diakses {len(self.__log_akses)}x)"
