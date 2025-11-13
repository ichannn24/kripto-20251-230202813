# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: [Cipher Modern (DES, AES, RSA)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Mengimplementasikan algoritma DES untuk blok data sederhana.
Menerapkan algoritma AES dengan panjang kunci 128 bit.
Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

## 2. Dasar Teori
Cipher modern adalah algoritma kriptografi yang menggunakan teknik enkripsi blok dan kunci yang lebih kompleks untuk menjamin keamanan data yang jauh lebih tinggi dibanding cipher klasik. DES (Data Encryption Standard) adalah algoritma blok simetris dengan panjang kunci 56 bit yang lebih dulu populer, namun kini dianggap kurang aman karena panjang kunci yang pendek.

AES (Advanced Encryption Standard) menggantikan DES dengan menggunakan panjang kunci 128 bit, 192 bit, atau 256 bit, memberikan keamanan yang jauh lebih kuat dengan efisiensi enkripsi/dekripsi yang lebih tinggi. Algoritma ini menggunakan beberapa putaran substitusi dan transposisi yang kompleks.

RSA adalah algoritma kriptografi asimetris yang menggunakan pasangan kunci publik dan privat. Proses pembangkitan kunci melibatkan pemilihan dua bilangan prima besar, perhitungan modulus, fungsi totien Euler, dan penentuan eksponen publik dan privat. RSA memungkinkan enkripsi dan tanda tangan digital yang aman dan telah banyak digunakan dalam protokol keamanan modern.

## 3. Alat dan Bahan
(- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  


## 4. Langkah Percobaan
1. Membuat file des_cipher.py di folder praktikum/week6-cipher-modern/src/.

2. Mengimplementasikan enkripsi dan dekripsi DES sederhana menggunakan library pycryptodome.

3. Membuat file aes_cipher.py dan menerapkan enkripsi dan dekripsi AES-128 menggunakan mode EAX.

4. Membuat file rsa_cipher.py dan mengimplementasikan pembangkitan kunci RSA, enkripsi dan dekripsi pesan.

## 5. Source Code
# DES (opsional/simulasi)
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # 64-bit key
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b'ABCDEFGH'
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)

# AES 128-bit
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128-bit key
cipher = AES.new(key, AES.MODE_EAX)
plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())

# RSA key generation, encryption, decryption
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())




## 6. Hasil dan Pembahasan
Program DES berhasil mengenkripsi dan mendekripsi blok data 8 byte menggunakan kunci 64 bit, sesuai ekspektasi meski DES saat ini kurang aman untuk aplikasi nyata.

Implementasi AES-128 dengan mode EAX berhasil menampilkan hasil enkripsi dan dekripsi teks secara tepat.

Proses pembangkitan kunci RSA dengan panjang 2048 bit dan enkripsi-dekripsi pesan berjalan lancar, membuktikan keamanan algoritma asimetris.

Tidak ada error selama implementasi karena mengikuti prosedur dan menggunakan library pycryptodome yang sudah teruji.

Menjalankan ketiga program dan mengambil screenshot hasilnya di folder screenshots: 
https://github.com/ichannn24/kripto-20251-230202813/blob/c96517c7413b2a308a250ebc10857caca7b3d729/praktikum/week6-cipher-modern/Screenshot%202025-11-13%20224644.png
## 7. Jawaban Pertanyaan
1. Perbedaan mendasar antara DES, AES, dan RSA terletak pada jenis kunci dan keamanan; DES dan AES menggunakan kunci simetris sementara RSA memakai kunci publik dan privat (asimetris). AES lebih kuat dan efisien karena panjang kunci lebih besar dan algoritma yang lebih kompleks dibanding DES.

2. AES lebih banyak digunakan dibanding DES karena DES rentan terhadap serangan brute force akibat kunci yang pendek (56 bit), sedangkan AES menyediakan pilihan kunci hingga 256 bit untuk keamanan lebih tinggi.

3. RSA dikategorikan algoritma asimetris karena melibatkan dua kunci berbeda, publik untuk enkripsi dan privat untuk dekripsi, dengan pembangkitan kunci dari bilangan prima besar dan operasi matematika modular yang kompleks.
## 8. Kesimpulan
Implementasi cipher modern DES, AES, dan RSA menunjukkan bahwa algoritma modern menawarkan keamanan lebih baik dibanding cipher klasik dengan panjang kunci dan metode enkripsi yang lebih rumit. AES dan RSA sangat cocok untuk aplikasi keamanan saat ini, sementara DES hanya cocok untuk simulasi atau pembelajaran.

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit def67890  
Author: Kingkin Kurnia Candrawati <email>  
Date:   2025-11-13  

    Implementasi DES, AES-128, dan RSA lengkap dengan laporan dan hasil uji.


    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
