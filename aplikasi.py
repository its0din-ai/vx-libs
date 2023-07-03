import crud
import time
import hashlib
import os

from pwinput import pwinput
from rich.console import Console
from rich import print
from rich.table import Table

def main():
    print("<<< Selamat Datang di VX-Lib >>>")
    print("1. Login\n2. Daftar\n3. Keluar")
    pilihan = str(input("Pilihan: "))
    if pilihan == "1":
        login()
    elif pilihan == "2":
        fungsiDaftar()
    elif pilihan == "3":
        exit(0)
    
def fungsiDaftar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Pendaftaran Akun VX-Lib")

    username = str(input("Username: "))
    nama = str(input("Nama: "))
    password = pwinput(prompt='Password: ', mask='x').encode('utf-8')
    konfirmPassword = pwinput(prompt='Konfirmasi Password: ', mask='x').encode('utf-8')

    if password == konfirmPassword:
        daftar = crud.daftarAkun(username, nama, password)
        if daftar == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username sudah ada\nMohon ulangi lagi")
            time.sleep(1)
            fungsiDaftar()
        else:
            print("Pendaftaran berhasil, anda akan dialihkan dalam 3 detik")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Password tidak sama\nMohon ulangi lagi")
        daftar()

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Login ke sistem VX-Lib")

    username = input("Username: ")
    password = pwinput(prompt='Password: ', mask='x').encode('utf-8')
    password = hashlib.md5(password).hexdigest()

    dataAkun = crud.ambilDataAkun(username)
    if dataAkun != None:
        if username == dataAkun[0] and password == dataAkun[2]:
            if list(dataAkun)[3] == {'staff'}:
                menuStaff(dataAkun)
            else:
                menu(dataAkun)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username atau Password salah!")
            main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Maaf, username tidak ada.\nSilahkan mendaftar")
        main()

def menu(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Halo [magenta]{user[1]}[/magenta]! Selamat Datang di VX-Lib\nSilahkan pilih menu")
    print("1. Lihat Semua Buku")
    print("2. Cari Buku")
    print("3. Inventori")
    print("4. Keluar")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        lihatSemuaBuku(user)
    elif pilihan == "2":
        cariBuku(user)
    elif pilihan == "3":
        inventori(user)
    elif pilihan == "4":
        exit(0)

def inventori(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Halo [magenta]{user[1]}[/magenta]! Pilih menu")
    print("1. Lihat Inventori\n2. Pinjam Buku\n3. Kembalikan Buku\n4. Kembali ke menu utama")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        lihatInventori(user)
    elif pilihan == "2":
        pinjamBuku(user)
    elif pilihan == "3":
        kembalikanBuku(user)
    elif pilihan == "4":
        menu(user)

def lihatInventori(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Daftar Buku")
    xx = crud.ambilInventori(user[0])
    table = Table()
    table.add_column("ID", justify="center", style="yellow")
    table.add_column("Katalog", justify="center", style="yellow")
    table.add_column("Judul", justify="left", style="yellow")
    table.add_column("Pengarang", justify="left", style="yellow")
    table.add_column("Penerbit", justify="left", style="yellow")
    table.add_column("Tahun Terbit", justify="center", style="yellow")
    
    for i in xx:
        table.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]))

    console = Console()
    console.print(table)

    print("1. Kembali")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        inventori(user)

def lihatSemuaBuku(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Daftar Buku")
    xx = crud.ambilSemuaBuku()
    table = Table()
    table.add_column("ID", justify="center", style="yellow")
    table.add_column("Katalog", justify="center", style="yellow")
    table.add_column("Judul", justify="left", style="yellow")
    table.add_column("Pengarang", justify="left", style="yellow")
    table.add_column("Penerbit", justify="left", style="yellow")
    table.add_column("Tahun Terbit", justify="center", style="yellow")
    
    for i in xx:
        table.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]))

    console = Console()
    console.print(table)

    print("1. Kembali")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        if list(user)[3] == {'staff'}:
            menuStaff(user)
        else:
            menu(user)

def menuStaff(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Halo [magenta]{user[1]}[/magenta]! Selamat bekerja\nSilahkan pilih menu")
    print("1. Lihat Semua Buku")
    print("2. Tambah Buku")
    print("3. Hapus Buku")
    print("4. Manage User")
    print("5. Keluar")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        lihatSemuaBuku(user)
    elif pilihan == "2":
        tambahBuku(user)
    elif pilihan == "3":
        hapusBuku(user)
    elif pilihan == "4":
        editRole(user)
    elif pilihan == "5":
        exit(0)

def cariBuku(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fitur pencarian buku dengan judul")
    judul = input("Judul: ")
    xx = crud.pencarianBuku(judul)

    table = Table()
    table.add_column("ID", justify="center", style="yellow")
    table.add_column("Katalog", justify="center", style="yellow")
    table.add_column("Judul", justify="left", style="yellow")
    table.add_column("Pengarang", justify="left", style="yellow")
    table.add_column("Penerbit", justify="left", style="yellow")
    table.add_column("Tahun Terbit", justify="center", style="yellow")
    
    for i in xx:
        table.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]))

    console = Console()
    console.print(table)

    print("1. Cari lagi\n2. Kembali")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        cariBuku(user)
    elif pilihan == "2":
        if list(user)[3] == {'staff'}:
            menuStaff(user)
        else:
            menu(user)

