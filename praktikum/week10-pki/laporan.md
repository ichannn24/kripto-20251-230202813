# Laporan Praktikum Kriptografi
Minggu ke-: 10 
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  



## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep Public Key Infrastructure (PKI) serta peran Certificate Authority (CA) dalam sistem keamanan informasi. Selain itu, praktikum ini bertujuan untuk mengimplementasikan pembuatan sertifikat digital sederhana dan memahami proses verifikasi sertifikat dalam komunikasi aman.
## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sebuah kerangka kerja yang digunakan untuk mengelola kunci publik dan sertifikat digital dalam sistem keamanan. PKI memungkinkan pengguna untuk bertukar informasi secara aman dengan memanfaatkan pasangan kunci publik dan privat yang diverifikasi melalui sertifikat digital.

Certificate Authority (CA) merupakan pihak tepercaya yang bertugas menerbitkan, memverifikasi, dan mengelola sertifikat digital. Sertifikat digital berisi identitas pemilik kunci publik dan ditandatangani oleh CA untuk menjamin keaslian identitas tersebut. Dengan adanya CA, pengguna dapat mempercayai bahwa kunci publik yang digunakan memang milik pihak yang sah.

PKI banyak digunakan dalam sistem keamanan modern seperti HTTPS dan TLS pada komunikasi internet. Melalui PKI, risiko serangan seperti Man-in-the-Middle (MITM) dapat diminimalkan karena identitas server dapat diverifikasi menggunakan sertifikat digital yang sah.

## 3. Alat dan Bahan
- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

## 4. Langkah Percobaan
Membuat folder praktikum/week10-pki/ beserta subfolder src dan screenshots.

Menginstal library cryptography dan pyopenssl menggunakan perintah pip install cryptography pyopenssl.

Membuat file pki_cert.py di dalam folder src.

Menuliskan kode program untuk generate pasangan kunci RSA.

Membuat sertifikat digital sederhana (self-signed certificate).

Menyimpan sertifikat dalam format .pem.

Menjalankan program dan memastikan sertifikat berhasil dibuat.

Mengambil screenshot hasil eksekusi program.

Melakukan commit hasil praktikum ke repository GitHub.

## 5. Source Code
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Subject dan issuer (self-signed CA)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Membuat sertifikat digital
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")


## 6. Hasil dan Pembahasan
Hasil dari praktikum ini menunjukkan bahwa sertifikat digital sederhana berhasil dibuat menggunakan library cryptography. Program berjalan tanpa error dan menghasilkan file sertifikat dengan ekstensi .pem.
Sertifikat yang dihasilkan merupakan self-signed certificate, di mana subject dan issuer berasal dari entitas yang sama. Hal ini cukup untuk keperluan pembelajaran, namun tidak direkomendasikan untuk lingkungan produksi karena tidak melibatkan CA tepercaya. Screenshot hasil eksekusi program disimpan pada folder screenshots/. 
https://github.com/ichannn24/kripto-20251-230202813/blob/8b71f24819fe83acaf539a999f88babe16214595/praktikum/week10-pki/Screenshot%202025-12-14%20235915.png


## 7. Jawaban Pertanyaan
Pertanyaan 1: Apa fungsi utama Certificate Authority (CA)?
CA berfungsi sebagai pihak tepercaya yang menerbitkan dan memverifikasi sertifikat digital untuk menjamin keaslian identitas pemilik kunci publik.
Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Karena sertifikat tersebut tidak diverifikasi oleh CA tepercaya sehingga tingkat kepercayaannya rendah dan rentan terhadap serangan keamanan.
Pertanyaan 3: Bagaimana PKI mencegah serangan MITM dalam TLS/HTTPS?
PKI memastikan identitas server melalui sertifikat digital yang diverifikasi CA, sehingga klien dapat mendeteksi sertifikat palsu dan mencegah komunikasi dengan pihak tidak sah.


## 8. Kesimpulan
Dari praktikum ini dapat disimpulkan bahwa PKI dan CA memiliki peran penting dalam menjaga keamanan komunikasi digital. Pembuatan sertifikat digital berhasil dilakukan dan menunjukkan bagaimana identitas dapat diverifikasi. PKI terbukti menjadi fondasi utama dalam sistem keamanan komunikasi modern.

## 9. Daftar Pustaka
•	Stallings, W. Cryptography and Network Security.

•	Katz, J., & Lindell, Y. Introduction to Modern Cryptography.

•	Stinson, D. Cryptography: Theory and Practice.


## 10. Commit Log
commit e5f6g7h8
Author: Kingkin Kurnia Candrawati <kurniachandra2404@gmail.com>
Date:   2025-11-XX

    week10-pki
