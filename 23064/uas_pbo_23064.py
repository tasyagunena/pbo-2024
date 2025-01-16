class Pegawai:
 def __init__(self, nama, nip, jabatan, gaji_pokok, tunjangan):
    self.nama = nama
    self.nip = nip
    self.jabatan = jabatan
    self.gaji_pokok = gaji_pokok
    self.tunjangan = tunjangan

 def hitung_gaji(self):
    return self.gaji_pokok + self.tunjangan

 def info_gaji(self):
    return f"Nama: {self.nama}\nNIP: {self.nip}\nJabatan: {self.jabatan}\nGaji Pokok: Rp{self.gaji_pokok}\nTunjangan: Rp{self.tunjangan}\nTotal Gaji: Rp{self.hitung_gaji()}\n"
 # Fungsi untuk setiap pegawai

def gaji_budi():
 budi = Pegawai("Budi Santoso", "123456789", "Manager", 10000000, 2000000)
 return budi.info_gaji()

def gaji_rina():
 rina = Pegawai("Rina Wahyuni", "987654321", "Programmer", 8000000, 1500000)
 return rina.info_gaji()

def gaji_andi():
 andi = Pegawai("Andi Setiawan", "111111111", "Kepala Bagian", 12000000, 2500000)
 return andi.info_gaji()

def gaji_ahmad():
 ahmad = Pegawai("Ahmad Fauzi", "222222222", "Staf", 6000000, 1000000)
 return ahmad.info_gaji()

def gaji_nur():
 nur = Pegawai("Nur Halimah", "333333333", "Asisten", 7000000, 1200000)
 return nur.info_gaji()

# Fungsi untuk menampilkan daftar gaji

def daftar_gaji():
 print("Daftar Gaji Pegawai:")
 print(gaji_budi() + "\n" + gaji_rina() + "\n" + gaji_andi() + "\n" + gaji_ahmad() + "\n" + gaji_nur())

daftar_gaji()


