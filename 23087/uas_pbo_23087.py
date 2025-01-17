def faktor_bilangan(n):
    faktor = []
    for i in range(1, n+1):
        if n % i == 0:
            faktor.append(i)
    return faktor

def samsulidan():
    bilangan = int(input("Masukkan bilangan: "))
    print("Faktor-faktor dari", bilangan, "adalah:", faktor_bilangan(bilangan))

