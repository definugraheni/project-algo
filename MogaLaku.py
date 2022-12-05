import pandas as pd
import csv
import json
import os
from time import sleep

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
        sleep(1)
        os.system("cls")
    else :
        print("Akun anda belum terdaftar, silahkan melakukan registrasi")
        print("Anda akan dikembalikan ke menu login")
        sleep(2)
        os.system("cls")
        begin()

def signup(name,pw):
    file = open('data_account.txt', "a")
    file.write("\n" + name + "," + pw)
    file.close()

def accsess(option):
    global Name
    if(option == "sign in"):
        name = input("Masukan username : ")
        pw = input("Masukan password : ")
        signin(name,pw)
    else :
        print("Masukan username dan pasword anda yang baru")
        name = input("Masukan username : " )
        pw = input("Masukan password : ")
        signup(name,pw)
        print("Anda telah berhasil, silahkan masuk")
        sleep(1)
        os.system("cls")

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
        
def mulai():
    if __name__ == "__main__":
        begin()
        accsess(option)
        while True:
            menu()

def menu_kembali():
    while True:
        ask = input("\nKembali ke menu awal?(Y/N) : ")
        if ask == "Y" or ask == "y":
            os.system("cls")
            menu()
        elif ask == "N" or ask == "n":
            True
        
def cek_harga():
    os.system("cls")
    df_beras = pd.read_csv("harga_beras.csv", index_col="No.")
    df_cabaimerah = pd.read_csv("harga_cabai_merah.csv", index_col="No.")
    df_cabairawit = pd.read_csv("harga_cabai_rawit.csv", index_col="No.")
    df_bawangmerah = pd.read_csv("harga_bawang_merah.csv", index_col="No.")
    df_bawangputih = pd.read_csv("harga_bawang_putih.csv", index_col="No.")
    komoditas = input("Komoditas yang ingin dicari : ")
    if komoditas != "beras" and komoditas != "cabai merah" and komoditas != "cabai rawit" and komoditas != "bawang putih" and komoditas != "bawang merah":
        cek_harga()
    else:
        if komoditas == "beras":
            print(df_beras)
            print()
            menu_kembali()
        elif komoditas == "cabai merah":
            print(df_cabaimerah)
            print()
            menu_kembali()
        elif komoditas == "cabai rawit":
            print(df_cabairawit)
            print()
            menu_kembali()
        elif komoditas == "bawang merah":
            print(df_bawangmerah)
            print()
            menu_kembali()
        elif komoditas == "bawang putih":
            print(df_bawangputih)
            print()
            menu_kembali()
            

def jual_komoditas():
    os.system("cls")
    jenis_komoditas = input("1. Masukkan jenis komoditas : ")
    nama_komoditas = input("2. Masukkan nama komoditas : ")
    deskripsi = input("3. Masukkan deskripsi : ")
    alamat = input("4. Masukkan alamat : ")
    harga = float(input("5. Masukkan harga : "))
    if jenis_komoditas == "cabai merah":
        with open("komoditas_cabai_merah.csv", "a") as file:
            kolom = ["jenis komoditas","nama komoditas","deskripsi","alamat","harga"]
            writer = csv.DictWriter(file, fieldnames=kolom)
            writer.writerow({'jenis komoditas' : jenis_komoditas, 'nama komoditas' : nama_komoditas, 'deskripsi' : deskripsi, 'alamat' : alamat, 'harga' : harga})
            menu_kembali()
    elif jenis_komoditas == "cabai rawit":
        with open("komoditas_cabai_rawit.csv", "a") as file:
            kolom = ["jenis komoditas","nama komoditas","deskripsi","alamat","harga"]
            writer = csv.DictWriter(file, fieldnames=kolom)
            writer.writerow({'jenis komoditas' : jenis_komoditas, 'nama komoditas' : nama_komoditas, 'deskripsi' : deskripsi, 'alamat' : alamat, 'harga' : harga})
            menu_kembali()
    elif jenis_komoditas == "bawang merah":
        with open("komoditas_bawang_merah.csv", "a") as file:
            kolom = ["jenis komoditas","nama komoditas","deskripsi","alamat","harga"]
            writer = csv.DictWriter(file, fieldnames=kolom)
            writer.writerow({'jenis komoditas' : jenis_komoditas, 'nama komoditas' : nama_komoditas, 'deskripsi' : deskripsi, 'alamat' : alamat, 'harga' : harga})
            menu_kembali()
    elif jenis_komoditas == "bawang putih":
        with open("komoditas_bawang_putih.csv", "a") as file:
            kolom = ["jenis komoditas","nama komoditas","deskripsi","alamat","harga"]
            writer = csv.DictWriter(file, fieldnames=kolom)
            writer.writerow({'jenis komoditas' : jenis_komoditas, 'nama komoditas' : nama_komoditas, 'deskripsi' : deskripsi, 'alamat' : alamat, 'harga' : harga})
            menu_kembali()
    
