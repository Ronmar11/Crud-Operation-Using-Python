from pathlib import Path
import sys

from flask import Flask, jsonify, render_template, request

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.models import Item
from services.item_service import ItemService
from utils.file_handle import save_data

app = Flask(
    __name__,
    static_folder=str(PROJECT_ROOT / "frontend" / "static"),
    template_folder=str(PROJECT_ROOT / "frontend" / "templates"),
)

service = ItemService()


def persist() -> None:
    save_data(service.to_dicts())


def get_json_body() -> dict:
    return request.get_json(silent=True) or {}


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/items")
def list_items():
    return jsonify([item.to_dict() for item in service.list_items()])


@app.post("/api/items")
def create_item():
    data = get_json_body()
    required = ("item_id", "name", "price", "image_url")

    if any(field not in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        item = Item(
            item_id=data["item_id"],
            name=data["name"],
            price=data["price"],
            image_url=data["image_url"],
        )
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid field types"}), 400

    if not service.create(item):
        return jsonify({"error": "Item with this ID already exists"}), 409

    persist()
    return jsonify(item.to_dict()), 201


@app.put("/api/items/<int:item_id>")
def update_item(item_id: int):
    data = get_json_body()
    changes = {}

    if "name" in data:
        changes["name"] = data["name"]
    if "price" in data:
        try:
            changes["price"] = float(data["price"])
        except (TypeError, ValueError):
            return jsonify({"error": "Price must be a number"}), 400
    if "image_url" in data:
        changes["image_url"] = data["image_url"]

    if not changes:
        return jsonify({"error": "No updatable fields provided"}), 400

    if not service.update(item_id, **changes):
        return jsonify({"error": "Item not found"}), 404

    persist()
    updated = service.find(item_id)
    return jsonify(updated.to_dict())


@app.delete("/api/items/<int:item_id>")
def delete_item(item_id: int):
    if not service.delete(item_id):
        return jsonify({"error": "Item not found"}), 404

    persist()
    return jsonify({"deleted": True})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
