from nltk.model import counter
from nltk.model import ngram
from nltk import download
from nltk.corpus import brown


def build_model(n):
	download('brown')
	vocab = counter.build_vocabulary(1, brown.words(categories='news'))
	ngram_counter = counter.count_ngrams(1, vocab, brown.words(categories='news'))
	model = ngram.BaseNgramModel(ngram_counter)
	return model

def get_avg_log_prob(model, text):
	return model.entropy(text)