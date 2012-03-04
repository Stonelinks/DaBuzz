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
  form = web.form.Form(
    web.form.Textbox('title', web.form.notnull, 
      description="I need to:"),
    web.form.Button('Add todo'),
  )

  def GET(self):
    """ Show page """
    todos = model.get_articles()
    form = self.form()
    return render.test(todos, form)

  def POST(self):
    """ Add new entry """
    form = self.form()
    if not form.validates():
      todos = model.get_articles()
      return render.test(todos, form)
    model.new_todo(form.d.title)
    raise web.seeother('/')

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
