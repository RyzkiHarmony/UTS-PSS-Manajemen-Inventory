# Sistem Inventaris

Sistem manajemen inventaris berbasis Django untuk mengelola barang, kategori, dan supplier.

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
- Bootstrap

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

## Cara Mengoperasikan Create (Tambah)

1. Membuat Superuser di Terminal
   ```bash
   docker-compose exec web python manage.py createsuperuser
2. Lakukan Login di http://localhost:8011/admin
3. Sekarang operasi Create sudah bisa dilakukan
4. Jika tidak melakukan login maka sistem akan memberikan pemberitahuan tidak dapat menambahkan data karena admin tidak ditemukan