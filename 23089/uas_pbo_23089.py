def susan():
    sisi = float(input("Masukkan panjang sisi kubus: "))

    luas_permukaan = 6 * sisi ** 2
    volume = sisi ** 3

    print(f"Luas permukaan kubus: {luas_permukaan}")
    print(f"Volume kubus: {volume}")
    
    return susan0(str(input("Apakah Anda Ingin Mengulangi Program (Y/T) : ")))

def susan0(msk):
    if msk == "Y":
        return susan()
    elif msk == "y":
        return susan()
    else:
        print("Terimakasih Telah Menggunakan Program Susan :)")

