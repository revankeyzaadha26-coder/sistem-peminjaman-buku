class DaftarAnggota:
    def __init__(self):
        self.__daftar = []

    def tambah(self, anggota):
        if self.cari(anggota.id_anggota) is not None:
            raise ValueError(f"ID anggota {anggota.id_anggota} sudah terdaftar.")
        self.__daftar.append(anggota)

    def cari(self, id_anggota: str):
        for a in self.__daftar:
            if a.id_anggota == id_anggota:
                return a
        return None

    def hapus(self, id_anggota: str):
        anggota = self.cari(id_anggota)
        if anggota is None:
            raise ValueError(f"Anggota dengan ID {id_anggota} tidak ditemukan.")
        self.__daftar.remove(anggota)
        return anggota

    def semua(self) -> list:
        return list(self.__daftar)

    def tampilkan(self):
        print("\n========== DAFTAR ANGGOTA ==========")
        if not self.__daftar:
            print("(kosong)")
        for i, a in enumerate(self.__daftar, 1):
            print(f"{i}. {a}")
