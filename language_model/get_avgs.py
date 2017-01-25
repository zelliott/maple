import os

for result_file in os.listdir('test_output'):
	file = open('test_output/'+result_file, 'r')
	lines = file.readlines()
	oovs_sum = 0.0
	length_sum = 0.0
	ppl_sum = 0.0
	ctr = 0
	for line in lines[1:]:
		ppl_sum = ppl_sum + float(line.split(',')[4])
		length_sum = length_sum + float(line.split(',')[2])
		oovs_sum = oovs_sum + float(line.split(',')[1])
		ctr = ctr + 1
	print result_file + ' - length: ' + str(length_sum/ctr)
	print result_file + ' - oovs: ' + str(oovs_sum/ctr)
	print result_file + ' - ppl: ' + str(ppl_sum/ctr) + '\n'
