import cherrypy
import MySQLdb
from random import randint

class RequestJob(object):
  def __init__(self, dbinfo):
    self.dbinfo = dbinfo

  @cherrypy.expose
  @cherrypy.tools.json_out()
  def index(self):
    conn = MySQLdb.connect(**self.dbinfo)

    cur = conn.cursor()

    sql = "SELECT RAND()*(SELECT count(*) FROM articles WHERE trainset=1)"
    cur.execute(sql)
    selection = int(cur.fetchone()[0])

    sql = "SELECT id,article_text FROM articles WHERE trainset=1 LIMIT 1 OFFSET %s"
    args = [selection]
    cur.execute(sql, args)

    result = cur.fetchone()

    cur.close()

    conn.close()

    return result