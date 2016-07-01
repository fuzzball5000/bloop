import os
import MySQLdb
import time
from time import strftime
import sys
from sklearn import linear_model
import datetime

db_pass = os.environ['sql_pass']
strtime = strftime("%Y-%m-%d %H:%M:%S")
epoch = int(time.time())
print epoch
oneDay = epoch - 86400

try:
    db = MySQLdb.connect('localhost','bloop_write',db_pass,'bloop' )
    cursor = db.cursor()
except MySQLdb.Error as e:
    print("DB connect error: {}".format(e))
    sys.exit(1)

cursor.execute ("select e_temp,e_hydro from edwin where epoc > 1466860141 order by epoc asc")

data = cursor.fetchall ()

for row in data :
    print row[0], row[1]
cursor.close ()
db.close()
