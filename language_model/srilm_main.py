import srilm_file_utils as file_utils
import srilm_build_model as build_model
import srilm_test_text as test_text
from subprocess import call
from constants import language_model_file as sri_lim_file
from constants import temp_train_file as tt_file
from constants import output_test_file

temp_train_file = tt_file
language_model_file = sri_lim_file

def create_and_test_model(train_file_dir, test_file_dir):
	file_utils.convert_dir_to_file(train_file_dir, temp_train_file)
	build_model.make_model()
	call(['rm', temp_train_file])
	test_text.test_model(test_file_dir, output_test_file)


create_and_test_model('algorithms', 'neoplasms')