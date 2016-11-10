from nltk.corpus import stopwords
import re
import random
import json
import fetch_random_abstracts


# return true for bad word and false for good word
# bad word include fitting the bad word regex, len < 3, being all caps
def check_bad(string):
    regex = re.compile('[^a-zA-Z]')
    return not (len(regex.findall(string)) > 0 or len(string) < 3 or string.isupper())


def remove_words(text, topic):
    random.seed()
    original = text
    marked = []
    text = re.sub(r'\([^)]*\)', '', text)  # remove parentheses
    word_tokens = text.split()
    common_words = stopwords.words('english')
    new_words = [x for x in word_tokens if check_bad(x)
                 and x.lower() not in common_words]

    # randomly select 5 out of the all the words
    sample_indices = random.sample(range(1, len(new_words)), 5)
    count = 1
    for word in new_words:
        if count in sample_indices:
            marked.append(word)
        count += 1

    temp = marked

    # fetch indices and order words according to original text
    # indices is based on removed punctuation and split on spaces.
    count = 0
    actual_indices = []
    result = []
    for word in original.split():
        if word in temp:
            actual_indices.append(count)
            temp.remove(word)
            result.append(word)
        count += 1

    json_dict = {"originalString": original, "topic": topic,
                 "indices": actual_indices, "removedWords": result}

    return json_dict
    #return json.dumps(json_dict, indent=4, separators=(',', ': '))


if __name__ == "__main__":
    files = ["algorithms", "cell_line_tumor", "neoplasms",
             "molecular_sequence_data", "magnetic_resonance_imaging",
             "obesity", "signal_transduction"]
    abs_data = {}
    for name in files:
        abs_data[name] = []
        fetch_random_abstracts.deterministic_samples(name, abs_data)

    for name in abs_data.keys():
        for text in abs_data[name]:
            print remove_words(text, name)