def beli_komoditas():
    os.system("cls")
    keranjang = []
    harga = []
    total = sum(harga)
    def cek_keranjang():
        if len(keranjang) < 1 and len(harga) < 1:
            print("Maaf anda belum melakukan pembelian")
            sleep(1)
            os.system("cls")
            beli_komoditas()
        else:
            for i in keranjang:
                print(i, end="")
            print(f"Total Pembayaran : IDR {total}K")
            menu_kembali()
    menu = ["1. Beli", "2. Cek Keranjang"]
    print("MENU")
    for i in menu:
        print(i)
    opsi = int(input("Opsi : "))
    if opsi == 1:
        os.system("cls")
        pencarian = input("Komoditas yang ingin dicari : ")
        if pencarian != "beras" and pencarian != "cabai merah" and pencarian != "cabai rawit" and pencarian != "bawang putih" and pencarian != "bawang putih":
            print("Data yang anda cari tidak ada")
            sleep(1)
            os.system("cls")
            beli_komoditas()
        else:
            if pencarian == "cabai merah":
                data = []
                df_cabaimerah = pd.read_csv("komoditas_cabai_merah.csv")
                print(df_cabaimerah)
                with open("komoditas_cabai_merah.csv", "r") as file :
                    csv_merah = csv.DictReader(file)
                    for row in csv_merah:
                        data.append(row)
                print(data)
                print(len(data))
                while True:
                    kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
                    if kode in range(0,len(data)):
                        keranjang.append(data[kode]['nama komoditas'])
                        harga.append(data[kode]['harga'])
                    ask = input("Mau membeli lagi?(Y/N): ")
                    if ask == "Y" or ask == "y":
                        True
                    elif ask == "N" or ask == "n":
                        print("Anda akan dibawa kembali ke menu awal")
                        sleep(2)
                        os.system("cls")
                        break
                # row = []
                # for i in df_cabaimerah:
                #     row.append(i)
                #     print(row)

                    
                    
            # if pencarian == "beras":
            #     file_beras = open("komoditas_beras.json")
            #     data = json.loads(file_beras.read())
            #     for i in range(0, len(data['data'])):
            #         print(f"Kode {[i]}")
            #         print(f"Jenis     : {data['data'][i]['jenis_komoditas']}")
            #         print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            #         print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            #         print(f"Alamat    : {data['data'][i]['alamat']}")
            #         print(f"Harga     : IDR {data['data'][i]['harga']}K")
            #     while True:
            #         kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
            #         if kode in range(0, len(data['data'])):
            #             keranjang.append(data['data'][kode]['nama_komoditas'])
            #             harga.append(data['data'][kode]['harga'])
            # elif pencarian == "cabai merah":
            #     file_cabaimerah = open("komoditas_cabai_merah.json")
            #     data = json.loads(file_cabaimerah.read())
            #     for i in range(0, len(data['data'])):
            #         print(f"Kode {[i]}")
            #         print(f"Jenis     : {data['data'][i]['jenis_komoditas']}")
            #         print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            #         print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            #         print(f"Alamat    : {data['data'][i]['alamat']}")
            #         print(f"Harga     : IDR {data['data'][i]['harga']}K")
            #     while True:
            #         kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
            #         if kode in range(0, len(data['data'])):
            #             keranjang.append(data['data'][kode]['nama_komoditas'])
            #             harga.append(data['data'][kode]['harga'])
            #         ask = input("Mau membeli lagi?(Y/N): ")
            #         if ask == "Y" or ask == "y":
            #             True
            #         elif ask == "N" or ask == "n":
            #             print("Anda akan dibawa kembali ke menu awal")
            #             sleep(2)
            #             os.system("cls")
            #             break
            # elif pencarian == "cabai rawit":
            #     file_cabairawit = open("komoditas_cabai_rawit.json")
            #     data = json.loads(file_cabairawit.read())
            #     for i in range(0, len(data['data'])):
            #         print(f"Kode {[i]}")
            #         print(f"Jenis     : {data['data'][i]['jenis_komoditas']}")
            #         print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            #         print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            #         print(f"Alamat    : {data['data'][i]['alamat']}")
            #         print(f"Harga     : IDR {data['data'][i]['harga']}K")
            #     while True:
            #         kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
            #         if kode in range(0, len(data['data'])):
            #             keranjang.append(data['data'][kode]['nama_komoditas'])
            #             harga.append(data['data'][kode]['harga'])
            #         ask = input("Mau membeli lagi?(Y/N): ")
            #         if ask == "Y" or ask == "y":
            #             True
            #         elif ask == "N" or ask == "n":
            #             print("Anda akan dibawa kembali ke menu awal")
            #             sleep(2)
            #             os.system("cls")
            #             break
            # elif pencarian == "bawang merah":
            #     file_bawangmerah = open("komoditas_bawang_merah.json")
            #     data = json.loads(file_bawangmerah.read())
            #     for i in range(0, len(data['data'])):
            #         print(f"Kode {[i]}")
            #         print(f"Jenis     : {data['data'][i]['jenis_komoditas']}")
            #         print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            #         print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            #         print(f"Alamat    : {data['data'][i]['alamat']}")
            #         print(f"Harga     : IDR {data['data'][i]['harga']}K")
            #     while True:
            #         kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
            #         if kode in range(0, len(data['data'])):
            #             keranjang.append(data['data'][kode]['nama_komoditas'])
            #             harga.append(data['data'][kode]['harga'])
            #         ask = input("Mau membeli lagi?(Y/N): ")
            #         if ask == "Y" or ask == "y":
            #             True
            #         elif ask == "N" or ask == "n":
            #             print("Anda akan dibawa kembali ke menu awal")
            #             sleep(2)
            #             os.system("cls")
            #             break
            # elif pencarian == "bawang putih":
            #     file_bawangputih = open("komoditas_bawang_putih.json")
            #     data = json.loads(file_bawangputih.read())
            #     for i in range(0, len(data['data'])):
            #         print(f"Kode {[i]}")
            #         print(f"Jenis     : {data['data'][i]['jenis_komoditas']}")
            #         print(f"Nama      : {data['data'][i]['nama_komoditas']}")
            #         print(f"Deskripsi : {data['data'][i]['deskripsi']}")
            #         print(f"Alamat    : {data['data'][i]['alamat']}")
            #         print(f"Harga     : IDR {data['data'][i]['harga']}K")
            #     while True:
            #         kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
            #         if kode in range(0, len(data['data'])):
            #             keranjang.append(data['data'][kode]['nama_komoditas'])
            #             harga.append(data['data'][kode]['harga'])
            #         ask = input("Mau membeli lagi?(Y/N): ")
            #         if ask == "Y" or ask == "y":
            #             True
            #         elif ask == "N" or ask == "n":
            #             print("Anda akan dibawa kembali ke menu awal")
            #             sleep(2)
            #             os.system("cls")
            #             break
    elif opsi == 2:
        cek_keranjang()
    else:
        beli_komoditas()
            
def menu():
    opsi = ["1. Cek harga", "2. Jual Komoditas", "3. Beli Komoditas", "4. Exit"]
    print("Pilihan Menu :")
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

mulai()
