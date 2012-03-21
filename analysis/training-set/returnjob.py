import cherrypy
import MySQLdb

class ReturnJob(object):
  def __init__(self, dbinfo):
    self.dbinfo = dbinfo

  @cherrypy.expose
  @cherrypy.tools.json_out()
  def index(self, articleid, score):
    conn = MySQLdb.connect(**self.dbinfo)

    cur = conn.cursor()

    if score not in (-1,0,1):
      return "FAILURE"

    #Get the id and the paragraph for all elements with an empty score
    #sql = "UPDATE trainset SET score=%s WHERE id=%s"
    sql = "UPDATE articles SET score=%s WHERE id=%s"
    args = score,articleid
    cur.execute(sql, args)

    cur.close()

    conn.commit()
    conn.close()

    return "SUCCESS"