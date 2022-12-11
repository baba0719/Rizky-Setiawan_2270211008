'''

Tugas praktek 
Nama : RIZKY SETIAWAN
Nim : 2270211008
Tugas membuat aplikasi kasir menggunakan bahasa python

'''

#created by ky

'''

kasir warung kopi

program ini berfungsi untuk mencetak bon transaksi kasir warung kopi
program akan meminta memasukkan indentias pelanggan, kemudian akan menghitung biaya dari pembelian pelanggan tsb dan mencetak bon hasil pembelian tsb

'''

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import time
tanggal = time.strftime(" %d-%m-%y %H:%M:%S ")
print(tanggal)

print(" Warung Kopi Ngablak ")
print(" Jalan raya Jatiwaringin Pondok Gede Jawa Barat ")
print(" No. 08123456789 ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Menu Di Toko kami ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" 1. kopi hitam  : 5000 ")
print(" 2. kopi toraja : 10000")
print(" 3. kopi sunda  : 15000")
print(" 4. kopi madura : 20000")
print(" 5. kopi medan  : 25000")
print(" 6. kopi aceh   : 30000")
print(" 7. kopi teknik : 50000")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

namaPelanggan=str(input(" Masukkan nama pelanggan : "))
nomorMeja=str(input(" Masukkan nomor meja : "))
ListMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia : "))
catatan=str(input(" Masukkan catatan pesanan : "))
JumlahPesanan=int(input(" Masukkan jumlah pesanan : "))

if ListMenu == "1":
    namaMenu = " kopi hitam "
    hargaPerBarang=(5000)
    jumlah=(5000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else: 
        totaljumlah=int(jumlah+pajak)

if ListMenu == "2":
    namaMenu = " kopi toraja "
    hargaPerBarang=(10000)
    jumlah=(10000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "3":
    namaMenu = " kopi sunda "
    hargaPerBarang=(15000)
    jumlah=(15000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "4":
    namaMenu = " kopi madura "
    hargaPerBarang=(20000)
    jumlah=(20000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "5":
    namaMenu = " kopi medan "
    hargaPerBarang=(25000)
    jumlah=(25000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)

if ListMenu == "6":
    namaMenu = " kopi aceh "
    hargaPerBarang=(30000)
    jumlah=(30000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5:
        totaljumlah=int(jumlah+pajak)
    else:
        totaljumlah=int(jumlah+pajak)
    
if ListMenu == "7":
    namaMenu = " kopi teknik "
    hargaPerBarang=(50000)
    jumlah=(50000*JumlahPesanan)
    pajak=int(jumlah * 0.1)
    if JumlahPesanan >= 5: 
        totaljumlah=int(jumlah+pajak)
    else:
        menu=input(" Maaf nomor yang anda pilih tidak ada di menu")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("       Struk Pembelian       ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Nama Pelanggan      :",namaPelanggan)
print(" Nomor Meja          :",nomorMeja)
print(" Nama Menu           :",namaMenu)
print(" Catatan             :",catatan)
print(" Jumlah Pesanan      :",JumlahPesanan)
print(" Harga Perbarang     :","Rp.",hargaPerBarang)
print(" Jumlah              :","Rp.",jumlah)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Total               :","Rp.",totaljumlah)
Bayar=int(input(" Dibayar             : Rp. "))
Kembalian= (Bayar-totaljumlah)
print(" Kembali             :","Rp.",Kembalian)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Terima kasih atas pesanan anda ")
print(" Harga Termasuk PPN ")