# Laporan Praktikum Kriptografi
Minggu ke-: 1 
Topik: [judul praktikum]  
Nama: [Kingkin Kurnia Candrawati ]  
NIM: [230202813]  
Kelas: [5Ikra]  

---

## 1. Tujuan
(Pembelajaran praktikum bertujuan untuk memahami dasar teori dan menerapkan algoritma kriptografi klasik serta modern melalui pembuatan kode enkripsi dan dekripsi. Praktikum ini juga bertujuan meningkatkan kemampuan analisis dan implementasi algoritma kriptografi dalam pengamanan pesan.)

---

## 2. Dasar Teori
(Kriptografi adalah ilmu dan seni untuk menjaga kerahasiaan pesan melalui pengkodean agar hanya pihak berhak yang dapat membacanya. Teknik dasar kriptografi meliputi cipher klasik seperti Caesar cipher, yang menggunakan pergeseran huruf, serta prinsip modular aritmetika yang mendukung algoritma enkripsi modern seperti RSA dan AES. Prinsip utama dalam kriptografi meliputi kerahasiaan, integritas, dan autentikasi, yang menjadi landasan dalam membangun sistem keamanan informasi.)

---

## 3. Alat dan Bahan
(Python 3.x

Visual Studio Code atau editor lain

Git dan akun GitHub)

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result
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
(Praktikum ini memberikan pemahaman dasar tentang bagaimana algoritma cipher bekerja dan pentingnya keamanan dalam komunikasi digital. Penggunaan kode sederhana dapat membantu memahami prinsip-prinsip kerahasiaan dan integritas pesan.)

---

## 9. Daftar Pustaka
(Stallings, W. Cryptography and Network Security (2017)

Schneier, B. Applied Cryptography (1996)

Katz & Lindell. Introduction to Modern Cryptography (2014))

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
