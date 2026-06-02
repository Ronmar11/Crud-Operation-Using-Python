
from typing import List, Optional
from modules.models import Item
from utils.file_handle import load_data


class ItemService:
    def __init__(self) -> None:
        raw = load_data()
        self._items: List[Item] = [Item.from_dict(d) for d in raw]

    def list_items(self) -> List[Item]:
        return list(self._items)

    def find(self, item_id: int) -> Optional[Item]:
        for it in self._items:
            if it.item_id == item_id:
                return it
        return None

    def create(self, item: Item) -> bool:
        if self.find(item.item_id) is not None:
            return False
        self._items.append(item)
        return True

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

    def delete(self, item_id: int) -> bool:
        target = self.find(item_id)
        if not target: 
            return False
        self._items.remove(target)
        return True

    def to_dicts(self) -> List[dict]:
        return [it.to_dict() for it in self._items]
