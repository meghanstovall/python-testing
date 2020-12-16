# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:24:58 2020

@author: Meghan Stovall
"""

class Centaur:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.cranky = False
        self.standing = True
        self.laying = False
        self.rested = False
        self.sick = False


    def shoot(self):
        if self.cranky or self.laying:
            return "NO!"
        return "Twang!!!"


    def run(self):
        if self.cranky or self.laying:
            return "NO!"
        return "Clop clop clop clop!!!"


    def ran_or_shot_three_times(self):
        self.cranky = True


    def sleep(self):
        if self.standing:
            return "NO!"
        self.cranky = False


    def lay_down(self):
        self.standing = False
        self.laying = True


    def stand_up(self):
        self.laying = False
        self.standing = True


    def drink_potion(self):
        if self.laying:
            return "NO!"
        elif self.rested:
            self.sick = True 
        self.rested = True
