# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:03:49 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-testing')[0]+"/python-testing/lib")
from Direwolf import Direwolf
from Direwolf import Stark


class TestDirewolf(unittest.TestCase):
    
    def setUp(self):
        self.direwolf = Direwolf('Nymeria')
        self.shaggy_direwolf = Direwolf('Shaggydog', "Winterfell", "Smol Pupper")
        self.lady_direwolf = Direwolf('Lady', "Winterfell")
        self.john_stark = Stark('John', "King's Landing")
        self.rickon_stark = Stark('Rickon')
        self.sansa_stark = Stark('Sansa')
        self.bran_stark = Stark('Bran')
        self.arya_stark = Stark('Arya')
        self.rob_stark = Stark('Rob')
        
        
    def test_direwolf_exists_and_has_a_name(self):
        self.assertTrue(isinstance(self.direwolf, Direwolf))
        self.assertEqual(self.direwolf.name, 'Nymeria')
    
    
    def test_default_home_is_betond_the_wall(self):
        self.assertEqual(self.direwolf.home, 'Beyond the Wall')
        
        
    def test_default_size_is_massive(self):
        self.assertEqual(self.direwolf.size, 'Massive')
        
        
    def test_can_have_another_home_or_size(self):
        self.assertEqual(self.shaggy_direwolf.name, 'Shaggydog')
        self.assertEqual(self.shaggy_direwolf.home, 'Winterfell')
        self.assertEqual(self.shaggy_direwolf.size, 'Smol Pupper')
        
        
    def test_starks_exists_and_has_a_name(self):
        self.assertTrue(isinstance(self.bran_stark, Stark))
        self.assertEqual(self.bran_stark.name, 'Bran')
        
    
    def test_starks_in_winterfell_by_default(self):
        self.assertEqual(self.bran_stark.location, 'Winterfell')

                
    def test_direwolf_starts_with_no_starks_to_protect(self):
        self.assertEqual(self.direwolf.starks_to_protect, [])
        
        
    def test_protects_stark_kid(self):
        self.lady_direwolf.protects(self.arya_stark)
        self.assertEqual(len(self.lady_direwolf.starks_to_protect), 1)
        self.assertEqual(self.lady_direwolf.starks_to_protect, [self.arya_stark])
        self.assertEqual(self.lady_direwolf.starks_to_protect[0], self.arya_stark)
    
    
    def test_can_only_protect_if_home_and_location_match(self):
        self.assertEqual(self.direwolf.home, 'Beyond the Wall')
        self.assertEqual(self.john_stark.location, "King's Landing")
        
        self.direwolf.protects(self.john_stark)
        self.assertEqual(self.direwolf.starks_to_protect, [])
        
        
    def test_direwolf_can_only_protect_two_at_a_time(self):
        self.shaggy_direwolf.protects(self.sansa_stark)
        self.shaggy_direwolf.protects(self.rickon_stark)
        self.lady_direwolf.protects(self.rob_stark)
        self.lady_direwolf.protects(self.bran_stark)
        self.lady_direwolf.protects(self.arya_stark)
    
        self.assertEqual(self.shaggy_direwolf.starks_to_protect, [self.sansa_stark, self.rickon_stark])
        self.assertEqual(self.lady_direwolf.starks_to_protect, [self.rob_stark, self.bran_stark])
        self.assertFalse(self.arya_stark in self.lady_direwolf.starks_to_protect)
        
        
    def test_starks_start_off_unsafe(self):
        self.assertFalse(self.rob_stark.safe)
        
    
    def test_starks_have_house_words(self):
        self.assertEqual(self.rob_stark.house_words(), 'Winter is Coming')
    
    
    def test_stark_safe_status_and_house_words_change_after_protected(self):
        self.lady_direwolf.protects(self.arya_stark)
        
        self.assertTrue(self.arya_stark.safe)
        self.assertFalse(self.sansa_stark.safe)
        self.assertEqual(self.arya_stark.house_words(), 'The North Remembers')
        self.assertEqual(self.sansa_stark.house_words(), 'Winter is Coming')
        
        
    def test_direwolf_hunts_white_walkers(self):
        self.assertTrue(self.shaggy_direwolf.hunts_white_walkers())
    
    
    def test_doesnt_hunt_white_walkers_if_protecting(self):
        self.shaggy_direwolf.protects(self.rickon_stark)
        self.assertFalse(self.shaggy_direwolf.hunts_white_walkers())
        
        
    def test_direwolf_can_leave_and_stop_protecting(self):
        self.lady_direwolf.protects(self.rob_stark)
        self.shaggy_direwolf.protects(self.rickon_stark)
        self.shaggy_direwolf.leave(self.rickon_stark)
        
        self.assertEqual(self.lady_direwolf.starks_to_protect, [self.rob_stark])
        self.assertEqual(self.shaggy_direwolf.starks_to_protect, [])
        self.assertFalse(self.rickon_stark.safe)
    
    
    
if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestDirewolf))

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
