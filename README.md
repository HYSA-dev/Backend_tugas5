# Tugas 5 - Backend REST API (v1)

Aplikasi REST API Flask dengan Layered Architecture, Standard Response Envelope, dan API Versioning (`/api/v1`).

## Struktur Direktori Proyek

```text
Tugas5-Backend/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── utils/
│   │   └── response_helper.py
│   ├── repositories/
│   │   └── item_repo.py
│   ├── services/
│   │   └── item_service.py
│   └── routes/
│       └── v1/
│           ├── item_routes.py
│           └── user_routes.py
├── run.py
├── requirements.txt
└── README.md

Endpoint API (/api/v1)
GET /api/v1/categories - Ambil daftar kategori produk
GET /api/v1/items - Ambil semua barang produk UMKM
GET /api/v1/items/<id> - Ambil detail barang berdasarkan ID
POST /api/v1/items - Tambah barang baru
PUT /api/v1/items/<id> - Update data barang
DELETE /api/v1/items/<id> - Hapus barang