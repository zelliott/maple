from nltk import download
from nltk.corpus import brown
from nltk.corpus import gutenberg
from constansts import train_data_clean_path
from constants import corpus_size

def clean_brown(corpus_size):
	download('brown')
	brown_categories = brown.categories()
	training_corpus = []
	for i in range(0, len(brown_categores)):
		to_add = brown.words(categories=brown_categories[i])
		training_corpus = training_corpus + to_add
	if len(training_corpus) > corpus_size:
		training_corpus[:corpus_size]
	training_corpus = ' '.join(training_corpus)
	to_write = open(train_data_clean_path + '/brown.txt', 'w')
	to_write.write(training_corpus.encode('UTF-8'))

clean_brown(corpus_size)


