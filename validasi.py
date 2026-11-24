def wajib_isi(nilai, nama_field: str) -> str:
    if not isinstance(nilai, str) or not nilai.strip():
        raise ValueError(f"{nama_field} tidak boleh kosong.")
    return nilai.strip()
