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
# src/secret_sharing.py
"""
Implementasi sederhana Shamir Secret Sharing (mandiri).
Mode:
 - fungsi split_secret(secret_int, k, n, prime) -> list of (x, y)
 - fungsi reconstruct_secret(shares, prime) -> secret_int
Contoh penggunaan ada di __main__.
"""

import random
from typing import List, Tuple

# --------------------------
# Util: operasi modulo
# --------------------------
def _egcd(a: int, b: int):
    if a == 0:
        return (b, 0, 1)
    g, y, x = _egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a: int, p: int) -> int:
    """Modular inverse a^{-1} mod p (p prime assumed and a % p != 0)."""
    g, x, _ = _egcd(a % p, p)
    if g != 1:
        raise ValueError("Inverse tidak ada")
    return x % p

# --------------------------
# Lagrange interpolation
# --------------------------
def lagrange_interpolate_at_zero(points: List[Tuple[int,int]], p: int) -> int:
    """
    Menghasilkan f(0) dari titik (x_i, y_i) modulo p menggunakan
    interpolasi Lagrange.
    points: list of (x, y), semua x unik dan non-zero idealnya
    """
    total = 0
    k = len(points)
    for i in range(k):
        xi, yi = points[i]
        num = 1
        den = 1
        for j in range(k):
            if i == j:
                continue
            xj, _ = points[j]
            num = (num * (-xj)) % p         # karena evaluasi di x=0, faktor (0 - xj)
            den = (den * (xi - xj)) % p
        inv_den = modinv(den, p)
        term = yi * num * inv_den
        total = (total + term) % p
    return total

# --------------------------
# Polinomial random
# --------------------------
def _eval_polynomial(coeffs: List[int], x: int, p: int) -> int:
    result = 0
    pow_x = 1
    for c in coeffs:
        result = (result + c * pow_x) % p
        pow_x = (pow_x * x) % p
    return result

def split_secret(secret_int: int, k: int, n: int, p: int) -> List[Tuple[int,int]]:
    """
    Membagi secret_int menjadi n shares dengan threshold k modulo p.
    Returns list of (x, y).
    """
    if not (1 <= k <= n):
        raise ValueError("Threshold k harus 1 <= k <= n")
    if secret_int >= p:
        raise ValueError("Secret harus < p")
    # buat koefisien acak a1..a_{k-1}, a0 = secret
    coeffs = [secret_int] + [random.randrange(0, p) for _ in range(k-1)]
    shares = []
    for i in range(1, n+1):
        x = i
        y = _eval_polynomial(coeffs, x, p)
        shares.append((x, y))
    return shares

def reconstruct_secret(shares: List[Tuple[int,int]], p: int) -> int:
    if len(shares) == 0:
        raise ValueError("Butuh minimal 1 share")
    return lagrange_interpolate_at_zero(shares, p)

# --------------------------
# Contoh penggunaan
# --------------------------
if __name__ == "__main__":
    # Contoh: rahasia adalah angka (mis. hasil konversi teks ke int)
    # Pilih prime p > max(secret, n)
    secret_text = "KriptografiUPB2025"
    # Konversi sederhana: representasikan sebagai integer melalui hex
    secret_int = int(secret_text.encode().hex(), 16)

    # pilih prime p lebih besar dari secret_int
    # untuk tujuan eksperimen, kita cari prime kecil yang cukup (bukan produksi)
    # di praktik nyata gunakan prime besar (mis. 2048-bit) sesuai kebutuhan.
    # Di sini, agar p > secret_int, kita ambil p = next_prime(secret_int*2 + 1)
    # Untuk kesederhanaan we'll set p = secret_int * 2 + 1 (asumsi prima kadang tidak benar),
    # tapi untuk eksperimen lokal, jika p tidak prima mod inverse masih dapat gagal.
    # Sebagai pendekatan aman: gunakan p sebagai bilangan prima yang diketahui lebih besar.
    # Untuk demo ini, kita pilih p melalui loop mencari prima kecil (sederhana).
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n and i < 10000:  # batas sederhana
            if n % i == 0:
                return False
            i += 2
        return True

    p_candidate = secret_int * 2 + 1
    while not is_prime(p_candidate):
        p_candidate += 2
    p = p_candidate

    print("Secret (text):", secret_text)
    print("Secret (int):", secret_int)
    print("Prime p chosen:", p)

    k = 3   # threshold
    n = 5   # jumlah shares
    shares = split_secret(secret_int, k, n, p)
    print("\nGenerated shares (x, y):")
    for s in shares:
        print(s)

    # Rekonstruksi menggunakan 3 shares
    subset = shares[:3]
    recovered_int = reconstruct_secret(subset, p)
    # konversi balik ke teks
    recovered_hex = format(recovered_int, "x")
    # pastikan hex panjangnya genap
    if len(recovered_hex) % 2:
        recovered_hex = "0" + recovered_hex
    recovered_text = bytes.fromhex(recovered_hex).decode(errors="ignore")
    print("\nRecovered int:", recovered_int)
    print("Recovered text (approx):", recovered_text)

    # Coba rekonstruksi dengan < k shares (seharusnya gagal atau memberi nilai yang bukan rahasia)
    try:
        bad_recovery = reconstruct_secret(shares[:2], p)
        print("\nRecovered with 2 shares (should not equal secret):", bad_recovery)
    except Exception as e:
        print("Reconstruction with insufficient shares raised error:", e)


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
