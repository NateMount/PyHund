#! /usr/bin/env python3

import re

def make_dl_target(target:str, **kwargs) -> dict:
	"""Used to make a DeepLink target"""
	return {'target':target, **kwargs}	#NOTE need to format and sanitize input

class DeepLinkControler:

	def __init__(self, *args):
		self.args:list = args

		self.target:dict = None

	def set_target(self, target:str, **kwargs) -> None:
		"""Sets active tracking target"""
		self.target = make_dl_target(target, **kwargs)

	@staticmethod
	def _load_dl_profiles(path:str):
		"""Internal Use Only : Loads DeepLink profiles data"""	
		profiles:dict = {}

		dl_file_data:str = open(path, 'r').read()
		
