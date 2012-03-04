#!/usr/bin/env python
import sys
sys.path.append('/dabuzz/')

import time, os
import web

urls = (
  '/', 'hello',
  '/(static)/(.*)', 'static'
)

class hello:
  def GET(self):
    web.header("Content-Type","text/html; charset=utf-8")
    return "<h1>HI!</h1>"

  def POST(self):
    web.header("Content-Type","text/html; charset=utf-8")
    return "<h1>HI!</h1>"

if __name__ == "__main__":
  print "starting local webserver on localhost on port " + sys.argv[1]
  app = web.application(urls, globals(), autoreload=True)
  app.internalerror = web.debugerror
  app.run()

sys.stdout = sys.stderr # mod_wsgi flips out if this isn't here
app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
