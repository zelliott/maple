779 total .xml files in `/nlp/data/corpora/medline_data/xml_files`

Chose file at random: `medline15n0778.xml`

Each abstract begins and ends with a `<MedlineCitation>` tag.  Thus, we count the number of abstracts by counting the number of these tags that we see in a given file.

Note, note all `MedlineCitation`s have `MeshHeadingList`s, which store the keywords by which we categorize papers into different topics.  Thus, we have two separate counts: (1) the number of abstracts in a file, and (2) the number of abstracts that also have `MeshHeadingList`s in them.

The file `medline15n0778.xml` has:

 - 30,000 abstracts
 - 14,221 abstracts with `MeshHeadingList`s

This analysis is performed by the script `count_abstracts.py`.