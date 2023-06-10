import linecache
#https://stackoverflow.com/questions/2081836/how-to-read-specific-lines-from-a-file-by-line-number
#https://www.geeksforgeeks.org/linecache-getline-in-python/

class awal():
  def __init__(self, nama):
    self.nama = nama

  def greeting(self):
    print('='*54)
    print('|\t          BERIKUT ADALAH LIST MENU:  \t         |')
    print('|\t\t\t\t\t  1.Login                        |')
    print('|\t\t\t\t\t  2.Register                     |')
    print('|\t\t\t\t\t  3.Exit                         |')
    print('='*54)

    satu.menu()
    
  def menu(self):
    pil = int(input("Masukkan pilihan kamu (1/2/3): "))
    if pil == 1:
      satu.login()

    elif pil == 2:
      satu.register()

    elif pil == 3:
      tiga.greeting()
      

  def register(self):
    print('='*54)
    print(f"{'Menu Pendaftaran':^54}")
    print('='*54)
    self.__username = input("Masukkan username (Tidak boleh menggunakan spasi!): ")
    if len(self.__username.split()) == 1:
      print('')
      for i in range(3):
        print("Mohon tunggu...")
      print('')    
      #https://www.pythonindo.com/operasi-file/
      file = open('login.txt', 'r')
      
      #https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/
      flag = False
      idx = 0
      for line in file:
        idx += 1
        if self.__username in line:
          flag = True
          break
            
      file.close()

      if flag==True:
        print("Username telah terdaftar pada indeks ke %d! Silahkan masuk ke menu login!" %idx)

        satu.login()

      else:
        file = open('login.txt', 'a')
        print("Username belum terdaftar, silahkan lanjutkan")
        self.__password = input("Masukkan password: ")
        file.write(self.__username + " " + self.__password + "\n")
        file.close()

        print('')
        for i in range(3):
          print("Mohon tunggu...")
        print('') 
        print('Pendaftaran berhasil! Anda dialihkan ke menu login')
        satu.login()
    
    else:
      print('Username ditolak! Username tidak boleh menggunakan spasi!!')
      satu.register()

    
    
  def login(self):
    print('='*54)
    print(f"{'Menu Login' :^54}")
    print('='*54)
    self.__username = input('Masukkan username: ')
    self.__password = input('Masukkan password: ')

    file = open('login.txt', 'r')
    flag = False
    idx = 0
    for line in file:
      idx += 1
      if self.__username in line:
        flag = True
        break
    file.close()


    baris = linecache.getline('login.txt', idx)
    baris = baris.split()
    #https://www.w3schools.com/python/ref_string_split.asp
    if (len(baris) != 0 and flag == True and self.__password == baris[1]):
      print('\nHai {}! Anda dialihkan ke main menu!' .format(self.nama))
      dua.greeting()
    
    else:
      pil = input('Login gagal! Anda ingin ke menu pendaftaran? (y/t) : ').lower()
      if pil =='y':
        satu.register()
      else:
        satu.greeting()


