#!/bin/bash

find /nlp/data/corpora/medline_data/xml_files -type f | head -n ${1} | python ~/developer/maple/medline_scripts/count_abstracts.py
