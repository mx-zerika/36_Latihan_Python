import  tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


# =========================
# WINDOW
# =========================


window  = tk.Tk()
window.title("Mathcheck")
window.geometry("650x550")
window.resizable(False, False)


# ========================
# COLOR
# ========================


BG = "#171722"
CARD  = "#242438"
CARD_LIGHT = "#2D2D45"

TEXT = "#F5F5F7"
SUBTEXT = "#A8A8BA"

ACCENT = "#9D7CFF"
ACCENT_HOVER = "#B29AFF"

BUTTON = "#383850"

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
        hasil_ganjil.config(
             text="Bilangan Genap", fg=ACCENT
             )
    else:
        hasil_ganjil.config(
             text="Bilangan Ganjil", fg=ACCENT
             )

def cek_prima(): 
    angka = int(input_prima.get()) 

    if angka < 2: 

        hasil_prima.config( 
             text=f"{angka} bukan bilangan prima", fg=ACCENT 
             ) 
        return 

    prima = True 

    for i in range(2, angka): 
        if angka % i == 0: 
            prima = False 
            break 

    if prima: 
            hasil_prima.config( 
                 text=f"{angka} adalah bilangan prima", fg=ACCENT 
                 ) 

    else: 
         hasil_prima.config( 
              text=f"{angka} bukan bilangan prima", fg=ACCENT 
              )

def analisis_angka():
     angka =  input_analisis.get()

     data = [float(x) for x in angka.split(",")]

     data_np = np.array(data)

     rata_rata = np.mean(data_np)
     terbesar = np.max(data_np)
     terkecil = np.min(data_np)

     hasil_analisis.config(
          text= f"Rata-rata: {rata_rata}\n"
                f"Terbesar: {terbesar}\n"
                f"Terkecil: {terkecil}"
     )

def tampilan_grafik():
     angka = input_analisis.get()

     data = [float(x) for x in angka.split(",")]

     data_np = np.array(data)


     plt.plot(data_np, marker="o")

     plt.title("Grafik Angka")
     plt.xlabel("Urutan Data")
     plt.ylabel("Nilai")

     plt.show()

# =============================================
# CONTAINER UNTUK SEMUA SCREEN
# =============================================

container = tk.Frame(
     window, 
     bg=BG
     )

container.pack(
     fill="both", 
     expand=True
     )

container.grid_rowconfigure(
     0, 
     weight=1
     )
container.grid_columnconfigure(
     0, 
     weight=1
     )

# ============================================
# HOME SCREEN
# ============================================

home_frame = tk.Frame(
     container, 
     bg=BG
     )
home_frame.grid(
     row=0, 
     column=0, 
     sticky="nsew"
     )

#  MAIN TITLE

tk.Label(
     home_frame, 
     text="MATHCHECK",
     font=("Arial", 28, "bold"), 
     bg=BG, 
     fg=TEXT
     ).pack()

# SMALL TOP TEXT

tk.Label(
     home_frame, 
     text="Pilih program yang ingin anda gunakan", 
     font=("Arial", 10), 
     bg=BG, 
     fg=ACCENT
     ).pack(pady =(55, 5))

# Card Home

home_card = tk.Frame(
     home_frame, 
     bg=CARD, 
     padx=40, 
     pady=30
     )

home_card.pack()


# ========================
# BUTTON
# ========================

# Tombol Ganjil genap

button_ganjil_genap = tk.Button(
     home_card, 
     text="Ganjil / Genap", 
     font=("Arial", 12, "bold"), 
     bg=BUTTON, 
     fg=TEXT, 
     activebackground=ACCENT_HOVER, 
     activeforeground=TEXT, 
     relief="flat", 
     width=28, 
     pady=12,
     cursor="hand2", 
     command=lambda: show_frame(ganjil_genap_frame)
     )

button_ganjil_genap.pack(pady=7)

# Tombol bilangan Prima

button_prima = tk.Button(
     home_card, 
     text=" Bilangan Prima", 
     font=("Arial", 12, "bold"), 
     bg=BUTTON, 
     fg=TEXT, 
     activebackground=ACCENT_HOVER, 
     activeforeground=TEXT, 
     relief="flat", 
     width=28, 
     pady=12,
     cursor="hand2", 
     command=lambda: show_frame(prima_frame))

