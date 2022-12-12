import pandas as pd
import csv
import os
from time import sleep

# Sign In
def signin(name,password):
    sukses = False
    file = open('data_account.csv', "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if (a == name and b == password):
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
        mulai()

# Sign Up
def signup(name,password):
    file = open('data_account.csv', "a")
    file.write("\n" + name + "," + password)
    file.close()

# Input Username dan Password
def accsess(option):
    global Name
    if(option == 1):
        name = input("Masukan username : ")
        password = input("Masukan password : ")
        signin(name,password)
    else :
        print("Masukan username dan pasword anda yang baru")
        name = input("Masukan username : " )
        password = input("Masukan password : ")
        signup(name,password)
        print("Anda telah berhasil, silahkan masuk")
        sleep(1)
        os.system("cls")

# Menampilkan Tampilan Awal
def begin():
    global option
    print("="*58)
    print("--------------->Selamat datang di MogaLaku<---------------")
    print("="*58)
    print("[1] Sign In\n[2] Sign Up")
    print("Ketik '1' jika sudah memiliki akun")
    print("Ketik '2' jika belum memiliki akun")
    option = int(input("Silahkan masukan (1/2) : "))
    if (option != 1 and option != 2):
        print("="*58)
        begin()
        
# Main Loop
def mulai():
    if __name__ == "__main__":
        begin()
        accsess(option)
        while True:
            menu()

# Konfirmasi untuk Kembali ke Menu Awal
def menu_kembali():
    while True:
        ask = input("\nKembali ke menu awal?(Y/N) : ")
        if ask == "Y" or ask == "y":
            os.system("cls")
            menu()
        elif ask == "N" or ask == "n":
            True

# Fitur Cek Harga
def cek_harga():
    os.system("cls")
    print("="*58)
    print("-"*24 + ">Cek Harga<" + "-"*23)
    print("="*58)
    print("[1]Cabai Merah\n[2]Cabai Rawit\n[3]Bawang Merah\n[4]Bawang Putih")
    df_cabaimerah = pd.read_csv("harga_cabai_merah.csv", index_col="No.")
    df_cabairawit = pd.read_csv("harga_cabai_rawit.csv", index_col="No.")
    df_bawangmerah = pd.read_csv("harga_bawang_merah.csv", index_col="No.")
    df_bawangputih = pd.read_csv("harga_bawang_putih.csv", index_col="No.")
    komoditas = int(input("Komoditas yang ingin dicari : "))
    os.system("cls")
    if komoditas != 1 and komoditas != 2 and komoditas != 3 and komoditas != 4:
        cek_harga()
    else:
        if komoditas == 1:
            print("-"*39 + ">Harga Cabai Merah<" + "-"*39)
            print()
            print(df_cabaimerah)
            menu_kembali()
        elif komoditas == 2:
            print("-"*39 + ">Harga Cabai Rawit<" + "-"*39)
            print()
            print(df_cabairawit)
            print()
            menu_kembali()
        elif komoditas == 3:
            print("-"*39 + ">Harga Bawang Merah<" + "-"*38)
            print()
            print(df_bawangmerah)
            menu_kembali()
        elif komoditas == 4:
            print("-"*39 + ">Harga Bawang Putih<" + "-"*38)
            print()
            print(df_bawangputih)
            menu_kembali()
            
# Fitur Jual Komoditas
def jual_komoditas():
    os.system("cls")
    print("="*58)
    print("-"*18 + ">Input Data Komoditas<" + "-"*18)
    print("="*58)
    print("Jenis Komoditas")
    print("[1]Cabai Merah\n[2]Cabai Rawit\n[3]Bawang Merah\n[4]Bawang Putih")
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
    else:
        print("Kata yang anda masukkan ada kesalahan")
        ask = input("Tekan enter untuk melanjutkan")
        os.system("cls")
        menu()

# Fitur Beli Komoditas    
def beli_komoditas():
    os.system("cls")
    def cek_keranjang(): # Fungsi Cek Keranjang
        keranjang = []
        harga = []
        with open("keranjang.csv", "r") as file:
            writer = csv.DictReader(file)
            for row in writer:
                keranjang.append(row)
        if len(keranjang) < 1 :
            print("Maaf anda belum melakukan pembelian")
            sleep(1)
            os.system("cls")
            beli_komoditas()
        else:
            for i in keranjang:
                harga.append(float(i['harga']))
            for i in keranjang:
                print(i['nama komoditas'])
            total = sum(harga)
            print(f"Total Pembayaran : IDR {total}K")
            ask = input("Apa anda ingin melakukan pembayaran ? (Y/N): ")
            if ask == "Y" or ask == "y":
                df = pd.read_csv("keranjang.csv")
                df = df.head(0)
                df.to_csv("keranjang.csv", index=False)
                print("Terima kasih telah menggunakan jas kami :)")
                menu_kembali()
            elif ask == "N" or ask == "n":
                print("Pilihan anda kami hargai")
                menu_kembali()
    menu = ["[1] Beli", "[2] Cek Keranjang"]
    print("="*58)
    print("-"*21 + ">Menu Pembelian<" + "-"*21)
    print("="*58)
    for i in menu:
        print(i)
    opsi = int(input("Opsi : "))
    if opsi == 1:
        os.system("cls")
        print("="*58)
        print("-"*24 + ">Pencarian<" + "-"*23)
        print("="*58)
        print("[1]Cabai Merah\n[2]Cabai Rawit\n[3]Bawang Merah\n[4]Bawang Putih")
        pencarian = int(input("Komoditas yang ingin dicari : "))
        if pencarian != 1 and pencarian != 2 and pencarian != 3 and pencarian != 4:
            print("Data yang anda cari tidak ada")
            sleep(1)
            os.system("cls")
            beli_komoditas()
        else:
            if pencarian == 1:
                data = []
                df_cabai = pd.read_csv("komoditas_cabai_merah.csv")
                with open("komoditas_cabai_merah.csv", "r") as file :
                    csv_merah = csv.DictReader(file)
                    for row in csv_merah:
                        data.append(row)
                if len(data) < 1 :
                    print("Tidak ada data yang dimasukkan")
                    sleep(2)
                    os.system("cls")
                    beli_komoditas()
                else:
                    print(df_cabai)
                    loop = True
                    while loop == True:
                        kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
                        if kode in range(0,len(data)):
                            with open("keranjang.csv", "a") as file:
                                kolom = ["nama komoditas","harga"]
                                writer = csv.DictWriter(file, fieldnames=kolom)
                                writer.writerow({"nama komoditas" : (data[kode]['nama komoditas']), 'harga' : (data[kode]['harga'])})
                        ask = input("Mau membeli lagi?(Y/N): ")
                        if ask == "Y" or ask == "y":
                            loop = True
                        elif ask == "N" or ask == "n":
                            loop = False
                            print("Anda akan dibawa kembali ke menu awal")
                            sleep(2)
                            os.system("cls")
                            beli_komoditas()
            elif pencarian == 2:
                data = []
                df_cabai = pd.read_csv("komoditas_cabai_rawit.csv")
                with open("komoditas_cabai_rawit.csv", "r") as file :
                    csv_merah = csv.DictReader(file)
                    for row in csv_merah:
                        data.append(row)
                if len(data) < 1 :
                    print("Tidak ada data yang dimasukkan")
                    sleep(2)
                    os.system("cls")
                    beli_komoditas()
                else:
                    print(df_cabai)
                    loop = True
                    while loop == True:
                        kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
                        if kode in range(0,len(data)):
                            with open("keranjang.csv", "a") as file:
                                kolom = ["nama komoditas","harga"]
                                writer = csv.DictWriter(file, fieldnames=kolom)
                                writer.writerow({"nama komoditas" : (data[kode]['nama komoditas']), 'harga' : (data[kode]['harga'])})
                        ask = input("Mau membeli lagi?(Y/N): ")
                        if ask == "Y" or ask == "y":
                            loop = True
                        elif ask == "N" or ask == "n":
                            loop = False
                            print("Anda akan dibawa kembali ke menu awal")
                            sleep(2)
                            os.system("cls")
                            beli_komoditas()
            elif pencarian == 3:
                data = []
                df_bawang = pd.read_csv("komoditas_bawang_merah.csv")
                with open("komoditas_bawang_merah.csv", "r") as file :
                    csv_merah = csv.DictReader(file)
                    for row in csv_merah:
                        data.append(row)
                if len(data) < 1 :
                    print("Tidak ada data yang dimasukkan")
                    sleep(2)
                    os.system("cls")
                    beli_komoditas()
                else:
                    print(df_bawang)
                    loop = True
                    while loop == True:
                        kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
                        if kode in range(0,len(data)):
                            with open("keranjang.csv", "a") as file:
                                kolom = ["nama komoditas","harga"]
                                writer = csv.DictWriter(file, fieldnames=kolom)
                                writer.writerow({"nama komoditas" : (data[kode]['nama komoditas']), 'harga' : (data[kode]['harga'])})
                        ask = input("Mau membeli lagi?(Y/N): ")
                        if ask == "Y" or ask == "y":
                            loop = True
                        elif ask == "N" or ask == "n":
                            loop = False
                            print("Anda akan dibawa kembali ke menu awal")
                            sleep(2)
                            os.system("cls")
                            beli_komoditas()
            elif pencarian == 4:
                data = []
                df_bawang = pd.read_csv("komoditas_bawang_putih.csv")
                with open("komoditas_bawang_putih.csv", "r") as file :
                    csv_merah = csv.DictReader(file)
                    for row in csv_merah:
                        data.append(row)
                if len(data) < 1 :
                    print("Tidak ada data yang dimasukkan")
                    sleep(2)
                    os.system("cls")
                    beli_komoditas()
                else:
                    print(df_bawang)
                    loop = True
                    while loop == True:
                        kode = int(input("\nMasukkan kode komoditas yang ingin dibeli : "))
                        if kode in range(0,len(data)):
                            with open("keranjang.csv", "a") as file:
                                kolom = ["nama komoditas","harga"]
                                writer = csv.DictWriter(file, fieldnames=kolom)
                                writer.writerow({"nama komoditas" : (data[kode]['nama komoditas']), 'harga' : (data[kode]['harga'])})
                        ask = input("Mau membeli lagi?(Y/N): ")
                        if ask == "Y" or ask == "y":
                            loop = True
                        elif ask == "N" or ask == "n":
                            loop = False
                            print("Anda akan dibawa kembali ke menu awal")
                            sleep(2)
                            os.system("cls")
                            beli_komoditas()
    elif opsi == 2:
        cek_keranjang()
    else:
        beli_komoditas()
 
# Menu Awal            
def menu():
    opsi = ["[1] Cek harga", "[2] Jual Komoditas", "[3] Beli Komoditas", "[4] Exit"]
    print("="*58)
    print("-"*22 + ">Pilihan Menu<" + "-"*22)
    print("="*58)
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
        print("\nTERIMA KASIH TELAH MENGGUNAKAN JASA KAMI")
        exit()
    else:
        print("Anda salah memasukkan opsi")
        sleep(1)
        os.system("cls")
        return

# Mulai Aplikasi
mulai()
