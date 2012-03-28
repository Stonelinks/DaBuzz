import web
import config

if config.is_local:
  db = web.database(dbn='sqlite', db=config.db_name)
else:
  print "NOT RUNNING LOCALLY"
  db = web.database(dbn='mysql', \
      db=config.db_name, \
      user=config.mysql_db_user, \
      pw=config.mysql_db_password)

def get_articles(q):
  if q:
   return db.query("SELECT * FROM articles WHERE LOWER(title) LIKE LOWER($query) ORDER BY time_crawled DESC LIMIT 50", vars=dict(query='%' + q + '%'))
   #Tried doing it with arguments, didn't work well.
   #return db.select('artcles', where="LOWER(title) LIKE LOWER($query)", order="time_crawled DESC", limit=50, vars=dict(query='%' + q + '%'))
  return db.select('articles', order='time_crawled DESC', limit=50)
  
def new_article(url, title, text, pos, neg, neu):
  db.insert('articles', 
            url=url, 
            title=title, 
            article_text=text, 
            pos=pos, 
            neg=neg,
            neutral=neu)

def del_article(id):
  db.delete('articles', 
            where="id=$id", 
            vars=locals())