import os
from constants import test_data_clean_path

total_files = 1000

for test_dir in os.listdir(test_data_clean_path):
	ctr = 0
	total_len = 0.0
	test_dir_path = test_data_clean_path + '/' + test_dir
	for test_file_name in os.listdir(test_dir_path):
		test_file = open(test_dir_path + '/' + test_file_name, 'r')
		test_file_text = test_file.read()
		total_len = total_len + len(test_file_text.split())

		ctr = ctr + 1
		if ctr == total_files:
			print test_dir
			print str(total_len / ctr)
			break
