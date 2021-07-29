from tinydb import TinyDB, Query, where

from validators import get_field_type

db = TinyDB('db.json')

sent_form = {
			"user_email": "blabla@gmail.com",
            "phone_number": "+7 555 555 55 55",
            "order_date": "01.01.2000" 
		}

db_commotn_keys = {'user_email', 'phone_number', 'order_date'}

def main():
	TamplateForm = Query()
	sent_form_keys = list(sent_form.keys())

	existing_keys = db_commotn_keys.intersection(sent_form_keys)
	t_forms_list = []

	for key in existing_keys:
		items = db.search(where(key).exists())
		for item in items:
			if item not in t_forms_list:
				t_forms_list.append(item)

	t_forms_list = [item for item in t_forms_list if len(set(item).intersection(existing_keys)) == len(existing_keys)]
	for item in t_forms_list:
		for key in existing_keys:
			if get_field_type(item[key]) != get_field_type(sent_form[key]):
				t_forms_list.remove(item)

	print(*[i['name'] for i in t_forms_list])
	






if __name__ == '__main__':
	main()