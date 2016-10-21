from subprocess import call
from constants import srilim_path
from constants import language_model_file
from constants import temp_train_file


def make_model:
	ngram_count_cmd = srilim_path + 'ngram_count'
	call([ngram_count_cmd, '-text', temp_train_file, '-lm', language_model_file])
