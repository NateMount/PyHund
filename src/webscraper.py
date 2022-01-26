#! /usr/bin/env python3.9

import json
import requests as r
from src.util import Log

#TODO remove after no longer needed
#spoof_head:dict = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9","Sec-Fetch-User": "?1","Upgrade-Insecure-Requests": "1",'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
site_index:dict = json.load(open("lib/manifest.json","r"))

def get_site(site_name:str) -> dict:
	"""Retrieve site data if avalible"""
	try:
		return site_index[site_name]
	except KeyError:
		Log(site_name)
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
		Log(site_data)
		return None


def verify(site_name, site) -> bool:
	"""Used to verify if a site is a valid user response"""
    
	Log(site_name, site, sep="\n")

	#Reformatting site info for more precise data
	site_data = get_site(site_name)
	site_text = site.text.replace('\n', '')

	is_invalid = False

	for check in site_data["invalid"]:
		if check in site_text:
			is_invalid = True

	return (site.status_code == 200) and (site_data["valid"] in site_text and not is_invalid)
