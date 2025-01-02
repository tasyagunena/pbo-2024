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


# ini adalah kontribusi MOH. JASMIN RUMALEAN
from modul_satu_pbo import jasmin, usia_kuliah, halo

# Menampilkan pesan sambutan
halo() 

# Membuat objek mahasiswa
mahasiswa_2 = jasmin("Moh Jasmin Rumalean", "121055520123082", " Teknik Informatika", 2023)
mahasiswa_2.tampilkan_info()

# Menampilkan informasi mahasiswa pertama
print("\nInformasi jasmin:")
usia_kuliah("1")
