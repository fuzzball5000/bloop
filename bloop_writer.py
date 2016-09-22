import requests
import os
import MySQLdb
import time
from time import strftime
import sys

db_pass = os.environ['sql_pass']
key = os.environ['met_key']
url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3544?res=hourly&key='
strtime = strftime("%Y-%m-%d %H:%M:%S")
url2 = 'http://81.187.136.232:8080/output.json'

epoch = int(time.time()) 

try:
    db = MySQLdb.connect('localhost','bloop_write',db_pass,'bloop' )
    cursor = db.cursor()
except MySQLdb.Error as e:
    print("DB connect error: {}".format(e))
    sys.exit(1)
try:
    response = requests.get(url+key)
except requests.exceptions.RequestException as e:
    print('Met office request failed: ',e)
    sys.exit(1)
try:
    response2 = requests.get(url2) 
except requests.exceptions.RequestException as e:
    print('Pi request failed: ',e)
    sys.exit(1)

data = response.json()
data2 = response2.json()
edwin_temp = data2['temp']
edwin_humid = data2['humid']

met_temp = data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['T']
met_code = data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['W']
met_hydro = data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['H']

try:
    cursor.execute("INSERT INTO edwin(epoc,e_temp,e_hydro,m_temp,m_code,m_hydro,datetime) VALUES(%s, %s, %s, %s, %s, %s, %s)", (epoch, edwin_temp,edwin_humid,met_temp,met_code,met_hydro,strtime))
    db.commit()
except:     
    db.rollback()
db.close()
