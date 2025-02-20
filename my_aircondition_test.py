import unittest

import my_aircondition


class TestMyAircondition(unittest.TestCase):
    def setUp(self):
        self.ac = my_aircondition.AirCondition()

    def test_turn_on(self):
        self.ac.turn_on()
        self.assertTrue(self.ac.get_status())

    def test_turn_off(self):
        self.ac.turn_on()
        self.ac.turn_off()
        self.assertFalse(self.ac.get_status())

    def test_increase_temperature(self):
        self.ac.turn_on()
        self.ac.get_temperature()
        self.ac.increase_temperature()
        self.assertTrue(self.ac.get_status())

    def test_decrease_temperature(self):
        self.ac.turn_on()
        self.ac.get_temperature()
        self.ac.decrease_temperature()
        self.assertTrue(self.ac.get_status())




if __name__ == '__main__':
    unittest.main()
