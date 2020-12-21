# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:04:37 2020

@author: Meghan Stovall
"""


class Direwolf:
    def __init__(self, name, home = 'Beyond the Wall', size = 'Massive'):
        self.name = name
        self.home = home
        self.size = size
        self.starks_to_protect = []
        
    
    def protects(self, stark):
        if self.home == stark.location and len(self.starks_to_protect) < 2:
            self.starks_to_protect.append(stark)
            stark.safe = True
    
    
    def hunts_white_walkers(self):
        if len(self.starks_to_protect) > 0:
            return False
        return True
    
    
    def leave(self, stark):
        self.starks_to_protect.remove(stark)
        stark.safe = False
    
    
    
class Stark:
    def __init__(self, name, location = 'Winterfell'):
        self.name = name
        self.location = location
        self.safe = False
        
        
    def house_words(self):
        if self.safe:
            return 'The North Remembers'
        return 'Winter is Coming'
    