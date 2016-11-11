from subprocess import call
from constants import srilm_path
from constants import language_model_file
from constants import temp_train_file


def make_model():
	ngram_count_cmd = srilm_path + '/ngram-count'
	args = [ngram_count_cmd, '-text', temp_train_file, '-lm', language_model_file]
	print ' '.join(args)
	call([ngram_count_cmd, '-text', temp_train_file, '-lm', language_model_file])
