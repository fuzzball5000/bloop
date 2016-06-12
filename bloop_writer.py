import requests
import os
import MySQLdb
import time
from time import strftime

db_pass = os.environ['sql_pass']
key = os.environ['met_key']
url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3544?res=hourly&key='
db = MySQLdb.connect('localhost','bloop_write',db_pass,'bloop' )
strtime = strftime("%Y-%m-%d %H:%M:%S")
url2 = 'http://81.187.136.232:8080/output.json'

response = requests.get(url+key)
epoch = int(time.time()) 
data = response.json()
response2 = requests.get(url2)
data2 = response2.json()
cursor = db.cursor()

edwin_temp = data2['temp']
edwin_humid = data2['humid']
met_temp = data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['T']
met_code = data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['W']
met_hydro = data['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['H']

print (met_temp,' ',met_code, ' ',met_hydro, ' ',edwin_temp, ' ',edwin_humid)

try:
    cursor.execute("INSERT INTO edwin(epoc,e_temp,e_hydro,m_temp,m_code,m_hydro,datetime) VALUES(%s, %s, %s, %s, %s, %s, %s)", (epoch, edwin_temp,edwin_humid,met_temp,met_code,met_hydro,strtime))
    db.commit()
except:     
    db.rollback()
db.close()
