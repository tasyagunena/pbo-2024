class PKM:
    def __init__(self, judul, bidang, anggota, deskripsi):
        self.judul = judul
        self.bidang = bidang
        self.anggota = anggota
        self.deskripsi = deskripsi

    def tampilkan_info(self):
        print("\n=== Informasi PKM ===")
        print(f"Judul       : {self.judul}")
        print(f"Bidang      : {self.bidang}")
        print(f"Anggota     : {', '.join(self.anggota)}")
        print(f"Deskripsi   : {self.deskripsi}")


def tambah_pkm():
    print("\n=== Tambah Ide PKM ===")
    judul = input("Masukkan judul PKM: ")
    bidang = input("Masukkan bidang PKM (contoh: Penelitian, Kewirausahaan, dll.): ")
    anggota = input("Masukkan nama anggota (pisahkan dengan koma): ").split(", ")
    deskripsi = input("Masukkan deskripsi singkat PKM: ")

    return PKM(judul, bidang, anggota, deskripsi)


def taex():
    daftar_pkm = []

    while True:
        print("\n=== Menu PKM ===")
        print("1. Tambah Ide PKM")
        print("2. Lihat Semua PKM")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            pkm_baru = tambah_pkm()
            daftar_pkm.append(pkm_baru)
            print("Ide PKM berhasil ditambahkan!")
        elif pilihan == "2":
            if daftar_pkm:
                for i, pkm in enumerate(daftar_pkm, 1):
                    print(f"\nPKM #{i}")
                    pkm.tampilkan_info()
            else:
                print("\nBelum ada ide PKM yang terdaftar.")
        elif pilihan == "3":
            print("Terima kasih telah menggunakan program PKM!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


