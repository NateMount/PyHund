#! /usr/bin/env python3.10

import re
from . import webscraper

def verify(site_name:str, site) -> bool:
	"""Used to verify if a site is a valid user response"""
	
	_data:dict = webscraper.get_site(site_name)

	if not _data:
		return False

	match site_data['verify-method']:
		case 'status':
			if 'verify-str' in _data:
				return site.status_code == int(_data['verify-str'])
			else:
				return site.status_code == 200

		case 'url':
			return _data['verify-str'] in site.url

		case 'match':
			return re.search(_data['verify-method'], site.text) != None

		case _:
			return False

