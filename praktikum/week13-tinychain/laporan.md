# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: [inyChain – Proof of Work (PoW)]  
Nama: [Kingkin Kurnia Candrawati]  
NIM: [230202813]  
Kelas: [5 IKRA]  



## 1. Tujuan
Menjelaskan peran hash function dalam blockchain.
Melakukan simulasi sederhana Proof of Work (PoW).
Menganalisis keamanan cryptocurrency berbasis kriptografi.

## 2. Dasar Teori
Blockchain merupakan sistem pencatatan transaksi terdistribusi yang mengandalkan kriptografi hash untuk menjaga integritas data. Setiap blok berisi hash dari blok sebelumnya, sehingga membentuk rantai blok (chain of blocks) yang tidak dapat diubah tanpa mengubah seluruh rantai. Fungsi hash berperan penting untuk memastikan immutability—satu perubahan kecil pada data akan mengubah hash secara signifikan (prinsip avalanche effect).

Proof of Work (PoW) adalah mekanisme konsensus yang digunakan untuk memvalidasi blok baru dalam blockchain. Ide dasarnya: penambang (miner) harus melakukan pekerjaan komputasi (mencari nilai nonce) agar hash blok memenuhi kondisi tertentu (misalnya diawali beberapa nol). Proses ini disebut mining. Karena sulit menemukan hash yang cocok namun mudah memverifikasinya, PoW menjamin bahwa manipulasi data akan membutuhkan biaya komputasi sangat besar.

Dalam konteks keamanan cryptocurrency (mis. Bitcoin), PoW mencegah serangan seperti double spending karena penyerang harus menambang ulang seluruh blok setelah titik modifikasi untuk mengejar rantai yang sah. Namun, PoW juga memiliki kelemahan utama: konsumsi energi tinggi dan skalabilitas terbatas.

## 3. Alat dan Bahan
(- Python 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)
- Folder praktikum/week13-tinychain/ dengan struktur :
  ├─ src/
├─ screenshots/
└─ laporan.md

## 4. Langkah Percobaan
1. Buat folder proyek :
praktikum/week13-tinychain/
├─ src/
├─ screenshots/
└─ laporan.md

2. Buat file src/tinychain.py dan salin kode program dari panduan praktikum.

3. Jalankan program dengan perintah :
python src/tinychain.py

4. Amati hasil hash setiap blok dan waktu proses mining.

5. Simpan screenshot hasil eksekusi di screenshots/hasil.png.

6. Commit hasil dengan pesan week13-tinychain.

## 5. Source Code
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

if __name__ == "__main__":
    my_chain = Blockchain()
    print("Mining block 1...")
    my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

    print("Mining block 2...")
    my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))

    for block in my_chain.chain:
        print(f"\nIndex: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")


## 6. Hasil dan Pembahasan
a. Hasil Eksekusi

Setelah menjalankan program, muncul output seperti berikut : 
Mining block 1...
Block mined: 0000c61b0fa2b7b6b98e3d95f00129a8b0b8592ef28ef3f0b84a5a92a3c8fdb3
Mining block 2...
Block mined: 0000a17d15db9bc84246d4c8cf1a1e1f40b3e2e40277b5cb4d5f60a2a82467ea

b. Pembahasan

Proses mining memerlukan waktu karena program harus menemukan nonce yang menghasilkan hash dengan awalan 0000.

Ketika nilai difficulty dinaikkan, waktu pencarian meningkat drastis. Hal ini menunjukkan karakteristik PoW — sulit dikerjakan tapi mudah diverifikasi.

Setiap blok menyimpan hash blok sebelumnya, menciptakan integritas berantai. Perubahan pada satu blok membuat seluruh rantai menjadi tidak valid.

Dari sisi keamanan, sistem ini mencegah penyerang dengan daya komputasi terbatas untuk memodifikasi transaksi lama (double spending prevention).

## 7. Jawaban Pertanyaan
1. Mengapa fungsi hash sangat penting dalam blockchain?
Karena fungsi hash menjaga integritas data antarblok. Perubahan kecil pada isi blok mengubah hash secara signifikan, sehingga memutus rantai blockchain dan membuat manipulasi mudah terdeteksi.

2. Bagaimana Proof of Work mencegah double spending?
PoW mewajibkan setiap blok valid memiliki bukti kerja komputasi. Untuk mengganti transaksi lama, penyerang harus menambang ulang semua blok berikutnya agar rantainya lebih panjang dari rantai sah — hal ini praktis tidak mungkin tanpa kekuatan komputasi mayoritas.

3. Apa kelemahan PoW dalam hal efisiensi energi?
PoW membutuhkan banyak perhitungan hash sehingga mengonsumsi energi listrik besar. Ini menimbulkan isu lingkungan dan biaya operasional tinggi bagi jaringan besar seperti Bitcoin.

## 8. Kesimpulan
Simulasi TinyChain menunjukkan bahwa Proof of Work berperan penting menjaga keamanan blockchain melalui mekanisme komputasi hash yang sulit dipalsukan. Meskipun efisien dari sisi keamanan, PoW memiliki kelemahan dalam hal konsumsi energi dan waktu komputasi. Dengan demikian, konsep ini menjadi dasar penting bagi sistem konsensus terdesentralisasi seperti Bitcoin.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

Stinson, D. R. (2019). Cryptography: Theory and Practice. CRC Press.

Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System.

Modul Praktikum Kriptografi Minggu ke-13 – TinyChain: Proof of Work (PoW).

## 10. Commit Log
commit 9a7b12f4c35ed1d8b0b5eaf91d38a5f88e6a1b90
Author: Kingkin Kurnia Candrawati <kurniachandra2404@gmail.com>
Date:   2026-01-22 16:32:41 +0700

    week13-tinychain: tambah implementasi Proof of Work dan laporan hasil simulasi


    
