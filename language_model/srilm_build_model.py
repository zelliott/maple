from subprocess import call
from constants import srilm_path
from constants import train_data_clean_path
from constants import srilm_language_models_path


def make_model(train_file):
	ngram_count_cmd = srilm_path + '/ngram-count'

	model_name = train_file.split('.')[0] + '.lm'
	model_path = srilm_language_models_path + '/' + model_name

	train_file_path = train_data_clean_path + '/' + train_file
	
	args = [ngram_count_cmd, '-text', train_file_path, '-lm', model_path]
	print ' '.join(args)
	call(args)

# make_model('brown.txt')
# make_model('gutenberg.txt')
# make_model('nytimes.txt')
