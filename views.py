from flask import Blueprint, render_template, request, redirect, url_for
import json
import os


main = Blueprint('main', __name__)


@main.route('/')
def index():
	#with open('list.json') as file:
	#	items = json.load(file)
	with open('lists.json') as file:
		try:
			lists = json.load(file)
		except:
			lists = ''
	return render_template('homepage.html', lists=lists)

@main.route('/list', methods=['POST'])
def list():
	name = request.form.get('chooselist')
	with open('/Users/austin/src/web_app/lists/' + name + '.json') as file:
		items = json.load(file)
	return render_template('list.html', items=items, name=name)

@main.route('/list_post', methods=['POST'])
def list_post():
	name = request.form.get('names')
	with open('/Users/austin/src/web_app/lists/' + name + '.json') as file:
		items = json.load(file)
	list_item = request.form.get('items')
	if list_item:
		items.append(f'{list_item}')
	with open('/Users/austin/src/web_app/lists/' + name + '.json', 'w') as file:
		json.dump(items, file)
	return render_template('list.html',items=items, name=name)

@main.route('/drop_down_remove', methods=['POST'])
def drop_down():
	name = request.form.get('names')
	with open('/Users/austin/src/web_app/lists/' + name + '.json') as file:
		items = json.load(file)
	list_remove = request.form.get('drop_down')
	if list_remove:
		items.remove(f'{list_remove}')
	with open('/Users/austin/src/web_app/lists/' + name + '.json', 'w') as file:
		json.dump(items, file)
	return render_template('list.html', items=items, name=name)

@main.route('/create_list', methods=['POST'])
def create_list():
	name = request.form.get('new_list')
	with open('/Users/austin/src/web_app/lists/' + name + '.json', 'w') as file:
		json.dump([], file)
	
	with open('lists.json') as file:
		lists = json.load(file)
		lists.append(f'{name}')
	with open('lists.json', 'w') as file:
		json.dump(lists, file)
	with open('/Users/austin/src/web_app/lists/' + name + '.json') as file:
		items = json.load(file)
	return render_template('list.html', items=items, name=name)

@main.route('/delete_list', methods=['POST'])
def delete_list():
	name = request.form.get('current_lists')
	try:
		os.remove('/Users/austin/src/web_app/lists/' + name + '.json')
		with open('lists.json') as file:
			lists = json.load(file)
			lists.remove(f'{name}')
		with open('lists.json', 'w') as file:
			json.dump(lists, file)
		return render_template('homepage.html', lists=lists)
	except FileNotFoundError:
		with open('lists.json') as file:
			lists = json.load(file)
		return render_template('homepage.html', lists=lists)
	except TypeError:
		with open('lists.json') as file:
			lists = json.load(file)
		return render_template('homepage.html', lists=lists)
	

