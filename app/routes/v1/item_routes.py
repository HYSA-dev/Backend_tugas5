from flask import Blueprint, request

from app.repositories.item_repo import ItemRepository
from app.services.item_service import ItemService
from app.utils.response_helper import fail_response, success_response

item_bp_v1 = Blueprint("api", __name__, url_prefix="/api/v1")

repo = ItemRepository()
service = ItemService(repo)


@item_bp_v1.route("/categories", methods=["GET"])
def get_categories():
    data, _, code = service.fetch_all_categories()
    return success_response(data=data, code=code)


@item_bp_v1.route("/items", methods=["GET"])
def get_items():
    category = request.args.get("category")
    min_price = request.args.get("min_price")
    data, errors, code = service.fetch_all_items(category, min_price)

    if errors:
        return fail_response(errors=errors, code=code)

    return success_response(data=data, code=code)


@item_bp_v1.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    data, errors, code = service.get_item_by_id(item_id)

    if errors:
        return fail_response(errors=errors, code=code)

    return success_response(data=data, code=code)


@item_bp_v1.route("/items", methods=["POST"])
def create_item():
    if not request.is_json:
        return fail_response(
            {"content_type": "Header harus application/json"}, 400
        )

    data = request.get_json(silent=True)
    created, errors, code = service.add_item(data)

    if errors:
        return fail_response(errors=errors, code=code)

    return success_response(
        data=created, message="Barang berhasil ditambahkan", code=code
    )


@item_bp_v1.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if not request.is_json:
        return fail_response(
            {"content_type": "Header harus application/json"}, 400
        )

    data = request.get_json(silent=True)
    updated, errors, code = service.update_item(item_id, data)

    if errors:
        return fail_response(errors=errors, code=code)

    return success_response(
        data=updated, message="Data berhasil diperbarui", code=code
    )


@item_bp_v1.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    errors, code = service.remove_item(item_id)

    if errors:
        return fail_response(errors=errors, code=code)

    return success_response(message="Data berhasil dihapus", code=code)