# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:16:18 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-testing')[0]+"/python-testing/lib")
from Centaur import Centaur


class TestCentaur(unittest.TestCase):
    
    def setUp(self):
        self.centaur = Centaur("George", "Palomino")

    def test_exists_and_has_attributes(self):
        self.assertTrue(isinstance(self.centaur, Centaur))
        self.assertEqual(self.centaur.name, "George")
        self.assertEqual(self.centaur.breed, "Palomino")


    def test_has_excellent_bow_skills(self):
        self.assertEqual(self.centaur.shoot(), "Twang!!!")


    def test_makes_horse_sound_when_runs(self):
        self.assertEqual(self.centaur.run(), "Clop clop clop clop!!!")


    def test_not_cranky_when_created(self):
        self.assertFalse(self.centaur.cranky)


    def test_standing_when_created(self):
        self.assertTrue(self.centaur.standing)


    def test_after_running_or_shooting_bow_three_times_it_gets_cranky(self):
        self.assertFalse(self.centaur.cranky)
        self.centaur.shoot()
        self.centaur.run()
        self.centaur.shoot()
        self.centaur.ran_or_shot_three_times()
        self.assertTrue(self.centaur.cranky)


    def test_wont_shoot_if_cranky(self):
        self.centaur.shoot()
        self.centaur.run()
        self.centaur.shoot()
        self.centaur.ran_or_shot_three_times()
        self.assertTrue(self.centaur.cranky)
        self.assertEqual(self.centaur.shoot(), "NO!")


    def test_wont_run_if_cranky(self):
        self.centaur.shoot()
        self.centaur.run()
        self.centaur.shoot()
        self.centaur.ran_or_shot_three_times()
        self.assertTrue(self.centaur.cranky)
        self.assertEqual(self.centaur.run(), "NO!")


    def test_wont_sleep_if_standing(self):
        self.assertEqual(self.centaur.sleep(), "NO!")


    def test_after_laying_its_not_standing(self):
        self.centaur.lay_down()
        self.assertFalse(self.centaur.standing)
        self.assertTrue(self.centaur.laying)


    def test_when_laying_it_cant_shoot(self):
        self.centaur.lay_down()
        self.assertEqual(self.centaur.shoot(), "NO!")


    def test_when_laying_it_cant_run(self):
        self.centaur.lay_down()
        self.assertEqual(self.centaur.run(), "NO!")


    def test_it_can_stand_up(self):
        self.centaur.lay_down()
        self.centaur.stand_up()
        self.assertFalse(self.centaur.laying)
        self.assertTrue(self.centaur.standing)


    def test_not_cranky_after_sleeping(self):
        self.centaur.shoot()
        self.centaur.run()
        self.centaur.shoot()
        self.centaur.ran_or_shot_three_times()
        self.assertTrue(self.centaur.cranky)

        self.centaur.lay_down()
        self.centaur.sleep()
        self.assertFalse(self.centaur.cranky)


    def test_becomes_rested_after_drinking_potion(self):
        self.centaur.drink_potion()
        self.assertTrue(self.centaur.rested)


    def test_can_only_drink_if_standing(self):
        self.centaur.lay_down()
        self.assertEqual(self.centaur.drink_potion(), "NO!")
        self.assertFalse(self.centaur.rested)

        self.centaur.stand_up()
        self.centaur.drink_potion()
        self.assertTrue(self.centaur.rested)


    def test_gets_sick_if_drinks_while_rested(self):
        self.centaur.stand_up()
        self.centaur.drink_potion()
        self.centaur.drink_potion()
        self.assertTrue(self.centaur.sick)


if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestCentaur))

    runner = unittest.TextTestRunner(verbosity = 1)
    f = runner.run(suite)
    if len(f.failures)>0 and len(f.errors)>0:
        raise Exception(str(len(f.failures))+ " Failures and " + str(len(f.errors))+ " Errors")
    if len(f.failures)>0:
        raise Exception(str(len(f.failures))+ " Failures")
    if len(f.errors)>0:
        raise Exception(str(len(f.errors))+ " Errors")
    if len(f.failures) == 0 and len(f.errors) == 0:
        print("All tests passed")
