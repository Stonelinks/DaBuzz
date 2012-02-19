# Christian Johnson
# NLTK Basic Processing

#Needs the feedparser library and simplejson library to function.

import pprint
import urllib
import simplejson
import urllib2
import feedparser

def sentiment(text):
  #Really basic sample, if it fails url encoding, it gives up...
  url = 'http://text-processing.com/api/sentiment/'
  values = {'text' : text}

  try:
    data = urllib.urlencode(values)
  except UnicodeEncodeError:
    return {"label":"Error", 
            "probability": {
              "pos": 0,
              "neg": 0,
              "neutral": 0
            }
    }
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)
  return simplejson.loads(response.read())

def sample():
  #Gets top stories from MarketWatch and analyzes their sentiment
  url = "http://feeds.marketwatch.com/marketwatch/topstories/"
  feed = feedparser.parse(url)
  text_to_analyze = []
  for entry in feed['entries']:
    title = entry['title']
    results = sentiment(title)
    if results["label"] != "Error":
      print "%s: Overall %s, Positive %.2f, Negative: %.2f, Nuetral: %.2f" % (title, results["label"], results["probability"]["pos"]*100, results["probability"]["neg"]*100, results["probability"]["neutral"]*100)
    
if __name__ == "__main__":
  sample()