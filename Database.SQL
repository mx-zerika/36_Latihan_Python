import sqlite3


# Membuat Database
koneksi = sqlite.connect("database.db")
cursor = koneksi.cursor()

cursor.execute("""
CREATE TABLE  IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

koneksi.commit()


def register():

    print("\n== REGISTER ==")

    username = input("buat Username:")
    password = input("Buat password:")

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        koneksi.commit()
        print("Akun berhasil dibuat!")

    except sqlite3.IntegrityError:
        print("Username sudah digunakan!")

def login():
    print("\n== LOGIN ==")

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT * FROM users WHERE USERNAME = ? AND password = ?",
        (username, password)
    )

    user =  cursor.fetchone()

    if user:
        print("Login Berhasil!")
        print("Selamat Datang,", username)
        return True
    else:
        print("Username atau password salah!")
        return False

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

def program():
    while true:
        print("\n== PROGRAM ==")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        pilihan = input("pilih: ")

        if pilihan == "1":
            if login():
                menu()

        elif pilihan == "2":
            register()

        elif pilihan == "3":
            print("Program Selesai.")
            break


        else:
            print("Pilihan tidak tersedia")


program()

koneksi.close()
