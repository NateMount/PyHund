#! /usr/bin/env python3.9

import json
import re
import requests as r
from src.util import Log

#TODO remove after no longer needed
site_index:dict = json.load(open("lib/manifest.json","r"))

def get_site(site_name:str) -> dict:
	"""Retrieve site data if avalible"""
	try:
		return site_index[site_name]
	except KeyError:
		return None


def get(site_name:str, username:str):
	"""get site from name and target username"""

	site_data:dict = get_site(site_name)

	try:
		_h = site_data["headers"]
	except KeyError:
		_h = {}
	
	try:
		_c = site_data["cookies"]
	except KeyError:
		_c = {}

	try:
		return r.get(site_data["url"].format(username), headers=_h, cookies=_c)
	except r.ConnectionError:
		return None


def verify(site_name:str, site) -> bool:
	"""Used to verify a site's response data"""

	_d:dict = get_site(site_name)

	if not _d:
		return False
	
	match _d['verify-method']:
		case 'status':
			return site.status_code == int(_d['verify-str']) if 'verify-str' in _d else site.status_code == 200
		case 'url':
			return _d['verify-str'] in site.url
		case 'match':
			return re.search(_data['verify-method'], site.text) != None
		case _:
			return False
