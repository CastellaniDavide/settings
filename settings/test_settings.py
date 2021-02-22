"""Test settings file
"""
from settings import *

__author__ = "help@castellanidavide.it"
__version__ = "2.0 2020-08-18"

def test():
	"""Tests the settings function in the settings class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert settings.settings() == "settings", "test failed"
	#assert settings.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
