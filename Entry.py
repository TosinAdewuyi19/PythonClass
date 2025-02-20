from datetime import datetime

class Entry:
    def __init__(self, id: int, title: str, body: str):
        self.id = id
        self.title = title
        self.body = body
        self.date_created = datetime.now()

    def __str__(self):
        return f'Entry(id={self.id}, title={self.title}, body={self.body}, date_created={self.date_created})'

