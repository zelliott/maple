from __future__ import division
import os
import math
import numpy as np
import random
from textblob import TextBlob as tb
from collections import Counter

num_docs = {'whole_corpus': 206780,
             'algorithms': 20103,
             'cell_line_tumor': 21136,
             'magnetic_resonance_imaging': 30394,
             'molecular_sequence_data': 71224,
             'neoplasm': 20579,
             'obesity': 11642,
             'signal_transduction': 31702}
# from gensim import models

# def make_idfs():
# 	all_docs = []
# 	for domain_file_name in os.listdir('corpora'):
# 		domain_file = open('corpora/' + domain_file_name, 'r')
# 		domain_file_text = domain_file.read()
# 		all_docs_in_file = domain_file_text.split('\n')
# 		all_docs.extend(all_docs_in_file)
# 		tfidf = models.TfidfModel(all_docs_in_file)
# 		tfidf.save('/idf_models/' + domain_file_name + '.model')
# 	tfidf = models.TfidfModel(all_docs)
# 	tfidf.save('/idf_models/whole_corpus.model')
def get_doc_counts():
	total_count = 0
	for domain_file_name in os.listdir('corpora'):
		domain_file = open('corpora/' + domain_file_name, 'r')
		domain_file_text = domain_file.read()
		all_docs_in_file = domain_file_text.split('\n')
		print(domain_file_name + ' doc count is ' + str(len(all_docs_in_file)))
		total_count = total_count + len(all_docs_in_file)

	print('total count is ' + str(total_count))

def make_dfs():
	all_dfs = Counter()
	for domain_file_name in os.listdir('corpora'):
		domain_file = open('corpora/' + domain_file_name, 'r')
		domain_file_text = domain_file.read()
		all_docs_in_file = domain_file_text.split('\n')

		print("converting " + domain_file_name + " to unicode")
		uni_all_docs_in_file = [unicode(x, 'utf-8') for x in all_docs_in_file]

		print("making " + domain_file_name + " blobs")
		domain_blobs = map(tb, uni_all_docs_in_file)


		print("making " + domain_file_name + " word counts list")
		domain_word_counts_list = map(lambda x: x.word_counts, domain_blobs)
		print("making " + domain_file_name + " words list")
		domain_words_list = [list(x.keys()) for x in domain_word_counts_list]
		print("making " + domain_file_name + " dfs")
		domain_dfs = Counter()
		print str(len(domain_words_list))
		for i in range(len(domain_words_list)):
			words_list = domain_words_list[i]
			if i % 1000 == 0:
				print str(i)
			c = Counter(words_list)
			domain_dfs.update(c)
			all_dfs.update(c)

		print("saving " + domain_file_name + " file")
		np.save('/Users/Zack/Developer/maple/extension/app/simplify_service/df_models/' + domain_file_name + '.npy', domain_dfs)

	print("making entire corpus dfs map")
	np.save('/Users/Zack/Developer/maple/extension/app/simplify_service/df_models/whole_corpus.npy', all_dfs)

def tf(word, blob):
	return blob.words.count(word) / len(blob.words)

# def n_containing(word, bloblist):
#     return sum(1 for blob in bloblist if word in blob.words)

def idf(word, dfs, num_doc):
    return np.log(num_doc / (1 + dfs[word]))

def tfidf(word, blob, dfs, num_doc):
	return tf(word, blob) * idf(word, dfs, num_doc)


# def get_top_words(doc, abstract_list, n=5):
# 	uni_doc = unicode(doc, 'utf-8')
# 	uni_abstract_list = [unicode(x, 'utf-8') for x in abstract_list]
# 	blob = tb(uni_doc)
# 	if len(uni_abstract_list) > 0:
# 		bloblist = map(tb, uni_abstract_list)
# 		scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
# 		sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# 		return [x[0] for x in sorted_words[:n]]
# 	else :
# 		return []
def get_top_words(doc, dfs, num_doc, n=5):
	uni_doc = unicode(doc, 'utf-8')
	blob = tb(uni_doc)
	scores = {word: tfidf(word, blob, dfs, num_doc) for word in blob.words}
	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	return [x[0] for x in sorted_words[:n]]

# def get_most_difficult(doc, doc_class):
# 	doc = doc.lower()
# 	all_docs = []
# 	for domain_file_name in os.listdir('corpora'):
# 		domain_file = open('corpora/' + domain_file_name, 'r')
# 		domain_file_text = domain_file.read()
# 		all_docs_in_file = domain_file_text.split('\n')
# 		all_docs.extend(all_docs_in_file)

# 	random.shuffle(all_docs)
# 	all_docs = all_docs[:1000]

# 	# print "getting corpora hard words"
# 	corpora_hard_words = get_top_words(doc, all_docs)
# 	set_corpora_hard_words = set(corpora_hard_words)
# 	class_docs_file = open('corpora/' + doc_class, 'r')
# 	class_docs_text = class_docs_file.read()
# 	all_class_docs = class_docs_text.split('\n')

# 	all_class_docs = all_class_docs[:1000]

# 	# print "getting class hard words"
# 	class_hard_words = get_top_words(doc, all_class_docs)
# 	set_class_hard_words = set(class_hard_words)
# 	# corpora_hard_words.extend(class_hard_words)
# 	# all_words = list(set(corpora_hard_words))
# 	all_words = {}
# 	set_class_hard_words = set_class_hard_words.difference(set_corpora_hard_words)
# 	all_words["all"] = list(set_corpora_hard_words)
# 	all_words["domain"] = list(set_class_hard_words)
# 	return all_words
def get_most_difficult(doc, doc_class):
	doc = doc.lower()
	dfs_class = np.load('/Users/Zack/Developer/maple/extension/app/simplify_service/df_models/' + doc_class + '.npy').item()
	num_doc_class = num_docs[doc_class]
	dfs_whole = np.load('/Users/Zack/Developer/maple/extension/app/simplify_service/df_models/whole_corpus.npy').item()
	num_doc_whole = num_docs['whole_corpus']

	corpora_hard_words = get_top_words(doc, dfs_whole, num_doc_whole)
	set_corpora_hard_words = set(corpora_hard_words)

	class_hard_words = get_top_words(doc, dfs_class, num_doc_class)
	set_class_hard_words = set(class_hard_words)

	all_words = {}
	set_class_hard_words = set_class_hard_words.difference(set_corpora_hard_words)
	all_words["all"] = list(set_corpora_hard_words)
	all_words["domain"] = list(set_class_hard_words)
	return all_words


# doc =  "most continent geriatric patients can be managed appropriately after a clinical assessment including a history, physical examination, urinalysis and culture, and simple tests of bladder function. a subgroup will benefit from urologic, gynecologic, and formal urodynamic evaluation. algorithms described in this chapter are being developed and tested; these algorithms will make clinical assessment more practical and cost effective."
# doc_type = "algorithms"
# print get_most_difficult(doc, doc_type)
# make_dfs()

