# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [2302028113]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

## 2. Dasar Teori
Shamir Secret Sharing adalah suatu skema pembagian rahasia berbasis polinomial yang diperkenalkan oleh Adi Shamir pada 1979. Ide utamanya: sebuah rahasia direpresentasikan sebagai konstanta (a₀) dari sebuah polinomial acak berderajat k−1 pada medan prima p. Selanjutnya share dibentuk sebagai pasangan (x, f(x)) untuk nilai x berbeda (x ≠ 0). Dengan sifat polinomial, diperlukan minimal k titik berbeda untuk merekonstruksi polinomial (dan karenanya a₀) melalui interpolasi Lagrange; sementara < k titik memberi informasi nol tentang a₀ (secara informasional sempurna) jika koefisien polinomial dipilih acak dan modulo prima besar.

Secara matematis, pilih prima p > rahasia, bangun polinomial f(x) = a₀ + a₁x + … + a_{k−1} x^{k−1} (koefisien acak modulo p). Untuk n partisipan, buat n share (x_i, y_i = f(x_i) mod p) dengan x_i ≠ 0 dan unik. Rekonstruksi rahasia dari k share dilakukan dengan Lagrange interpolation modulo p untuk mendapatkan f(0) = a₀. Keamanan skema bergantung pada threshold k: semakin besar k, semakin kuat resistensi terhadap kolusi tetapi juga menambah beban koordinasi; sebaliknya k kecil mempermudah rekonstruksi tetapi mengurangi toleransi terhadap pengungkapan sebagian share.

## 3. Alat dan Bahan  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  


## 4. Langkah Percobaan
1. Buat struktur folder :
   praktikum/week11-secret-sharing/
├─ src/
├─ screenshots/
└─ laporan.md

2. Buat file src/secret_sharing.py berisi implementasi Shamir (contoh disertakan di bagian Source Code).

3. Jalankan skrip untuk membagi rahasia menjadi n shares dengan threshold k dan tunjukkan rekonstruksi dari kombinasi k shares.

4. Ambil screenshot hasil eksekusi: keluaran shares, rekonstruksi sukses, serta contoh rekonstruksi gagal jika < k shares digunakan. Simpan di screenshots/.

5. Commit perubahan dengan pesan week11-secret-sharing.

## 5. Source Code


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
