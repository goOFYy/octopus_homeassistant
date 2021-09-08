import mysql.connector
import configparser

def cnx(args):
    config= configparser.RawConfigParser()
    config.read(args)

    c = mysql.connector.connect(user=config.get('mysql','user'), password=config.get('mysql','password'),
                              host=config.get('mysql','host'),
                              database=config.get('mysql','database'))
    cursor = c.cursor()
    return c, cursor

def close_cnx(c, cursor):
    cursor.close()
    c.close()

# Octopus is my table name with 3 column ID, consumption, Date
# I clean the data every 30 min following octopuse's 30 min updated data
def clean(args):
    c, cursor = cnx (args)
    query = 'Delete from octopus'
    cursor.execute(query)
    c.commit()
    close_cnx(c,cursor)

def insert(args, values):
    c, cursor = cnx (args)
    query = 'insert into octopus ( consumption, date) Values ( + "' + str(values[0]) +'" , "' + str(values[1]) +'")'
    print(query)
    cursor.execute(query)
    c.commit()
    close_cnx(c,cursor)

def select_all(args):
    c, cursor = cnx (args)
    query = 'SELECT * From octopus'

    cursor.execute(query)
    myresult = cursor.fetchall()
    close_cnx(c,cursor)
    return myresult

def insert_daily(args, cost, date,cons):
    c, cursor = cnx (args)
    query = 'insert into octopus_daily ( date , cost, consumption) Values ( + "' + str(date) +'" , "' + str(cost) +'", "' + str(cons) +'")'
    print(query)
    cursor.execute(query)
    c.commit()
    close_cnx(c,cursor)