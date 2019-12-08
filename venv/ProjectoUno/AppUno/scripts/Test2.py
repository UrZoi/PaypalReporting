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

def rreplace(s, old, new):
    return (s[::-1].replace(old[::-1],new[::-1], 1))[::-1]


def LinkGenerator(example,sheetnumber):
    l=[]
    for i in range(int(sheetnumber)):
        if i != 0:
            l.append(rreplace(str(example),str(sheetnumber),str(i+1)))
    #print (l)
    return l   



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
                             auth=('Heres go your Paypal key'))
    data = json.loads(response.text)
    #print(data)

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
    #print(response2.status_code)
    #print(response2.text)

    Datas.append(json.loads(response2.text))

    f = open("json.txt", "w")
    f.write(str(response2.text))
    f.close()
    if int(Datas[0]['total_items']) > 5:
        #print(Datas[0]['links'][0]['href'])
        #print(Datas[0]['total_pages'])
        lacosa = LinkGenerator(Datas[0]['links'][0]['href'],Datas[0]['total_pages'])
        for i in range(len(lacosa)):
            #print(Datas['links'][i]['href'])
            #print('IAM THE RESPONSE    ' ,response2.text)
            response2 = requests.get(lacosa[i], headers=headers2)
            Datas.append(json.loads(response2.text))
    #print(Datas[0]['total_items'])
   # print(len(Datas))
    #print(len(data2['account_number']))
    #print(data2['transaction_details'][0]['transaction_info']['transaction_amount'])
    #print (data2['transaction_details'][1])


    return Datas


def Balancesheet(MData):
    negativebalance = []
    #print (len(MData))
    for j in range(len(MData)):
        for i in range(len(MData[j]['transaction_details'])):

                try:
                    if 'CALLE CALDERON DE LA BARCA, 488' in MData[j]['transaction_details'][i]['shipping_info']['address']['line1'] or 'AVENIDA CIRCUNVALACION AGUSTIN YANEZ, 2481' in MData[j]['transaction_details'][i]['shipping_info']['address']['line1'] :
                        print (MData[j]['transaction_details'][i]['transaction_info']['transaction_amount']['value'], MData[j]['transaction_details'][i]['shipping_info']['address']['line1'])
                        negativebalance.append(MData[j]['transaction_details'][i]['transaction_info']['transaction_amount']['value'])
                except:
                    print('this transaction dont care')

    num = 0
    for i in negativebalance:
        num += float(i)
        print(i)
    print(num)
    negativebalance.append(num)

    return negativebalance




MData = monthly_data('2019-11-16T23:20:50.52Z', '2019-12-07T23:20:50.52Z')
Balance = Balancesheet(MData)

