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
    if tag not in ["+", "-"]:
      raise

    self.data.append( (extract_features(s), tag) )

    self.classifier = nltk.NaieveBayesClassifier.train(self.train_set)

  def extract_features(self, s):
    #Remove irregularities in the string
    s = preprocess_raw_string(s)

    #Get a list of common words
    common_words = set(stopwords.words("english"))

    #Generate a "bag of words"
    word_bag = set(s)

    #Remove common words
    word_bag = word_bag - common_words

    return dict([(word,True) for word in word_bag])  