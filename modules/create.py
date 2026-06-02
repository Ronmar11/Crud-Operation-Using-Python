from modules.models import Item
from services.item_service import ItemService


def add_item(service: ItemService) -> bool:
    print("\n=== CREATE ITEM ===")

    item_id = input("Enter item ID: ").strip()
    if not item_id.isdigit():
        print("Invalid ID. Must be a number.")
        return False

    item_id = int(item_id)
    if service.find(item_id) is not None:
        print("Item ID already exists.")
        return False

    name = input("Enter item name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return False

    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid price.")
        return False

    image_url = input("Enter image URL: ").strip()
    if not image_url:
        print("Image URL cannot be empty.")
        return False

    new_item = Item(item_id=item_id, name=name, price=price, image_url=image_url)

    created = service.create(new_item)
    if created:
        print("Item added successfully.")
    else:
        print("Failed to add item.")
    return created
