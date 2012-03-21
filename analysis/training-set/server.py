import cherrypy
from cherrypy.lib.static import serve_file

import os.path

from requestjob import RequestJob
from returnjob import ReturnJob

from dbinfo_manager import recover

current_path = os.path.dirname(os.path.abspath(__file__))

class Root(object):
  pass

def main():
  cherrypy.config.update("./site-config.conf")
  """
  cherrypy.config.update({
    'server.socket_host':'0.0.0.0',
  })
  """

  dbinfo = recover()

  root = Root()
  root.requestjob = RequestJob(dbinfo)
  root.returnjob = ReturnJob(dbinfo)

  cherrypy.quickstart(root, '/', config="./app-config.conf")

if __name__ == "__main__":
  main()