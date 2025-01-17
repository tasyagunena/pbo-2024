class Skincare:
    def __init__(self, nama, merk, harga):
        self.nama = nama
        self.merk = merk
        self.harga = harga
        
    def deskripsi(self):
        print(f"Skincare: {self.nama}, merk: {self.merk}, harga: {self.harga}")
        
    def ubah_merk(self, merk_baru):
        self.merk = merk_baru
        print(f"Merk {self.nama} telah diubah menjadi: {self.merk}")
        
def skincare():
    skincare1 = Skincare("bedak", "wardah", "50k")
    skincare1.deskripsi()
