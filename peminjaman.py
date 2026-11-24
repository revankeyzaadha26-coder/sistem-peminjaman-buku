from datetime import date
from buku import BukuFisik

class Peminjaman:
    def __init__(self):
        self.__transaksi_aktif = {}  # {isbn: (anggota, tanggal_pinjam)}

    @property
    def transaksi_aktif(self) -> dict:
        return dict(self.__transaksi_aktif)

    def sedang_dipinjam(self, isbn: str) -> bool:
        return isbn in self.__transaksi_aktif

    def jumlah_pinjaman(self, anggota) -> int:
        return sum(1 for a, _ in self.__transaksi_aktif.values()
                   if a.id_anggota == anggota.id_anggota)

    def proses_peminjaman(self, anggota, buku):
        print("\n--- Proses Peminjaman ---")
        if not isinstance(buku, BukuFisik):
            print(f"Penolakan: '{buku.judul}' adalah e-book dan tidak dipinjam. Gunakan akses e-book.")
            return

        print(f"Memeriksa ketersediaan buku '{buku.judul}'...")
        if buku.tersedia():
            buku.pinjam()
            self.__transaksi_aktif[buku.isbn] = (anggota, date.today())
            print(f"Sukses: '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
            print(f"Status buku diubah menjadi: '{buku.status}'.")
        else:
            print(f"Penolakan: Buku '{buku.judul}' tidak tersedia (sedang dipinjam).")

    def proses_pengembalian(self, anggota, buku):
        print("\n--- Proses Pengembalian ---")
        print(f"Memeriksa status peminjaman buku '{buku.judul}'...")

        if buku.isbn not in self.__transaksi_aktif:
            print(f"Pengembalian tidak valid: '{buku.judul}' tidak tercatat sedang dipinjam.")
            return

        peminjam, _ = self.__transaksi_aktif[buku.isbn]
        if peminjam.id_anggota != anggota.id_anggota:
            print(f"Pengembalian ditolak: '{buku.judul}' dipinjam oleh {peminjam.nama}, bukan {anggota.nama}.")
            return

        del self.__transaksi_aktif[buku.isbn]
        buku.kembalikan()
        print(f"Sukses: '{buku.judul}' telah dikembalikan oleh {anggota.nama}.")
        print(f"Status buku diubah menjadi: '{buku.status}'.")
