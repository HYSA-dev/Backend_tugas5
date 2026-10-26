class ItemRepository:

    def __init__(self):
        self.categories = [
            {"id": 1, "name": "Makanan"},
            {"id": 2, "name": "Minuman"},
            {"id": 3, "name": "Pakaian"},
            {"id": 4, "name": "Aksesori"},
        ]
        self.items = [
            {
                "id": 1,
                "name": "Keripik Pisang",
                "category": "Makanan",
                "price": 15000,
                "stock": 20,
            },
            {
                "id": 2,
                "name": "Keripik Singkong",
                "category": "Makanan",
                "price": 12000,
                "stock": 15,
            },
            {
                "id": 3,
                "name": "Kopi Robusta",
                "category": "Minuman",
                "price": 35000,
                "stock": 10,
            },
            {
                "id": 4,
                "name": "Teh Celup Herbal",
                "category": "Minuman",
                "price": 20000,
                "stock": 25,
            },
            {
                "id": 5,
                "name": "Batik Banyuwangi",
                "category": "Pakaian",
                "price": 150000,
                "stock": 5,
            },
            {
                "id": 6,
                "name": "Kaos Etnik",
                "category": "Pakaian",
                "price": 65000,
                "stock": 12,
            },
            {
                "id": 7,
                "name": "Gantungan Kunci UD",
                "category": "Aksesori",
                "price": 10000,
                "stock": 50,
            },
            {
                "id": 8,
                "name": "Tas Anyaman",
                "category": "Aksesori",
                "price": 45000,
                "stock": 8,
            },
            {
                "id": 9,
                "name": "Bagiak Khas Bwi",
                "category": "Makanan",
                "price": 18000,
                "stock": 30,
            },
            {
                "id": 10,
                "name": "Dompet Batik",
                "category": "Aksesori",
                "price": 25000,
                "stock": 15,
            },
        ]

    def get_all_categories(self):
        return self.categories

    def get_all(self, category=None, min_price=None):
        filtered = self.items
        if category:
            filtered = [
                i
                for i in filtered
                if i["category"].lower() == category.lower()
            ]
        if min_price is not None:
            filtered = [i for i in filtered if i["price"] >= min_price]
        return filtered

    def get_by_id(self, item_id):
        return next((i for i in self.items if i["id"] == item_id), None)

    def create(self, data):
        new_item = {
            "id": len(self.items) + 1,
            "name": data["name"],
            "author": data.get("author", "-"),
            "category": data.get("category", "Umum"),
            "price": data["price"],
            "stock": data.get("stock", 0),
        }
        self.items.append(new_item)
        return new_item

    def update(self, item_id, data):
        item = self.get_by_id(item_id)
        if not item:
            return None
        item["name"] = data.get("name", item["name"]) # Ganti title ke name
        item["category"] = data.get("category", item["category"])
        item["price"] = data.get("price", item["price"])
        item["stock"] = data.get("stock", item["stock"])
        return item

    def delete(self, item_id):
        item = self.get_by_id(item_id)
        if not item:
            return False
        self.items = [i for i in self.items if i["id"] != item_id]
        return True