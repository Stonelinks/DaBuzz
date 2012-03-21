import cherrypy
import MySQLdb

class ReturnJob(object):
  def __init__(self, dbinfo):
    self.dbinfo = dbinfo

  @cherrypy.expose
  @cherrypy.tools.json_out()
  def index(self, articleid, score):
    try:
      articleid = int(articleid)
      score = int(score)
    except:
      return "FAILURE"

    conn = MySQLdb.connect(**self.dbinfo)

    cur = conn.cursor()

    if score not in (-1,0,1):
      return "FAILURE"

    if score == -1:
      field = "trainneg"
    elif score == 0:
      field = "trainneutral"
    elif score == 1:
      field = "trainpos"

    #Get the id and the paragraph for all elements with an empty score
    sql = "UPDATE articles SET " + field + "=" + field + "+1 WHERE id=%s"
    args = articleid
    cur.execute(sql, args)

    cur.close()

    conn.commit()
    conn.close()

    return "SUCCESS"