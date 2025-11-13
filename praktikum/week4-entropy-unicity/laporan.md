# Laporan Praktikum Kriptografi
Minggu ke-: 4 
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menyelesaikan perhitungan sederhana terkait entropi kunci.
Menggunakan teorema Euler pada contoh perhitungan modular & invers.
Menghitung unicity distance untuk ciphertext tertentu.
Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

## 2. Dasar Teori
Entropi dalam konteks kriptografi adalah ukuran ketidakpastian atau tingkat acak dari suatu sistem kunci. Semakin besar entropi suatu kunci, semakin sulit bagi penyerang untuk menebaknya. Entropi dihitung menggunakan rumus:  H(K)=log2​∣K∣
dengan ∣K∣ menyatakan jumlah kemungkinan kunci.
Sedangkan unicity distance adalah panjang minimum ciphertext yang dibutuhkan agar penyerang dapat secara unik menentukan kunci yang benar. Nilainya dihitung dengan:
U= H(K)/R⋅log2 ∣A∣	​
di mana R adalah redundansi bahasa dan ∣A∣ adalah ukuran alfabet.
## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
import math

# Fungsi menghitung entropi
def entropy(keyspace_size):
    return math.log2(keyspace_size)

# Fungsi menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

# Fungsi estimasi waktu brute force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

# Perhitungan utama
HK_caesar = entropy(26)
HK_AES128 = entropy(2**128)

print("Entropy ruang kunci Caesar Cipher =", HK_caesar, "bit")
print("Entropy ruang kunci AES-128 =", HK_AES128, "bit")

print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK_caesar))

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")

## 6. Hasil dan Pembahasan
Entropy ruang kunci Caesar Cipher = 4.700439718141093 bit
Entropy ruang kunci AES-128 = 128.0 bit
Unicity Distance untuk Caesar Cipher = 0.3
Waktu brute force Caesar Cipher (26 kunci) = 0.0000003 hari
Waktu brute force AES-128 = 1.078e+30 hari

hasil run vscode : https://github.com/ichannn24/kripto-20251-230202813/blob/84efe9ef1573dcdb2c7b97f63882a6095a70e50e/praktikum/week4-entropy-unicity/Screenshot%202025-11-13%20221705.png
## 7. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?
Entropi menunjukkan tingkat ketidakpastian atau keacakan suatu kunci. Semakin tinggi entropi, semakin sulit bagi penyerang untuk menebak kunci dengan benar.

2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
Karena unicity distance menunjukkan seberapa panjang ciphertext yang diperlukan agar hanya ada satu kunci yang mungkin benar. Jika nilainya kecil, cipher mudah dipecahkan.

3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
Karena brute force tidak tergantung pada kelemahan algoritma, tetapi pada kekuatan komputasi. Jika teknologi meningkat, serangan brute force menjadi semakin cepat dan berpotensi mengancam sistem yang dahulu aman.
## 8. Kesimpulan
Dari percobaan ini, dapat disimpulkan bahwa entropi dan unicity distance berperan penting dalam menilai kekuatan kriptosistem. Algoritma dengan entropi tinggi dan unicity distance besar seperti AES jauh lebih aman dari serangan brute force dibanding cipher klasik seperti Caesar Cipher.

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit a7b93c2
Author: Kingkin Kurnia Candrawati <kingkin.kurnia@univxyz.ac.id>
Date:   2025-11-13

    week4-entropy-unicity: tambah perhitungan entropi, unicity distance, dan brute force

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
