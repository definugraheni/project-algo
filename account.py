import pandas as pd

def signin(name,pw):
    sukses = False
    file = open('data_account.txt', "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if (a == name and b == pw):
            sukses = True
            break
    file.close()
    if (sukses):
        print("Login anda berhasil", "\nSilahkan pilih opsi berikut :")
    else :
        print("akun anda belum terdaftar, silahkan melakukan resgistrasi")

def signup(name,pw):
    file = open('data_account.txt', "a")
    file.write("\n" + name + "," + pw)
    file.close()

def accsess(option):
    global Name
    if(option == "sign in"):
        name = input("masukan username : ")
        pw = input("masukan password : ")
        signin(name,pw)
    else :
        print("Masukan username dan pasword anda yang baru")
        name = input("Masukan username : " )
        pw = input("Masukan password : ")
        signup(name,pw)
        print("anda telah berhasil, silahkan masuk")

def begin():
    global option
    print("="*58)
    print("--------------->Selamat datang di MogaLaku<---------------")
    print("="*58)
    print("Ketik 'sign in' jika sudah memiliki akun")
    print("Ketik 'sign up' jika belum memiliki akun")
    option = input("Silahkan masukan (sign in/sign up) : ")
    if (option != "sign in" and option != "sign up"):
        print("="*58)
        begin()
begin()
accsess(option)



def cek_harga():
    harga_beras = {
        "Harga" : ["Rp 11.400","Rp 10.600","Rp 11.850","Rp 10.950"],
        "Daerah" : ["Jember","Banyuwangi","Surabaya","Probolinggo"]
    }
    df_beras = pd.DataFrame(harga_beras, index = range(1, (len(harga_beras["Harga"])+1)))

    harga_cabaimerah = {
        "Harga" : ["Rp 20.850","Rp 18.250","Rp 24.400","Rp 18.000"],
        "Daerah" : ["Jember","Banyuwangi","Surabaya","Probolinggo"]
    }
    df_cabaimerah = pd.DataFrame(harga_cabaimerah, index = range(1, (len(harga_beras["Harga"])+1)))

    harga_cabairawit = {
        "Harga" : ["Rp 13.400","Rp 23.500","Rp 26.900","Rp 25.000"],
        "Daerah" : ["Jember","Banyuwangi","Surabaya","Probolinggo"]
    }
    df_cabairawit = pd.DataFrame(harga_cabairawit, index = range(1, (len(harga_beras["Harga"])+1)))

    komoditas = input("Komoditas yang ingin dicari : ")
    if komoditas == "beras":
        print(df_beras)
    elif komoditas == "cabai merah":
        print(df_cabaimerah)
    elif komoditas == "cabai rawit":
        print(df_cabairawit)

def jual_komoditas():
    nama = input("Nama komoditas : ")

opsi = ["1. Cek harga", "2. Jual Komoditas", "3. Beli Komoditas"]
for i in opsi:
    print(i)
opsi_1 = int(input("Opsi : "))
if opsi_1 == 1:
    cek_harga()
