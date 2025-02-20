class MainApplication:
    def __init__(self):
        from Diaries import Diaries
        self.diaries = Diaries()

    def display_menu(self):
        print("\n===== Diary Main Menu =====")
        print("1. Create a new diary")
        print("2. Unlock diary")
        print("3. Create a new entry")
        print("4. View all entries")
        print("5. Update an entry")
        print("6. Delete an entry")
        print("7. Lock diary")
        print("8. Exit")

    def create_diary(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.diaries.add(username, password)
        print(f"Diary for {username} created successfully!")

    def unlock_diary(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            diary = self.diaries.find_diary_by_username(username)
            diary.unlock_diary(password)
            print(f"Diary for {username} unlocked successfully!")
            return diary
        except ValueError as e:
            print(e)
        except PermissionError as e:
            print(e)
        return None

    def create_entry(self, diary):
        if diary and not diary.is_locked:
            title = input("Enter entry title: ")
            body = input("Enter entry body: ")
            diary.create_entry(title, body)
            print("Entry created successfully!")
        else:
            print("Diary is locked or not found.")

    def view_entries(self, diary):
        if diary and not diary.is_locked:
            if not diary.entries:
                print("No entries found.")
            else:
                for entry in diary.entries:
                    print(entry)
        else:
            print("Diary is locked or not found.")

    def update_entry(self, diary):
        if diary and not diary.is_locked:
            entry_id = int(input("Enter entry ID to update: "))
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            try:
                diary.update_entry(entry_id, title, body)
                print("Entry updated successfully!")
            except ValueError as e:
                print(e)
        else:
            print("Diary is locked or not found.")

    def delete_entry(self, diary):
        if diary and not diary.is_locked:
            entry_id = int(input("Enter entry ID to delete: "))
            try:
                diary.delete_entry(entry_id)
                print("Entry deleted successfully!")
            except ValueError as e:
                print(e)
        else:
            print("Diary is locked or not found.")

    def lock_diary(self, diary):
        if diary:
            diary.lock_diary()
            print("Diary locked successfully!")
        else:
            print("Diary not found.")

    def main(self):
        current_diary = None
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_diary()
            elif choice == "2":
                current_diary = self.unlock_diary()
            elif choice == "3":
                self.create_entry(current_diary)
            elif choice == "4":
                self.view_entries(current_diary)
            elif choice == "5":
                self.update_entry(current_diary)
            elif choice == "6":
                self.delete_entry(current_diary)
            elif choice == "7":
                self.lock_diary(current_diary)
                current_diary = None
            elif choice == "8":
                print("Exiting the diary system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = MainApplication()
    app.main()