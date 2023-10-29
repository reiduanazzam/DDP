#1. buat list untuk menampilkan data pada kategori kendaraan
# [namakendaraan, jeniskendaraan, merk kendaraan, cc kendaraan]

kendaraan1 = ["Innova", "Mobil", "Toyota", 2000]
print(kendaraan1)

#2. dari nomor 1 ditambahkan dari list yang sudah ada
#[warna kendaraan, jml ban kendaraan, harga kendaraan]
#dihapus jenis kendaraannya

kendaraan1 = kendaraan1 + ["hitam", 4, 400_000_000]
kendaraan1.remove("Mobil")
print(kendaraan1)

#3.
pesan = """
menu:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan = input(pesan)

match pilihan:
  case "1":
    print("anda memasukkan angka 1 untuk menghitung luas persegi")
    sisi = int(input("masukkan sisi:"))
    luas = sisi * sisi
    print("luas persegi dengan sisi", sisi, "adalah", luas)

  case "2":
    print("anda memasukkan angka 2 untuk menghitung luas lingkaran")
    jari = int(input("masukkan jari jari: "))
    luas = 22/7 * jari * jari
    print("luas lingkaran dengan jari", jari, "adalah", luas)

  case "3":
    print("anda memasukkan angka 3 untuk menghitung luas segitiga")
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = 1/2 * (alas * tinggi)
    print("luas segitiga dengan alas * tinggi", alas * tinggi, "adalah", luas)

  case _:
    print("")