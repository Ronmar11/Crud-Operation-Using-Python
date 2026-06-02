from typing import Dict, Any


# CLASS: Item is an OOP class that represents one item/order product.
class Item:
    # METHOD: Constructor method; initializes the object's data.
    def __init__(self, item_id: int, name: str, price: float, image_url: str) -> None:
        # ENCAPSULATION: These attributes keep all item data grouped inside one object.
        self.item_id = int(item_id)
        self.name = str(name)
        self.price = float(price)
        self.image_url = str(image_url)

    # METHOD: Converts the Item object into a dictionary for saving or returning as JSON.
    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url,
        }

    # METHOD: Factory method; creates an Item object from dictionary data.
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Item":
        return cls(
            item_id=data.get("item_id"),
            name=data.get("name"),
            price=data.get("price"),
            image_url=data.get("image_url"),
        )
