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
