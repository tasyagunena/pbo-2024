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

#nurul
import modul_satu_pbo as nurul0

nurul1= nurul0.nurul("nurul","20","membaca","patani","infomatika")
nurul1.proses()

print("Ini Adalah Tambah")
print(nurul0.tambah(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Kali")
print(nurul0.kali(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Kurang")
print(nurul0.kurang(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Bagi")
print(nurul0.bagi(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Pangkat")
print(nurul0.pangkat(nurul0.input3(),nurul0.input3()))
print("Ini Adalah Akar")
print(nurul0.akar(nurul0.input3()))

