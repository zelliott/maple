# FAQ

#### What does each .py script do?

`count_abstracts.py`:  Counts the number of abstracts in a given file/directory of files.  This script returns two separate counts:

1. A count of the number of abstracts in the file(s)
2. A count of the number of abstracts in the file(s) that also have non-empty MeshHeadingLists.

`descriptors_by_popularity.py`: Tallys all of the topics in a given file/directory of files, and returns a list of these topics to their counts, sorted by count.  Topic information is held in an XML parent element called `MeshHeadingList`, with the following structure:

```
<MeshHeadingList>
  <MeshHeading><DescriptorName>[topic here]</DescriptorName></MeshHeading>
  <MeshHeading><DescriptorName>[topic here]</DescriptorName></MeshHeading>
  ...
</MeshHeadingList>
```

`grab_abstracts_by_topic.py`: Given a certain topic (i.e. DescriptorName), return all of the abstracts (in their original XML) who have that topic as one of their MeshHeadings.

#### What's with all the corresponding .sh scripts?

The shell scripts just make the .py scripts easier to call on nlpgrid.

#### What is the `scripts_output` folder?

This folder holds the output/results of the various medline_scripts.  The output comes in pairs, and have the following naming convention:

```
[name_of_script].e[qsub_job_id]
[name_of_script].o[qsub_job_id]
```

We only care about the `.o` output file (the `.e` ones are always empty, idk what they are used for).  That is, if the program `count_abstracts.py` was run with `qsub`, and was given id `397715`, its output would have the filename `count_abstracts.py.o397715`.
