from services.item_service import ItemService


def remove_item(service: ItemService) -> bool:
    print("\n=== DELETE ITEM ===")

    items = service.list_items()
    if not items:
        print("No items to delete.")
        return False

    print("\nAvailable Items:")
    for item in items:
        print(f"ID: {item.item_id}, Name: {item.name}, Price: ${item.price}")

    item_id_input = input("\nEnter item ID to delete: ").strip()
    if not item_id_input.isdigit():
        print("Invalid ID. Must be a number.")
        return False

    item_id = int(item_id_input)
    target = service.find(item_id)
    if target is None:
        print(f"Item with ID {item_id} not found.")
        return False

    confirm = input(f"Are you sure you want to delete '{target.name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted = service.delete(item_id)
        if deleted:
            print(f"Item '{target.name}' has been deleted successfully.")
        return deleted
    else:
        print("Deletion cancelled.")
        return False
