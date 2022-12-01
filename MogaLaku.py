import pandas as pd
import json

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
        print("Login anda berhasil")
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
    df_beras = pd.read_csv("harga_beras.csv", index_col="No.")

    harga_cabaimerah = {
        "Harga" : ["Rp 20.850","Rp 18.250","Rp 24.400","Rp 18.000"],
        "Daerah" : ["Jember","Banyuwangi","Surabaya","Probolinggo"]
    }
    df_cabaimerah = pd.DataFrame(harga_cabaimerah, index = range(1, (len(harga_cabaimerah["Harga"])+1)))

    harga_cabairawit = {
        "Harga" : ["Rp 13.400","Rp 23.500","Rp 26.900","Rp 25.000"],
        "Daerah" : ["Jember","Banyuwangi","Surabaya","Probolinggo"]
    }
    df_cabairawit = pd.DataFrame(harga_cabairawit, index = range(1, (len(harga_cabairawit["Harga"])+1)))

    komoditas = input("Komoditas yang ingin dicari : ")
    if komoditas == "beras":
        print(df_beras)
    elif komoditas == "cabai merah":
        print(df_cabaimerah)
    elif komoditas == "cabai rawit":
        print(df_cabairawit)

def jual_komoditas():
    jenis_komoditas = input("1. Masukkan jenis komoditas : ")
    nama_komoditas = input("2. Masukkan nama komoditas : ")
    deskripsi = input("3. Masukkan deskripsi : ")
    alamat = input("4. Masukkan alamat : ")
    harga = input("5. Masukkan harga : ")
    if jenis_komoditas == "beras":
        with open("komoditas_beras.json", "r+") as data:
            data_baru = {
                "jenis_komoditas" : nama_komoditas, 
                "nama_komoditas" : jenis_komoditas, 
                "deskripsi" : deskripsi, 
                "alamat" : alamat, 
                "harga" : harga
                }
            data_beras = json.load(data)
            data_beras["data"].append(data_baru)
            data.seek(0)
            json.dump(data_beras, data, indent = 4)
    elif jenis_komoditas == "cabai merah":
        with open("komoditas_cabaimerah.json", "r+") as data:
            data_baru = {
                "jenis_komoditas" : nama_komoditas, 
                "nama_komoditas" : jenis_komoditas, 
                "deskripsi" : deskripsi, 
                "alamat" : alamat, 
                "harga" : harga
                }
            data_cabaimerah = json.load(data)
            data_cabaimerah["data"].append(data_baru)
            data.seek(0)
            json.dump(data_cabaimerah, data, indent = 4)
    elif jenis_komoditas == "cabai rawit" :
        with open("komoditas_cabairawit.json", "r+") as data:
            data_baru = {
                "jenis_komoditas" : nama_komoditas, 
                "nama_komoditas" : jenis_komoditas, 
                "deskripsi" : deskripsi, 
                "alamat" : alamat, 
                "harga" : harga
                }
            data_cabairawit = json.load(data)
            data_cabairawit["data"].append(data_baru)
            data.seek(0)
            json.dump(data_cabairawit, data, indent = 4)
            
def beli_komoditas():
    pencarian = input("Komoditas yang ingin dicari [beras/cabai merah/cabai rawit]: ")
    if pencarian == "beras":
        file_beras = open("komoditas_beras.json")
        data = json.loads(file_beras.read())
        for i in range(0, len(data['data'])):
            print(f"\nJenis   : {data['data'][i]['jenis_komoditas']}")
            print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            print(f"Alamat    : {data['data'][i]['alamat']}")
            print(f"Harga     : Rp {data['data'][i]['harga']}")
    elif pencarian == "cabai merah":
        file_cabaimerah = open("komoditas_cabaimerah.json")
        data = json.loads(file_cabaimerah.read())
        for i in range(0, len(data['data'])):
            print(f"\nJenis   : {data['data'][i]['jenis_komoditas']}")
            print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            print(f"Alamat    : {data['data'][i]['alamat']}")
            print(f"Harga     : Rp {data['data'][i]['harga']}")
    elif pencarian == "cabai rawit":
        file_cabairawit = open("komoditas_cabairawit.json")
        data = json.loads(file_cabairawit.read())
        for i in range(0, len(data['data'])):
            print(f"\nJenis   : {data['data'][i]['jenis_komoditas']}")
            print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            print(f"Alamat    : {data['data'][i]['alamat']}")
            print(f"Harga     : Rp {data['data'][i]['harga']}")
            
def menu():
    opsi = ["1. Cek harga", "2. Jual Komoditas", "3. Beli Komoditas", "4. Exit"]
    print("\nPilihan Menu :")
    for i in opsi:
        print(i)
    opsi_1 = int(input("Opsi : "))
    if opsi_1 == 1:
        cek_harga()
    elif opsi_1 == 2:
        jual_komoditas()
    elif opsi_1 == 3:
        beli_komoditas()
    elif opsi_1 == 4:
        exit()

if __name__ == "__main__":
    while True:
        menu()
