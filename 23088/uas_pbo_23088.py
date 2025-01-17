def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)

def imam():
    print("Program Menghitung Faktorial")
    print("-" * 40)

    angka = int(input("Masukkan angka: "))

    if angka < 0:
        print("Faktorial tidak didefinisikan untuk angka negatif.")
    else:
        hasil = faktorial(angka)
        print(f"Faktorial dari {angka} adalah {hasil}")

