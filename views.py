from flask import Blueprint, render_template, request, redirect, url_for
#from . import crud
from .__init__ import db
from .models import Lists, Items
import time
main = Blueprint('main', __name__)


@main.route('/')
def index():
	lists =  Lists.query.all()
	list_name = [i.name for i in lists]
	db.session.close()
	return render_template('homepage.html', lists=list_name)

@main.route('/list', methods=['POST'])
def list():
	#db.session.close()
	name = request.form.get('chooselist')
	list_choice = Lists.query.filter_by(name = name).one()
	items = [i.name for i in list_choice.item]
	db.session.close()
	return render_template('list.html', items=items, name=name)

@main.route('/list_post/<name>', methods=['POST'])
def list_post(name):
	#db.session.close()
	list = Lists.query.filter_by(name = name).first()
	list_item = request.form.get('items')
	
	if list_item:
		new_item = Items(name = list_item, list_name = list)
		db.session.add(new_item)
		db.session.commit()
		load_list = Lists.query.filter_by(name = name).first()
		items = [i.name for i in load_list.item]
		db.session.close()

	return render_template('list.html',items=items, name=name)

@main.route('/drop_down_remove/<name>', methods=['POST'])
def drop_down(name):
	#db.session.close()
	list = Lists.query.filter_by(name = name).one()
	list_item = request.form.get('drop_down')
	if list_item:
		remove_item = Items.query.filter_by(name = list_item,list_id = list.id).one()
		db.session.delete(remove_item)	
		db.session.commit()
		try:
			load_items = Items.query.filter_by(list_id=list.id).all()
			items = [i.name for i in load_items]
			db.session.close()
		except:
			pass
		
	return render_template('list.html', name = name, items = items)

@main.route('/create_list', methods=['POST'])
def create_list():
	#format the list/item to make sure there are no spaces at the very end.
	#db.session.close()
	name = request.form.get('new_list')
	add_list = Lists(name = name)
	db.session.add(add_list)
	db.session.commit()
	load_lists = Lists.query.all()
	list_item = Lists.query.filter_by(name = name).first()
	list_id = list_item.id
	list_name = [i.name for i in load_lists]
	items = [i.name for i in list_item.item]
	db.session.close()


	return render_template('homepage.html',name = name, lists = list_name)

@main.route('/delete_list', methods=['POST'])
def delete_list():
	#db.session.close()
	name = request.form.get('current_lists')
	remove = Lists.query.filter_by(name = name).first()
	for i in remove.item:
		removing = Items.query.filter_by(id = i.id).first()
		db.session.delete(removing)

	db.session.delete(remove)
	db.session.commit()
	db.session.close()
	load_lists = Lists.query.all()
	lists = [i.name for i in load_lists]
	return render_template('homepage.html', lists=lists)

