import tkinter as tk
from tkinter import messagebox

class SistemMesinCuci:
    def __init__(self):
        self.keadaan = ['Mati', 'Isi Air', 'Pencucian', 'Bilas', 'Putar Kering', 'Selesai','Mesin Mati']
        self.keadaan_saat_ini = 'Mati'
        self.transisi = {
            ('Mati', 'Nyalakan'): 'Isi Air',
            ('Isi Air', 'Isi Air'): 'Pencucian',
            ('Pencucian', 'Mulai Cuci'): 'Bilas',
            ('Bilas', 'Bilas'): 'Putar Kering',
            ('Putar Kering', 'Kering'): 'Selesai',
            ('Selesai', 'Matikan'): 'Mesin Mati'
        }

    def transisi_keadaan(self, tombol):
        if (self.keadaan_saat_ini, tombol) in self.transisi:
            self.keadaan_saat_ini = self.transisi[(self.keadaan_saat_ini, tombol)]
            return f"Mesin cuci sekarang dalam keadaan: {self.keadaan_saat_ini}"
        else:
            return "Tombol yang ditekan tidak valid untuk keadaan mesin cuci saat ini."

# Inisialisasi sistem otomatisasi mesin cuci
sistem_mesin_cuci = SistemMesinCuci()

class MesinCuciGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Otomatisasi Mesin Cuci")

        self.label = tk.Label(root, text="Sistem Otomatisasi Mesin Cuci", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.status_label = tk.Label(root, text=f"Keadaan saat ini: {sistem_mesin_cuci.keadaan_saat_ini}", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.buttons = {
            'Nyalakan': tk.Button(self.button_frame, text="Nyalakan mesin cuci", command=lambda: self.proses_transisi('Nyalakan')),
            'Isi Air': tk.Button(self.button_frame, text="Isi air", command=lambda: self.proses_transisi('Isi Air')),
            'Mulai Cuci': tk.Button(self.button_frame, text="Mulai pencucian", command=lambda: self.proses_transisi('Mulai Cuci')),
            'Bilas': tk.Button(self.button_frame, text="Mulai pembilasan", command=lambda: self.proses_transisi('Bilas')),
            'Kering': tk.Button(self.button_frame, text="Mulai putar kering", command=lambda: self.proses_transisi('Kering')),
            'Matikan': tk.Button(self.button_frame, text="Matikan mesin cuci", command=lambda: self.proses_transisi('Matikan'))
        }

        for button in self.buttons.values():
            button.pack(pady=5)

    def proses_transisi(self, tombol):
        hasil = sistem_mesin_cuci.transisi_keadaan(tombol)
        self.status_label.config(text=f"Keadaan saat ini: {sistem_mesin_cuci.keadaan_saat_ini}")
        messagebox.showinfo("Info", hasil)

# Jalankan aplikasi GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = MesinCuciGUI(root)
    root.mainloop()
