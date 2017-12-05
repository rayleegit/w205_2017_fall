import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if len(sys.argv) > 2:
    print "word argument missing"
    exit(1)

if len(sys.argv) == 2:
    uWord = sys.argv[1]

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute("SELECT word, count from tweetwordcount WHERE word=%s", (uWord, ))
    records = cur.fetchall()
    for rec in records:
       print "word = ", rec[0]
       print "count = ", rec[1], "\n"
    conn.commit()

else:
#    word = sys.argv[1]

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute("SELECT word, count from tweetwordcount ORDER BY word")
    records = cur.fetchall()
    for rec in records:
       print "word = " + str(rec[0]) + ", count = " + str(rec[1])
#       print "count = ", rec[1], "\n"
    conn.commit()


conn.close()

