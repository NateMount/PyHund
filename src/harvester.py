#! /usr/bin/env python3.10

import json
import yaml
import re
import sys
from .webscraper import get_site, get
from .util import Log

#Global Variables
site_tokens = json.load(open("lib/manifest.json","r"))

#PyHund - Revision 5 harvestor
#Harvestor is used to extract data for the user and compile all data into an easily readable file

#Harvestor filetypes:

#JSON:
#Stores all text and link data into a json file. will ignore actual file data and instead look for
#url based information for content like images and videos
#Will not condense information and will have a per-user, per-site map

#CSV / TSV:
#Stores all text and link data into a csv / tsv file. will ignore actual file data instead look
#for url based information for content like images and videos
#Will not condense information and will have a page per line list

#TEXT:
#Stores all text and link data into a text file. will ignore actual file data and instead look for
#url based information for content like images and videos
#Will attempt to condense information on a per-site basis

#HTML
#Stores all text and link data into a html file. will load file data to be presented in html 
#document including pictures and videos
#Will try to condense data on a per-site basis

def harvest_clients(targets:list, scan_data:list) -> None:
	"""
	Harvest data for all clients
	"""

	_data = {}
	for _t in targets:
		_data[_t] = {}
		for _s in scan_data:
			if not _s:
				continue

			Log(_s)
			site_data:dict = get_site(_s)

			if not site_data:
				continue

			if site_data['harvester-tokens'] == {}:
				continue

			html_content = get(_s, _t).text if site_data['http-version'] == 1 else ""

			_data[_t][_s] = _harvest(_s, html_content)

	if 'json' in sys.argv:
		json.dump(_data, open('out.json','w'))
	elif 'yaml' in sys.argv:
		yaml.dump(_data, open('out.yaml', 'w'))
	else:
		print(_data)

def _harvest(site_name:str, html_content:str) -> dict:
	"""Harvest data from given website"""

	_tokens:dict = site_tokens[site_name]
	Log(_tokens)

	_data = {}

	for _tok in _tokens:
		if not _tok:
			continue

		_r = re.search(fr"{_tokens[_token]}", html_content)
		if _r:
			_data[_tok] = _r[0]

	Log(_data)

	return _data

