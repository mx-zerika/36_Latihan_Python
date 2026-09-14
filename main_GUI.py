import  tkinter as tk


window  = tk.Tk()
window.title("Program Kia")
window.geometry("400x300")

def cek_ganjil_genap():
    angka = int(input_angka.get())

    if angka % 2 ==  0:
        hasil.config(text="Bilangan Genap")
    else:
        hasil.config(text="Bilangan Ganjil")    

def cek_prima():
    angka =  int(input_angka.get())

    if angka < 2:
        hasil.config(text=f"{angka} bukan bilangan prima")
    else:
        prima= True

    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

        if prima:
            hasil.config(text=f"{angka} bukan bilangan prima")
        else:
            hasil.config(text=f"{angka} adalah bilangan prima")


    hasil.config(text=f"{angka} adalah bilangan prima")

judul = tk.Label(window, text="MODUL PERULANGAN")
judul.pack()

label_angka = tk.Label(window, text="Masukkan angka: ")
label_angka.pack()

input_angka = tk.Entry(window)
input_angka.pack()

button_ganjil_genap = tk.Button(
    window,
    text="cek Ganjil / Genap",
    command=cek_ganjil_genap
)
button_ganjil_genap.pack()

hasil = tk.Label(window, text="")
hasil.pack()

button_prima = tk.Button(
     window,
     text="Cek Bilangan Prima",
     command=cek_prima  
 )
button_prima.pack()

window.mainloop()