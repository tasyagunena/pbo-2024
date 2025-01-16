class data:
    def __init__(self, nama,npm,kelas,jurusan,umur,alamat):
        self.nama=nama
        self.npm=npm
        self.kelas=kelas
        self.jurusan=jurusan
        self.umur=umur
        self.alamat=alamat

    def outputdata(self):
        print(f"Nama \t\t: {self.nama}\nNpm \t\t: {self.npm}\nJurusan \t: {self.jurusan}\nUmur \t\t: {self.umur}\nAlamat \t\t: {self.alamat}")

dt76=data("Alfaris","23076","Info 4","Informatika","19","Fitu")
dt77=data("Nurul","23077","Info 4","Informatika","19","Sasa")
dt78=data("Adi Putra","23078","Info 4","Informatika","19","Fora")
dt80=data("Lestari Lutfi","23080","Info 4","Informatika","19","Sasa")
dt82=data("Jasmin","23082","Info 4","Informatika","19","Sasa")
dt83=data("Muh. Fadel Nur","23083","Info 4","Informatika","19","Sasa")
dt84=data("Nursin","23084","Info 4","Informatika","19","Sasa")
dt85=data("Saris Soleman","23085","Info 4","Informatika","19","Sasa")
dt86=data("Alifia","23086","Info 4","Informatika","19","Sasa")
dt87=data("Samsulidan","23087","Info 4","Informatika","19","Sasa")

def programclass(iptdata):
    if iptdata == "076":
        dt76.outputdata()

    elif iptdata == "077":
        dt77.outputdata()

    elif iptdata == "078":
        dt78.outputdata()

    elif iptdata == "080":
        dt80.outputdata()

    elif iptdata == "082":
        dt82.outputdata()

    elif iptdata == "083":
        dt83.outputdata()
    
    elif iptdata == "084":
        dt84.outputdata()

    elif iptdata == "085":
        dt85.outputdata()

    elif iptdata == "086":
        dt86.outputdata()

    elif iptdata == "087":
        dt87.outputdata()

    else:
        print("**Data Mahasiswa Tidak Ditemukan**")

    return loop(str(input("Apakah Anda Ingin Mengulangi Program (Y/T): ")))

def input0():
    print(" ")
    print("Program Melihat Data Mahasiswa Kelas Info 4")
    return programclass(input("Masukan 3 (tiga) Digit NPM (076-087): "))

def loop(masukan):
    if masukan == "Y":
        return input0()
    
    elif masukan == "y":
        return input0()
    
    else:
        print("Terima Kasih Telah Menggunakan Program Fadel :)")
