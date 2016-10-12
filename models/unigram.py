from nltk.probability import (
	ConditionalFreqDist,
	LaplaceProbDist)
from nltk.util import ngrams
import numpy as np

class UnigramModel:

	def __init__(self, trainfiles):

		cfd = ConditionalFreqDist()

		self._ngrams = set()

		for trainfile in trainfiles:
			raw_ngrams = ngrams(trainfile.split(" "), 1)
			for ngram in raw_ngrams:
				self._ngrams.add(ngram)
				context = tuple(ngram[:-1])
				token = ngram[-1]
				cfd[(context, token)] += 1

		self._probdist = LaplaceProbDist(cfd)


	def prob(self, context, word):
		context = tuple(context)
		return self._probdist.prob((context, word))

	def log_prob(self, context, word):
		return -np.log2(self.prob(context, word))

	def entropy(self, text):
		e = 0.0
		text = text.split(" ")
		for word in text:
			context = word
			e +=self.log_prob(context, word)
		return e / float(len(text))


