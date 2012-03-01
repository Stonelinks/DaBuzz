from __future__ import division

import cStringIO
from collections import defaultdict

def preprocess_raw_string(s):
  #Convert the string to lower case
  s = s.lower()

  #Take only letters, spaces and newlines
  letters = "abcdefghijklmnopqrstuvwxyz \n"

  result = ("".join([c for c in s if c in letters])).split()

  return result

class Train(object):
  def __init__(self):
    self.positive = []
    self.pos_count = 0
    self.negative = []
    self.neg_count = 0

  def add_string(self, s, tag):
    s = preprocess_raw_string(s)
    if tag == "+":
      self.positive.extend(s)
      self.pos_count += 1
    elif tag == "-":
      self.negative.extend(s)
      self.neg_count += 1

  def extract_features(self):
    #Create a histogram for positive and negative words
    pos_hist = defaultdict(int)
    for item in self.positive:
      pos_hist[item] += 1
    pos_sum = len(self.positive)

    neg_hist = defaultdict(int)
    for item in self.negative:
      neg_hist[item] += 1
    neg_sum = len(self.negative)

    #Compute p(word|pos)
    pos_prob = dict()
    for item,count in self.pos_hist.iteritems():
      pos_prob[item] = count / (count + neg_hist[item])

    #Compute p(word|neg)
    neg_prob = dict()
    for item,count in self.neg_hist.iteritems():
      neg_prob[item] = count / (count + pos_hist[item])

    #Compute p(word)
    word_prob = dict()
    for word in set(self.positive).union( set(self.negative) ):
      word_prob[word] = 