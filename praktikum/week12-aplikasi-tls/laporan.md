# Laporan Praktikum Kriptografi
Minggu ke-: 12 
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  

---

## 1. Tujuan
Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
Menjelaskan enkripsi dalam transaksi e-commerce.
Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

## 2. Dasar Teori
TLS (Transport Layer Security) merupakan protokol keamanan jaringan yang melindungi komunikasi data antara dua pihak, biasanya antara browser dan server web. TLS adalah penerus SSL (Secure Sockets Layer) dan menyediakan tiga lapisan keamanan utama:

Confidentiality (Kerahasiaan): data dienkripsi agar tidak bisa dibaca oleh pihak ketiga.

Integrity (Integritas): data tidak dapat diubah selama transmisi tanpa terdeteksi.

Authentication (Autentikasi): memastikan pihak yang berkomunikasi benar (bukan penipu).

TLS bekerja dengan mekanisme handshake, di mana klien dan server bertukar sertifikat digital, menentukan algoritma enkripsi (RSA, AES, SHA, ECDHE), dan menghasilkan session key simetris yang digunakan selama sesi komunikasi. Sertifikat digital dikeluarkan oleh Certificate Authority (CA) yang dipercaya publik.

Dalam konteks e-commerce, TLS digunakan untuk mengamankan transaksi seperti login pengguna, pengiriman data kartu kredit, dan proses pembayaran. Tanpa TLS, data sensitif dapat disadap oleh penyerang melalui teknik seperti Man-in-the-Middle attack. Selain itu, kriptografi juga digunakan pada sistem email (PGP, S/MIME) untuk menjaga privasi pesan.

## 3. Alat dan Bahan
- Python  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  


## 4. Langkah Percobaan
1. Membuat folder proyek :
   praktikum/week12-aplikasi-tls/
├─ screenshots/
└─ laporan.md

2. Mengunjungi beberapa situs e-commerce melalui browser, contoh:

https://www.tokopedia.com

3. Membuka informasi sertifikat digital dengan klik ikon gembok → Connection is secure → Certificate.
Catat:

Issuer (CA)

Masa berlaku

Algoritma enkripsi (RSA/AES)

4. Bandingkan situs dengan HTTPS dan tanpa HTTPS (jika ada).

5. Analisis bagaimana TLS digunakan saat login/pembayaran di e-commerce.

6. Buat analisis isu privasi dan etika, misalnya hak privasi pengguna vs kebutuhan pengawasan pemerintah.

7. Simpan screenshot sertifikat TLS pada folder screenshots/.

8. Commit hasilnya dengan pesan week12-aplikasi-tls.

## 5. Source Code
import ssl
import socket
from pprint import pprint

def get_certificate_info(host, port=443):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    conn.connect((host, port))
    cert = conn.getpeercert()
    conn.close()
    return cert

if __name__ == "__main__":
    host = "www.tokopedia.com"
    cert_info = get_certificate_info(host)
    print(f"Informasi Sertifikat TLS untuk {host}:")
    pprint(cert_info)

## 6. Hasil dan Pembahasan
a. Hasil Observasi Sertifikat
| Website   | Issuer CA             | Masa Berlaku | Algoritma Enkripsi        | Hasil Observasi                |
| --------- | --------------------- | ------------ | ------------------------- | ------------------------------ |
| Tokopedia | Google Trust Services | 2025–2026    | RSA 2048-bit, AES_128_GCM | Koneksi aman, sertifikat valid |
| Shopee    | DigiCert Inc          | 2025–2026    | RSA 2048-bit, AES_256_GCM | HTTPS aktif, enkripsi kuat     |

b. Analisis

Semua situs e-commerce besar menggunakan HTTPS (TLS) untuk melindungi komunikasi antara pengguna dan server.

Sertifikat diterbitkan oleh CA tepercaya (Google Trust Services, DigiCert).

Algoritma enkripsi modern digunakan, seperti RSA untuk pertukaran kunci dan AES-GCM untuk enkripsi simetris.

Situs tanpa HTTPS menampilkan peringatan “Not Secure” dan data dapat disadap melalui packet sniffing.

c. Error / Kendala

Saat menjalankan script Python, beberapa domain menolak koneksi langsung karena SNI (Server Name Indication) atau firewall restriction. Solusi: gunakan library requests dengan parameter verify=True atau gunakan openssl s_client untuk observasi manual.

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara HTTP dan HTTPS?
HTTP mentransfer data tanpa enkripsi, sehingga bisa disadap atau diubah pihak ketiga. HTTPS menggunakan protokol TLS untuk mengenkripsi data, menjamin keamanan dan integritas komunikasi antara klien dan server.

2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
Sertifikat digital memastikan autentikasi identitas server (dan kadang klien). Dengan sertifikat dari CA tepercaya, pengguna dapat yakin bahwa mereka berkomunikasi dengan situs asli, bukan situs palsu (phishing).

3. Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi menimbulkan tantangan hukum dan etika?
Kriptografi menjaga privasi dengan mencegah penyadapan, tetapi juga dapat menyulitkan otoritas hukum dalam memantau aktivitas kriminal. Dilema muncul antara hak atas privasi individu dan kebutuhan keamanan publik.

## 8. Kesimpulan
TLS merupakan komponen penting dalam keamanan e-commerce karena menyediakan enkripsi, autentikasi, dan integritas data. Penggunaan TLS menjamin transaksi online berjalan aman. Namun, penerapan kriptografi juga menimbulkan tantangan etika dan hukum, terutama terkait privasi dan pengawasan.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

Katz, J., & Lindell, Y. (2015). Introduction to Modern Cryptography. CRC Press.

Dokumentasi resmi Mozilla: How TLS Works.

Modul Praktikum Kriptografi Minggu ke-12 – Aplikasi TLS & E-commerce.

## 10. Commit Log
commit c8a29e47e5d1b9f3bce73a81f04a6a2d6c78afc4
Author: Kingkin Kurnia Candrawati <kurniachandra2404@gmail.com>
Date:   2026-01-22 14:20:55 +0700

    week12-aplikasi-tls: analisis sertifikat TLS dan e-commerce, tambah laporan.md & screenshots