def pinjamBuku(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fitur peminjaman buku")
    print(f"[red]*masukkan angka nol untuk kembali[/red]")
    idBuku = input("Masukkan ID Buku: ")
    idAkun = list(user)[0]
    if idBuku != "0":
        pinjam = crud.pinjamBuku(idBuku, idAkun)
        if pinjam == True:
            print("Anda meminjam buku:")
            hasil = crud.lihatBuku(idBuku)
            print(f"ID Buku: {hasil[0]}")
            print(f"Judul: {hasil[2]}\n")
            print("Tunggu 4 detik, anda akan dialihkan . . .")
            time.sleep(4)
            inventori(user)        
        else:
            print(f"Maaf, Buku dengan id {idBuku} tidak ada atau sudah anda pinjam")
            time.sleep(4)
            pinjamBuku(user)
    else:
        inventori(user)

def kembalikanBuku(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fitur pengembalian buku")
    print(f"[red]*masukkan angka nol untuk kembali[/red]")
    idBuku = input("Masukkan ID Buku: ")
    idAkun = list(user)[0]
    if idBuku != "0":
        kembali = crud.kembalikanBuku(idBuku, idAkun)
        if kembali == True:
            print("Anda mengembalikan buku:")
            hasil = crud.lihatBuku(idBuku)
            print(f"ID Buku: {hasil[0]}")
            print(f"Judul: {hasil[2]}\n")
            print("Tunggu 4 detik, anda akan dialihkan . . .")
            time.sleep(4)
            inventori(user)        
        else:
            print(f"Maaf, Buku dengan id {idBuku} tidak ada di inventori anda")
            time.sleep(4)
            kembalikanBuku(user)
    else:
        inventori(user)

def tambahBuku(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fitur penambahan buku")
    print("Pilih katalognya")

    dataKatalog = crud.ambilKatalog()
    tableKatalog = Table()
    tableKatalog.add_column("ID Katalog", justify="center", style="yellow")
    tableKatalog.add_column("Nomor Rak", justify="center", style="yellow")
    tableKatalog.add_column("Lokasi", justify="left", style="yellow")
    tableKatalog.add_column("Jenis Buku", justify="left", style="yellow")
    
    for i in dataKatalog:
        tableKatalog.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]))

    console = Console()
    console.print(tableKatalog)

    print(f"[red]*masukkan angka nol untuk kembali[/red]")
    katalog = input("Masukkan id katalog: ")
    if katalog == dataKatalog[0][0]:
        idbuku = input("ID Buku: ")
        judul = input("Judul: ")
        pengarang = input("Pengarang: ")
        penerbit = input("Penerbit: ")
        tahunTerbit = input("Tahun Terbit: ")
        if katalog != "0":
            tambah = crud.tambahBuku(idbuku, katalog, judul, pengarang, penerbit, tahunTerbit)
            if tambah == True:
                print("Buku berhasil ditambahkan")
                time.sleep(2)
                menuStaff(user)
            else:
                print(f"Maaf, Buku dengan id {idbuku} sudah ada")
                time.sleep(2)
                tambahBuku(user)
    else:
        menuStaff(user)

def hapusBuku(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fitur penghapusan buku")
    print(f"[red]*masukkan angka nol untuk kembali[/red]")
    idBuku = input("Masukkan id Buku: ")
    buku = crud.lihatBuku(idBuku)
    if idBuku != "0":
        if buku != None:
            table = Table()
            table.add_column("ID", justify="center", style="red")
            table.add_column("Katalog", justify="center", style="red")
            table.add_column("Judul", justify="left", style="red")
            table.add_column("Pengarang", justify="left", style="red")
            table.add_column("Penerbit", justify="left", style="red")
            table.add_column("Tahun Terbit", justify="center", style="red")
            
            table.add_row(str(buku[0]), str(buku[1]), str(buku[2]), str(buku[3]), str(buku[4]), str(buku[5]))

            console = Console()
            console.print(table)

            validasi = str(input("Apakah anda yakin ingin menghapus buku ini? (y/n): "))
            if validasi == "y":
                hapus = crud.hapusBuku(idBuku)
                if hapus == True:
                    print("Buku berhasil dihapus")
                    time.sleep(2)
                    menuStaff(user)
                else:
                    print(f"Maaf, Buku dengan id {idBuku} tidak ada")
                    time.sleep(2)
                    hapusBuku(user)
            elif validasi == "n":
                print("Buku tidak jadi dihapus")
                time.sleep(2)
                hapusBuku(user)
        else:
            print(f"Maaf, Buku dengan id {idBuku} tidak ada")
            time.sleep(2)
            hapusBuku(user)
    else:
        menuStaff(user)
    
def editRole(user):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fitur penambahan staff")
    print("1. Lihat Pengguna\n2. Jadikan Staff\n3. Hapus Staff\n4. Kembali")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        dataAkun = crud.ambilSemuaAkun()
        table = Table()
        table.add_column("Username", justify="center", style="yellow")
        table.add_column("Nama", justify="center", style="yellow")
        table.add_column("Role", justify="left", style="yellow")
        
        for i in dataAkun:
            table.add_row(str(i[0]), str(i[1]), str(i[3]))

        console = Console()
        console.print(table)

        print("1. Kembali")
        pilihan = input("Pilihan: ")
        if pilihan == "1":
            editRole(user)

    elif pilihan == "2":
        username = input("Username: ")
        role = "staff"
        tambah = crud.updateStaff(username, role)
        if tambah == True:
            print(f"Staff dengan username {username} berhasil ditambahkan")
            time.sleep(2)
            editRole(user)
        else:
            print(f"Staff dengan username {username} sudah ada")
            time.sleep(2)
            editRole(user)
    elif pilihan == "3":
        username = input("Username: ")
        role = "pengguna"
        hapus = crud.updateStaff(username, role)
        if hapus == True:
            print(f"Staff dengan username {username} berhasil dihapus")
            time.sleep(2)
            editRole(user)
        else:
            print(f"Staff dengan username {username} tidak ada")
            time.sleep(2)
            editRole(user)
    elif pilihan == "4":
        menuStaff(user)



if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()