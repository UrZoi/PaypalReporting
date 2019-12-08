# PaypalReporting
A paypalreporting script in monthly basis.


Script who retrivespaypal information trhoug GET request is under PaypalReporting/venv/ProjectoUno/AppUno/scripts/Test2.py

Function def monthly_data(start_date, end_date): will return transactions of paypal with below format.

'transaction_info': {
			'paypal_account_id': 'XXXXXXXXXXXXX',
			'transaction_id': 'XXXXXXXXXXXXXXXXX',
			'paypal_reference_id': 'X-XXXXXXXXXXXXXXXXX',
			'paypal_reference_id_type': 'PAP',
			'transaction_event_code': 'TXXX',
			'transaction_initiation_date': '2019-06-04T01:27:43+0000',
			'transaction_updated_date': '2019-06-04T01:27:43+0000',
			'transaction_amount': {
				'currency_code': 'MXN',
				'value': '-78.00'
			},
			'transaction_status': 'S',
			'ending_balance': {
				'currency_code': 'MXN',
				'value': '-78.00'
			},
			'available_balance': {
				'currency_code': 'MXN',
				'value': '-78.00'
			},
			'custom_field': 'XXXXXXXXX',
			'protection_eligibility': 'XX'
		}		
		
"shipping_info":{"name":"Name of ppl who will receive ","address":
	{"line1":"STREET ADRESS",
	"line2":"second adress",
	"city":" :) this is a happy face ",
	"country_code":"country code with 2 letters",
	"postal_code":" PS code"}
	}
