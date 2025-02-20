from Diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username: str, password: str):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def find_diary_by_username(self, username: str):
        for diary in self.diaries:
            if diary.username == username:
                return diary
        raise ValueError(f'Diary with username {username} not found')

    def delete_diary(self, username: str, password: str):
        diary = self.find_diary_by_username(username)
        diary.unlock_diary(password)
        self.diaries.remove(diary)

    def __str__(self):
        return f"Diaries(diaries={self.diaries}"