def konversi(usd):
    print("Hasil tukar USD ke IDR: ",usd*float(16.361))
    return mengulagi(str(input("ketik Y untuk melanjutkan :")))


def ulang():
    konversi(int(input("masukan nilai USD yang akan di tukar ke IDR : ")))

def mengulagi(masukan):
    if masukan =="Y":
        return ulang()
    
    elif masukan =="y":
        return ulang()
    
    else:
        print("sekian terimkasi")

