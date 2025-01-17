def Nursin():
    nama = input("Masukkan nama Anda: ")
    umur = float(input("Masukkan umur Anda: "))
    asal = input("Masukkan asal anda: ")

    print(f"Halo, Nama saya {nama}! Saya berusia {umur} tahun, saya berasal {asal} dari. ")

    if umur < 18:
        print("anda masih berusia di bawa umur.")
    else:
        print("anda sudah dewasa.")

