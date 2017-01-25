<<<<<<< HEAD
import xml.etree.ElementTree as et
import random
from tornado.escape import utf8


# fetch the shared abstracts from given filename (string),
# store into abs_data (dictionary)
def deterministic_samples(filename, abs_data):
    random.seed(324932)
    num_of_samples = 4
    sample_points = random.sample(range(1, 100), num_of_samples)

    fileformat = ".xml"
    tree = et.parse(filename + fileformat)
    root = tree.getroot()

    count = 1
    for abstractTextElement in root.findall('.//File//Abstract'):
        if (len(abstractTextElement.text) > 2):
            if count in sample_points:
                abs_data[filename].append(abstractTextElement.text.strip())
            count += 1
            if count > 100:
                break


# fetch the randomized abstracts from given filename (string),
# store into abs_data (dictionary)
def random_samples(filename, abs_data):
    random.seed()
    num_of_samples = 10
    fileformat = ".xml"
    sample_prob = 500  # 1/500 chance

    tree = et.parse(filename + fileformat)
    root = tree.getroot()

    count = 1
    for abstractTextElement in root.findall('.//File//Abstract'):
        if len(abstractTextElement.text) > 2:
            if count > 100 and random.randrange(1, sample_prob) == 1:
                abs_data[filename].append(abstractTextElement.text.strip())
                num_of_samples -= 1
                if num_of_samples == 0:
                    break
            count += 1


# remove extra abstracts from the shared pool,
# seeded for deterministic randomness
def random_remove(abs_data, num):
    random.seed(123905)
    mark_remove = random.sample(range(1, 7), num)
    count = 1
    for name in abs_data.keys():
        if count in mark_remove:
            abs_data[name].pop(0)
        count += 1

# randomly choose some abstracts (at most one from each topic)
# and add to abs_data again.


def random_repeat(abs_data, num):
    mark_repeat = random.sample(range(1, 7), num)
    count = 1
    for name in abs_data.keys():
        if count in mark_repeat:
            abs_data[name].append(abs_data[name][random.randrange(4, 12)])
        count += 1


def transform_json(abs_data):
    json_formatted = "{"
    for names in abs_data:
        for text in abs_data[names]:
            json_formatted = json_formatted + \
                "\n\t\"abstract\": {\n" + "\t\t\"topic\": \"" + names + \
                "\",\n" + "\t\t\"text\": \"" + text + "\"\n\t},"
    json_formatted = json_formatted[:-1] + "\n}"
    return json_formatted


# main function call
def fetch_abstracts():
    files = ["algorithms", "cell_line_tumor", "neoplasms",
             "molecular_sequence_data", "magnetic_resonance_imaging",
             "obesity", "signal_transduction"]
    abs_data = {}
    for name in files:
        abs_data[name] = []
        deterministic_samples(name, abs_data)

    print "finished determinstic sampling"
    random_remove(abs_data, 3)

    for name in files:
        random_samples(name, abs_data)

    random_repeat(abs_data, 5)

    return transform_json(abs_data)


if __name__ == "__main__":
    f = open("result.txt", "w")
    f.write(fetch_abstracts().encode('utf8'))
    f.close()
=======
import xml.etree.ElementTree as et
import random
from tornado.escape import utf8


# fetch the shared abstracts from given filename (string),
# store into abs_data (dictionary)
def deterministic_samples(filename, abs_data):
    random.seed(324932)
    num_of_samples = 4
    sample_points = random.sample(range(1, 100), num_of_samples)

    fileformat = ".xml"
    tree = et.parse(filename + fileformat)
    root = tree.getroot()

    count = 1
    for abstractTextElement in root.findall('.//File//Abstract'):
        if (len(abstractTextElement.text) > 2):
            if count in sample_points:
                abs_data[filename].append(abstractTextElement.text.strip())
            count += 1
            if count > 100:
                break


# fetch the randomized abstracts from given filename (string),
# store into abs_data (dictionary)
def random_samples(filename, abs_data):
    random.seed()
    num_of_samples = 10
    fileformat = ".xml"
    sample_prob = 500  # 1/500 chance

    tree = et.parse(filename + fileformat)
    root = tree.getroot()

    count = 1
    for abstractTextElement in root.findall('.//File//Abstract'):
        if len(abstractTextElement.text) > 2:
            if count > 100 and random.randrange(1, sample_prob) == 1:
                abs_data[filename].append(abstractTextElement.text.strip())
                num_of_samples -= 1
                if num_of_samples == 0:
                    break
            count += 1


# remove extra abstracts from the shared pool,
# seeded for deterministic randomness
def random_remove(abs_data, num):
    random.seed(123905)
    mark_remove = random.sample(range(1, 7), num)
    count = 1
    for name in abs_data.keys():
        if count in mark_remove:
            abs_data[name].pop(0)
        count += 1

# randomly choose some abstracts (at most one from each topic)
# and add to abs_data again.


def random_repeat(abs_data, num):
    random.seed()
    mark_repeat = random.sample(range(1, 7), num)
    count = 1
    for name in abs_data.keys():
        if count in mark_repeat:
            abs_data[name].append(abs_data[name][random.randrange(4, 12)])
        count += 1


def transform_json(abs_data):
    json_formatted = "{"
    for names in abs_data:
        for text in abs_data[names]:
            json_formatted = json_formatted + \
                "\n\t\"abstract\": {\n" + "\t\t\"topic\": \"" + names + \
                "\",\n" + "\t\t\"text\": \"" + text + "\"\n\t},"
    json_formatted = json_formatted[:-1] + "\n}"
    return json_formatted


# main function call
def fetch_abstracts():
    files = ["algorithms", "cell_line_tumor", "neoplasms",
             "molecular_sequence_data", "magnetic_resonance_imaging",
             "obesity", "signal_transduction"]
    abs_data = {}
    for name in files:
        abs_data[name] = []
        deterministic_samples(name, abs_data)

    random_remove(abs_data, 3)

    for name in files:
        random_samples(name, abs_data)

    random_repeat(abs_data, 5)

    return abs_data
#    return transform_json(abs_data)


if __name__ == "__main__":
    f = open("result.txt", "w")
    f.write(fetch_abstracts().encode('utf8'))
    f.close()
>>>>>>> f02d37d8f0bc494819877394430791d29784b347
