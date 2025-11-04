# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: [Modular Arithmetic ]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5IKRA]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu menyelesaikan operasi aritmetika modular, menentukan bilangan prima dan menghitung Greatest Common Divisor (GCD), serta menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )
Aritmetika modular adalah cabang matematika yang mempelajari hitungan sisa pembagian suatu bilangan dengan bilangan bulat positif (modulus). Dalam kriptografi, operasi modular sangat penting karena membantu membuat sistem yang aman seperti RSA dan Diffie-Hellman. Konsep penting dalam aritmetika modular antara lain penjumlahan, pengurangan, perkalian, eksponensiasi, invers modular, serta algoritma Euclidean untuk menghitung GCD.
GCD (Greatest Common Divisor) adalah bilangan bulat terbesar yang dapat membagi dua bilangan lain tanpa menyisakan sisa. Algoritma Euclidean efisien digunakan untuk mencari GCD dengan prinsip pengurangan berulang. Selain itu, invers modular digunakan dalam algoritma kunci publik, yaitu bilangan yang menghasilkan hasil kali 1 modulo n. Logaritma diskrit adalah invers dari operasi eksponensial dalam modular, yang sulit diselesaikan pada modulus besar dan menjadi dasar kekuatan keamanan beberapa algoritma kriptografi.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)
4. Menambahkan fungsi Extended Euclidean untuk mencari invers modular.
5. Membuat fungsi untuk logaritma diskrit sederhana.
6. Menjalankan program dan menguji fungsi-fungsi dengan contoh kasus.
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
def modadd(a, b, n):
    return (a + b) % n

def modsub(a, b, n):
    return (a - b) % n

def modmul(a, b, n):
    return (a * b) % n

def modexp(base, exp, n):
    return pow(base, exp, n)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    else:
        return x % n

def discretelog(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

# Contoh pengujian
print("7 + 5 mod 12 =", modadd(7, 5, 12))
print("7 * 5 mod 12 =", modmul(7, 5, 12))
print("7^128 mod 13 =", modexp(7, 128, 13))
print("GCD of 54 and 24 =", gcd(54, 24))
print("Inverse of 3 mod 11 =", modinv(3, 11))
print("Discrete log of 4 base 3 mod 7 =", discretelog(3, 4, 7))

```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
