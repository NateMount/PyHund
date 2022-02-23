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

	return NotImplementedError


def get(site_name:str, username:str):
	"""get site from name and target username"""

	site_data:dict = get_site(site_name)

	#TODO Simplify
	try:
		site_head = site_data["headers"]
	except KeyError:
		site_head = {}

	try:
		return r.get(site_data["url"].format(username), headers=site_head)
	except r.ConnectionError:
		return None
