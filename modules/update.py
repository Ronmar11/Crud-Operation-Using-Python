<<<<<<< HEAD

from modules.create import Item
from utils.file_handle import load_data, save_data


def modify_item():
    """Load items from storage, allow the user to modify one, then save."""
    print("\n=== Update Item ===")

    raw = load_data()
    if not raw:
        print("No items available to update.")
        return

    # Convert stored dicts to Item objects (be permissive with types)
    items = []
    for d in raw:
        try:
            iid = int(d.get("item_id", d.get("id", 0)))
        except (TypeError, ValueError):
            iid = 0
        name = d.get("name", "")
        try:
            price = float(d.get("price", 0))
        except (TypeError, ValueError):
            price = 0.0
        image = d.get("image_url", d.get("image", ""))
        items.append(Item(iid, name, price, image))

    # Display all items
    print("\nAvailable items:")
    for item in items:
        print(f"ID: {item.item_id} | Name: {item.name} | Price: ${item.price:.2f}")

    item_id = input("\nEnter item ID to update: ").strip()
    if not item_id.isdigit():
        print("Invalid item ID. It should be a number.")
        return

    item_id = int(item_id)

    # Find the item
    item_to_update = None
    for item in items:
        if item.item_id == item_id:
            item_to_update = item
            break

    if item_to_update is None:
        print(f"Item with ID {item_id} not found.")
        return

    # Display current item details
    print("\nCurrent item details:")
    item_to_update.display()

    # Choose what to update
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
            return
        item_to_update.name = new_name
        print("Item name updated successfully.")

    elif choice == "2":
        try:
            new_price = float(input("Enter new item price: "))
            if new_price < 0:
                print("Price cannot be negative.")
                return
            item_to_update.price = new_price
            print("Item price updated successfully.")
        except ValueError:
            print("Invalid price.")
            return

    elif choice == "3":
        new_image_url = input("Enter new image URL: ").strip()
        if new_image_url == "":
            print("Image URL cannot be empty.")
            return
        item_to_update.image_url = new_image_url
        print("Item image URL updated successfully.")

    elif choice == "4":
        print("Update cancelled.")
        return

    else:
        print("Invalid choice.")
        return

    # Persist changes back to storage
    to_save = []
    for item in items:
        to_save.append({
            "item_id": item.item_id,
            "name": item.name,
            "price": item.price,
            "image_url": item.image_url,
        })

    save_data(to_save)
    print("Changes saved.")
=======
def modify_item():
    print("Update function here")
>>>>>>> 8bc12d7d762bd00656d487dcf8fff9af92f518dd
