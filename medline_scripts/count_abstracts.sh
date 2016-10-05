#!/bin/bash

find /nlp/data/corpora/medline_data/xml_files -type f | head -n ${1} | python count_abstracts.py