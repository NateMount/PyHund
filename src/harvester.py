#! /usr/bin/env python3

import json
import bs4
from src.util import Log

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
	"""
	Harvest
	Used to harvest user data from provided html file
	will use harvester tokens to identify important data
	:param html_content: string containing all html data of the page
	:returns: dictionary containing all parsed content
	"""

	data:dict = {}
	tokens:dict = site_tokens[site_name]
	Log(tokens)

	for token_set in tokens:
		Log(token_set, tokens[token_set])

		segment:str = html_content.split(tokens[token_set][0])[-1].split(tokens[token_set][-1])[0]

		data[token_set] = segment

	Log(data)

	return data


def form_html(data:dict):
	"""Generates html document from dict"""
	pass
