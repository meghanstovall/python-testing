# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:16:18 2020

@author: Meghan Stovall
"""

import unittest
import sys, os
sys.path.append(os.path.abspath(__file__).split('python-testing')[0]+"/python-testing/lib")


class CLASSNAME(unittest.TestCase):



if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(   CLASSNAME   ))

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
