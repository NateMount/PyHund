#! /usr/bin/env python3.9

import json
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


def get_hyper(site_name:str, username:str):
	"""get site using hyper from name and target username"""

	raise NotImplementedError


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