class tengah(awal):
  def greeting(self):
    batas = '|'
    teks1 = 'Selamat datang di main menu {}!'.format(self.nama)
    teks2 = 'Berikut adalah menu yang dapat kamu pilih:'
    teks3 = '1. List Buku'
    teks4 = '2. Peminjaman Buku'
    teks5 = '3. Pengembalian Buku'
    teks6 = '4. Logout'
    print("="*54)
    print(f"{batas : <2}{teks1 : ^50}{batas : >2}")
    print(f"{batas : <2}{teks2 : ^50}{batas : >2}")
    print(f"{batas : <2}{teks3 : ^50}{batas : >2}")
    print(f"{batas : <2}{teks4 : ^50}{batas : >2}")
    print(f"{batas : <2}{teks5 : ^50}{batas : >2}")
    print(f"{batas : <2}{teks6 : ^50}{batas : >2}")
    print("="*54)

    dua.menu()

  def menu(self):
    pil = int(input("Masukan Pilihan anda (1/2/3/4): "))
    if pil == 1:
      dua.listbuku()
    elif pil == 2:
      dua.pinjambuku()
    elif pil == 3:
      dua.pengembalianbuku()
    elif pil == 4:
      dua.logout()
    else:
      print("Maaf inputan tidak tersedia.")
      dua.greeting()
      
  def listbuku(self):
    print("="*54)
    batas = '|'
    print(f"{batas : <2}{'List Buku' : ^50}{batas : >2}")
    txt1 = "Sejarah      ===> Kode Buku 001"
    txt2= "Novel        ===> Kode Buku 002"
    txt3 = "Buku Pelajaran => Kode Buku 003"
    txt4 = "Jurnal       ===> Kode Buku 004"
    txt5= "Fiksi        ===> Kode Buku 005"
    print(f"{batas : <2}{txt1 : ^50}{batas : >2}")
    print(f"{batas : <2}{txt2 : ^50}{batas : >2}")
    print(f"{batas : <2}{txt3 : ^50}{batas : >2}")
    print(f"{batas : <2}{txt4 : ^50}{batas : >2}")
    print(f"{batas : <2}{txt5 : ^50}{batas : >2}")
    print("="*54)
    pil1 = input('Apakah kamu ingin meminjam buku?(y/t): ')
    if pil1 =='y':
      dua.pinjambuku()
    else:
      dua.greeting()
  
  def pinjambuku(self):
    print('Ini adalah menu peminjaman buku')
    kode = input('Silahkan Masukan Kode Buku Yang Ingin Anda Pinjam : ')
    durasi = input("Masukkan tanggal pengembalian(dd/mm/yyyy) : ")

    with open('buku.txt', 'r') as f1:
      flag = False
      idx = 0
      for line in f1:
        idx += 1
        if kode in line:
          flag = True
          break

      brs = linecache.getline('buku.txt', idx)
      brs = brs.split()
      #https://www.w3schools.com/python/ref_string_split.asp
      if (len(brs) != 0 and flag == True):
        judul = brs[1:]

    with open('datapeminjaman.txt', 'a') as f2:
      f2.write(self.nama)
      f2.write(" ")
      f2.write(kode)
      f2.write(" ")
      f2.write(' '.join(judul))
      f2.write(" ")
      f2.write(now_wib.strftime("%d/%m/%Y"))
      f2.write(" - ")
      f2.write(durasi)
      f2.write("\n")

    print('\n\nBuku {} telah terpinjam! Jangan lupa untuk mengembalikan buku tepat waktu!' .format(kode))
    dua.greeting()

  
  def pengembalianbuku(self):
    print('')
    for i in range(3):
      print('Mengecek data peminjaman buku...')
    print('')

    with open('datapeminjaman.txt', 'r') as f3 :
      flag = False
      idx = 0
      for line in f3:
        idx += 1
        if self.nama in line:
          flag = True
          break

    if flag == True:
      brs3 = linecache.getline('datapeminjaman.txt', idx)
      print(brs3)

      pil2 = input('Apakah anda ingin mengembalikan buku ini?(y/t) : ')
    
      #https://www.kite.com/python/answers/how-to-delete-a-line-from-a-file-in-python
      if pil2 == 'y':
        with open('datapeminjaman.txt', 'r') as file:
          lines = file.readlines()
        
        del lines[idx-1]

        with open('datapeminjaman.txt', 'w+') as newfile:
          for line in lines:
            newfile.write(line)

        print('Buku telah dikembalikan!')
        dua.greeting()
      else:
        print('Buku tidak jadi dikembalikan!')
        dua.greeting()
    else:
      print('Anda tidak sedang meminjam buku!')
      dua.greeting()

      
        

    
  def logout(self):
    satu.greeting()
  


class akhir(awal):
    
  def greeting(self):
    print('='*54)
    print(f"{'Terima Kasih Telah Menggunakan Aplikasi Ini!' : ^54}")
    print(f"{'Sampai Jumpa Lagi!' : ^54}")
    print('='*54)


import datetime
from datetime import datetime
import time
from time import gmtime, mktime

wib = 7 * 60 * 60
now_utc = datetime.utcnow()
base_utc = datetime(1970, 1, 1)

time_delta = now_utc - base_utc
time_delta = time_delta.total_seconds()
time_delta = time_delta + wib

now_wib = datetime.fromtimestamp(mktime(gmtime(time_delta)))
print('='*54)
print('|\t SELAMAT DATANG DI APLIKASI PEMINJAMAN BUKU \t |')
print('='*54)
panggil = input('Masukkan username kamu: ')


satu = awal(panggil)
dua = tengah(panggil)
tiga = akhir(panggil)

satu.greeting()
