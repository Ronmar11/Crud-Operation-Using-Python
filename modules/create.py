<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 8fccb5673d66e5b9f8c676cfa3e01224b87bb7ac
class Item:
    def __init__(self, item_id, name, price, image_url):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.image_url = image_url

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url
        }


def add_item(items):
    print("\n=== CREATE ITEM ===")

    item_id = input("Enter item ID: ").strip()

    if not item_id.isdigit():
        print("Invalid ID. Must be a number.")
        return

    item_id = int(item_id)

    if any(item["item_id"] == item_id for item in items):
        print("Item ID already exists.")
        return

    name = input("Enter item name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid price.")
        return

    image_url = input("Enter image URL: ").strip()
    if not image_url:
        print("Image URL cannot be empty.")
        return

    new_item = Item(item_id, name, price, image_url)

    items.append(new_item.to_dict())

<<<<<<< HEAD
    print("Item added successfully.")
=======
    print("Item added successfully.")
=======
def add_item():
    print("Create function here")
>>>>>>> 8bc12d7d762bd00656d487dcf8fff9af92f518dd
>>>>>>> 8fccb5673d66e5b9f8c676cfa3e01224b87bb7ac
