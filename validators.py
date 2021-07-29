from email_validator import validate_email, EmailNotValidError

import datetime
import re


def get_field_type(string):
	if _validate_date(string):
		return 'date'

	if _validate_phone_number(string):
		return 'phone_number'

	if _validate_mail(string):
		return 'email'

	return 'text'

def _validate_date(date_string):
	try:
		datetime.datetime.strptime(date_string, '%d.%m.%Y')
	except ValueError:
		pass
	else:
		return True

	try:
		datetime.datetime.strptime(date_string, '%Y-%m-%d')
	except ValueError:
		return False
	else:
		return True

def _validate_phone_number(phone_number_string):
	if re.match(r'7 \d{3} \d{3} \d{2} \d{2}', phone_number_string[1:]):
		return True
	else:
		return False

def _validate_mail(email_string):
	try:
		validate_email(email_string)
	except EmailNotValidError:
		return False
	else:
		return True