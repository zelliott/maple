import os
import re
import xml.etree.ElementTree as et
import build_models

brown_model = build_models.build_brown()
gutenberg_model = build_models.build_gutenberg()
spanish_model = build_models.build_spanish()

def get_abstracts(file_path):
	texts = []

	f = open(file_path)
	xml = f.read()

	root = et.fromstring(xml)

	for abstract in root.findall('.//Abstract'):
		texts.append(abstract.text)
	return texts

def print_entropies(topic, texts):
	print topic + '\n'
	for i in range(len(texts)):
		print 'Abstract ' + str(i) + ' - Brown: ' + str(brown_model.entropy(texts[i]))
		print 'Abstract ' + str(i) + ' - Gutenberg: ' + str(gutenberg_model.entropy(texts[i]))
		print 'Abstract ' + str(i) + ' - Spanish: ' + str(spanish_model.entropy(texts[i]))
		print ' '

# algorithms_path = os.path.dirname(os.path.abspath(__file__)) + "/../medline_scripts/scripts_output/abstracts_by_topic/_algorithms.xml"
# algorithms_texts = get_abstracts(algorithms_path)

# neoplasms_path = os.path.dirname(os.path.abspath(__file__)) + "/../medline_scripts/scripts_output/abstracts_by_topic/_neoplasms.xml"
# neoplasms_texts = get_abstracts(neoplasms_path)

obesity_path = os.path.dirname(os.path.abspath(__file__)) + "/../medline_scripts/scripts_output/abstracts_by_topic/obesity.xml"
obesity_texts = get_abstracts(obesity_path)

# print_entropies('algoirthms', algorithms_texts)
# print_entropies('neoplasms', neoplasms_texts)
print_entropies('obesity', obesity_texts)
