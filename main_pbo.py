# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")

msatu.batas();
msatu.batas();

# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py
from modul_satu_pbo import Mahasiswa

mahasiswa1 = Mahasiswa("Dila", "23062", "Teknik Informatika")
mahasiswa1.tambah_nilai("Basis Data", 85)
mahasiswa1.tambah_nilai("Fisika", 90)
mahasiswa1.tambah_nilai("Algoritma", 78)

mahasiswa1.tampilkan_info()

## Ini Program Kontribusi Dari Muh. Fadel Nur
import modul_satu_pbo as fadel

fdl= fadel.fadel("Muh. Fadel Nur","23083","Info 4","Sasa","Buton")
fdl.output()

fadel.fadel_0()
# ini contoh implementasi atau menguji fungsi dan class, versi refaa
# modul_satu_pbo.py

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_pinjam = []

    def pinjam_buku(self, buku):
        self.buku_pinjam.append(buku)
        print(f"{self.nama} berhasil meminjam buku '{buku}'.")

    def tampilkan_buku_pinjam(self):
        print(f"Anggota {self.nama} dengan ID {self.id_anggota} meminjam buku:")
        for buku in self.buku_pinjam:
            print(f"- {buku}")
            
# Pengujian Kelas Anggota
if __name__ == "__main__":
    # Membuat objek Anggota
    anggota1 = Anggota("Ali", "A001")
    anggota2 = Anggota("Rina", "A002")
    
    # Meminjam buku
    anggota1.pinjam_buku("Algoritma Pemrograman")
    anggota1.pinjam_buku("Struktur Data")
    
    anggota2.pinjam_buku("Basis Data")
    
    # Menampilkan daftar buku yang dipinjam
    anggota1.tampilkan_buku_pinjam()
    anggota2.tampilkan_buku_pinjam()

