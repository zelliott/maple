import random
import json

import fetch_random_abstracts
import remove_words

def Generate_Test(start_num, count):
    questions = {}
    tests = {}
    for i in range(count):
        print i
        abstract_data = fetch_random_abstracts.fetch_abstracts()
        j = 1
        for name in abstract_data.keys():
            for text in abstract_data[name]:
                questions["Question"+str(j)] = remove_words.remove_words(text, name)
                j += 1
        tests["Test" + str(start_num+i)] = questions
        questions = {}

    return json.dumps(tests, indent=4, separators=(',', ': '), sort_keys=True)


f = open("Tests.txt", "w")
f.write(Generate_Test(1, 100).encode('utf8'))
f.close()
