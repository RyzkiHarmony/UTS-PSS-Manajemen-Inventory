## Anggota Kelompok: 
   Muhammad Rizki - A11.2022.14657


## Sistem Inventaris

Sistem manajemen inventaris berbasis Django untuk mengelola barang, kategori, dan supplier. Untuk memenuhi UTS Pemrograman Sisi Server.

## Fitur

- Manajemen Item (Create, Read)
- Manajemen Kategori (Create, Read)
- Manajemen Supplier (Create, Read)
- Dashboard dengan ringkasan sistem
- Laporan stok rendah
- Statistik per kategori
- Statistik per supplier

## Teknologi

- Django
- PostgreSQL
- Docker

## Cara Menjalankan

1. Pastikan Docker dan Docker Compose sudah terinstall
2. Clone repository ini
3. Hapus folder postgres-data
3. Buka terminal dan masuk ke direktori project
4. Jalankan perintah:
   ```bash
   docker-compose up -d
5. Attach Shell ke container uts-pss-manajemen-inventory-django
6. Jalankan command berikut di shell:
   ```bash
   python manage.py migrate
7. Jalankan ULANG Container Docker
   ```bash
   docker-compose down
   docker-compose up -d
8. Akses aplikasi di http://localhost:8011

## Cara Mengimport Database

1. Attach shell ke container uts-pss-manajemen-inventory-django
2. Ketik command berikut di shell:
   ```bash
   python manage.py shell < importer.py

## Cara Mengoperasikan Create (Tambah)

1. Lakukan Login di http://localhost:8011/admin
   dengan mengisi username dan password yang ada pada file code/db_seed/admins.csv
2. Sekarang operasi Create sudah bisa dilakukan.
3. Jika tidak melakukan login maka sistem akan memberikan pemberitahuan tidak dapat menambahkan data karena admin tidak ditemukan.
