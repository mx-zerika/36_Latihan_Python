import  tkinter as tk



# =========================
# WINDOW
# =========================


window  = tk.Tk()
window.title("Program Kia")
window.geometry("500x400")
window.resizable(False, False)

# Warna
BG = "#1E1E2E"
CARD  = "#2A2A3C"
TEXT = "#F5F5F5"
SUBTEXT = "#B8B8C7"
ACCENT = "#9D7CFF"
BUTTON = "#3A3A52"

# =========================
# FUNCTION UNTUK PINDAH SCREEN
# =========================

def show_frame(frame):
    frame.tkraise()
    

# ========================
# FUNCTION
# ========================


def cek_ganjil_genap():
    angka = int(input_ganjil.get())

    if angka % 2 ==  0:
        hasil_ganjil.config(text="Bilangan Genap", fg=ACCENT)
    else:
        hasil_ganjil.config(text="Bilangan Ganjil", fg=ACCENT)

def cek_prima(): 
    angka = int(input_prima.get()) 

    if angka < 2: 

        hasil_prima.config( text=f"{angka} bukan bilangan prima", fg=ACCENT ) 
        return 

    prima = True 

    for i in range(2, angka): 
        if angka % i == 0: 
            prima = False 
            break 

    if prima: 
            hasil_prima.config( text=f"{angka} adalah bilangan prima", fg=ACCENT ) 

    else: 
         hasil_prima.config( text=f"{angka} bukan bilangan prima", fg=ACCENT )


# =============================================
# CONTAINER UNTUK SEMUA SCREEN
# =============================================

container = tk.Frame(window, bg=BG)

container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# ============================================
# HOME SCREEN
# ============================================

home_frame = tk.Frame(container, bg=BG)
home_frame.grid(row=0, column=0, sticky="nsew")

judul_home =  tk.Label(home_frame, text="MODULPERULANGAN", font=("Arial", 24, "bold"), bg=BG, fg=TEXT)
judul_home.pack(pady=(60, 5))

subjudul_home =  tk.Label(home_frame, text="Pilih program yang ingin anda gunakan", font=("Arial", 10), bg=BG, fg=SUBTEXT)
subjudul_home.pack(pady=(0, 30))

# Card Home

home_card = tk.Frame(home_frame, bg=CARD, padx=40, pady=30)
home_card.pack()


# ========================
# BUTTON
# ========================

# Tombol Ganjil genap

button_ganjil_genap = tk.Button(home_card, text="Bilangan Ganjil-Genap", font=("Arial", 11, "bold"), bg=BUTTON, fg=TEXT, activebackground=ACCENT, activeforeground=TEXT, relief="flat", width=25, pady=10, command=lambda: show_frame(ganjil_genap_frame))
button_ganjil_genap.pack(pady=8)

# Tombol bilangan Prima

button_prima = tk.Button(home_card, text="Bilangan Prima", font=("Arial", 11, "bold"), bg=BUTTON, fg=TEXT, activebackground=ACCENT, activeforeground=TEXT, relief="flat", width=25, pady=10, command=lambda: show_frame(prima_frame))

button_prima.pack(pady=8)


# ========================================
# GANJIL GENAP SCREEN
# ========================================

ganjil_genap_frame = tk.Frame(container, bg=BG)
ganjil_genap_frame.grid(row=0, column=0, sticky="nsew")

judul_ganjil_genap = tk.Label(ganjil_genap_frame, text="Cek Ganjil / Genap", font=("Arial", 24, "bold"), bg=BG, fg=TEXT)
judul_ganjil_genap.pack(pady=(50, 5))

subjudul_ganjil_genap = tk.Label(ganjil_genap_frame, text="Masukkan angka yang ingin di-cek", font=("Arial", 10), bg=BG, fg=SUBTEXT)
subjudul_ganjil_genap.pack(pady=(0, 25))

ganjil_card = tk.Frame(ganjil_genap_frame, bg=CARD, padx=40, pady=30)
ganjil_card.pack(pady=(0, 10))


input_ganjil = tk.Entry(ganjil_genap_frame, font=("Arial", 14), justify="center", width=20)
input_ganjil.pack(pady=(0, 15))


button_cek = tk.Button(ganjil_genap_frame, text="Cek", font=("Arial", 10, "bold"), bg=BUTTON, fg=TEXT, activebackground=ACCENT, activeforeground=TEXT, relief="flat", width=20, pady=8, command=cek_ganjil_genap)
button_cek.pack()

hasil_ganjil  = tk.Label(ganjil_card, text="Hasil akan muncul di sini", font=("Arial", 11, "bold"), bg=CARD, fg=SUBTEXT)
hasil_ganjil.pack(pady=(20, 0))

# Tombol Back

button_back_ganjil = tk.Button(ganjil_genap_frame, text="<- Back", font=("Arial", 10), bg=BG, fg=SUBTEXT, activebackground=ACCENT, activeforeground=TEXT, relief="flat", width=10, pady=5, command=lambda: show_frame(home_frame))
button_back_ganjil.pack(pady=25)

# ========================================
# BILANGAN PRIMA SCREEN
# ========================================

prima_frame = tk.Frame(container, bg=BG)
prima_frame.grid(row=0, column=0, sticky="nsew")

judul_prima = tk.Label(prima_frame, text="Cek Bilangan Prima", font=("Arial", 24, "bold"), bg=BG, fg=TEXT)
judul_prima.pack(pady=(50, 5))

subjudul_prima = tk.Label(prima_frame, text="Masukkan angka yang ingin di-cek", font=("Arial", 10), bg=BG, fg=SUBTEXT)
subjudul_prima.pack(pady=(0, 25))

prima_card = tk.Frame(prima_frame, bg=CARD, padx=40, pady=30)

prima_card.pack()


label_prima = tk.Label(prima_card, text="Masukkan angka", font=("Arial", 11, "bold"), bg=CARD, fg=TEXT ) 
label_prima.pack(pady=(0, 10))

input_prima = tk.Entry(prima_card, font=("Arial", 14), justify="center", width=20)
input_prima.pack(pady=(0, 15))


button_cek_prima = tk.Button(prima_frame, text="Cek", font=("Arial", 10, "bold"), bg=BUTTON, fg=TEXT, activebackground=ACCENT, activeforeground=TEXT, relief="flat", width=20, pady=8, command=cek_prima)
button_cek.pack()

hasil_prima  = tk.Label(prima_card, text="Hasil akan muncul di sini", font=("Arial", 11, "bold"), bg=CARD, fg=SUBTEXT)
hasil_prima.pack(pady=(20, 0))

# Tombol Back

button_back_prima = tk.Button(prima_frame, text="<- Back", font=("Arial", 10), bg=BG, fg=SUBTEXT, activebackground=BG, activeforeground=TEXT, command=lambda: show_frame(home_frame))
button_back_prima.pack(pady=25)

# ==============================================================
# TAMPILKAN HOME SAAT PROGRAM DIMULAI
# =============================================================

show_frame(home_frame)


# ==============================================================
# RUN 
#  =============================================================

window.mainloop() 
