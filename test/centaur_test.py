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

    def test_exists_and_has_attributes(self):
        centaur = Centaur("George", "Palomino")
        self.assertTrue(isinstance(centaur, Centaur))
        self.assertEqual(centaur.name, "George")
        self.assertEqual(centaur.breed, "Palomino")


    def test_has_excellent_bow_skills(self):
        centaur = Centaur("George", "Palomino")
        self.assertEqual(centaur.shoot(), "Twang!!!")


    def test_makes_horse_sound_when_runs(self):
        centaur = Centaur("George", "Palomino")
        self.assertEqual(centaur.run(), "Clop clop clop clop!!!")


    def test_not_cranky_when_created(self):
        centaur = Centaur("George", "Palomino")
        self.assertFalse(centaur.cranky)


    def test_standing_when_created(self):
        centaur = Centaur("George", "Palomino")
        self.assertTrue(centaur.standing)


    def test_after_running_or_shooting_bow_three_times_it_gets_cranky(self):
        centaur = Centaur("George", "Palomino")
        self.assertFalse(centaur.cranky)
        centaur.shoot()
        centaur.run()
        centaur.shoot()
        centaur.ran_or_shot_three_times()
        self.assertTrue(centaur.cranky)


    def test_wont_shoot_if_cranky(self):
        centaur = Centaur("George", "Palomino")
        centaur.shoot()
        centaur.run()
        centaur.shoot()
        centaur.ran_or_shot_three_times()
        self.assertTrue(centaur.cranky)
        self.assertEqual(centaur.shoot(), "NO!")


    def test_wont_run_if_cranky(self):
        centaur = Centaur("George", "Palomino")
        centaur.shoot()
        centaur.run()
        centaur.shoot()
        centaur.ran_or_shot_three_times()
        self.assertTrue(centaur.cranky)
        self.assertEqual(centaur.run(), "NO!")


    def test_wont_sleep_if_standing(self):
        centaur = Centaur("George", "Palomino")
        self.assertEqual(centaur.sleep(), "NO!")


    def test_after_laying_its_not_standing(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down()
        self.assertFalse(centaur.standing)
        self.assertTrue(centaur.laying)


    def test_when_laying_it_cant_shoot(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down()
        self.assertEqual(centaur.shoot(), "NO!")


    def test_when_laying_it_cant_run(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down()
        self.assertEqual(centaur.run(), "NO!")


    def test_it_can_stand_up(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down()
        centaur.stand_up()
        self.assertFalse(centaur.laying)
        self.assertTrue(centaur.standing)


    def test_not_cranky_after_sleeping(self):
        centaur = Centaur("George", "Palomino")
        centaur.shoot()
        centaur.run()
        centaur.shoot()
        centaur.ran_or_shot_three_times()
        self.assertTrue(centaur.cranky)

        centaur.lay_down()
        centaur.sleep()
        self.assertFalse(centaur.cranky)


    def test_becomes_rested_after_drinking_potion(self):
        centaur = Centaur("George", "Palomino")
        centaur.drink_potion()
        self.assertTrue(centaur.rested)


    def test_can_only_drink_if_standing(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down()
        self.assertEqual(centaur.drink_potion(), "NO!")
        self.assertFalse(centaur.rested)

        centaur.stand_up()
        centaur.drink_potion()
        self.assertTrue(centaur.rested)


    def test_gets_sick_if_drinks_while_rested(self):
        centaur = Centaur("George", "Palomino")
        centaur.stand_up()
        centaur.drink_potion()
        centaur.drink_potion()
        self.assertTrue(centaur.sick)


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
