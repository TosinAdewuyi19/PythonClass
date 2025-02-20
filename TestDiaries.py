import unittest

from Diaries import Diaries


class TestDiaries(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_add_diary(self):
        self.diaries.add("user1", "password")
        self.assertEqual(len(self.diaries.diaries), 1)

    def test_find_diary_by_username(self):
        self.diaries.add("user1", "password")
        diary = self.diaries.find_diary_by_username("user1")
        self.assertEqual(diary.username, "user1")

    def test_delete_diary(self):
        self.diaries.add("user1", "password")
        self.diaries.add("user2", "password")
        self.diaries.delete_diary("user2", "password")
        self.assertEqual(len(self.diaries.diaries), 1)




if __name__ == '__main__':
    unittest.main()
