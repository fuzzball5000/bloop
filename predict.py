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

cursor.execute ("select MIN(datetime),e_temp,e_hydro from edwin GROUP BY DATE(datetime),HOUR(datetime) order by epoc DESC LIMIT 72")

data = cursor.fetchall ()

c = csv.writer(open("/home/centos/bloop/temp.csv","wb"))
c.writerow(['date','e_temp','e_hydro'])
for i in data:
    c.writerow(i)

cursor.close ()
db.close()

##This isn't even close to working... sure beats
##empty whitespace though...
##clf = linear_model.BayesianRidge()
##clf.fit(x, y)
##BayesianRidge(alpha_1=1e-06, alpha_2=1e-06, compute_score=False, copy_X=True,
##fit_intercept=True, lambda_1=1e-06, lambda_2=1e-06, n_iter=300,
##normalize=False, tol=0.001, verbose=False)
