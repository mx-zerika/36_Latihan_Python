def ganjil_genap():
    while True:
        nilai = int(input("masukkan nilai (0 untuk kembali): "))

        if nilai == 0:
            break

        if nilai % 2 == 0:
            print("nilai", nilai, "adalah bilangan genap")
        else:
            print("nilai", nilai, "adalah bilangan ganjil")

def bilangan_prima():
    while True:
        angka = int(input("masukkan angka (0 untuk kembali): "))

        if angka == 0:
            break 

        if angka < 2:
            print(angka, "bukanlah bilangan prima")
        else:
            prima = True

            for i in range(2, angka):
                if angka % i == 0:
                    prima = False
                    break

            if prima:
                print(angka, "adalah bilangan prima")
            else:
                print(angka, "bukanlah bilangan prima")

def menu():
    while True:
        print("==  MENU ==")
        print("1. Ganjil - Genap")
        print("2. Bilangan Prima")
        print("3. Keluar")

        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            ganjil_genap()

        elif pilihan == "2":
            bilangan_prima()

        elif pilihan == "3":
            print("Program Selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")

menu()
