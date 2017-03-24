import os

def make_corpora_file(source_dir, dest_dir, file_name):
	output_file = open(dest_dir + '/' + file_name, 'w')
	for source_file_name in os.listdir(source_dir):
		source_file = open(source_dir + '/' + source_file_name, 'r')
		source_file_text = source_file.read()
		source_file_text = source_file_text.replace('\n', ' ')
		source_file_text = source_file_text.lower()
		output_file.write(source_file_text + '\n')
	output_file.close()

make_corpora_file('old_text/algorithms', 'corpora', 'algorithms')
make_corpora_file('old_text/cell_line_tumor', 'corpora', 'cell_line_tumor')
make_corpora_file('old_text/neoplasms', 'corpora', 'neoplasms')
make_corpora_file('old_text/obesity', 'corpora', 'obesity')
make_corpora_file('old_text/signal_transduction', 'corpora', 'signal_transduction')