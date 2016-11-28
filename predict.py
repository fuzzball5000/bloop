import os
import MySQLdb
import time
import sys
from sklearn import linear_model
import csv

db_pass = os.environ['sql_pass']
epoch = int(time.time())
oneDay = epoch - 86400

try:
    db = MySQLdb.connect('localhost','bloop_write',db_pass,'bloop' )
    cursor = db.cursor()
except MySQLdb.Error as e:
    print("DB connect error: {}".format(e))
    sys.exit(1)

cursor.execute ("select MIN(datetime),e_temp,e_hydro,m_temp,m_hydro,m_code from edwin GROUP BY DATE(datetime),HOUR(datetime) order by epoc DESC LIMIT 100")

data = cursor.fetchall ()

c = csv.writer(open("/home/centos/bloop/temp.csv","wb"))
c.writerow(['date','e_temp','e_hydro','m_temp','m_hydro','m_code'])
for i in data:
    c.writerow(i)

cursor.close ()
db.close()
