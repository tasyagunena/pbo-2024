# code utama untuk memanggil fungsi dari UAS Mahasiswa
# setiap Mahasiswa hanya boleh berkontribusi 2 baris (maksimal) untuk memanggil fungsinya 
# bagian ini nanti saya (Elyas) yang modif
import sys
sys.path.append("23000")  # Tambahkan folder 23000 ke path
import uas_pbo_23000 as elyas


# bagian dibawah silahkan tambahkan menyesuaikan 
npm=input("Masukkan NPM (tiga digit) :")
if npm == "000":
    # silahkan isi 2 (dua) baris Maksimal untuk memanggil fungsinya ELyas 
    elyas.fall()
elif npm == "066":
    # silahkan isi 2 (dua) baris Maksimal untuk memanggil fungsinya Jelia
    fasasdfa() 
elif npm == "072":
    # silahkan isi 2 (dua) baris Maksimal untuk memanggil fungsinya ariyanti
    sambarang()
else:
    # silahkan isi 2 (dua) baris Maksimal untuk memanggil fungsinya ???
    fasasdfa()
