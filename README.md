# 📚 Ringkasan Tugas Python

---

## 📄 Tugas 4 — Struktur Data Python

**Topik:** List, Tuple, Set, Dict, Nested Structure, Comprehension, Keanggotaan

### Soal 1 — List
Membuat list campuran (`int`, `str`, `bool`, `float`), lalu menampilkan elemen pertama & terakhir serta slicing `[1:5:2]`. Dilanjutkan dengan operasi mutasi:
- `append()` — menambahkan elemen di akhir
- `insert()` — menyisipkan elemen di indeks tertentu
- `extend()` — menggabungkan list lain
- `pop()` — menghapus elemen terakhir
- `remove()` — menghapus nilai tertentu

### Soal 2 — Tuple
Membuat tuple `(8, 9, "hey", "ya", "yu")`, menampilkan panjang (`len()`), akses indeks, dan **unpacking** menggunakan `*rest` untuk menangkap sisa elemen.

### Soal 3 — Set
Mendefinisikan dua set (`set_a`, `set_b`) dan menampilkan operasi himpunan:
| Operasi | Simbol |
|---|---|
| Union | `\|` |
| Intersection | `&` |
| Difference | `-` |
| Symmetric Difference | `^` |

Juga mendemonstrasikan bahwa set secara otomatis menghilangkan duplikat.

### Soal 4 — Dictionary
Membuat dict `mahasiswa` dengan key: `nama`, `nim`, `angkatan`, `kota`. Operasi yang dilakukan:
- Menambah key baru (`email`)
- Mengubah nilai key (`kota`)
- Menghapus key (`del`)
- Iterasi menggunakan `.keys()`, `.values()`, `.items()`

### Soal 5 — Nested Structure
Membuat list of dict berisi data album musik. Menampilkan semua judul dengan loop, lalu memfilter album dengan tahun ≥ 2000 menggunakan **list comprehension**.

### Soal 6 — Comprehension & Utilitas
- **List comprehension:** bilangan genap (1–20) dan kuadrat (1–20)
- **Dict comprehension:** pemetaan angka 1–10 ke label `"genap"` / `"ganjil"`
- **Set comprehension:** ekstraksi huruf unik lowercase dari sebuah kalimat

### Soal 7 — Keanggotaan & Pencarian
Mengecek keberadaan item di list dan set menggunakan operator `in`, lalu menampilkan posisi indeks dengan `.index()` jika ditemukan.

---

## 📄 Tugas 5 — Function & OOP Dasar

**Topik:** Fungsi, Type Hint, Docstring, Class, Method, `__str__`

### Soal 1 — Functions
Tiga fungsi dengan **type hint** dan **docstring**:

| Fungsi | Deskripsi |
|---|---|
| `greet(nama)` | Mengembalikan string sapaan |
| `tambah(a, b=0.0)` | Penjumlahan dengan nilai default parameter |
| `rata_rata(angka)` | Rata-rata list; mengembalikan `0.0` jika kosong |

### Soal 2 — Class `Student`
Class dengan atribut `nama`, `nim`, dan `nilai` (list). Method yang dimiliki:

| Method | Deskripsi |
|---|---|
| `tmbh_nilai(skor)` | Menambahkan skor ke list nilai |
| `rata_nilai()` | Mengembalikan rata-rata nilai (memanggil `rata_rata()`) |
| `status(threshold=70.0)` | Mengembalikan `"LULUS"` atau `"TIDAK LULUS"` |
| `__str__()` | Representasi string objek Student |

### Soal 3 — Demo
Dijalankan dalam blok `if __name__ == "__main__"`:
- Pengujian ketiga fungsi dari Soal 1
- Pembuatan 2 objek `Student` dengan skor berbeda — satu lulus, satu tidak lulus

---

## 📄 Tugas 6 — NumPy, Pandas, File I/O & OOP Lanjut

**Topik:** NumPy statistik, Pandas DataFrame, File I/O `.txt`, Class `GradeBook`

### Bagian 1 — NumPy
Array nilai ujian 12 mahasiswa diolah menggunakan fungsi statistik NumPy:

| Statistik | Fungsi |
|---|---|
| Rata-rata | `np.mean()` |
| Median | `np.median()` |
| Standar Deviasi | `np.std()` |
| Min / Maks | `np.min()` / `np.max()` |

Seed ditetapkan dengan `np.random.seed(42)` untuk reproduksibilitas.

### Bagian 2 — Pandas DataFrame
DataFrame dibuat dari dict berisi kolom `nama`, `nim`, dan `nilai`. Kolom `status` ditambahkan menggunakan `.apply()` dengan lambda: nilai ≥ 70 → `"LULUS"`, selainnya → `"TIDAK LULUS"`.

### Bagian 3 — File I/O
Fungsi `menulis_ringkasan(path, df)` menulis ringkasan statistik NumPy dan detail tabel mahasiswa ke file `ringkasan_tugas6.txt` dalam format teks terstruktur.

### Bagian 4 — OOP: Class `GradeBook`
Class yang membungkus DataFrame dan menyediakan method analisis:

| Method | Deskripsi |
|---|---|
| `average()` | Rata-rata kolom nilai |
| `pass_rate(threshold=70.0)` | Persentase mahasiswa lulus |
| `save_summary(path)` | Menambahkan ringkasan OOP ke file `.txt` (mode `"a"`) |
| `__str__()` | Representasi string objek GradeBook |

### Demo
Blok `if __name__ == "__main__"` menjalankan seluruh alur: cetak statistik NumPy → tampilkan DataFrame → tulis file → instansiasi `GradeBook` → cetak hasil analisis → simpan ringkasan tambahan ke file yang sama.

---

*Dibuat sebagai ringkasan akademik — Pemrograman Python*
