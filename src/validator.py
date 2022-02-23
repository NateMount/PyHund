#! /usr/bin/env python3

import re
from . import webscraper

def verify(site_name:str, site) -> bool:
	"""Used to verify if a site is a valid user response"""
	
	site_data:dict = webscraper.get_site(site_name)
	
	if site_data['verify-method'] == 'status':
		return site.status_code == 200
	elif site_data['verify-method'] == 'url':
		return site_data['valid-str'] in site.url
	elif site_data['verify-method'] == 'match':
		return re.search(site_data['verify-method'], site.text) != None
	else:
		return False
