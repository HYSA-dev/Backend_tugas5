class ItemService:

    def __init__(self, repo):
        self.repo = repo

    def fetch_all_categories(self):
        cats = self.repo.get_all_categories()
        return {"categories": cats, "total": len(cats)}, None, 200

    def fetch_all_items(self, category_query, min_price_query):
        errors = {}
        min_price = None

        if min_price_query:
            try:
                min_price = float(min_price_query)
            except ValueError:
                errors["min_price"] = "Parameter min_price harus berupa angka"

        if errors:
            return None, errors, 400

        data = self.repo.get_all(
            category=category_query, min_price=min_price
        )
        return {"items": data, "total": len(data)}, None, 200

    def get_item_by_id(self, item_id):
        item = self.repo.get_by_id(item_id)
        if not item:
            return None, {"id": "Barang/Buku tidak ditemukan"}, 404
        return item, None, 200

    def add_item(self, data):
        errors = {}
        if not data or not isinstance(data, dict):
            return None, {"body": "Payload JSON tidak boleh kosong"}, 400

        name = data.get("name")  # Menggunakan 'name'
        price = data.get("price")
        stock = data.get("stock", 0)

        if not name or not isinstance(name, str) or not name.strip():
            errors["name"] = "Nama barang wajib diisi"  # Perbarui ke field 'name'

        if price is None or not isinstance(price, (int, float)):
            errors["price"] = "Harga barang harus berupa angka"
        elif price <= 0:
            errors["price"] = "Harga barang harus lebih besar dari 0"

        if stock is not None and (
            not isinstance(stock, int) or stock < 0
        ):
            errors["stock"] = "Stok barang tidak boleh negatif"

        if errors:
            return None, errors, 400

        created = self.repo.create(data)
        return created, None, 201

    def update_item(self, item_id, data):
        errors = {}
        if not data or not isinstance(data, dict):
            return None, {"body": "Payload JSON tidak boleh kosong"}, 400

        if "price" in data:
            price = data.get("price")
            if not isinstance(price, (int, float)) or price <= 0:
                errors["price"] = "Harga barang harus lebih besar dari 0"

        if "stock" in data:
            stock = data.get("stock")
            if not isinstance(stock, int) or stock < 0:
                errors["stock"] = "Stok barang tidak boleh negatif"

        if errors:
            return None, errors, 400

        updated = self.repo.update(item_id, data)
        if not updated:
            return None, {"id": "Barang/Buku tidak ditemukan"}, 404

        return updated, None, 200

    def remove_item(self, item_id):
        success = self.repo.delete(item_id)
        if not success:
            return {"id": "Barang/Buku tidak ditemukan"}, 404
        return None, 200