class Item:
    def __init__(self, item_id, name, price, image_url):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.image_url = image_url

    def display(self):
        print(f"ID: {self.item_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Image Link: {self.image_url}")


def add_item(items):
    print("\n=== Create Item ===")

    item_id = input("\nEnter item ID: ").strip()

    if not item_id.isdigit():
        print("Invalid item ID. It should be a number.")
        return

    item_id = int(item_id)

    if any(item.item_id == item_id for item in items):
        print("Item ID already exists.")
        return

    name = input("Enter item name: ").strip()

    if name == "":
        print("Item name cannot be empty.")
        return

    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price.")
        return

    image_url = input("Enter item image URL: ").strip()

    if image_url == "":
        print("Image URL cannot be empty.")
        return

    new_item = Item(item_id, name, price, image_url)
    items.append(new_item)

    print("Item added successfully.")