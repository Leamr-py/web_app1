import json
from flask import render_template
import os

def read_lists():
	with open('lists.json') as file:
		lists = json.load(file)
	return lists
def append_lists(lists):
	with open('lists.json', 'w') as file:
		json.dump(lists, file)


def open_file(file_name):
	with open('/Users/austin/src/web_app/lists/' + file_name + '.json') as file:
		items = json.load(file)
	return items

def append_file(file_name, items):
	with open('/Users/austin/src/web_app/lists/' + file_name + '.json', 'w') as file:
		json.dump(items, file)

