class ItemRepository:

    def __init__(self):
        self.categories = [
            {"id": 1, "name": "Pemrograman"},
            {"id": 2, "name": "Basis Data"},
            {"id": 3, "name": "Fiksi & Sastra"},
        ]
        self.items = [
            {
                "id": 1,
                "title": "Pemrograman Python Dasar",
                "author": "Guido van Rossum",
                "category": "Pemrograman",
                "price": 95000,
                "stock": 10,
            },
            {
                "id": 2,
                "title": "Dasar-Dasar Backend & REST API",
                "author": "Sony Panca Budiarto",
                "category": "Pemrograman",
                "price": 120000,
                "stock": 5,
            },
            {
                "id": 3,
                "title": "Mastering MySQL & NoSQL",
                "author": "Riki Pratama",
                "category": "Basis Data",
                "price": 85000,
                "stock": 15,
            },
            {
                "id": 4,
                "title": "Laskar Pelangi",
                "author": "Andrea Hirata",
                "category": "Fiksi & Sastra",
                "price": 65000,
                "stock": 20,
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
            "title": data["title"],
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
        item["title"] = data.get("title", item["title"])
        item["author"] = data.get("author", item["author"])
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