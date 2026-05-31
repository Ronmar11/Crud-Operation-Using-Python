from modules import create, read, update, delete

def main():
    while True:
        print("\nMenu:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            break
