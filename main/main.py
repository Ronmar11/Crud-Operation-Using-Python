
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.create import add_item
from modules.read import show_items
from modules.update import modify_item
from modules.delete import remove_item



DATA_FILE = Path(__file__).resolve().parents[1] / "storage" / "data.json"


def load_items():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []



def save_items(items):
    with open(DATA_FILE, "w") as f:
        json.dump(items, f, indent=4)


def main():
    items = load_items()

    actions = {
        '1': lambda: add_item(items),
        '2': lambda: show_items(items),
        '3': lambda: modify_item(items),
        '4': lambda: remove_item(items),
    }

    while True:
        print("\n====== MENU ======")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in actions:
            actions[choice]()

            
            if choice in ['1', '3', '4']:
                save_items(items)

        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()