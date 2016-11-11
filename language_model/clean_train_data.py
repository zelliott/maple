from nltk import download
from nltk.corpus import brown
from nltk.corpus import gutenberg
from constants import train_data_clean_path
from constants import corpus_size
from srilm_file_utils import convert_file_to_lines

def clean_brown():
	download('brown')
	brown_categories = brown.categories()
	training_corpus = []
	for i in range(0, len(brown_categories)):
		to_add = brown.words(categories=brown_categories[i])
		training_corpus = training_corpus + to_add
	if len(training_corpus) > corpus_size:
		training_corpus[:corpus_size]
	training_corpus = u' '.join(training_corpus).encode('ascii', 'ignore')
	training_corpus = convert_file_to_lines(training_corpus)
	to_write = open(train_data_clean_path + '/brown.txt', 'w')
	to_write.write(training_corpus)
	to_write.close()

def clean_gutenberg():
	download('gutenberg')
	gutenberg_files = gutenberg.fileids()
	training_corpus = []
	for i in range(0, len(gutenberg_files)):
		to_add = u' '.join(gutenberg.words(gutenberg_files[i])).split(u' ')
		training_corpus = training_corpus + to_add
	if len(training_corpus) > corpus_size:
		training_corpus[:corpus_size]
	training_corpus = u' '.join(training_corpus).encode('ascii', 'ignore')
	training_corpus = convert_file_to_lines(training_corpus)
	to_write = open(train_data_clean_path + '/gutenberg.txt', 'w')
	to_write.write(training_corpus)
	to_write.close()

# clean_brown()
# clean_gutenberg()



