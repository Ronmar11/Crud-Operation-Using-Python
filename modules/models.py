from typing import Dict, Any


class Item:
    def __init__(self, item_id: int, name: str, price: float, image_url: str) -> None:
        self.item_id = int(item_id)
        self.name = str(name)
        self.price = float(price)
        self.image_url = str(image_url)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Item":
        return cls(
            item_id=data.get("item_id"),
            name=data.get("name"),
            price=data.get("price"),
            image_url=data.get("image_url"),
        )
