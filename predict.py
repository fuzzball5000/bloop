import os
import MySQLdb
import time
from time import strftime
import sys
from sklearn import linear_model

db_pass = os.environ['sql_pass']
strtime = strftime("%Y-%m-%d %H:%M:%S")

try:
    db = MySQLdb.connect('localhost','bloop_write',db_pass,'bloop' )
    cursor = db.cursor()
except MySQLdb.Error as e:
    print("DB connect error: {}".format(e))
    sys.exit(1)
