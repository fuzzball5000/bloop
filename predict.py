import os
import MySQLdb
import time
import sys
from sklearn import linear_model

db_pass = os.environ['sql_pass']
epoch = int(time.time())
oneDay = epoch - 86400

try:
    db = MySQLdb.connect('localhost','bloop_write',db_pass,'bloop' )
    cursor = db.cursor()
except MySQLdb.Error as e:
    print("DB connect error: {}".format(e))
    sys.exit(1)

cursor.execute ("select datetime,e_temp,e_hydro from edwin where epoc > 1466860141 order by epoc asc")

data = cursor.fetchall ()

for row in data :
    print row[0], row[1]
cursor.close ()
db.close()
