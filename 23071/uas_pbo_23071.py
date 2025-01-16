class Pantai:
    def __init__(self, nama_pantai):
        self.nama_pantai = nama_pantai
    
    def tampilkan(self):
        print(f"Pantai {self.nama_pantai} sangat indah!")

# Daftar nama pantai di Sulamadaha
pantai_sulamadaha = [
    "Jikomalamo",
    "Pantai Masirete",
    "Talaganita",
    "Hol"
]

# Menampilkan semua pantai
def pantai():
    for nama_pantai in pantai_sulamadaha:
        Pantai(nama_pantai).tampilkan()

# Fungsi utama untuk menjalankan modul ini
if __name__ == "__main__":
    pantai()
