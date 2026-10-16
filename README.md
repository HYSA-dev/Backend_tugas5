# Tugas 4 - REST API Modular & Layered Architecture

Aplikasi REST API Flask dengan **Layered Architecture** (Controller, Service, Repository) dan **Flask Blueprint**.

## Diagram Alur Layer

```text
[ Client / Postman ]
       │ (HTTP Request)
       ▼
[ Controller / Route ] ──► (item_routes.py)
       │ (Aturan Bisnis & Validasi)
       ▼
[ Service Layer ]      ──► (item_service.py)
       │ (Akses Data)
       ▼
[ Repository Layer ]   ──► (item_repo.py)

Daftar Endpoint
GET /api/v1/categories - Ambil semua kategori
GET /api/v1/items - Ambil semua barang (dukung filter ?category= & ?min_price=)
GET /api/v1/items/<id> - Detail barang berdasarkan ID
POST /api/v1/items - Tambah barang baru (Validasi: harga > 0 & stok >= 0)
PUT /api/v1/items/<id> - Update barang
DELETE /api/v1/items/<id> - Hapus barang