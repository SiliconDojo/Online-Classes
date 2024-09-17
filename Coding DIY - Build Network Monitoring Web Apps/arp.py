import os
import requests

command = 'arp -a'

response = os.popen(command).readlines()
#print(response)

for x in response:
    #print(x)
    if ':' in x:
        #print(x)
        record =[0,0,0]
        x = x.split(' ')
        for y in x:
            if '.' in y:
                y = y.replace('(', '').replace(')','')
                #print(y)
                record[0] = y
            elif ':' in y:
                #print(y)
                record[1] = y
        try:
            response_mac = requests.get(f'https://api.maclookup.app/v2/macs/{record[1]}').json()
            record[2] = response_mac['company']
            if response_mac['company'] == '':
                record[2] = 'Not in Database'
        except:
            record[2] = 'Not Found'

        print(record)
