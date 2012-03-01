class Classifier(object):
  def __init__(self, learner):
    self.learner = learner

  def classify(self, s):
    return self.learner.classifier.classify(self.learner.extract_features(s))