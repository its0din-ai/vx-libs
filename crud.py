import hashlib

import mysql.connector

conn = mysql.connector.connect(
    host='192.168.128.1',
    username='root',
    database='lib_l200210056'
)

def ambilSemuaAkun():
    cur = conn.cursor()
    cur.execute("SELECT * FROM akun")
    hasil = cur.fetchall()
    cur.close()
    return hasil

def ambilDataAkun(username):
    cur = conn.cursor()
    cur.execute("SELECT * FROM akun WHERE username = %s", (username,))
    hasil = cur.fetchone()
    cur.close()
    return hasil

def daftarAkun(username, nama, password):
    try:
        password = hashlib.md5(password).hexdigest()

        cur = conn.cursor()
        cur.execute("""INSERT INTO akun(username, nama, passwords, roles, status_akun)
        VALUES (%s, %s, %s, 'pengguna', 'aktif')""",
        (username, nama, password))

        conn.commit()
        cur.close()

        return True
    except:
        return False

def ambilSemuaBuku():
    cur = conn.cursor()
    cur.execute("SELECT * FROM buku")
    hasil = cur.fetchall()
    cur.close()
    return hasil

def pencarianBuku(judul):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM buku WHERE judul LIKE '%{judul}%'")
    hasil = cur.fetchall()
    cur.close()
    return hasil

def ambilInventori(idUser):
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM buku WHERE id_buku IN
                (SELECT buku_id_buku FROM akun_has_buku WHERE akun_username = '{idUser}')""")
    hasil = cur.fetchall()
    cur.close()
    return hasil

def lihatBuku(idBuku):
    cur = conn.cursor()
    cur.execute("SELECT * FROM buku WHERE id_buku = %s", (idBuku,))
    hasil = cur.fetchone()
    cur.close()
    return hasil

def pinjamBuku(idBuku, idAkun):
    try:
        cur = conn.cursor()
        cur.execute("""INSERT INTO akun_has_buku(akun_username, buku_id_buku)
                    VALUES (%s, %s)""", (idAkun, idBuku))
        conn.commit()
        cur.close()
        return True
    except:
        return False
    
def kembalikanBuku(idBuku, idAkun):
    try:
        cur = conn.cursor()
        cur.execute("""DELETE FROM akun_has_buku WHERE akun_username = %s AND buku_id_buku = %s""",
                    (idAkun, idBuku))
        conn.commit()
        cur.close()
        return True
    except:
        return False

def ambilKatalog():
    cur = conn.cursor()
    cur.execute("SELECT * FROM katalog")
    hasil = cur.fetchall()
    cur.close()
    return hasil

def tambahBuku(idBuku, idKatalog, judul, pengarang, penerbit, tahunTerbit):
    try:
        cur = conn.cursor()
        cur.execute("""INSERT INTO buku(id_buku, katalog_id_katalog, judul, pengarang, penerbit, tahun_terbit)
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    (idBuku, idKatalog, judul, pengarang, penerbit, tahunTerbit))
        conn.commit()
        cur.close()
        return True
    except:
        return False

def hapusBuku(idBuku):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM buku WHERE id_buku = %s", (idBuku,))
        conn.commit()
        cur.close()
        return True
    except:
        return False

def updateStaff(username, roles):
    cur = conn.cursor()
    cur.execute("UPDATE akun SET roles = %s WHERE username = %s", (roles, username))
    conn.commit()
    cur.close()
    return True