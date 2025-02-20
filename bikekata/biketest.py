import unittest

import bike


class BikeTest(unittest.TestCase):
    def setUp(self):
        self.bike = bike.Bike()

    def test_turn_bike_on(self):
        self.bike.turn_on()
        self.assertTrue(self.bike.get_status(), "Bike should be on")

    def test_turn_bike_off(self):
        self.bike.turn_on()
        self.bike.Turn_off()
        self.assertFalse(self.bike.get_status(), "Bike should be off")

    def test_accelerate_gear_is_1(self):
        self.bike.turn_on()
        self.bike.speed = 15
        self.bike.gear = 1
        self.bike.accelerate()
        self.assertEqual(self.bike.get_speed(),  16,"Bike should speed should increase by 1 in gear 1")

    def test_accelerate_gear_is_2(self):
        self.bike.turn_on()
        self.bike.speed = 24
        self.bike.gear = 2
        self.bike.accelerate()
        self.assertEqual(self.bike.get_speed(), 26, "Bike should speed should increase by 2 in gear 2")

    def test_accelerate_gear_is_3(self):
        self.bike.turn_on()
        self.bike.speed = 35
        self.bike.gear = 3
        self.bike.accelerate()
        self.assertEqual(self.bike.get_speed(), 38, "Bike should speed should increase by 3 in gear 3")

    def test_decelerate_gear_is_4(self):
        self.bike.turn_on()
        self.bike.speed = 44
        self.bike.gear = 4
        self.bike.decelerate()
        self.assertEqual(self.bike.get_speed(), 40, "Bike should speed should decrease by 4 in gear 4")

    def test_that_gear_can_change_when_i_accelerate(self):
        self.bike.turn_on()
        self.bike.speed = 20
        self.bike.gear = 2
        self.bike.accelerate()
        self.assertEqual(self.bike.get_gear(), 2, "gear should change to 2 when speed exceeds 20")
        self.assertEqual(self.bike.get_speed(), 22, "Speed should be 22 after acceleration")

    def test_that_gear_can_change_when_i_decelerate(self):
        self.bike.turn_on()
        self.bike.speed = 21
        self.bike.gear = 2
        self.bike.decelerate()
        self.assertEqual(self.bike.get_gear(), 1, "gear should change to 1 when speed drops 20")
        self.assertEqual(self.bike.get_speed(), 19, "Speed should be 19 after deceleration")



if __name__ == '__main__':
    unittest.main()
