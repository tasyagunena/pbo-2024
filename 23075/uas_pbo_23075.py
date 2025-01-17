class Kecap:
    def __init__(self, merk, rasa, ukuran, harga):
        self.merk = merk
        self.rasa = rasa
        self.ukuran = ukuran  
        self.harga = harga

    def info_kecap(self):
        print(f"Merk Kecap: {self.merk}")
        print(f"Rasa: {self.rasa}")
        print(f"Ukuran: {self.ukuran} liter")
        print(f"Harga: Rp {self.harga}")
    
    def ganti_rasa(self, rasa_baru):
        self.rasa = rasa_baru
        print(f"Rasa kecap telah diganti menjadi {self.rasa}")

    def diskon(self, persentase):
        diskon = self.harga * (persentase / 100)
        harga_setelah_diskon = self.harga - diskon
        print(f"Harga setelah diskon {persentase}%: Rp {harga_setelah_diskon:.2f}")

