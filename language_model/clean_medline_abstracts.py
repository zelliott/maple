import os
import re
import xml.etree.ElementTree as et
from subprocess import call


def get_abstracts(file_path):
	texts = []

	f = open(file_path)
	xml = f.read()

	root = et.fromstring(xml)

	for abstract in root.findall('.//Abstract'):
		texts.append(abstract.text)
	return texts

def create_abstract_dirs(abstract_files):
	for abstract_file in abstract_files:
		abstract_dir =  abstract_file.split('.')[0]
		call(['mkdir', abstract_dir])
		abstracts = get_abstracts(abstract_file)
		for i in range(0, len(abstracts)):
			if len(abstracts[i].replace(' ', '').replace('\n', '')) > 0:
				to_write = open(abstract_dir + '/' + str(i), 'w')
				to_write.write(abstracts[i].encode('UTF-8'))

create_abstract_dirs(['neoplasms.xml'])
