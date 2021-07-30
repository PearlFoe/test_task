from flask import Flask, request, jsonify
from tinydb import TinyDB, Query, where

from validators import get_field_type

import copy

app = Flask(__name__)
db = TinyDB('db.json')

db_common_keys = {'user_email', 'phone_number', 'order_date'}

@app.route('/get_form', methods=['GET', 'POST'])
def get_form_data():
	if request.method == 'GET':
		return jsonify([])

	sent_form = dict(request.args)
	sent_form_keys = list(sent_form.keys())
	existing_keys = db_common_keys.intersection(sent_form_keys)

	t_forms_list = []
	for key in existing_keys:
		items = db.search(where(key).exists())
		for item in items:
			if item not in t_forms_list:
				t_forms_list.append(item)

	for item in copy.copy(t_forms_list):
		if len(set(item).intersection(existing_keys)) != len(existing_keys):
			t_forms_list.remove(item)
			continue 

		for key in existing_keys:
			if item[key] != get_field_type(sent_form[key]):
				t_forms_list.remove(item)

	if len(t_forms_list) > 0:
		return jsonify([i['name'] for i in t_forms_list])
	else:
		for (filed_name, field_value) in sent_form.items():
			sent_form[filed_name] = get_field_type(field_value)
			
		return jsonify(sent_form)