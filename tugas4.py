#--------
# Soal 1 - List
#--------
myy_list = [6, 7, "keren", True, "sekali", 7.6]

# Tampilkan: elemen pertama & terakhir, slicing 
print("\n" + "="*50)
print("Soal 1 - List ")
print("elemen pertama:", myy_list[0])
print("elemen terakhir:", myy_list[-1])
print("Slicing [1:5:2]:", myy_list[1:5:2])

# Lakukan: append(), insert(), extend(), pop(), remove() lalu tampilkan sebelum & sesudah.
print(f"Sebelum: {myy_list}")

myy_list.append("coolll")
print(f"Setelah append: {myy_list}")

myy_list.insert(3, "betul")
print(f"Setelah insert: {myy_list}")

myy_list.extend(["jazz", 44])
print(f"Setelah extend: {myy_list}")

myy_list.pop()
print(f"Setelah pop: {myy_list}")

myy_list.remove(7)
print(f"Setelah remove: {myy_list}")
print("="*50)

#--------
# Soal 2 - Tuple
#--------

myy_tuple = (8, 9, "hey", "ya", "yu")

print("\n" + "="*50)
print("Soal 2 - Tuple ")

#Tampilkan panjang (len()), akses indeks, dan unpacking (minimal 3 variabel, gunakan *rest bila perlu).
print(f"panjang tuple: {len(myy_tuple)}")
print(f"Elemen ke-1 (idx 0): {myy_tuple[0]}")
print(f"Elemen ke-3 (idx 2): {myy_tuple[2]}")
print(f"Elemen Terakhir    : {myy_tuple[-1]}")

##unpacking
lapan, bilan, *rest = myy_tuple
print(f"\nUnpacking: lapan='{lapan}', bilan={bilan}, rest={rest}")
print("="*50)

#--------
# Soal 3 - Set
#--------

print("\n" + "="*50)
print("Soal 3 - Set ")


#Tampilkan: union (|), intersection (&), difference (-), symmetric_difference (^).
set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}
print(f"Set A : {set_a}")
print(f"Set B : {set_b}")
 
print(f"\nUnion (|)                : {set_a | set_b}")
print(f"Intersection (&)         : {set_a & set_b}")
print(f"Difference A-B (-)       : {set_a - set_b}")
print(f"Symmetric Difference (^) : {set_a ^ set_b}")

#Tunjukkan bahwa duplikat otomatis hilang.
set_duplikat = {6, 6, 7, 7, 8, 9, 10, 10}
print(f"\nSet dengan duplikat {{6, 6, 7, 7, 8, 9, 10, 10}} menjadi {set_duplikat}")

print("="*50)


#--------
# Soal 4 - Dict
#--------

print("\n" + "="*50)
print("Soal 4 - Dict ")
mahasiswa = {
    "nama"    : "Gabriel Tarikh Omar",
    "nim"     : "2332063",
    "angkatan": 2023,
    "kota"    : "Batam"
}
print(f"Dict mahasiswa : {mahasiswa}")
 
# Tambah key baru
mahasiswa["email"] = "abel@gmail.com"
print(f"\nSetelah tambah 'email'  : {mahasiswa}")
 
# Ubah nilai key
mahasiswa["kota"] = "Kijang"
print(f"Setelah ubah 'kota'     : {mahasiswa}")
 
# Hapus key
del mahasiswa["email"]
print(f"Setelah hapus 'email'   : {mahasiswa}")
 
print(f"\nkeys()   : {list(mahasiswa.keys())}")
print(f"values() : {list(mahasiswa.values())}")
print(f"items()  : {list(mahasiswa.items())}")
 
print("\nIterasi key: value")
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")

print("="*50)

#--------
# Soal 5 - Nested Structure
#--------

print("\n" + "="*50)
print("Soal 5 - Nested Structure ")

daftar_album = [
    {"title": "Transcendence into the Peripheral", "artist": "Disembowelment", "tahun": 1993},
    {"title": "Vidrio", "artist": "Titanic", "tahun": 2023},
    {"title": "In a Silent Way", "artist": "Miles Davis", "tahun": 1969},
    {"title": "First Utterance", "artist": "Comus", "tahun": 1971},
    {"title": "Paracletus", "artist": "Deathspell Omega", "tahun": 2010},
]

# Cetak semua judul dengan loop. 
print("Semua title album:")
for album in daftar_album:
    print(f"  - {album['title']} ({album['tahun']}) oleh {album['artist']}")
 
# Filter album  menggunakan list comprehension
tahun_filter = 2000
album_baru = [b for b in daftar_album if b["tahun"] >= tahun_filter]
print(f"\nalbum terbit ≥ {tahun_filter} (list comprehension):")
for album in album_baru:
    print(f"  - {album['title']} ({album['tahun']})")
print("="*50)

#--------
# Soal 6 - Comprehension & Utilitas
#--------

print("\n" + "="*50)
print("Soal 6 - Comprehension & Utilitas ")

# List comprehension
list_genap   = [x for x in range(1, 21) if x % 2 == 0]
list_kuadrat = [x**2 for x in range(1, 21)]
print(f"Genap (1–20)   : {list_genap}")
print(f"Kuadrat (1–20) : {list_kuadrat}")
 
# Dict comprehension
dict_paritas = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print(f"\nDict genap/ganjil (1–10) :")
for angka, label in dict_paritas.items():
    print(f"  {angka}: {label}")
 
# Set comprehension
sentence = "Nama Saya adalah Gabriel Tarikh Omar"
huruf_lowercase = {ch.lower() for ch in sentence if ch.isalpha()}
print(f"\nlowercase dari sentence:")
print(f"  '{sentence}'")
print(f"  lowercase: {sorted(huruf_lowercase)}")
print("="*50)


#--------
# Soal 7 - Keanggotaan & pencarian sederhana
#--------

print("\n" + "="*50)
print("Soal 7 - Keanggotaan & pencarian sederhana ")
 
smartphone_list = ["apple", "samsung", "gpixel", "huawei", "poco"]
smartphone_set  = {"apple", "samsung", "gpixel", "huawei", "poco"}
 
cari_ada    = "samsung"
cari_tidak  = "vivo"
 
#Cek keanggotaan (in) pada list/set
print(f"List smartphone : {smartphone_list}")
print(f"Set smartphone  : {smartphone_set}")
print(f"\nCek '{cari_ada}' in list  → {cari_ada in smartphone_list}")
print(f"Cek '{cari_tidak}' in list → {cari_tidak in smartphone_list}")
print(f"Cek '{cari_ada}' in set   → {cari_ada in smartphone_set}")
print(f"Cek '{cari_tidak}' in set  → {cari_tidak in smartphone_set}")
 
# Gunakan index() atau in untuk melaporkan posisi/keberadaan item secara ringkas.
for item in [cari_ada, cari_tidak]:
    if item in smartphone_list:
        print(f"\n'{item}' ditemukan di index {smartphone_list.index(item)} (list)")
    else:
        print(f"\n'{item}' tidak ditemukan dalam list")

print("=" * 55)


print("="*50)
