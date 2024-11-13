# Sistem Inventaris

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
3. Buka terminal dan masuk ke direktori project
4. Jalankan perintah:
   ```bash
   docker-compose up -d
5. Jalankan migrasi database:
   ```bash
   docker-compose exec web python manage.py migrate
6. Akses aplikasi di http://localhost:8011

## Cara Mengimport Database

1. Buka terminal
2. Masuk ke direktori UTS-PSS-Manajemen-Inventory
3. Ketik command berikut di terminal:
   ```bash
   docker-compose exec web python manage.py shell < importer.py

## Cara Mengoperasikan Create (Tambah)

1. Lakukan Login di http://localhost:8011/admin
   dengan mengisi username dan password yang ada pada file [text](code/db_seed/admins.csv)
2. Sekarang operasi Create sudah bisa dilakukan
3. Jika tidak melakukan login maka sistem akan memberikan pemberitahuan tidak dapat menambahkan data karena admin tidak ditemukan