# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Caesar chiper]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5IKRA]  

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
Mempelajari dasar-dasar kriptografi, terutama konsep enkripsi dan dekripsi untuk menjaga keamanan pesan agar hanya dapat dipahami oleh pihak yang berhak.
---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )
Kriptografi adalah ilmu dan seni untuk menjaga keamanan pesan dengan cara pengkodean (cipher). Salah satu metode kriptografi klasik adalah Caesar Cipher, yaitu teknik enkripsi sederhana dengan pergeseran huruf dalam alfabet.
Modular aritmetika digunakan untuk menjaga pergeseran huruf tetap dalam rentang alfabet, sehingga pergeseran lebih dari jumlah huruf tetap "melingkar" kembali ke awal alfabet. Prinsip dasar kriptografi meliputi kerahasiaan (confidentiality), integritas, dan autentikasi pesan.
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
4. Memasukkan teks dan kunci pergeseran sesuai instruksi.
5. Mengamati hasil enkripsi dan dekripsi.
---

## 5. Source Code
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

if __name__ == "__main__":
    text = input("Masukkan teks: ")
    key = int(input("Masukkan kunci geser: "))
    encrypted = encrypt(text, key)
    print("Hasil Enkripsi:", encrypted)
    decrypted = decrypt(encrypted, key)
    print("Hasil Dekripsi:", decrypted)

)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Program berhasil mengenkripsi teks dengan pergeseran yang diberikan dan dapat mendekripsi kembali ke teks asli.
- Tidak ditemukan error selama eksekusi.
- Modular aritmetika memastikan pergeseran huruf tetap dalam batas alfabet sehingga program berfungsi dengan semestinya.
- Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Apa definisi dasar dari Caesar Cipher?
Jawaban: Teknik menggeser huruf dalam teks asli sebanyak k posisi untuk membuat teks terenkripsi.

- Pertanyaan 2:   
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )
Praktikum ini berhasil mengimplementasikan Caesar Cipher dengan baik. 
Enkripsi dan dekripsi berjalan sesuai teori menggunakan modular aritmetika untuk menjaga keutuhan hasil.


---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. Introduction to Modern Cryptography.
- Stallings, W. Cryptography and Network Security.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  

```
    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
Commit awal: Menambahkan file caesar_cipher.py dengan fungsi enkripsi dan dekripsi.

Commit perbaikan: Memperbaiki logika modular shift.

Commit final: Menambahkan input/output user dan dokumentasi.
```
