import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(path, "./../training-set"))
del sys, os

from learner import Learner
from classifier import Classifier

import MySQLdb

from dbinfo_manager import recover

def main():
  dbinfo = recover()
  conn = MySQLdb.connect(**dbinfo)

  cur = conn.cursor()

  #Learn
  sql = "SELECT id,article_text,trainpos,trainneg,trainneutral FROM articles WHERE trainset=1 AND (trainpos>0 OR trainneg>0 OR trainneutral>0)"
  cur.execute(sql)
  a = Learner()
  for aid,article_text,trainpos,trainneg,trainneutral in cur.fetchall():
    aid = int(aid)
    items = [ (1, int(trainpos)),(0, int(trainneutral)),(-1, int(trainneg)) ]
    classification = max(items, key=lambda x : x[1])[0]
    a.add_string(article_text, classification)

    #sql = "UPDATE articles SET score=%s WHERE id=%s"
    #args = [classification,aid]
    #cur.execute(sql,args)
  a.train()

  #Predict
  sql = "SELECT id,article_text FROM articles"
  cur.execute(sql)
  b = Classifier(a)
  for aid,article_text in cur.fetchall():
    aid = int(aid)
    classification = b.classify(article_text)
    sql = "UPDATE articles SET score=%s WHERE id=%s"
    args = [classification,aid]
    cur.execute(sql,args)
    print aid

  conn.commit()

if __name__ == "__main__":
  main()