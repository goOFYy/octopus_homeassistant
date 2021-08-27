import requests
import datetime
from datetime import datetime, time, timedelta
import json
import configparser

def api_query(args):
    midnight = datetime.combine(datetime.today(), time.min)
    yesterday_midnight = midnight - timedelta(days=1)
    print(yesterday_midnight)
    config= configparser.RawConfigParser()
    config.read(args)
    mpan = config.get('api','mpan')
    msn = config.get('api','msn')
    auth = config.get('api','auth')
    
    url = "https://api.octopus.energy/v1/electricity-meter-points/"+ mpan +"/meters/"+ msn +"/consumption/?period_from=" + str(yesterday_midnight)

    payload={}
    headers = {
    'Authorization':  auth ,
    
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    #print(response.text)
    data =json.loads(response.text)
    element_list=[]
    for x in data['results']:
        
        element= (
            x['consumption'],
            x['interval_start']
        )
        element_list.append(element)
    return(element_list)


