# FAQ

#### What is the `scripts_output` folder?

This folder holds the output/results of the various medline_scripts.  The output comes in pairs, and have the following naming convention:

```
[name_of_script].e[qsub_job_id]
[name_of_script].o[qsub_job_id]
```

We only care about the `.o` output file (the `.e` ones are always empty, idk what they are used for).  That is, if the program `count_abstracts.py` was run with `qsub`, and was given id `e397715`, its output would have the filename `count_abstracts.py.o397715`.
