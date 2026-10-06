import pwinput

def kosong(data):
    return data == ""

ebooks = []

kategori_ebook = ["Pembelajaran", "Penelitian", "Novel"]

ebooks_pembelajaran = [("DP", "Pak Amin"), 
                    ("PTI", "Pak Hamdani"), 
                    ("KSI", "Pak Putut")]

ebooks_penelitian = [("Research Design", "John W."), 
                    ("Study Case", "Robert K."), 
                    ("Metode Penelitian", "Wiratna S.")]

ebooks_novel = [("Hujan", "Tere Liye"), 
                ("Rindu", "Tere Liye"), 
                ("Sebelas", "Tere Liye")]   

akun = {
    "admin": {
    "nama": "admin",
    "password": "admin00", 
    "akses": "admin"}, 
        "user": {
    "nama": "user",
    "password": "user00", 
    "akses": "user"}
    }

#login
def login():
    while True:
        username = input("Username: ")

        if kosong(username):
            print("Username tidak boleh kosong")
            continue

        if username not in akun:
            print("Username Salah")
            continue

        password = pwinput.pwinput("Password: ")

        if kosong (password):
            print("Password tidak boleh kosong")
            continue

        if password == akun[username]["password"]:
            akses = akun [username]["akses"]
            return akses
        else:
            print("Password salah")

akses = login()

#fuction menu
def lihat_ebook(ebooks):
    print("Daftar Ebook:")
    for ebook in ebooks:
        print(ebook[0], ebook[1])

def tambah_ebook(ebooks):
    while True:
        judul = input("Judul: ")
        if kosong(judul):
            print("Judul tidak boleh kosong")
            continue

        penulis = input("Penulis: ")
        if kosong(penulis):
            print("Penulis tidak boleh kosong")
        break
    
    ebook_baru = (judul, penulis)
    ebooks.append(ebook_baru)
    print("Ebook ditambahkan")
    for ebook in ebooks:
        print(ebook[0], ebook[1])

def ubah_ebook(ebooks):
    while True:
        if ebooks:
            print("Daftar Ebook lama:")
            for ebook in ebooks:
                print(ebook[0], ebook[1])

        ebook_lama = input("Masukkan judul ebook yang ingin diubah: ")
        if kosong(ebook_lama):
            print("Judul tidak boleh kosong")
            continue
        penulis_lama = input("Penulis lama: ")
        if kosong(penulis_lama):
            print("Penulis tidak boleh kosong")
            continue
        ebooks.remove((ebook_lama, penulis_lama))

        ebook_baru = input("Judul baru: ")
        if kosong(ebook_baru):
            print("Judul tidak boleh kosong")
            continue    
        penulis_baru = input("Penulis baru: ")
        if kosong(penulis_baru):
            print("Penulis tidak boleh kosong")
            continue
        ebooks.append((ebook_baru, penulis_baru))
        for ebook in ebooks:
            print(ebook[0], ebook[1])
        print("Ebook berhasil diubah")
        break
    else:
        print("Tidak ada ebook yang bisa diubah")

def hapus_ebook(ebooks):
    while True:
        if ebooks:
            print("Daftar Ebook sekarang:")
            for ebook in ebooks:
                print(ebook[0], ebook[1])
        
        ebooks_hapus = input("Masukkan judul ebook yang dihapus:")
        if kosong(ebooks_hapus):
            print("Judul tidak boleh kosong")
            continue
        
        penulis_hapus = input("Masukkan penulis ebook yang dihapus:")
        if kosong(penulis_hapus):
            print("Penulis tidak boleh kosong")
            continue

        for ebook in ebooks:
            if ebook[0] == ebooks_hapus and ebook[1] == penulis_hapus:
                ebooks.remove(ebook)
        if ebooks:  
            print("Daftar Ebook sekarang:")
            for ebook in ebooks:
                print(ebook[0], ebook[1])
        print("Ebook berhasil dihapus")
        break
    else:
        print("Tidak ada ebook yang bisa dihapus")

while True:
    print("Pilih Kategori:")
    print("1. Pembelajaran")
    print("2. Penelitian")
    print("3. Novel")
    print("4. Keluar")
    pilihan_kategori = input("Pilih kategori 1-4: ")

    if pilihan_kategori == "1":
        kategori = kategori_ebook[0]
        ebooks = ebooks_pembelajaran

    elif pilihan_kategori == "2":
        kategori = kategori_ebook[1]
        ebooks = ebooks_penelitian

    elif pilihan_kategori == "3":
        kategori = kategori_ebook[2]
        ebooks = ebooks_novel

    elif pilihan_kategori == "4":
        print("Program Selesai")
        break

    else:
        print("Pilihan kategori tidak ada")
        continue

#Menu untuk admin
    if akses == "admin":
        print("1. Lihat Ebook")
        print("2. Tambah Ebook")
        print("3. Ubah Ebook")
        print("4. Hapus Ebook")     
        print("5. Kembali ke Kategori")

        pilihan = input("Pilih menu 1-5: ")

        if pilihan == "1":
            lihat_ebook(ebooks)

        elif pilihan == "2":
            tambah_ebook(ebooks)    

        elif pilihan == "3":
            ubah_ebook(ebooks)

        elif pilihan == "4":
            hapus_ebook(ebooks)

        elif pilihan == "5":
            continue

        else:
            print("Pilihan menu tidak ada")

#Menu untuk user
    elif akses == "user":
        print("1. Lihat Ebook")
        print("2. Kembali ke Kategori")

        pilihan = input("Pilih menu 1-2: ")

        if pilihan == "1":
            lihat_ebook(ebooks) 

        elif pilihan == "2":
            continue

        else:
            print("Pilihan menu tidak ada")
