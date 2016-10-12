import model
import clean_text
import sys
import os

ngram_model = model.build_model(1)
topics_list = []
if len(sys.argv) >= 2:
	topics_list = sys.argv[1:]

clean_text.clean_text(topics_list)

curr_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = curr_dir + "/data"

for topic in topics_list:
	topic_dir = data_dir + "/" + topic
	files = os.listdir(topic_dir)
	print "TOPIC: " + topic + "\n"
	for f in files:
		text = open(topic_dir + "/" + f, 'r').read()
		print "\t FILENAME: " + f
		print "\t SCORE: " + str(model.get_avg_log_prob(ngram_model, text))
	print "\n"
print curr_dir

