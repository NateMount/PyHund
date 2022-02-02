#! /usr/bin/env python3.9

import json
import requests as r
from bs4 import BeautifulSoup
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


def verify(site_name, site) -> bool:
	"""Used to verify if a site is a valid user response"""
    
	Log(site_name, site, sep="\n")

	#Reformatting site info for more precise data
	site_data = get_site(site_name)
	
	soup = BeautifulSoup(site.txt, 'html.parser')
	

	is_invalid = False

	for check in site_data["invalid"]:
		if check in site_text:
			is_invalid = True

	return (site.status_code == 200) and (site_data["valid"] in site_text and not is_invalid)
