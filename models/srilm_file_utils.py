import os


def convert_file_to_lines(file_str):
	split_sentences = file_str.split('.')
	for sentence in split_sentences:
		sentence = sentence.replace('\n', '')
	return split_sentences.join('\n') + '\n'


def convert_dir_to_file(file_dir, output_file):
	output_file = open(output_file, 'w')

	for filename in os.listdir(file_dir):
		input_file = open(filename, "r")
		to_write = convert_file_to_lines(input_file.read())
		output_file.write(to_write)

	output_file.close()
