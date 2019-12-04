

def monthly_difference():
    print("""In this function is really not necessary this point so i just will comment this shit and 
    let this shit begin
    I want to call to this phase the learning part of how to use Django with some interesting API
        """)


def dbinsertion():
    print("""This function will insert all our data in different tables, based on the flag it will  decide which table 
    will be used, at this moment we have 3 different  all monthly data, segregated data, report data.""")


def segregation():
    print("""Here we have the fuction to segregate the Monthly data based in thier description and also the 
    Address and credit card used for the transaction.""")


def reconciliation():
    print("""This fuction will compare all the transaction retrieved in a month, if this return a number greater than 0
    that means we have transaction missed in the last report...""")


def get_dates():
    """How can i get the dates.... easy peace tu jefa en bici, i jsut need to check the last date in my DB and then
    Start from last date available till today date"""
    dates = []
    return dates


def monthly_data(start_date, end_date):
    import requests
    import json
    import re
    from datetime import datetime
    from datetime import timedelta

    headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en_US',

        }

    data = [
        ('grant_type', 'client_credentials'),
    ]

    response = requests.post('https://api.paypal.com/v1/oauth2/token',
                             headers=headers,
                             data=data,
                             auth=('Here should be your auth from Paypal :) '))
    data = json.loads(response.text)
    print(data)

    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + data['access_token'],
    }
    params = (
        ('start_date', start_date),  # dates must look like this: '2018-06-10T23:20:50.52Z'
        ('end_date', end_date),
        ('page_size', 5),
        ('fields', 'transaction_info, shipping_info'),  # all
    )
    Datas = []
    response2 = requests.get('https://api.paypal.com/v1/reporting/transactions', headers=headers2, params=params)
    print(response2.status_code)
    print(response2.text)

    Datas.append(json.loads(response2.text))


    if int(Datas[0]['total_items']) > 100:
        print(Datas[0]['links'][0].keys())
        print (len(Datas[0]['links']))
        for i in range(len(Datas[0]['links'] )- 2 ):
            #print(data2['links'][i]['href'])
            response2 =  requests.get(Datas[0]['links'][i]['href'], headers=headers2)
            #print(response2.text)
            Datas.append(json.loads(response2.text))
    print(Datas[0]['total_items'])
    print(len(Datas))
    #print(len(data2['account_number']))
    #print(data2['transaction_details'][0]['transaction_info']['transaction_amount'])
    #print (data2['transaction_details'][1])

    f = open("json.txt", "w")
    f.write(str(Datas))
    f.close()
    return Datas


MData = monthly_data('2019-05-01T23:20:50.52Z', '2019-06-01T23:20:50.52Z')