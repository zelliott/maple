from subprocess import call
from constants import srilm_path
from constants import train_data_clean_path
from constants import srilm_language_models_path

def make_model(train_file):
	"""
	Function to make the srilm langauge model. Issues a srilm command line 
	argument to make a model of the same name as the train file, placing it in 
	the srilm_models directory.
	args:
		train_file - the string name of the training file located in the 
		train_data/clean directory.
	"""

	# the srilm command used to create a language model
	ngram_count_cmd = srilm_path + '/ngram-count'

	model_name = train_file.split('.')[0] + '.lm'
	model_path = srilm_language_models_path + '/' + model_name

	train_file_path = train_data_clean_path + '/' + train_file
	
	# The arguments used for srilm command. Change these arguments to change
	# the parameters such as smoothing.
	args = [ ngram_count_cmd, 
			'-unk', 
			'-text', 
			train_file_path, 
			'-lm', 
			model_path ]
	print ' '.join(args)
	call(args)

# To run this function, simply add a function call to the end of this file, and
# run the file directly from the command line. An example function call would 
# look like:
# make_model('nytimes.txt')
