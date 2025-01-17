def oktal(desimal):
    print(f"Oktal: {oct(desimal)[2:]}")

def biner(desimal):
    print(f"Biner: {bin(desimal)[2:]}")

def heksadesimal(desimal):
    print(f"Heksadesimal: {hex(desimal)[2:].upper()}")


def ipt():
    print("Program Konversi Nilai Desimal Ke Oktal, Biner, Heksadesimal")
    desimal0 = int(input("Masukkan bilangan desimal: "))
    oktal(desimal0)
    biner(desimal0)
    heksadesimal(desimal0)

