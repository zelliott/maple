import classify
import find_words
import sys
import json

def main(argv):
	[text] = argv
	[doc_class] = classify.classify([text])
	most_difficult = find_words.get_most_difficult(text, doc_class)
	print json.dumps(most_difficult, ensure_ascii=False)

if __name__ == "__main__":
	main(sys.argv[1:])