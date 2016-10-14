from nltk import download
from nltk.corpus import brown
from nltk.corpus import gutenberg
from unigram import UnigramModel


def build_brown():
	download('brown')
	brown_news = brown.words(categories='news')
	# brown_editorial = brown.words(categories='editorial')

	total_size = len(brown_news) #+ len(brown_editorial)
	print 'Brown Corpus contains ' + str(total_size) + ' total tokens'


	brown_trainfiles = [' '.join(brown_news)]#, ' '.join(brown_editorial)]
	return UnigramModel(brown_trainfiles)

def build_gutenberg():
	download('gutenberg')
	macbeth = gutenberg.words('shakespeare-macbeth.txt')
	hamlet = gutenberg.words('shakespeare-hamlet.txt')
	caesar = gutenberg.words('shakespeare-caesar.txt')

	total_size = len(macbeth) + len(hamlet) + len(caesar)
	print 'Gutenberg Corpus contains ' + str(total_size) + ' total tokens'

	gutenberg_trainfiles = [' '.join(macbeth), ' '.join(hamlet), ' '.join(caesar)]
	return UnigramModel(gutenberg_trainfiles)

def build_wiki():
	return None