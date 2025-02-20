import unittest

from Diary import Diary


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("user1", "password1")

    def test_unlock_diary(self):
        self.diary.unlock_diary("password1")
        self.assertEqual(self.diary.is_locked, False)


    def test_create_entry(self):
        self.diary.unlock_diary("password1")
        self.diary.create_entry("Title","body")
        self.assertEqual(len(self.diary.entries), 1)

    def test_that_i_can_delete_entry(self):
        self.diary.unlock_diary("password1")
        self.diary.create_entry("Title","body")
        self.diary.create_entry("Title","body")
        self.diary.delete_entry(1)
        self.assertEqual(len(self.diary.entries), 1)

    def test_that_i_can_update_entry(self):
        self.diary.unlock_diary("password1")
        self.diary.create_entry( "body", "Title")
        self.diary.update_entry(1, "New Title", "New Body")
        entry = self.diary.find_entry_by_id(1)
        self.assertEqual(entry.title, "New Title")
        self.assertEqual(entry.body, "New Body")

    def test_that_i_can_find_entry_by_id(self):
        self.diary.unlock_diary("password1")
        self.diary.create_entry("body", "Title")
        entry = self.diary.find_entry_by_id(1)
        self.assertEqual(entry.title, "body")



if __name__ == '__main__':
    unittest.main()
