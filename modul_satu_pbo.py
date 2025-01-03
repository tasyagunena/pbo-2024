# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/
# .
# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;
        
# ini Kontribusi dari Ikhwan 
def batas():
    print("-"*35)

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

#modul_satu_pbo.py

class Mahasiswa:
    def __init__(self, name, npm, jurusan):
        self.name = name
        self.npm = npm
        self.jurusan = jurusan
        self.nilai = []

    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai.append({"mata_kuliah": mata_kuliah, "nilai": nilai})

    def rata_rata_nilai(self):
        if not self.nilai:
            return 0
        total_nilai = sum([item["nilai"] for item in self.nilai])
        return total_nilai / len(self.nilai)

    def tampilkan_info(self):
        print(f"Nema: {self.name}")
        print(f"NPM: {self.npm}")
        print(f"Jurusan: {self.jurusan}")
        print("Nilai:")
        for item in self.nilai:
            print(f"  {item['mata_kuliah']}: {item['nilai']}")
        print(f"Rata-rata Nilai: {self.rata_rata_nilai():.2f}")


#ini kontribusi MOH. JASMIN RUMALEAN
class jasmin:
    def __init__ (self, nama, npm, jurusan, tahun_masuk):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.tahun_masuk = tahun_masuk
    def tampilkan_info(self):
        print(f"NAMA: {self.nama}")
        print(f"NPM: {self.npm}")
        print(f"JURUSAN: {self.jurusan}")
        print(f"TAHUN MASUK: {self.tahun_masuk}")
    
def usia_kuliah(usia):
    print(f"Mahasiswa ini sudah kuliah selama {usia} tahun.")
        
def halo():
    print(" Selamat datang di Program Mahasiswa Informatika ")

#Ini Kontribusi Dari Muh. Fadel Nur
class fadel:
    def __init__ (self, nama, npm, kelas, alamat, asal):
        self.n=nama
        self.npm=npm
        self.k=kelas
        self.a=alamat
        self.asal=asal

    def output(self):
        print(f"Nama Saya \t\t: {self.n} \nNpm Saya \t\t: {self.npm} \nKelas \t\t\t: {self.k} \nAlamat Saya Di \t\t: {self.a} \nAsal Saya Dari \t\t: {self.asal}")

def fadel_0():
    return fadel_1(int(input("Masukan Nilai Anda : ")))

def fadel_1(nilai):
    if nilai >= 80:
        print("Nilai Yang Anda Peroleh Adalah : A")

    elif nilai >=70:
        print("Nilai Yang Anda Peroleh Adalah : B")

    elif nilai >=60:
        print("Nilai Yang Anda Peroleh Adalah : C")

    elif nilai >=50:
        print("Nilai Yang Anda Peroleh Adalah : D")

    else:
        print("Nilai Yang Anda Peroleh Adalah : E")

    return fadel_3(str(input("Apakah Anda Ingin Mengulangi Program ( Y / T ) : ")))
    
def fadel_3(masukan):
    if masukan == "Y":
        return fadel_0()
    
    if masukan == "y":
        return fadel_0()
    
    if masukan == "T":
        print("Ini Adalah Akhir Program Terima Kasih Sudah Mencoba Program FADEL :) ")

    if masukan == "t":
        print("Ini Adalah Akhir Program Terima Kasih Sudah Mencoba Program FADEL :) ")

    else:
        print("Ini Adalah Akhir Program Terima Kasih Sudah Mencoba Program FADEL :) ")

# ini Kontribusi dari Refalina
# modul_satu_pbo.py

class Course:
    def __init__(self, kode, nama_mata_kuliah):
        self.kode = kode
        self.nama_mata_kuliah = nama_mata_kuliah
        self.mahasiswa_terdaftar = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_terdaftar.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        print(f"Mata Kuliah: {self.nama_mata_kuliah} ({self.kode})")
        print("Mahasiswa yang Terdaftar:")
        for mahasiswa in self.mahasiswa_terdaftar:
            print(f"- {mahasiswa.name} ({mahasiswa.npm})")
            
# Pengujian Kelas Course
if __name__ == "__main__":
    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa("Budi", "123456", "Informatika")
    mahasiswa2 = Mahasiswa("Siti", "654321", "Matematika")
    
    # Membuat objek Course dan menambahkan mahasiswa
    kursus = Course("IF101", "Pemrograman Berorientasi Objek")
    kursus.tambah_mahasiswa(mahasiswa1)
    kursus.tambah_mahasiswa(mahasiswa2)
    
    # Menampilkan informasi kursus
    kursus.tampilkan_mahasiswa()

#Ini Kontribusi Dari Srinagita Irwan
class gita_c:
    def __init__(self,nama,kelas,jurusan,npm,alamat,hobi,umur):
        self.nama=nama
        self.kelas=kelas
        self.jurusan=jurusan
        self.npm=npm
        self.alamat=alamat
        self.hobi=hobi
        self.umur=umur

    def gita1(self):
        print(f"Perkenalkan nama saya {self.nama} saya dari kelas {self.kelas} jurusan {self.jurusan} npm saya {self.npm} alamat saya {self.alamat} dan hobi saya {self.hobi} umur saya {self.umur}")

def gita_tambah(a,b):
    print(a+b)

def gita_kurang(a,b):
    print(a-b)

def gita_kali(a,b):
    print(a*b)

def gita_bagi(a,b):
    print(a/b)

