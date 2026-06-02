from services.item_service import ItemService


def show_items(service: ItemService) -> bool:
    print("\n=== LIST ITEMS ===")
    items = service.list_items()
    if not items:
        print("No items available.")
        return False

    for item in items:
        print(f"ID: {item.item_id} | Name: {item.name} | Price: ${item.price}")
    return False