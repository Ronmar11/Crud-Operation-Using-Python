<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 8fccb5673d66e5b9f8c676cfa3e01224b87bb7ac
def remove_item(items):
    print("\n=== DELETE ITEM ===")

    if not items:
        print("No items to delete.")
        return

    print("\nAvailable Items:")
    for item in items:
        print(f"ID: {item['item_id']}, Name: {item['name']}, Price: ${item['price']}")

    item_id_input = input("\nEnter item ID to delete: ").strip()

    if not item_id_input.isdigit():
        print("Invalid ID. Must be a number.")
        return

    item_id = int(item_id_input)

    item_to_delete = None
    for item in items:
        if item["item_id"] == item_id:
            item_to_delete = item
            break

    if item_to_delete is None:
        print(f"Item with ID {item_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete '{item_to_delete['name']}'? (yes/no): ").strip().lower()

    if confirm == "yes":
        items.remove(item_to_delete)
        print(f"Item '{item_to_delete['name']}' has been deleted successfully.")
    else:
        print("Deletion cancelled.")
<<<<<<< HEAD
=======
=======
def remove_item():
    print("Delete function here")
>>>>>>> 8bc12d7d762bd00656d487dcf8fff9af92f518dd
>>>>>>> 8fccb5673d66e5b9f8c676cfa3e01224b87bb7ac
