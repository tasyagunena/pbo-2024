# uas_main_pbo.py

import sys
sys.path.append("23071")  # Menambahkan folder yang berisi file uas_pbo_23072.py ke path

# Mengimpor file uas_pbo_23072.py
import uas_pbo_23071 as refalina  

npm = input("Masukkan NPM (tiga digit) : ")

if npm == "000":
    print("Fungsi Elyas")
elif npm == "071":
    # Memanggil fungsi milik Refalina
    refalina.tampilkan_pantai()
else:
    print("Fungsi belum terdaftar untuk NPM tersebut.")
