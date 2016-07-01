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

cursor.execute ("select datetime,e_temp,e_hydro from edwin where epoc > 1466850141 order by epoc asc")

data = cursor.fetchall ()

x = []
y = []

for row in data :
    x.append(row[1])
    y.append(row[2])
print x
print y
cursor.close ()
db.close()
