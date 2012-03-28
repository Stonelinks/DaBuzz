from __future__ import division

import nltk
from nltk.corpus import stopwords

def preprocess_raw_string(s):
  #Convert the string to lower case
  s = s.lower()

  #Take only letters, spaces and newlines
  letters = "abcdefghijklmnopqrstuvwxyz \n"

  result = ("".join([c for c in s if c in letters])).split()

  return result

class Learner(object):
  def __init__(self):
    self.data = []
    self.classifier = None

  def add_string(self, s, tag):
    if tag not in [1, -1, 0]:
      raise

    self.data.append( (self.extract_features(s), tag) )

  def train(self):
    self.classifier = nltk.NaiveBayesClassifier.train(self.data)

  def extract_features(self, s):
    #Remove irregularities in the string
    s = preprocess_raw_string(s)

    #Get a list of common words
    common_words = set(stopwords.words("english"))

    #Generate a "bag of words"
    word_bag = set(s)

    #Remove common words
    word_bag = word_bag - common_words

    d = dict([(word,True) for word in word_bag])

    #Generate collocations
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(s)

    #Find 10 best collocations
    l = finder.nbest(bigram_measures.pmi, 10)
    d.update(dict([(collocation,True) for collocation in l]))

    return d
