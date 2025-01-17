class Buku:
    def __init__(self, nama_toko,jenis,harga ):
        self.nama_toko=nama_toko
        self.jenis=jenis
        self.harga=harga

    def deskripsi(self):
        print(f"buku: {self.nama_toko},jenis:{self.jenis},harga:{self.harga}")

    def ubah_jenis(self, jenis_baru):
        self.jenis = jenis_baru
        print(f"jenis{self.nama_toko} telah di ubah menjadi:{self.jenis}")

def buku():
    buku1 = Buku("buku abadi","filsafat","RP 100.000")  
    buku1.deskripsi()              
def buku2():
    buku2 = Buku("buku abadi","logika","RP 200.000")  
    buku2.deskripsi()              
        
def buku3():
    buku3 = Buku("gramedia","tuntunan solat","RP 250.000")  
    buku3.deskripsi()              
        
        














