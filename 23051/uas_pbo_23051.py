class Elektronik:
    def __init__(self, nama, merk, harga):
        self.nama = nama
        self.merk = merk
        self.harga = harga

    def deskripsi(self):
        print(f"Elektronik: {self.nama}, Merk: {self.merk}, Harga: {self.harga}")
    
    def ubah_harga(self, harga_baru):
        self.harga = harga_baru
        print(f"harga{self. nama} telah diubah menjadi: {self. harga}")

def elektronik():
    elektronik1 = Elektronik("Oppo", "Samsung", "Iphone")
    elektronik1.deskripsi()

