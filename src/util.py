#! /usr/bin/env python3
#PyHund-r5 : util module

import sys

def Log(*args, **kwargs):
	"""Will display data to the screen if debug enabled"""
	if "debug" in sys.argv:
		print(*args, **kwargs)
