class Classifier(object):
  def __init__(self, learner):
    self.learner = learner

  def classify(self, s):
    #return self.learner.classifier.classify(self.learner.extract_features(s))
    dist = self.learner.classifier.prob_classify(self.learner.extract_features(s))
    if dist.prob(1) > dist.prob(-1):
      return dist.prob(1)
    else:
      return -dist.prob(-1)