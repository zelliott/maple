# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:20:32 2017

@author: omarpaladines
"""

from subprocess import check_output
import srilm_file_utils as file_utils
from constants import srilm_path
from constants import test_data_clean_path
from constants import test_data_post_path
from constants import train_data_clean_path
from constants import srilm_language_models_path as lm_path
from constants import temp_test_file
from postprocessing import vocabulary
from postprocessing import postprocess

# Returns the ppl score for a single abstract and language model
def test_model(test_file, language_model, order):
    
    # preprocess unknown words wrt model
    vocab = vocabulary(train_data_clean_path + '/' + language_model + '.txt')
    test_file_path = test_data_clean_path + '/' + test_file
    test_file_path_post = test_data_post_path + '/' + test_file
    postprocess(vocab, test_file_path, test_file_path_post)
    
    # calculate perplexity
    language_model = lm_path + '/' + language_model + '.lm'
    ngram_cmd = srilm_path + '/ngram'

    test_file = open(test_file_path_post, 'r')
    test_file_text = test_file.read()
    test_file_text_formatted = file_utils.convert_file_to_lines(test_file_text)
    
    temp_test = open(temp_test_file, 'w')
    temp_test.write(test_file_text_formatted)
    temp_test.close()
	
    # actual call to srilm	
    args = [ngram_cmd,
			'-lm',
			language_model,
			'unk',
			'-order',
			order,
			'-ppl',
			temp_test_file]
   
    model_output = check_output(args)
    stats = model_output.split('\n')[1]
    stats_split = stats.split(' ')
    ppl = stats_split[7]
    return float(ppl)

#print (test_model('0','nytimes_uni', '1'))
