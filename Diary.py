from Entry import Entry


class Diary:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []
        self.id = 1

    def unlock_diary(self, password: str):
        if password == self.password:
            self.is_locked = False
        else:
            raise ValueError("Passwords do not match")

    def create_entry(self, title: str, body: str):
        if self.is_locked:
            raise ValueError("Diary is locked. Please unlock it.")
        entry_id = len(self.entries)
        new_entry = Entry(self.id, title, body)
        self.entries.append(new_entry)
        self.id += 1

    def delete_entry(self, entry_id: int):
        if self.is_locked:
            raise ValueError("Diary is locked. Please unlock it.")
        entry = self.find_entry_by_id(entry_id)
        self.entries.remove(entry)

    def find_entry_by_id(self, entry_id: int):
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        raise ValueError(f"Entry with id {entry_id} not found")

    def update_entry(self, entry_id: int, title: str, body: str):
        if self.is_locked:
            raise PermissionError("Diary is locked. Please unlock it.")
        entry = self.find_entry_by_id(entry_id)
        entry.title = title
        entry.body = body

    def __str__(self):
        return f"Diary ({self.username}, islocked = {self.is_locked}, entries = {self.entries})"