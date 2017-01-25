"""
All functions used to clean specific datasets are placed in this file. Functions
commented out are for datasets we are currently not using. Additionally, if a
dataset is stored locally, said function to clean it will take it from the
train_data/raw directory. Each cleaned dataset is converted into a single txt
file with the correct formatting to be used directly with srilm. Each txt file
is placed in the train_data/clean directory.
"""

import os
import xml.etree.ElementTree as et
from subprocess import call
from nltk import download
from nltk.corpus import brown
from nltk.corpus import gutenberg
from constants import train_data_clean_path
from constants import train_data_raw_path
from constants import corpus_size
from srilm_file_utils import convert_file_to_lines
from constants import test_data_clean_path as abstracts_path

# def clean_brown():
# 	download('brown')
# 	brown_categories = brown.categories()
# 	training_corpus = []
# 	for i in range(0, len(brown_categories)):
# 		to_add = brown.words(categories=brown_categories[i])
# 		training_corpus = training_corpus + to_add
# 	if len(training_corpus) > corpus_size:
# 		training_corpus[:corpus_size]
# 	training_corpus = u' '.join(training_corpus).encode('ascii', 'ignore')
# 	training_corpus = convert_file_to_lines(training_corpus)
# 	to_write = open(train_data_clean_path + '/brown.txt', 'w')
# 	to_write.write(training_corpus)
# 	to_write.close()

# def clean_gutenberg():
# 	download('gutenberg')
# 	gutenberg_files = gutenberg.fileids()
# 	training_corpus = []
# 	for i in range(0, len(gutenberg_files)):
# 		to_add = u' '.join(gutenberg.words(gutenberg_files[i])).split(u' ')
# 		training_corpus = training_corpus + to_add
# 	if len(training_corpus) > corpus_size:
# 		training_corpus[:corpus_size]
# 	training_corpus = u' '.join(training_corpus).encode('ascii', 'ignore')
# 	training_corpus = convert_file_to_lines(training_corpus)
# 	to_write = open(train_data_clean_path + '/gutenberg.txt', 'w')
# 	to_write.write(training_corpus)
# 	to_write.close()

def clean_nytimes():
	training_corpus = []
	counter = 1
	nytimes_raw_dir = train_data_raw_path + '/nytimes'
	for year in os.listdir(nytimes_raw_dir):
		year = nytimes_raw_dir + '/' +  year
		if len(training_corpus) > corpus_size:
			break
		for month in os.listdir(year):
			month = year + '/' +  month
			for day in os.listdir(month):
				day = month + '/' + day
				for article in os.listdir(day):
					article = day + '/' + article
					f = open(article)
					xml = f.read()
					root = et.fromstring(xml)
					if len(training_corpus) > corpus_size:
						break
					for content_paragraph in root.findall(".//block[@class='full_text']/p"):
						print counter
						print article
						print len(training_corpus)
						counter = counter + 1
						text = content_paragraph.text.encode('ascii', 'ignore')
						training_corpus = training_corpus + text.split(' ')
					f.close()
	if len(training_corpus) > corpus_size:
		training_corpus[:corpus_size]
	print len(training_corpus)
	training_corpus = ' '.join(training_corpus)
	training_corpus = convert_file_to_lines(training_corpus)
	to_write = open(train_data_clean_path + '/nytimes.txt', 'w')
	to_write.write(training_corpus)
	to_write.close()

def clean_medline():
	to_write = open(train_data_clean_path + '/medline.txt', 'w')
	training_corpus = []
	for abstracts_dir in os.listdir(abstracts_path):
		abstract_dir_path = abstracts_path + '/' + abstracts_dir
		for abstract_file in os.listdir(abstract_dir_path):
			f = open(abstract_dir_path + '/' + abstract_file)
			training_corpus = training_corpus + f.read().split()
			print len(training_corpus)
			if len(training_corpus) > corpus_size:
				break
		if len(training_corpus) > corpus_size:
			break
	if len(training_corpus) > corpus_size:
		training_corpus[:corpus_size]
	print len(training_corpus)
	training_corpus = ' '.join(training_corpus)
	training_corpus = convert_file_to_lines(training_corpus)
	to_write.write(training_corpus)
	to_write.close()
		

# clean_brown()
# clean_gutenberg()
# clean_nytimes()
# clean_medline()



