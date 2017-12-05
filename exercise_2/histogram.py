import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if len(sys.argv) != 2:
    print "word argument missing"
    exit(1)
else:
    k = sys.argv[1].split(",")
    k1 = k[0]
    k2 = k[1]

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute("SELECT word, count from tweetwordcount WHERE count >= %s AND count <= %s", (k1, k2))
    records = cur.fetchall()
    for rec in records:
       print str(rec[0]) + ": " + str(rec[1])
#       print "count = ", rec[1], "\n"
    conn.commit()


conn.close()

