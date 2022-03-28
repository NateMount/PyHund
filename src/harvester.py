#! /usr/bin/env python3

import json
import re
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

def harvest(site_name:str, html_content:str) -> dict:
	"""Harvest data from given website"""

	tokens:dict = site_tokens[site_name]
	Log(_tokens)

	_data:dict = {_token : re.search(_tokens[token], html_content) for _token in _tokens if _token}

	Log(_data)

	return _data


def _html(data:dict) -> None:
	"""Generates html document from dict"""
	raise NotImplementedError

def _sv(data:dict, delimeter:str = ',') -> None:
	"""Generates csv/tsv file from dict"""
	raise NotImplementedError

def _txt(data:dict) -> None:
	"""Generates a text file from dict"""
	raise NotImplementedError

def _json(data:dict) -> None:
	"""Generates json document from dict"""
	json.dump(data, open('out.json', 'w'))
