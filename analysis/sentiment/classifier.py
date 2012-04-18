class Classifier(object):
  def __init__(self, learner):
    self.learner = learner

  def classify(self, s):
    dist = self.learner.classifier.prob_classify(self.learner.extract_features(s))
    print dist.samples()
    return self.learner.classifier.classify(self.learner.extract_features(s))