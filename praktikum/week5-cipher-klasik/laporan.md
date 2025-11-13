# Laporan Praktikum Kriptografi
Minggu ke-: 5 
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik.
## 2. Dasar Teori
Cipher klasik adalah metode enkripsi yang menggunakan teknik substitusi dan transposisi untuk mengamankan pesan teks. Contohnya adalah Caesar Cipher yang menggantikan setiap huruf dengan huruf lain yang terletak beberapa posisi tertentu dalam alfabet, dan Vigenère Cipher yang menggunakan kunci berupa kata untuk menghasilkan variasi substitusi yang lebih kompleks. Transposisi cipher mengacak posisi huruf-huruf dalam pesan berdasarkan suatu kunci, bukan mengganti hurufnya.

Konsep penting dalam cipher klasik adalah aritmetika modular, yang memungkinkan pergeseran posisi huruf dalam alfabet secara melingkar (misalnya mod 26 untuk alfabet Inggris). Kelemahan utama cipher klasik termasuk ketahanan rendah terhadap analisis frekuensi dan serangan brute force sederhana karena ruang kunci yang terbatas.
cipher clasik terdapat 3 jenis  yaitu : caesar cioher, vignere cipher, dan transposition cipher.

## 3. Alat dan Bahan
(- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
1. Membuat file caesar_cipher.py di folder praktikum/week5-cipher-klasik/src/.

2. Menyalin dan mengimplementasikan kode Caesar Cipher dari panduan praktikum.

3. Membuat file vigenere_cipher.py dan mengimplementasikan algoritma Vigenère Cipher dengan variasi kunci.

4. Membuat file transposition_cipher.py dan menerapkan algoritma transposisi sederhana.

5. Menjalankan program dengan perintah python <nama_file>.py dan mengamati hasil enkripsi dan dekripsi.

6. Mengambil screenshot hasil output program sebagai bukti percobaan.

## 5. Source Code
# Caesar Cipher
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Vigenere Cipher
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)

# Transposition Cipher
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = key
    num_of_rows = len(ciphertext) // num_of_cols
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_rows
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if (row == num_of_rows) or (row == num_of_rows - 1 and col >= num_of_cols - num_of_shaded_boxes):
            row = 0
            col += 1
    return ''.join(plaintext)

## 6. Hasil dan Pembahasan
1. Hasil eksekusi program Caesar Cipher menunjukkan bahwa pesan teks berhasil dienkripsi dan didekripsi sesuai dengan kunci yang diberikan.

2. Program Vigenère Cipher juga berhasil memproses teks dengan variasi kunci, menampilkan hasil yang benar saat dekripsi.

3. Algoritma transposisi sederhana berhasil mengacak dan mengembalikan pesan ke bentuk aslinya.

4. Tidak ditemukan error selama percobaan karena implementasi mengikuti teori yang tepat.

Berikut contoh screenshot hasil uji coba di folder screenshots :
https://github.com/ichannn24/kripto-20251-230202813/blob/c90f33a5ee732b85e24d5ce43b70aafbd4e80942/praktikum/week5-cipher-klasik/Screenshot%202025-11-13%20223307.png

## 7. Jawaban Pertanyaan
1. Kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher adalah mudahnya metode ini diserang menggunakan analisis frekuensi dan space key yang relatif kecil sehingga rentan terhadap serangan brute force.

2. Cipher klasik mudah diserang dengan analisis frekuensi karena karakteristik frekuensi huruf dalam bahasa asli masih bisa dikenali setelah enkripsi pada substitusi sederhana.

3. Cipher substitusi mengubah huruf secara langsung sehingga lebih rentan terhadap analisis frekuensi, sedangkan transposisi mengacak posisi huruf sehingga menyembunyikan pola frekuensi lebih baik, tetapi keduanya dapat dipecahkan dengan teknik kriptanalisis modern.
## 8. Kesimpulan
Algoritma cipher klasik seperti Caesar dan Vigenère relatif sederhana dan mudah diimplementasikan. Namun, mereka memiliki kelemahan keamanan karena mudah dipecahkan dengan analisis frekuensi dan teknik dekripsi brute force. Transposisi memperbaiki beberapa kelemahan dengan mengacak posisi huruf, namun masih tidak cukup kuat untuk penggunaan modern.

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit abc12345  
Author: Kingkin Kurnia Candrawati <email>  
Date:   2025-11-13  

    Implementasi dasar cipher klasik Caesar, Vigenère, dan Transposisi lengkap dengan laporan dan hasil uji.


  
