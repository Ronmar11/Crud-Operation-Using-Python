
from typing import List, Optional
from modules.models import Item
from utils.file_handle import load_data


# CLASS: ItemService is an OOP class that manages Item objects.
# ABSTRACTION: This class hides the item CRUD logic from the UI, API, and main program.
class ItemService:
    # METHOD: Constructor method; loads saved items when the service object is created.
    def __init__(self) -> None:
        raw = load_data()
        # ENCAPSULATION: _items is internal service data; other modules use methods to access it.
        self._items: List[Item] = [Item.from_dict(d) for d in raw]

    # METHOD: Returns a copy of the item list.
    def list_items(self) -> List[Item]:
        return list(self._items)

    # METHOD: Searches for one item by ID.
    def find(self, item_id: int) -> Optional[Item]:
        for it in self._items:
            if it.item_id == item_id:
                return it
        return None

    # METHOD: Adds a new item if the ID is not already used.
    def create(self, item: Item) -> bool:
        if self.find(item.item_id) is not None:
            return False
        self._items.append(item)
        return True

    # METHOD: Updates an existing item's editable fields.
    def update(self, item_id: int, **fields) -> bool:
        target = self.find(item_id)
        if not target:
            return False
        if "name" in fields:
            target.name = fields["name"]
        if "price" in fields:
            target.price = fields["price"]
        if "image_url" in fields:
            target.image_url = fields["image_url"]
        return True

    # METHOD: Deletes an item by ID.
    def delete(self, item_id: int) -> bool:
        target = self.find(item_id)
        if not target: 
            return False
        self._items.remove(target)
        return True

    # METHOD: Converts all Item objects into dictionaries.
    def to_dicts(self) -> List[dict]:
        return [it.to_dict() for it in self._items]
