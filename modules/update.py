from services.item_service import ItemService


def modify_item(service: ItemService) -> bool:
    print("\n=== UPDATE ITEM ===")

    items = service.list_items()
    if not items:
        print("No items available to update.")
        return False

    print("\nAvailable items:")
    for item in items:
        print(f"ID: {item.item_id} | Name: {item.name} | Price: ${item.price}")

    item_id = input("\nEnter item ID to update: ").strip()
    if not item_id.isdigit():
        print("Invalid item ID. It should be a number.")
        return False

    item_id = int(item_id)

    target = service.find(item_id)
    if not target:
        print(f"Item with ID {item_id} not found.")
        return False

    print("\nCurrent item details:")
    print(f"ID: {target.item_id} | Name: {target.name} | Price: ${target.price}")

    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Price")
    print("3. Image URL")
    print("4. Cancel")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        new_name = input("Enter new item name: ").strip()
        if new_name == "":
            print("Item name cannot be empty.")
            return False
        changed = service.update(item_id, name=new_name)
        if changed:
            print("Item name updated successfully.")
        return changed

    elif choice == "2":
        try:
            new_price = float(input("Enter new item price: "))
            if new_price < 0:
                print("Price cannot be negative.")
                return False
            changed = service.update(item_id, price=new_price)
            if changed:
                print("Item price updated successfully.")
            return changed
        except ValueError:
            print("Invalid price.")
            return False

    elif choice == "3":
        new_image_url = input("Enter new image URL: ").strip()
        if new_image_url == "":
            print("Image URL cannot be empty.")
            return False
        changed = service.update(item_id, image_url=new_image_url)
        if changed:
            print("Item image URL updated successfully.")
        return changed

    elif choice == "4":
        print("Update cancelled.")
        return False

    else:
        print("Invalid choice.")
        return False
