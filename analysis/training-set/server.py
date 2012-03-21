import cherrypy
from requestjob import RequestJob
from returnjob import ReturnJob

from dbinfo_manager import recover

class Root(object):
  @cherrypy.expose
  def index(self):
    return "Hello, world!"

def main():
  cherrypy.config.update({
    'server.socket_host':'0.0.0.0',
  })

  dbinfo = recover()
  print dbinfo

  root = Root()
  root.requestjob = RequestJob(dbinfo)
  root.returnjob = ReturnJob(dbinfo)

  cherrypy.quickstart(root)

if __name__ == "__main__":
  main()