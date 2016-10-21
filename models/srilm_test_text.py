import os
import srilm_file_utils as file_utils
from subprocess import call
from subprocess import check_output
from constants import srilm_path
from constants import language_model_file
from constants import temp_test_file
from constants import model_order as order

def test_model(test_dir_path, output_file_path):
	ngram_cmd = srilm_path + '/ngram'
	output_file = open(output_file_path, 'w')
	for test_file in os.listdir(test_dir_path):
		test_file = open(test_dir_path + '/' + test_file, 'r')
		test_file_text = test_file.read()
		test_file_text_formatted = file_utils.convert_file_to_lines(test_file_text)
		temp_test = open(temp_test_file, 'w')
		temp_test.write(test_file_text_formatted)
		temp_test.close()
		args = [ngram_cmd,
			'-lm',
			language_model_file,
			'-order',
			order
			'-ppl',
			temp_test_file]
		entropy = check_output(args)
		output_file.write(test_file + '\n' + entropy + '\n\n')
		call(['rm', temp_test_file])

	output_file.close()