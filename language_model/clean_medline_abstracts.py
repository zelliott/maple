import os
import re
import xml.etree.ElementTree as et
from subprocess import call
from constants import test_data_raw_path
from constants import test_data_clean_path

'''
COMMENT ABOUT FILE
'''

'''
COMMENT ABOUT FUNCTION
'''
def get_abstracts(file_path):
	texts = []
	f = open(file_path)
	xml = f.read()
	root = et.fromstring(xml)

	for abstract in root.findall('.//Abstract'):
		texts.append(abstract.text)

	return texts

'''
COMMENT ABOUT FUNCTION
'''
def create_abstract_dirs(abstract_files):
	for abstract_file in abstract_files:

		abstract_dir =  abstract_file.split('.')[0]
		abstract_dir = test_data_clean_path + '/' + abstract_dir

		call(['mkdir', abstract_dir])

		abstracts = get_abstracts(test_data_raw_path + '/' + abstract_file)

		for i in range(0, len(abstracts)):
			if len(abstracts[i].replace(' ', '').replace('\n', '')) > 0:
				to_write = open(abstract_dir + '/' + str(i), 'w')
				to_write.write(abstracts[i].encode('UTF-8'))
				to_write.close()

abstract_files = os.listdir(test_data_raw_path)
create_abstract_dirs(abstract_files)
