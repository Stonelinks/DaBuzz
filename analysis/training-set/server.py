import cherrypy
from cherrypy.lib.static import serve_file

import os.path

from requestjob import RequestJob
from returnjob import ReturnJob

from dbinfo_manager import recover

class Root(object):
  @cherrypy.expose
  def index(self):
    #return "Hello, world!"
    current_path = os.path.dirname(os.path.abspath(__file__))
    return serve_file(os.path.join(current_path, "static", "index.html"))

def main():
  cherrypy.config.update({
    'server.socket_host':'0.0.0.0',
  })

  dbinfo = recover()

  root = Root()
  root.requestjob = RequestJob(dbinfo)
  root.returnjob = ReturnJob(dbinfo)

  cherrypy.quickstart(root)

if __name__ == "__main__":
  main()