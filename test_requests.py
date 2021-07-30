import requests

params_list = [
	{
	'expected_result': ['Tamplate Form 3'],
	'params': {
		"user_email": "blabla@gmail.com",
		"phone_number": "+7 555 555 55 55",
		"order_date": "01.01.2000",
		"message": "Some message text"
		}
	},

	{
	'expected_result': ['Tamplate Form 3', 'Tamplate Form 5'],
	'params': {
		"phone_number": "+7 555 555 55 55",
		"order_date": "2000-01-01",
		"message": "Some message text"
		}
	},
	{
	'expected_result': {'order_date': 'date', 'phone_number': 'phone_number', 'user_email': 'text'},
	'params': {
		"user_email": "blabla@@gmail.com", #invalid email
		"phone_number": "+7 555 555 55 55",
		"order_date": "2000-01-01"
		}
	},
	{
	'expected_result':  {'message': 'text', 'order_date': 'date', 'phone_number': 'text', 'user_email':'email'},
	'params': {
		"user_email": "blabla@gmail.com",
		"phone_number": "+8 555 555 55 55", #invalid phone number
		"order_date": "2000-01-01",
		"message": "Some message text"
		}
	},
	{
	'expected_result':  {'message': 'text', 'order_date': 'text', 'phone_number': 'phone_number', 'user_email': 'email'},
	'params': {
		"user_email": "blabla@gmail.com",
		"phone_number": "+7 555 555 55 55", 
		"order_date": "01-01-2000", #invalid date
		"message": "Some message text"
		}
	},
	{
	'expected_result':  {'email': 'email', 'message': 'text', 'order_date': 'text', 'phone_number': 'phone_number'},
	'params': {
		"email": "blabla@gmail.com", #different field name
		"phone_number": "+7 555 555 55 55", 
		"order_date": "01-01-2000", 
		"message": "Some message text"
		}
	}
]
def main():
	for params in params_list:
		response = requests.post('http://127.0.0.1:5000/get_form', params=params['params'])
		result = 'Test passed' if response.json() == params['expected_result'] else 'Test failed'

		print('------')
		print(result)
		print()
		print('Sent data:', params['params'])
		print()
		print('Recieved data:', response.json())
		print('------')


if __name__ == '__main__':
	main()