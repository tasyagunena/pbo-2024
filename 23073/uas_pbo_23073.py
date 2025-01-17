
supermi_menu = {
    "Supermi Original": 3000,
    "Supermi Rasa Ayam Bakar": 3500,
    "Supermi Rasa Soto": 4000,
    "Supermi Rasa Mie Goreng": 4000
}

def tampilkan_menu():
    """Menampilkan daftar menu Supermi"""
    print("---- Menu Supermi ----")
    for nomor, (nama, harga) in enumerate(supermi_menu.items(), start=1):
        print(f"{nomor}. {nama} - Rp {harga}")

def hitung_total_harga(pilihan, jumlah_pesanan):
    """Menghitung total harga berdasarkan pilihan dan jumlah"""
    varian_pilihan = list(supermi_menu.keys())[int(pilihan) - 1]
    harga = supermi_menu[varian_pilihan]
    return harga * jumlah_pesanan
