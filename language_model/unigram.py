# from nltk.probability import (
# 	ConditionalFreqDist,
# 	LaplaceProbDist)
from nltk.util import ngrams
from collections import Counter
import numpy as np
import string
import re

class UnigramModel:

	def __init__(self, trainfiles):
		"""
		trainfiles: list of files, where each file is a string

		"""

		total_words = 0
		word_count = Counter()

		self._ngrams = set()

		for trainfile in trainfiles:
			trainfile_ascii = trainfile.encode('ascii', 'ignore').lower()
			trainfile_no_punc = trainfile_ascii.translate(None, string.punctuation)
			trainfile_clean = re.sub(' +', ' ', trainfile_no_punc)
			raw_ngrams = ngrams(trainfile_clean.split(' '), 1)
			for ngram in raw_ngrams:
				self._ngrams.add(ngram)
				# context = tuple(ngram[-1])
				token = ngram[-1]
				word_count[token] += 1
				total_words += 1

		for word in word_count:
			if word_count[word] is 0:
				word_count['<UNK>'] += 1
				word_count[word] = 0

		self._word_count = word_count
		self._total_words = total_words
		# self._probdist = LaplaceProbDist(cfd)


	def prob(self, word):
		"""
		"""
		# context = tuple(context)
		# return self._probdist.prob((context, word))
		if self._word_count[word] is 0:
			return float((1.0 + self._word_count['<UNK>']) / self._total_words)
		else:
			return float((1.0 + self._word_count[word]) / self._total_words)

	def log_prob(self, word):
		"""
		"""
		return -np.log2(self.prob(word))

	def entropy(self, text):
		"""
		"""
		e = 0.0
		text_ascii = text.encode('ascii', 'ignore').lower()
		text_no_punc = text_ascii.translate(None, string.punctuation)
		text_clean = re.sub(' +', ' ', text_no_punc)
		text_split = text_clean.split(' ')
		for word in text_split:
			e += self.log_prob(word)
		return e / float(len(text_split))


	def ngrams(self):
		return self._ngrams