#--------
# Import & Setup
#--------

import numpy as np
import pandas as pd
import os
np.random.seed(42)

#--------
# NumPy – Data & Statistik
#--------

nilai_ujian = np.array([78, 67, 93, 62, 74, 23, 55, 91, 70, 34, 70, 69])

rata_rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
stnd_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

#--------
# pandas – DataFrame
#--------

data = {
    "nama": ["Abel", "Fripp", "Comus", "Gabriel", "Ale",
              "Alex", "Michael", "Frank", "Logan", "Matilda",
              "Chuck", "Walter"],
    "nim": [f"A{100 + i}" for i in range(12)],
    "nilai": nilai_ujian.tolist(),
}

df = pd.DataFrame(data)

df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


#--------
# File I/O – Tulis Ringkasan ke .txt
#--------

OUTPUT_FILE = "ringkasan_tugas6.txt"

def menulis_ringkasan(path:str, df: pd.DataFrame) -> None:
    jmlh_lulus = (df["status"] == "LULUS").sum()
    jmlh_tdk_lulus = (df["status"] == "TIDAK LULUS").sum()

    with open(path, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(" Ringkasan Statistik Numpy\n")
        f.write("=" * 50 + "\n")
        f.write(f"Jumlah data    : {len(nilai_ujian)}\n")
        f.write(f"Rata-rata      : {rata_rata:.2f}\n")
        f.write(f"Median         : {median:.2f}\n")
        f.write(f"Standar Deviasi: {stnd_dev:.2f}\n")
        f.write(f"Nilai Minimum  : {nilai_min}\n")
        f.write(f"Nilai Maksimum : {nilai_max}\n")
        f.write("\n" + "=" * 50 + "\n")
        f.write("Ringkasan Dataframe Pandas\n")
        f.write("=" * 50 + "\n")
        f.write(f"Jumlah baris   : {len(df)}\n")
        f.write(f"Jumlah LULUS   : {jmlh_lulus}\n")
        f.write(f"Jumlah TDK LULUS: {jmlh_tdk_lulus}\n")
        f.write("\nDetail Mahasiswa:\n")
        f.write(f"{'Nama':<10} {'NIM':<8} {'Nilai':>6}  {'Status'}\n")
        f.write("-" * 40 + "\n")
        for _, row in df.iterrows():
            f.write(f"{row['nama']:<10} {row['nim']:<8} {row['nilai']:>6}  {row['status']}\n")
        f.write("=" * 50 + "\n")

#--------
# OOP Sederhana
#--------

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df =df

    def average(self) -> float:
        """rata-rata kolom nilai"""
        return round(self.df["nilai"].mean(), 2)
    
    def pass_rate(self, threshold: float = 70.0) -> float:
        """presentase mahasiswa yang lulus"""
        lulus = (self.df["nilai"] >= threshold).sum()
        return round((lulus / len(self.df)) * 100, 2)
    
    def save_summary(self, path: str) -> None:
        """menulis ringkasan ke file .txt"""
        jmlh_lulus = (self.df["status"] == "LULUS").sum()
        jmlh_tidak = (self.df["status"] == "TIDAK LULUS").sum()

        with open(path, "a", encoding="utf-8") as f:
            f.write("\n" + "=" * 50 + "\n")
            f.write(" ringkasan oop: gradebook\n")
            f.write("=" * 50 + "\n")
            f.write(f"Jumlah data    : {len(self.df)}\n")
            f.write(f"Rata-rata nilai: {self.average()}\n")
            f.write(f"Pass rate      : {self.pass_rate()}%\n")
            f.write(f"Jumlah LULUS   : {jmlh_lulus}\n")
            f.write(f"Jumlah TIDAK LULUS: {jmlh_tidak}\n")
            f.write("=" * 50 + "\n")
        print(f"  [GradeBook] Ringkasan ditambahkan ke '{path}'")

    def __str__(self) -> str:
        return (
            f"GradeBook(jumlah_data={len(self.df)}), "
            f"rata_rata={self.average()})"
        )
    

#--------
# demo
#--------

if __name__ == "__main__":
 
    # Numpy
    print("=" * 50)
    print(" Numpy")
    print("=" * 50)
    print(f"Array nilai ujian : {nilai_ujian}")
    print(f"Rata-rata         : {rata_rata:.2f}")
    print(f"Median            : {median:.2f}")
    print(f"Standar Deviasi   : {stnd_dev:.2f}")
    print(f"Nilai Minimum     : {nilai_min}")
    print(f"Nilai Maksimum    : {nilai_max}")
 
    # Pandas
    print("\n" + "=" * 50)
    print("Pandas")
    print("=" * 50)
    print("5 baris pertama DataFrame (df.head()):")
    print(df.head())
    print(f"\nJumlah LULUS      : {(df['status'] == 'LULUS').sum()}")
    print(f"Jumlah TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}")
 
    # File I/O
    menulis_ringkasan(OUTPUT_FILE, df)
    print(f"\nRingkasan statistik & DataFrame ditulis ke '{OUTPUT_FILE}'")
 
    # OOP: GradeBook
    print("\n" + "=" * 50)
    print("=== OOP: GRADEBOOK ===")
    print("=" * 50)
 
    gb = GradeBook(df)
    print(gb)
    print(f"average()         : {gb.average()}")
    print(f"pass_rate()       : {gb.pass_rate()}%")
    gb.save_summary(OUTPUT_FILE)
 
    print("\n" + "=" * 50)
    print("Selesai! Cek file:", OUTPUT_FILE)
    print("=" * 50)
