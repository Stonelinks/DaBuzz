#Fix old entries

import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(path, "./../../server"))
del sys, os

import MySQLdb

from dbinfo_manager import recover
from html_extract import text_from_url

def main():
  dbinfo = recover()
  conn = MySQLdb.connect(**dbinfo)

  cur = conn.cursor()

  sql = "SELECT id,url FROM articles"
  cur.execute(sql)
  for aid,url in cur.fetchall():
    aid = int(aid)

    with open("bad_urls","w") as f:
    try:
      article_text = text_from_url(url)
    except:
      import sys
      f.write(str(aid) + " " + sys.exc_info() + "\n")

    sql = "UPDATE articles SET article_text=%s WHERE id=%s"
    args = [article_text,aid]
    cur.execute(sql,args)

  conn.commit()

if __name__ == "__main__":
  main()