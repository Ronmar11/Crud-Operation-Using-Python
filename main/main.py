import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.create import add_item
from modules.read import show_items
from modules.update import modify_item
from modules.delete import remove_item
from utils.file_handle import save_data
from services.item_service import ItemService


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    service = ItemService()

    actions = {
        '1': lambda: add_item(service),
        '2': lambda: show_items(service),
        '3': lambda: modify_item(service),
        '4': lambda: remove_item(service),
    }

    while True:
        print("\n====== MENU ======")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in actions:
            changed = actions[choice]()
            if changed:
                save_data(service.to_dicts())

        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()