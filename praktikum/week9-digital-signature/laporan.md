# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [Digital Signature (RSA/DSA)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  



## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep tanda tangan digital serta mengimplementasikan algoritma RSA dalam pembuatan dan verifikasi tanda tangan digital. Selain itu, praktikum ini bertujuan untuk membuktikan bahwa tanda tangan digital dapat menjamin keaslian (otentikasi) dan keutuhan (integritas) suatu pesan.

## 2. Dasar Teori
Tanda tangan digital (digital signature) merupakan salah satu mekanisme kriptografi yang digunakan untuk memastikan bahwa sebuah pesan benar-benar berasal dari pengirim yang sah dan tidak mengalami perubahan selama proses pengiriman. Berbeda dengan enkripsi yang berfokus pada kerahasiaan data, tanda tangan digital berfokus pada integritas data, autentikasi pengirim, dan non-repudiation (pengirim tidak dapat menyangkal telah mengirim pesan).

Pada algoritma RSA, tanda tangan digital dibuat dengan cara melakukan proses penandatanganan menggunakan kunci privat pengirim terhadap nilai hash dari pesan. Nilai hash ini biasanya dihasilkan menggunakan fungsi hash kriptografis seperti SHA-256. Penerima kemudian dapat memverifikasi tanda tangan tersebut menggunakan kunci publik pengirim. Jika hasil verifikasi berhasil, maka pesan dinyatakan asli dan tidak dimodifikasi.

Tanda tangan digital banyak digunakan dalam sistem keamanan modern seperti sertifikat digital, transaksi elektronik, dan komunikasi aman di internet. Dalam praktiknya, keberadaan Certificate Authority (CA) berperan penting untuk menjamin keaslian kunci publik yang digunakan.

## 3. Alat dan Bahan
- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
Membuat folder praktikum/week9-digital-signature/ beserta subfolder src dan screenshots.

Menginstal library pycryptodome menggunakan perintah pip install pycryptodome.

Membuat file signature.py di dalam folder src.

Menuliskan kode program untuk generate kunci RSA dan membuat tanda tangan digital.

Menjalankan program untuk melakukan verifikasi tanda tangan menggunakan kunci publik.

Menguji kegagalan verifikasi dengan memodifikasi pesan asli.

Mengambil screenshot hasil eksekusi program.

Melakukan commit hasil praktikum ke repository GitHub.

## 5. Source Code
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan asli
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Membuat tanda tangan digital
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

# Verifikasi tanda tangan
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Uji pesan yang dimodifikasi
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")


## 6. Hasil dan Pembahasan
Berdasarkan hasil eksekusi program, tanda tangan digital berhasil dibuat menggunakan kunci privat RSA. Proses verifikasi terhadap pesan asli menunjukkan hasil berhasil, yang menandakan bahwa tanda tangan valid dan pesan tidak mengalami perubahan.
Pada pengujian kedua, pesan dimodifikasi dan dilakukan verifikasi menggunakan tanda tangan yang sama. Hasilnya, verifikasi gagal, yang membuktikan bahwa tanda tangan digital mampu mendeteksi perubahan isi pesan. Hal ini sesuai dengan teori bahwa tanda tangan digital menjamin integritas dan keaslian pesan.
https://github.com/ichannn24/kripto-20251-230202813/blob/b3907b20f5ffcc46886a38ecc37084257012a4de/praktikum/week9-digital-signature/src/Screenshot%202025-12-14%20232549.png

## 7. Jawaban Pertanyaan
Pertanyaan 1: Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
Enkripsi RSA digunakan untuk menjaga kerahasiaan pesan, sedangkan tanda tangan digital RSA digunakan untuk menjamin keaslian, integritas, dan non-repudiation pesan.
Pertanyaan 2: Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
Karena tanda tangan dibuat dari hash pesan menggunakan kunci privat pengirim, sehingga setiap perubahan pada pesan akan menyebabkan verifikasi gagal.
Pertanyaan 3: Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital?
CA berperan sebagai pihak tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital agar kunci publik tersebut dapat dipercaya.

## 8. Kesimpulan
Dari praktikum ini dapat disimpulkan bahwa tanda tangan digital menggunakan RSA dapat menjamin keaslian dan keutuhan pesan. Proses verifikasi berhasil pada pesan asli dan gagal pada pesan yang dimodifikasi. Hal ini membuktikan efektivitas tanda tangan digital dalam sistem keamanan informasi.
## 9. Daftar Pustaka
•	Katz, J., & Lindell, Y. Introduction to Modern Cryptography.

•	Stallings, W. Cryptography and Network Security.

•	Stinson, D. (2019). Cryptography: Theory and Practice.


## 10. Commit Log
commit a1b2c3d4
Author: Kingkin Kurnia Candrawati <kurniachandra2404@gmail.com>
Date:   2025-11-XX

    week9-digital-signature
