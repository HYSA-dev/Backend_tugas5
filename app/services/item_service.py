class ItemService:

    def __init__(self, repo):
        self.repo = repo

    def fetch_all_categories(self):
        cats = self.repo.get_all_categories()
        return {"status": "success", "total": len(cats), "data": cats}, 200

    def fetch_all_items(self, category_query, min_price_query):
        min_price = None
        if min_price_query:
            try:
                min_price = float(min_price_query)
            except ValueError:
                return {
                    "status": "fail",
                    "message": "Parameter min_price harus berupa angka",
                }, 400

        data = self.repo.get_all(
            category=category_query, min_price=min_price
        )
        return {"status": "success", "total": len(data), "data": data}, 200

    def get_item_by_id(self, item_id):
        item = self.repo.get_by_id(item_id)
        if not item:
            return {
                "status": "fail",
                "message": "Barang/Buku tidak ditemukan",
            }, 404
        return {"status": "success", "data": item}, 200

    def add_item(self, data):
        if not data or "title" not in data or "price" not in data:
            return {
                "status": "fail",
                "message": "Judul dan harga barang wajib diisi",
            }, 400

        if data["price"] <= 0:
            return {
                "status": "fail",
                "message": "Harga barang harus lebih besar dari 0",
            }, 400

        if data.get("stock", 0) < 0:
            return {
                "status": "fail",
                "message": "Stok barang tidak boleh negatif",
            }, 400

        created = self.repo.create(data)
        return {
            "status": "success",
            "message": "Barang berhasil ditambahkan",
            "data": created,
        }, 201

    def update_item(self, item_id, data):
        if not data:
            return {
                "status": "fail",
                "message": "Payload JSON tidak boleh kosong",
            }, 400

        if "price" in data and data["price"] <= 0:
            return {
                "status": "fail",
                "message": "Harga barang harus lebih besar dari 0",
            }, 400

        if "stock" in data and data["stock"] < 0:
            return {
                "status": "fail",
                "message": "Stok barang tidak boleh negatif",
            }, 400

        updated = self.repo.update(item_id, data)
        if not updated:
            return {
                "status": "fail",
                "message": "Barang/Buku tidak ditemukan",
            }, 404

        return {
            "status": "success",
            "message": "Data barang berhasil diperbarui",
            "data": updated,
        }, 200

    def remove_item(self, item_id):
        success = self.repo.delete(item_id)
        if not success:
            return {
                "status": "fail",
                "message": "Barang/Buku tidak ditemukan",
            }, 404

        return {
            "status": "success",
            "message": "Data barang berhasil dihapus",
        }, 200