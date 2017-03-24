from __future__ import division
import os
import math
import numpy as np
import random
from textblob import TextBlob as tb

def tf(word, blob):
	# print blob.words.count(word)
	# print len(blob.words)
	return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return np.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word, blob) * idf(word, bloblist)


def get_top_words(doc, abstract_list, n=5):
	uni_doc = unicode(doc, 'utf-8')
	uni_abstract_list = [unicode(x, 'utf-8') for x in abstract_list]
	blob = tb(uni_doc)
	if len(uni_abstract_list) > 0:
		bloblist = map(tb, uni_abstract_list)
		scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

		return [x[0] for x in sorted_words[:n]]
	else :
		return []

def get_most_difficult(doc, doc_class):
	doc = doc.lower()
	all_docs = []
	for domain_file_name in os.listdir('corpora'):
		domain_file = open('corpora/' + domain_file_name, 'r')
		domain_file_text = domain_file.read()
		all_docs_in_file = domain_file_text.split('\n')
		all_docs.extend(all_docs_in_file)

	random.shuffle(all_docs)
	# all_docs = all_docs[:1000]

	# print "getting corpora hard words"
	corpora_hard_words = get_top_words(doc, all_docs)

	class_docs_file = open('corpora/' + doc_class, 'r')
	class_docs_text = class_docs_file.read()
	all_class_docs = class_docs_text.split('\n')

	# all_class_docs = all_class_docs[:1000]

	# print "getting class hard words"
	class_hard_words = get_top_words(doc, all_class_docs)

	corpora_hard_words.extend(class_hard_words)
	all_words = list(set(corpora_hard_words))
	return all_words