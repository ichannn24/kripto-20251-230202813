# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202794]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


## 2. Dasar Teori
Diffie-Hellman adalah protokol kriptografi untuk pertukaran kunci rahasia melalui saluran komunikasi publik tanpa perlu bertukar kunci secara langsung. Protokol ini memanfaatkan konsep matematika bilangan prima besar dan fungsi pangkat modular untuk menghasilkan kunci bersama yang hanya diketahui oleh kedua pihak.

Kelemahan utama Diffie-Hellman adalah rentannya terhadap serangan Man-in-the-Middle (MITM), dimana pihak ketiga dapat mencegat dan mengubah kunci publik yang dipertukarkan, sehingga pihak ketiga bisa mendapatkan kunci bersama tanpa diketahui. Pencegahan MITM dapat dilakukan menggunakan autentikasi tambahan, seperti sertifikat digital atau metode kriptografi lainnya.

## 3. Alat dan Bahan
(- Python  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
1. Membuat file diffiehellman.py di folder praktikum/week7-diffiehellman/src/.

2. Menulis kode simulasi Diffie-Hellman menggunakan bilangan prima dan generator yang disepakati.

3. Melakukan simulasi pertukaran kunci publik antara dua pihak (Alice dan Bob).

4. Menambahkan simulasi serangan Man-in-the-Middle dengan pihak ketiga (Eve) mencegat dan mengganti kunci publik.

## 5. Source Code
import random

# Parameter publik disepakati
p = 23  # bilangan prima
g = 5   # generator

# Alice memilih kunci privat a dan menghitung kunci publik A
a = random.randint(1, p-1)
A = pow(g, a, p)

# Bob memilih kunci privat b dan menghitung kunci publik B
b = random.randint(1, p-1)
B = pow(g, b, p)

# Pertukaran kunci publik dan menghitung kunci rahasia bersama
shared_key_Alice = pow(B, a, p)
shared_key_Bob = pow(A, b, p)

print(f"Kunci publik Alice: {A}")
print(f"Kunci publik Bob: {B}")
print(f"Kunci rahasia Alice: {shared_key_Alice}")
print(f"Kunci rahasia Bob: {shared_key_Bob}")

# Simulasi serangan MITM
# Eve memilih dua kunci privat dan memanipulasi pertukaran kunci publik
e1 = random.randint(1, p-1)
e2 = random.randint(1, p-1)
Eve_A = pow(g, e1, p)
Eve_B = pow(g, e2, p)

# Alice mengira Eve_A adalah kunci publik Bob
shared_key_Alice_mitm = pow(Eve_A, a, p)
# Bob mengira Eve_B adalah kunci publik Alice
shared_key_Bob_mitm = pow(Eve_B, b, p)
# Eve mengetahui kedua kunci bersama
shared_key_Eve_to_Alice = pow(A, e1, p)
shared_key_Eve_to_Bob = pow(B, e2, p)

print("\nSimulasi Serangan Man-in-the-Middle (MITM)")
print(f"Kunci rahasia Alice (MITM): {shared_key_Alice_mitm}")
print(f"Kunci rahasia Bob (MITM): {shared_key_Bob_mitm}")
print(f"Kunci rahasia Eve dengan Alice: {shared_key_Eve_to_Alice}")
print(f"Kunci rahasia Eve dengan Bob: {shared_key_Eve_to_Bob}")


## 6. Hasil dan Pembahasan
1. Simulasi Diffie-Hellman berhasil menghasilkan kunci rahasia bersama yang sama antara Alice dan Bob, yang menunjukkan bahwa algoritma bekerja sesuai teori.

2. Pada simulasi serangan Man-in-the-Middle, Alice dan Bob memiliki kunci rahasia berbeda karena kunci publik yang dipertukarkan telah dimanipulasi, sementara Eve berhasil mendapatkan kunci rahasia dari kedua pihak.

3. Hasil simulasi mengindikasikan bahwa protokol Diffie-Hellman tanpa autentikasi rentan terhadap serangan MITM.

4. Tidak ada error pada saat eksekusi program. Screenshot hasil simulasi disimpan di folder screenshots/.
## 7. Jawaban Pertanyaan
1. Diffie-Hellman memungkinkan pertukaran kunci di saluran publik karena menggunakan operasi pangkat modular dengan bilangan prima besar yang sulit untuk dikalkulasi balik (logaritma diskrit), sehingga kunci privat tidak terlihat meskipun kunci publik dipertukarkan.

2. Kelemahan utama protokol Diffie-Hellman adalah rentan terhadap serangan Man-in-the-Middle, di mana pihak ketiga dapat mencegat dan mengganti kunci publik yang dipertukarkan.

3. Pencegahan serangan MITM dapat dilakukan dengan menambahkan autentikasi kunci publik, seperti sertifikat digital atau penggunaan protokol tambahan yang memastikan identitas pihak yang berkomunikasi.
   Menjalankan program dan mengambil screenshot hasilnya di folder screenshots : https://github.com/ichannn24/kripto-20251-230202813/blob/8a14d41ce0b5a2b14a140c64d6220382e77f690f/praktikum/week7-diffie-hellman/Screenshot%202025-11-13%20230110.png

## 8. Kesimpulan
Simulasi protokol Diffie-Hellman berhasil memperlihatkan mekanisme pertukaran kunci rahasia di saluran publik dan menunjukkan kerentanan terhadap serangan Man-in-the-Middle tanpa autentikasi tambahan. Untuk keamanan optimal, protokol ini harus diintegrasikan dengan mekanisme autentikasi.
## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit abc78901  
Author: Kingkin Kurnia Candrawati <email>  
Date:   2025-11-13  

    Implementasi simulasi Diffie-Hellman lengkap dengan serangan MITM dan laporan.
