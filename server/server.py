#!/usr/bin/env python
import sys, os
sys.stdout = sys.stderr # mod_wsgi flips out if this isn't here
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

import config
import time, os
import web
import model
import crawler

urls = (
  '/', 'index',
  '/crawl', 'crawl',
  '/blog', 'blog',
  '/about', 'about',
  '/(static)/(.*)', 'static',
  '/del/(\d+)', 'delete'
)

render = web.template.render('templates', base='base')

class crawl:
  def GET(self):
    for article in crawler.get_stories():
      model.new_article(article[0], 
                        article[1],
                        article[2],
                        article[3],
                        article[4],
                        article[5])
    raise web.seeother('/')

class index:
  def GET(self):
    """ Show page """
    i = web.input(q='')
    query = web.websafe(i.q) 
    todos = model.get_articles(query)
    return render.index(todos)

class blog:
  def GET(self):
    return render.blog()

  def POST(self):
    return self.GET()

class about:
  def GET(self):
    return render.about()

  def POST(self):
    return self.GET()

class delete:
  def POST(self, id):
    """ Delete based on ID """
    id = int(id)
    model.del_article(id)
    raise web.seeother('/')

if __name__ == "__main__":
  print "starting webserver on localhost on port", config.local_server_port
  
  # annoying hack to make webpy start on the right port locally
  sys.argv.append(str(config.local_server_port))
  
  app = web.application(urls, globals(), autoreload=True)
  app.internalerror = web.debugerror
  app.run()

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
