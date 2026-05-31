from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules.create import add_item
from modules.read import show_items
from modules.update import modify_item
from modules.delete import remove_item

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
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in actions:
            actions[choice]()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
