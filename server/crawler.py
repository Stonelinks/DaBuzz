# Christian Johnson
# NLTK Basic Processing
#Uses http://text-processing.com/docs/sentiment.html API

'''

Sample output:

Weekend Investor: 5 game changers for small-cap stocks: Overall neutral, Positive 38.98, Negative: 61.02, Nuetral: 74.02
NewsWatch: U.S. stock indexes end with weekly rise: Overall neutral, Positive 66.49, Negative: 33.51, Nuetral: 66.39
NewsWatch: U.S. stock indexes end with weekly rise: Overall neutral, Positive 66.49, Negative: 33.51, Nuetral: 66.39
Asia Markets: China data, Esprit earnings ahead in Asia: Overall neutral, Positive 62.27, Negative: 37.73, Nuetral: 51.46
Auto Review: Mazda 3 a sporty choice as gas prices rise: Overall neutral, Positive 52.04, Negative: 47.96, Nuetral: 67.71
Energy Stocks: First Solar, $103 crude rally energy stocks: Overall neg, Positive 39.63, Negative: 60.37, Nuetral: 9.12
Latin American Markets: Brazilian stocks edge up ahead of holiday break: Overall neutral, Positive 70.16, Negative: 29.84, Nuetral: 85.28
Applied shares ease after rising on results: Overall neutral, Positive 40.50, Negative: 59.50, Nuetral: 74.58

'''

#Needs the feedparser library and simplejson library to function.
# http://code.google.com/p/feedparser/
# http://pypi.python.org/pypi/simplejson/

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

def get_stories():
  #Gets top stories from MarketWatch and analyzes their sentiment
  url = "http://feeds.marketwatch.com/marketwatch/topstories/"
  feed = feedparser.parse(url)
  stories = []
  for entry in feed['entries']:
    title = entry['title']
    url = entry['link']
    summary = entry['summary']
    results = sentiment(title)
    if results["label"] != "Error":
      pos = float(results["probability"]["pos"])
      neg = float(results["probability"]["neg"])
      neu = float(results["probability"]["neutral"])
      stories.append( (url, title, summary, pos, neg, neu) )
  return stories