button_prima.pack(pady=7)

# Footer
tk.Label(
     home_frame,
     text="MADE WITH PYTHON . TKINTER",
     font=("Arial", 9),
        bg=BG,
        fg=SUBTEXT
).pack(pady=25)

# ========================================
# GANJIL GENAP SCREEN
# ========================================

ganjil_genap_frame = tk.Frame(
     container, 
     bg=BG)
ganjil_genap_frame.grid(
     row=0, 
     column=0, 
     sticky="nsew"
     )

judul_ganjil_genap = tk.Label(
     ganjil_genap_frame, 
     text="Cek Ganjil / Genap", 
     font=("Arial", 24, "bold"), 
     bg=BG, 
     fg=TEXT
     )

judul_ganjil_genap.pack(pady=(50, 5))

subjudul_ganjil_genap = tk.Label(
     ganjil_genap_frame, 
     text="Masukkan angka yang ingin di-cek", 
     font=("Arial", 10), 
     bg=BG, 
     fg=SUBTEXT
     )
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


button_cek_prima = tk.Button(
    prima_card,
    text="Cek",
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=ACCENT,
    activeforeground=TEXT,
    relief="flat",
    width=20,
    pady=8,
    command=cek_prima
)

button_cek_prima.pack(pady=(0, 5))


hasil_prima  = tk.Label(prima_card, text="Hasil akan muncul di sini", font=("Arial", 11, "bold"), bg=CARD, fg=SUBTEXT)
hasil_prima.pack(pady=(20, 0))

# Tombol Back

button_back_prima = tk.Button(prima_frame, text="<- Back", font=("Arial", 10), bg=BG, fg=SUBTEXT, activebackground=BG, activeforeground=TEXT, command=lambda: show_frame(home_frame))
button_back_prima.pack(pady=25)

analisis_frame= tk.Frame(
     container,
     bg=BG
)

analisis_frame.grid(
     row=0,
     column=0,
     sticky="nsew"
)

tk.Label(
     analisis_frame,
     text="Analisis Angka",
     font=("Arial", 26, "bold"),
     bg=BG,
     fg=TEXT
).pack(pady=(55, 5))

tk.Label(
     analisis_frame,
     text="Masukkan angka yang dipisahkan koma",
     font=("Arial", 10),
     bg=BG,
     fg=SUBTEXT
).pack(pady=(0, 25))

analisis_card = tk.Frame(
    analisis_frame,
    bg=CARD,
    padx=45,
    pady=30
)

analisis_card.pack()


tk.Label(
    analisis_card,
    text="ENTER NUMBERS",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=SUBTEXT
).pack(pady=(0, 8))


input_analisis = tk.Entry(
    analisis_card,
    font=("Arial", 14),
    justify="center",
    width=25,
    bg=CARD_LIGHT,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)

input_analisis.pack(
    pady=(0, 18),
    ipady=8
)


tk.Button(
    analisis_card,
    text="ANALYZE",
    font=("Arial", 10, "bold"),
    bg=ACCENT,
    fg=TEXT,
    activebackground=ACCENT_HOVER,
    relief="flat",
    width=22,
    pady=9,
    cursor="hand2",
    command=analisis_angka
).pack()


hasil_analisis = tk.Label(
    analisis_card,
    text="Result will appear here",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=SUBTEXT
)

hasil_analisis.pack(pady=(20, 10))


tk.Button(
    analisis_card,
    text="SHOW GRAPH",
    font=("Arial", 10, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=ACCENT_HOVER,
    relief="flat",
    width=22,
    pady=9,
    cursor="hand2",
    command=tampilan_grafik
).pack()


tk.Button(
    home_card,
    text="  Analisis Angka",
    font=("Arial", 12, "bold"),
    bg=BUTTON,
    fg=TEXT,
    activebackground=ACCENT_HOVER,
    activeforeground=TEXT,
    relief="flat",
    width=28,
    pady=12,
    cursor="hand2",
    command=lambda: show_frame(analisis_frame)
).pack(pady=7)

# ==============================================================
# TAMPILKAN HOME SAAT PROGRAM DIMULAI
# ==============================================================

show_frame(home_frame)


# ==============================================================
# RUN 
#  =============================================================

window.mainloop() 
