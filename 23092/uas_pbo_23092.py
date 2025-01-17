def tampilkan_jadwal():
    jadwal = {
        "Senin": ["Matematika Diskrit", "Algoritma dan Pemrograman", "Bahasa Inggris"],
        "Selasa": ["Jaringan Komputer", "Sistem Operasi", "Pemrograman Web"],
        "Rabu": ["Struktur Data", "Logika Informatika", "Kewirausahaan"],
        "Kamis": ["Basis Data", "Kecerdasan Buatan", "Pemrograman Mobile"],
        "Jumat": ["Komputasi Awan", "Proyek Informatika", "Olahraga"]
    }

    hari = input("Masukkan hari (Senin - Jumat): ").capitalize()
    
    if hari in jadwal:
        print(f"Jadwal mata kuliah hari {hari}: ")
        for mata_kuliah in jadwal[hari]:
            print(f"- {mata_kuliah}")
    else:
        print("Hari tidak valid atau tidak ada jadwal!")

