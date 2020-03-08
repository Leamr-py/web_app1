from flask import Blueprint, render_template, request, redirect, url_for
import json
import os
from . import crud
import sys

main = Blueprint('main', __name__)

#cannot define function and use in a route. try creating a module of functions and importing

@main.route('/')
def index():
	lists = crud.read_lists()
	return render_template('homepage.html', lists=lists)


@main.route('/list', methods=['POST'])
def list():
	name = request.form.get('chooselist')
	items = crud.open_file(name)
	return render_template('list.html', items=items, name=name)

@main.route('/list_post/<name>', methods=['POST'])
def list_post(name):

	items = crud.open_file(name)
	list_item = request.form.get('items')
	if list_item:
		items.append(f'{list_item}')
	crud.append_file(name, items)
	return render_template('list.html',items=items, name=name)

@main.route('/drop_down_remove/<name>', methods=['POST'])
def drop_down(name):
	
	items = crud.open_file(name)
	list_remove = request.form.get('drop_down')
	if list_remove:
		items.remove(f'{list_remove}')
	crud.append_file(name, items)
	return render_template('list.html', items=items, name=name)

@main.route('/create_list', methods=['POST'])
def create_list():
	name = request.form.get('new_list')
	crud.append_file(name, [])
	
	lists = crud.read_lists()
	lists.append(f'{name}')
	crud.append_lists(lists)
	items = crud.open_file(name)
	return render_template('list.html', items=items, name=name)

@main.route('/delete_list', methods=['POST'])
def delete_list():
	name = request.form.get('current_lists')
	try:
		os.remove('/Users/austin/src/web_app/lists/' + name + '.json')
		lists = crud.read_lists()
		lists.remove(f'{name}')
		crud.append_lists(lists)
		return render_template('homepage.html', lists=lists)
	except FileNotFoundError:
		lists =  crud.read_lists()
		return render_template('homepage.html', lists=lists)
	except TypeError:
		lists = crud.read_lists()
		return render_template('homepage.html', lists=lists)

