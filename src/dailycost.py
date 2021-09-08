import conx
import datetime

from datetime import datetime, date
import configparser

def cost(args):
    

    config= configparser.RawConfigParser()
    config.read(args)
    l=float(config.get('rate','low'))
    h=float(config.get('rate','high'))
    rows=conx.select_all(args)
    low=0
    high=0
    total=0
    i=0
    consumption=0
    for x in rows :
        t =x[2].split('T')[1].split('+')[0]
        d1=datetime.strptime('20:30:00', '%H:%M:%S' ).time()
        d2=datetime.strptime('01:30:00', '%H:%M:%S' ).time()
        d3=datetime.strptime('23:59:00', '%H:%M:%S' ).time()
        d4=datetime.strptime('23:00:00', '%H:%M:%S' ).time()
        
        # upper_limit = str(d1).split(' ')[1]
        # lower_limit = str(d2).split(' ')[1]
        t2=  datetime.strptime(t, '%H:%M:%S').time()
        # t3 = str(t2).split(' ')[1]
        
  
           
        if d1 <= t2 <= d3 or d3 < t2 < d4 :
            low +=x[1]
            
        else:
            high += x[1]
            # print(x[2].split('+')[0])
            
    total = (low*l + high*h)/100

    print(str(total) + ' £')
    consumption=low+high
    print(consumption)
  
    conx.insert_daily(args,total,date.today(),consumption)
