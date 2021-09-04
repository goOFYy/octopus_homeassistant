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
    for x in rows :
        t =x[2].split('T')[1].split('+')[0]
        d1=datetime.strptime('00:30:00', '%H:%M:%S' )
        d2=datetime.strptime('04:30:00', '%H:%M:%S' )
        # upper_limit = str(d1).split(' ')[1]
        # lower_limit = str(d2).split(' ')[1]
        t2=  datetime.strptime(t, '%H:%M:%S')
        # t3 = str(t2).split(' ')[1]
    
        if t2 <= d2 and t2 >= d1:
            low +=x[1]
            
        else:
            high += x[1]
            # print(x[2].split('+')[0])
            
    total = (low*l + high*h)/100
    print(str(total) + ' £')
    
  
    conx.insert_daily(args,total,date.today())
