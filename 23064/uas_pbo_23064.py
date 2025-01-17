class Batu:
    def __init__(self,nama,jenis,ukuran):
        self.nama =nama
        self.jenis =jenis
        self.ukuran =ukuran
    def deskripsi(self):
       print(f"batu: {self.nama}, jenis: {self.jenis}, ukuran: {self.ukuran}")

    def ubah_jenis(self, jenis_baru):
       self.jenis = jenis_baru
       print(f"jenis: {self.nama}, telah diubah menjadi: {self.jenis}") 


def batu():
    batu1 = Batu("batu", "batu gunung", "5kg")
    batu1.deskripsi()

    


