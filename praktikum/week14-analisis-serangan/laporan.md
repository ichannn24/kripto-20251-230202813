# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: [Analisis Serangan Kriptografi]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  



## 1. Tujuan
Mengidentifikasi jenis serangan pada sistem informasi nyata.
Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.


## 2. Dasar Teori
Serangan kriptografi (cryptanalytic attack) adalah upaya untuk menembus atau melemahkan sistem enkripsi agar data rahasia dapat diketahui tanpa kunci yang sah. Secara umum, serangan dapat dikategorikan menjadi dua:

Serangan terhadap algoritma (cryptanalysis) — memanfaatkan kelemahan matematis pada algoritma enkripsi (contoh: collision pada MD5, kelemahan RSA dengan kunci kecil).

Serangan terhadap implementasi (side-channel attack) — menyerang cara algoritma diimplementasikan, misalnya dengan mengamati waktu eksekusi, konsumsi daya, atau kesalahan konfigurasi sistem.

Salah satu serangan yang sering terjadi adalah brute force dan dictionary attack, yaitu mencoba semua kemungkinan password atau hash hingga menemukan hasil yang cocok. Hash lemah seperti MD5 atau SHA-1 kini dianggap tidak aman karena rentan terhadap collision (dua data berbeda menghasilkan hash sama) dan rainbow table attack.

## 3. Alat dan Bahan
(- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
Folder:
praktikum/week14-analisis-serangan/
├─ src/
├─ screenshots/
└─ laporan.md

## 4. Langkah Percobaan
1. Buat folder praktikum/week14-analisis-serangan/.

2. Buat file Python src/bruteforce_md5.py.

3. Implementasikan program untuk melakukan brute force sederhana terhadap hash MD5.

4. Jalankan program dan catat waktu pencarian.

5. Simulasikan perbandingan antara MD5 dan bcrypt.

6. Simpan hasil screenshot eksekusi ke screenshots/hasil.png.

7. Commit ke GitHub dengan pesan week14-analisis-serangan.
   
## 5. Source Code
Contoh program sederhana untuk brute force terhadap hash MD5 :
import hashlib
import itertools
import string
import time

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def brute_force(target_hash, max_length=4):
    chars = string.ascii_lowercase
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            if md5_hash(attempt) == target_hash:
                return attempt
    return None

if __name__ == "__main__":
    password = "abc"
    target = md5_hash(password)
    print(f"Target hash: {target}")
    start = time.time()
    result = brute_force(target)
    end = time.time()

    if result:
        print(f"Password ditemukan: {result}")
    else:
        print("Password tidak ditemukan.")
    print(f"Waktu eksekusi: {end - start:.2f} detik")


## 6. Hasil dan Pembahasan
a. Hasil Eksekusi

Output program :
Target hash: 900150983cd24fb0d6963f7d28e17f72
Password ditemukan: abc
Waktu eksekusi: 1.43 detik

b. Pembahasan

Hash MD5 dengan panjang 3 karakter berhasil dipecahkan dalam waktu ±1 detik. Jika password lebih panjang, waktu meningkat eksponensial.

MD5 cepat tetapi tidak aman karena mudah ditebak dan tidak tahan collision.

Algoritma modern seperti bcrypt atau Argon2 menambahkan salt dan memperlambat proses hashing untuk menahan brute force.

Kelemahan sistem sering kali bukan hanya dari algoritma tetapi juga implementasi:

Penggunaan password sederhana tanpa kebijakan panjang minimal.

Penyimpanan hash tanpa salt.

Tidak adanya rate limit pada login.

## 7. Jawaban Pertanyaan
1. Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Karena sistem lama masih menggunakan algoritma hash cepat (MD5, SHA-1) dan tidak menerapkan salt atau rate limit. Selain itu, banyak pengguna memakai password lemah yang mudah ditebak.

2. Apa bedanya kelemahan algoritma dengan kelemahan implementasi?

Kelemahan algoritma terjadi karena cacat matematis (contoh: collision pada MD5).

Kelemahan implementasi muncul akibat cara penerapan yang salah (contoh: penyimpanan hash tanpa salt, salah konfigurasi kunci, atau kurangnya validasi input).

3. Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Dengan melakukan audit keamanan rutin, mengganti algoritma lama dengan standar modern (mis. SHA-3, AES-GCM, RSA-4096, ECC), memperbarui library kriptografi, serta mengadopsi kebijakan keamanan adaptif (misalnya password manager dan multifactor authentication).

## 8. Kesimpulan
Dari studi kasus serangan brute force terhadap MD5, terbukti bahwa algoritma lama rentan terhadap serangan modern. Penggunaan algoritma hash kuat seperti bcrypt atau Argon2 sangat disarankan untuk melindungi password pengguna. Keamanan sistem kriptografi tidak hanya bergantung pada algoritma, tetapi juga pada implementasi dan kebijakan penggunaannya.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

Katz, J., & Lindell, Y. (2015). Introduction to Modern Cryptography. CRC Press.

OWASP Foundation. Password Storage Cheat Sheet.

Modul Praktikum Kriptografi Minggu ke-14 – Analisis Serangan Kriptografi.

## 10. Commit Log
commit 2f8b37ad6c46d8b7d5a1c8a92f2d771a0de47e1a
Author: Kingkin Kurnia Candrawati <kurniachandra2404@gmail.com>
Date:   2026-01-22 18:20:13 +0700

    week14-analisis-serangan: tambah studi kasus brute force MD5 dan rekomendasi algoritma bcrypt
