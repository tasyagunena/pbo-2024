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

#ini firna
import modul_satu_pbo as firna67

firna6= firna67.firna("firna","19","membaca","halteng","infomatika")
firna6.proses()

print("Ini Adalah Tambah")
print(firna67.tambah(firna67.input3(),firna67.input3()))
print("Ini Adalah Kali")
print(firna67.kali(firna67.input3(),firna67.input3()))
print("Ini Adalah Kurang")
print(firna67.kurang(firna67.input3(),firna67.input3()))
print("Ini Adalah Bagi")
print(firna67.bagi(firna67.input3(),firna67.input3()))
print("Ini Adalah Pangkat")
print(firna67.pangkat(firna67.input3(),firna67.input3()))
print("Ini Adalah Akar")
print(firna67.akar(firna67.input3()))

