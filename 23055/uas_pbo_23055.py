class Film:
    def __init__(self, judul, tahun):
        if not isinstance(tahun, int) or tahun <= 0:
            raise ValueError("Tahun must be a positive integer.")
        self.judul = judul
        self.tahun = tahun

    def info(self):
        return f"{self.judul} ({self.tahun})"

    def get_judul(self):
        return self.judul

    def get_tahun(self):
        return self.tahun

    def set_tahun(self, new_tahun):
        if not isinstance(new_tahun, int) or new_tahun <= 0:
            raise ValueError("Tahun must be a positive integer.")
        self.tahun = new_tahun
