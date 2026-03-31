#--------
# Soal 1 - Function
#--------


def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"
 
 
def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b
 
 
def rata_rata(angka: list) -> float:
    """Mengembalikan rata-rata list. Jika kosong, kembalikan 0.0."""
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


#--------
# Soal 2 - Class
#--------


class Student:
    def __init__(self, nama: str, nim: str):
        self.nama: str = nama
        self.nim: str = nim
        self.nilai: list = []

    def tmbh_nilai(self, skor: float) -> None:
        """menambahkan satu nilai ke list nilai"""
        self.nilai.append(skor)
    
    def rata_nilai(self) -> float:
        """mengembalikan rata-rata nilai"""
        return rata_rata(self.nilai)
    
    def status(self, threshold: float = 70.0) -> str:
        """mengembalikan 'LULUS' jika rata-rata >= threshold,selain itu 'TIDAK LULUS'"""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"
    
    def __str__(self) -> str:
        return (
            f"student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )



#--------
# Soal 3 - Demo
#--------

print("\n" + "="*50)
print("Demo ")

if __name__ == "__main__":


    # function(soal 1)

    print("=" * 45)
    print("=== FUNCTIONS ===")
    print("=" * 45)

    print(greet("Arifian"))

    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10) = {tambah(10)}")

    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]) = {rata_rata([])}")
    print("="*50)


    # class (soal 2)

    print("\n" + "=" * 45)
    print("=== CLASS STUDENT ===")
    print("=" * 45)


    # mahasiswa 1
    sis1 = Student("Abel", "2332043")
    sis1.tmbh_nilai(65.0)
    sis1.tmbh_nilai(88.0)
    print(sis1)
    print(f" rata-rata: {sis1.rata_nilai()}")
    print(f" status: {sis1.status()}")
    print()

    # mahasiswa 2
    sis2 = Student("Afghan", "2332067")
    sis2.tmbh_nilai(20.0)
    sis2.tmbh_nilai(40.0)
    print(sis2)
    print(f" rata-rata: {sis2.rata_nilai()}")
    print(f" status: {sis2.status()}")

    print("=" * 45)

