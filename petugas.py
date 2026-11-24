class Petugas:
    def __init__(self, nama: str, id_petugas: str):
        self.__nama = nama
        self.__id_petugas = id_petugas

    @property
    def nama(self) -> str:
        return self.__nama

    @property
    def id_petugas(self) -> str:
        return self.__id_petugas

    # ----- Buku -----
    def kelola_buku(self, katalog, buku_baru):
        katalog.tambah(buku_baru)
        print(f"Petugas {self.__nama} menambahkan buku baru: {buku_baru.judul} ({buku_baru.jenis})")

    def ubah_buku(self, katalog, isbn: str, judul: str = None, penulis: str = None):
        buku = katalog.cari(isbn)
        if buku is None:
            raise ValueError(f"Buku dengan ISBN {isbn} tidak ditemukan.")
        if judul:
            buku.judul = judul
        if penulis:
            buku.penulis = penulis
        print(f"Petugas {self.__nama} mengubah data buku: {buku}")

    def hapus_buku(self, katalog, peminjaman, isbn: str):
        if peminjaman.sedang_dipinjam(isbn):
            raise ValueError("Buku sedang dipinjam, tidak bisa dihapus.")
        buku = katalog.hapus(isbn)
        print(f"Petugas {self.__nama} menghapus buku: {buku.judul}")

    # ----- Anggota -----
    def kelola_anggota(self, daftar_anggota, anggota_baru):
        daftar_anggota.tambah(anggota_baru)
        print(f"Petugas {self.__nama} mendaftarkan anggota baru: {anggota_baru.nama}")

    def ubah_anggota(self, daftar_anggota, id_anggota: str, nama_baru: str):
        anggota = daftar_anggota.cari(id_anggota)
        if anggota is None:
            raise ValueError(f"Anggota dengan ID {id_anggota} tidak ditemukan.")
        anggota.nama = nama_baru
        print(f"Petugas {self.__nama} mengubah data anggota: {anggota}")

    def hapus_anggota(self, daftar_anggota, peminjaman, id_anggota: str):
        anggota = daftar_anggota.cari(id_anggota)
        if anggota is None:
            raise ValueError(f"Anggota dengan ID {id_anggota} tidak ditemukan.")
        if peminjaman.jumlah_pinjaman(anggota) > 0:
            raise ValueError("Anggota masih memiliki pinjaman aktif, tidak bisa dihapus.")
        daftar_anggota.hapus(id_anggota)
        print(f"Petugas {self.__nama} menghapus anggota: {anggota.nama}")
