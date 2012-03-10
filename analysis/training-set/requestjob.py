import cherrypy
import psycopg2
from random import randint

class RequestJob(object):
  @cherrypy.expose
  @chrrypy.tools.json_out()
  def index(self):
    conn = psycopg2.connect()

    cur = conn.cursor()

    #Get the id and the paragraph for all elements with an empty score
    sql = "SELECT id,para FROM trainset WHERE score IS NULL"
    cur.execute(sql)

    #Pick a result
    selection = radint(0, cur.rowcount-1)
    result = cur.fetchall()[selection]

    cur.close()

    return result