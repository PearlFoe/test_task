from flask import Flask, request, jsonify

from validators import get_field_type

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/get_form', methods=['GET', 'POST'])
def get_form_data():
	sent_form = request.args
	sent_from_keys = sent_form.keys()


    return jsonify(request.args)