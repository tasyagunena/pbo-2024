class Warung:
    def __init__(self, nama, harga, jenis):
        self.nama= nama
        self.harga= harga
        self.jenis= jenis
    
    def deskripsi(self):
        print(f"Warung: {self.nama}, Harga: {self.harga}, Jenis: {self.jenis}")

    def ubah_jenis(self, jenis_baru):
        self.jenis = jenis_baru
        print(f"Jenis {"self.nama"} telah diubah menjadi: {self.jenis}")
def warung():
    warung1 = Warung("warung jelia", "25k", "nasi goreng", )
    warung1.deskripsi()

def warung2():
    warung2 = Warung("warung jelia", "20k", "ketoprak", )
    warung2.deskripsi()

def warung3():
    warung3 = Warung("warung jelia", "20k", "ayam lalap kecil", )
    warung3.deskripsi()

def warung4():
    warung4 = Warung("warung jelia", "30k", "ayam lalap besar", )
    warung4.deskripsi()


