import cherrypy
from requestjob import RequestJob
from returnjob import ReturnJob

class Root(object):
  @cherrypy.expose
  def index(self):
    return "Hello, world!"

def main():
  cherrypy.config.update({
    'server.socket_host':'0.0.0.0',
  })

  root = Root()
  root.requestjob = RequestJob()
  root.returnjob = ReturnJob()

  cherrypy.quickstart(root)

if __name__ == "__main__":
  main()