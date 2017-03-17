import os
import re
from subprocess import call
from subprocess import check_output

import srilm_file_utils as file_utils
from constants import srilm_path
from constants import model_order as order
from constants import test_data_clean_path
from constants import test_data_post_path
from constants import srilm_language_models_path as lm_path
from constants import temp_test_file
from postprocessing import vocabulary
from postprocessing import postprocess

def test_model(test_dir, output_file, language_model, doc_limit=1000, word_limit=600):

    '''
    # perform postprocessing step first
    vocab = vocabulary(lm_path + '/' + language_model)
    test_dir_path = test_data_clean_path + '/' + test_dir
    test_dir_path_post = test_data_post_path + '/' + test_dir
    for test_file_name in os.listdir(test_dir_path):
        postprocess(vocab, test_dir_path + '/' + test_file_name, 
                    test_dir_path_post + '/' + test_file_name )
    '''
    
    language_model = lm_path + '/' + language_model
    ngram_cmd = srilm_path + '/ngram'
    output_file = open(output_file, 'w')
    output_file.write('file_name,oov,doc_length,logprob,ppl,ppl1\n')
    test_dir_path = test_data_post_path + '/' + test_dir
    ctr = 0
    for test_file_name in os.listdir(test_dir_path):

        test_file = open(test_dir_path + '/' + test_file_name, 'r')
        test_file_text = test_file.read()
        test_file_text = test_file_text.split()
        if len(test_file_text) > word_limit:
            test_file_text = test_file_text[:word_limit]
        doc_length = len(test_file_text)
        test_file_text = ' '.join(test_file_text)
        test_file_text_formatted = file_utils.convert_file_to_lines(test_file_text)

        temp_test = open(temp_test_file, 'w')
        temp_test.write(test_file_text_formatted)
        temp_test.close()
		
        args = [ngram_cmd,
			'-lm',
			language_model,
			'unk',
			'-order',
			order,
			'-ppl',
			temp_test_file,
			'> logs/test_output.txt']
        model_output = check_output(args)
        oovs = model_output.split('\n')[0].split(',')[2].split()[0]
        stats = model_output.split('\n')[1]
        stats_split = stats.split(' ')
        logprob = stats_split[3]
        ppl = stats_split[5]
        ppl1 = stats_split[7]
        output_file.write(test_file_name + ',' + 
			oovs + ',' + 
			str(doc_length) + ',' + 
			logprob + ',' + 
			ppl + ',' + 
			ppl1 + '\n')
        ctr = ctr + 1
       
        if ctr % 100 == 0:
            print 'testing file ' + str(ctr)
        if ctr == doc_limit:
		 break

    output_file.close()
    call(['rm', temp_test_file])

'''
for test_dir in os.listdir(test_data_post_path):
	print 'Starting tests on ' + test_dir
	for lm in os.listdir(lm_path):
		print 'Using model ' + lm
		lm_name = lm.split('.')[0]
		output_file = 'test_output/' + lm_name + '_' + test_dir + '.txt'
		test_model(test_dir, output_file, lm)
  '''
    
output_file = 'test_output/' + 'nytimes' + '_' + 'cloze_tests' + '.txt'
test_model('cloze_tests', output_file, 'nytimes.lm')

