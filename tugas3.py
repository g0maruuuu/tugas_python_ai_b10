#--------
# Soal 1 - Deklarasi Variabel dan Tipe Data
#--------

nama = "abel"   # string
umur = 21   # integer
ipk = 3.86   # float
is_keren = True   # boolean
hobby = ["music", "gaming", "collecting vinyl", "hifi audio", "watching movies dan tv shows"] # list

print("\n" + "="*50)
print("Soal 1 - Deklarasi Variabel dan Tipe Data ")
print(f"Nama: {nama}  -> tipe: {type(nama)}")
print(f"Umur: {umur}  -> tipe: {type(umur)}")
print(f"IPK: {ipk}  -> tipe: {type(ipk)}")
print(f"Apakah Keren?: {is_keren}  -> tipe: {type(is_keren)}")
print(f"hobby: {hobby}  -> tipe: {type(hobby)}")
print("="*50)


#--------
# Soal 2 - Manipulasi String
#--------
print("\n" + "="*50)
print("Soal 2 - Manipulasi String ")
#length
print(f"Lenght: {len(nama)}")

#uppercae
print(f"uppercase: {nama.upper()}")

#strip
contoh = "  wiwi don  "
print(f"strip: {contoh.strip()}")

#replace
name = "abeb"
print(f"replace: {name.replace("b", "z")}")

#split
kalimat = "clavicular mogged and"
print(f"split: {kalimat.split()}")

#join 
kata_kata = "itiswhatitis"
print(f"join: {'-'.join(kata_kata)}")
print("="*50)

#--------
# Soal 3 - Operasi Matematika Sederhana
#--------

x = 17
z = 5
 
print("\n" + "="*50)
print("Soal 3 - Operasi Matematika Sederhana ") 
print(f"x = {x}, z = {z}")
print(f"Penjumlahan  (x + z)  = {x + z}")
print(f"Pengurangan  (x - z)  = {x - z}")
print(f"Perkalian    (x * z)  = {x * z}")
print(f"Pembagian    (x / z)  = {x / z:.2f}")
print(f"Bagi Bulat   (x // z) = {x // z}")
print("="*50)

#--------
# Soal 4 - List dan Akses Elemen
#--------
print("\n" + "="*50)
print("Soal 4 - List dan Akses Elemen ") 
item_shop = ["Slowing Bullets", "Arcane Surge", "Divine Kevlar", "Elephant Shots", "Toxic Bullets"]
print(f"List item        : {item_shop}")
 
# Akses elemen tertentu
print(f"Elemen ke-1 (idx 0): {item_shop[0]}")
print(f"Elemen ke-3 (idx 2): {item_shop[2]}")
print(f"Elemen Terakhir    : {item_shop[-1]}")
 
# Tambah item baru
item_shop.append("Withering Whip")
print(f"Setelah append()   : {item_shop}")
 
# Hapus item dengan remove()
item_shop.remove("Slowing Bullets")
print(f"Setelah remove()   : {item_shop}")
 
# Hapus item terakhir dengan pop()
item_shop.pop()
print(f"Setelah pop()      : {item_shop}")
print("="*50)

#--------
# Soal 5 - Penggunaan Input dari User
#--------
print("\n" + "=" * 50)
print("  5. PENGGUNAAN INPUT DARI USER")
 
nama_input = input("Masukkan nama Anda : ")
umur_input = input("Masukkan umur Anda : ")
 
print(f"\nHalo, nama saya {nama_input} dan umur saya {umur_input} tahun.")
print("=" * 50)