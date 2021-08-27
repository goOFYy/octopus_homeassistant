import api
import conx
import configparser

config= configparser.RawConfigParser()
config.read('/script/auth.ini')
path =  '/script/auth.ini'
res = api.api_query(path)
print(res)
conx.clean(path)
for x in res:
    conx.insert(path,x)
print('done')