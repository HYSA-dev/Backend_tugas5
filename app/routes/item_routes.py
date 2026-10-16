from flask import Blueprint, jsonify, request

from app.repositories.item_repo import ItemRepository
from app.services.item_service import ItemService

item_bp = Blueprint("api", __name__, url_prefix="/api/v1")

repo = ItemRepository()
service = ItemService(repo)

@item_bp.route("/categories", methods=["GET"])
def get_categories():
    resp, code = service.fetch_all_categories()
    return jsonify(resp), code

@item_bp.route("/items", methods=["GET"])
def get_items():
    category = request.args.get("category")
    min_price = request.args.get("min_price")
    resp, code = service.fetch_all_items(category, min_price)
    return jsonify(resp), code

@item_bp.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    resp, code = service.get_item_by_id(item_id)
    return jsonify(resp), code

@item_bp.route("/items", methods=["POST"])
def create_item():
    data = request.get_json() if request.is_json else None
    resp, code = service.add_item(data)
    return jsonify(resp), code

@item_bp.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json() if request.is_json else None
    resp, code = service.update_item(item_id, data)
    return jsonify(resp), code

@item_bp.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    resp, code = service.remove_item(item_id)
    return jsonify(resp), code