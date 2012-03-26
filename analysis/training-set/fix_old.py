#Fix old entries

import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(path, "./../../server"))
sys.path.insert(0, os.path.join(path, "/dabuzz/server"))
del sys, os

import MySQLdb

from dbinfo_manager import recover
from html_extract import extract_text

def main():
  dbinfo = recover()
  conn = MySQLdb.connect(**dbinfo)

  cur = conn.cursor()

  sql = "SELECT id,article_text FROM articles"
  cur.execute(sql)
  for aid,article_text in cur.fetchall():
    aid = int(aid)

    #print article_text
    article_text = extract_text(article_text)
    #print article_text

    #Keep your hands away...
    #sql = "UPDATE articles SET article_text=%s WHERE id=%s"
    #args = [article_text,aid]
    #cur.execute(sql,args)

  conn.commit()

if __name__ == "__main__":
  main()