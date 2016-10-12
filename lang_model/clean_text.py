import os
import re
import xml.etree.ElementTree as et

xml_file_path = os.path.dirname(os.path.abspath(__file__)) + "/test/test.xml"

xml = ''
with open(xml_file_path) as f:

	# Honestly, having to do this is just stupid on my part...
	# the [topic].xml files are not perfectly valid xml, so you
	# have to 'fix' them before parsing.
	xml = f.read()
	xml = re.sub(r'(<\?xml[^>]+\?>)', '', xml)
	xml = '<?xml version=\'1.0\' encoding=\'utf8\'?>' + xml
	xml = re.sub(r'(<\?xml[^>]+\?>)', r'\1\n<root>', xml) + '</root>'

def clean_text(topics):
	curr_dir = os.path.dirname(os.path.abspath(__file__))
	clean_dir = curr_dir + "/clean"
	if not os.path.exists(clean_dir):
		os.makedirs(clean_dir)
	for topic in topics:
		if not os.path.exists(clean_dir + "/" + topic):
			os.makedirs(clean_dir + "/" + topic)

	parser = et.XMLParser(encoding='utf-8')
	root = et.fromstring(xml, parser=parser)

	# Count each abstract/citation
	for citation in root.iter('MedlineCitation'):

	# If this article has a mesh list...
		for descriptor in citation.findall('.//DescriptorName'):
			if descriptor.text in topics:
				topic = descriptor.text
				title = citation.findall('.//ArticleTitle')[0]
				text = citation.findall('.//AbstractText')[0]

				new_file = open(clean_dir + "/" + topic + "/" + title, 'w')
				new_file.write(text)
				new_file.close()
				break




