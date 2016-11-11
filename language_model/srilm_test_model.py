import os
import re
from subprocess import call
from subprocess import check_output

import srilm_file_utils as file_utils
from constants import srilm_path
from constants import model_order as order
from constants import test_data_clean_path
from constants import srilm_language_models_path as lm_path
from constants import temp_test_file

def test_model(test_dir, output_file, language_model):
	language_model = lm_path + '/' + language_model
	ngram_cmd = srilm_path + '/ngram'
	output_file = open(output_file, 'w')
	output_file.write('file_name,logprob,ppl,ppl1')
	test_dir_path = test_data_clean_path + '/' + test_dir
	for test_file_name in os.listdir(test_dir_path):

		test_file = open(test_dir_path + '/' + test_file_name, 'r')
		test_file_text = test_file.read()
		test_file_text_formatted = file_utils.convert_file_to_lines(test_file_text)

		temp_test = open(temp_test_file, 'w')
		temp_test.write(test_file_text_formatted)
		temp_test.close()
		
		args = [ngram_cmd,
			'-lm',
			language_model,
			'-order',
			order,
			'-ppl',
			temp_test_file]
		model_output = check_output(args)
		stats = model_output.split('\n')[1]
		stats_split = model_output_stats.split(' ')
		logprob = stats_split[3]
		ppl = stats_split[5]
		ppl1 = stats_split[7]
		output_file.write(test_file_name + ',' + logprob + ',' + ppl + ',' + ppl1 + '\n')

	output_file.close()
	call(['rm', temp_test_file])

for test_dir in os.listdir(test_data_clean_path):
	for lm in os.listdir(lm_path):
		lm_name = lm.split('.')[0]
		output_file = 'test_output/' + lm_name + '_' + test_dir + '.txt'
		test_model(test_dir, output_file, lm)

