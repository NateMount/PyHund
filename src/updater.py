#! /usr/bin/env python3
#PyHund-R5 : Updater

import sys, os
import requests as r
from src.util import Log

def update():
	"""Attempts to update the PyHund client"""

	#Opening the version info file
	ver_c:list[str] - open('version','r').read().split('\n')
	
	print("\033[1;91mChecking for updates...\033[0;0m") #NOTE Could add Rich for extra flare

	try:
		ver_r:str = r.get('https://raw.githubusercontent.com/NateMount/PyHund/main/version').text
		Log(ver_r)
		if ver_r[0] in ver_c:
			print("\033[1;92mPyHund up to date\033[0;0m")
		else:
			print("\033[1;96mNew version detected\033[0;0m")

	except:

		print("\033[1;93m[Warning]\033[1;96m: Remote update source not avalible\033[0;0m")
		sys.exit()
