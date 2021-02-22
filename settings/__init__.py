"""settings
"""

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-2-22"

class settings:
	def __init__ (self):
		"""Where it all begins
		"""
		print(settings.settings())
	
	def settings():
		"""settings first funtion
		"""
		return "settings" #for the test (see test_settings.py)
		
if __name__ == "__main__":
	settings()
