
import os
import csv 
from subprocess import call
from constants import test_data_raw_path
from constants import test_data_clean_path


'''
COMMENT ABOUT FILE
'''

'''
COMMENT ABOUT FUNCTION
'''
def get_abstracts():
    texts = []
    fr = open("clozeAbstracts.csv", "r")
    csv_reader = csv.reader(fr, delimiter=',')
    for row in csv_reader:
        #row[0] is the abstract
        #row[1] would be topic
        texts.append(row[0])

    return texts

'''
COMMENT ABOUT FUNCTION
.encode('UTF-8')
'''
def create_abstract_files(abstract_dir):
	call(['mkdir', abstract_dir])
 
	abstracts = get_abstracts()

	for i in range(0, len(abstracts)):
		if len(abstracts[i].replace(' ', '').replace('\n', '')) > 0:
			to_write = open(abstract_dir + '/' + str(i), 'w')
			to_write.write(abstracts[i])
			to_write.close()

create_abstract_files("./post_test/cloze_test/")