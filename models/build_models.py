from nltk import download
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import cess_esp
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

def build_spanish():
	download('cess_esp')
	words = cess_esp.words()[:100000]

	total_size = len(words)
	print 'Spanish Corpus contains ' + str(total_size) + ' total tokens'

	esp_trainfiles = [' '.join(words)]
	return UnigramModel(esp_trainfiles)