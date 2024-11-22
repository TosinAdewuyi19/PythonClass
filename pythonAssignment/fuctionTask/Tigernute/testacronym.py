from unittest import TestCase
import acronym

class TestGetAcronymFunction(TestCase):
    def test_that_get_acronym_function_exists(self):
        word = ["Portable Network Service"]
        acronym.get_acronym(word)
