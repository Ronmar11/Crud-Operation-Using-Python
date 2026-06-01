<<<<<<< HEAD

import json
from pathlib import Path
import sys

=======
from pathlib import Path
import sys


>>>>>>> 8bc12d7d762bd00656d487dcf8fff9af92f518dd
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.create import add_item
from modules.read import show_items
from modules.update import modify_item
from modules.delete import remove_item

<<<<<<< HEAD


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
=======
def main():
    actions = {
        '1': add_item,
        '2': show_items,
        '3': modify_item,
        '4': remove_item,
    }

    while True:
        print("\nMenu:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
>>>>>>> 8bc12d7d762bd00656d487dcf8fff9af92f518dd
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in actions:
            actions[choice]()
<<<<<<< HEAD

            
            if choice in ['1', '3', '4']:
                save_items(items)

        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
=======
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
>>>>>>> 8bc12d7d762bd00656d487dcf8fff9af92f518dd
