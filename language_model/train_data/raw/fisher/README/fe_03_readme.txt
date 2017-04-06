
Fisher English Training Transcript Data, Part 1 -- LDC2004T19
=============================================================

This corpus represents the first half of a collection of
conversational telephone speech (CTS) that was created at the LDC
during 2003.  It contains transcript data for 5850 complete
conversations, each lasting up to 10 minutes.  In addition to the
transcriptions, which are found under the "trans" directory, there is
a complete set of tables describing the speakers, the properties of
the telephone calls, and the set of topics that were used to initiate
the conversations.

The second half of the collection (Fisher English Training Transcript
Data, Part 2) will be released by the LDC in 2005, and will be
organized as an extension of the Part 1 corpus.  Taken as a whole, the
two parts comprise 11,699 recorded telephone conversations.

Data collection and transcription were sponsored by DARPA and the
U.S. Department of Defense, as part of the EARS project for research
and development in automatic speech recognition.


Properties and Types of transcript files
----------------------------------------

Overall, about 12% of the conversations were transcribed at the LDC,
and the rest were done by BBN and WordWave, using a significantly
different approach to the task.  A central goal in both sets was to
maximize the speed and economy of the transcription process, and this
in turn involved certain aspects of mark-up detail and quality control
that may have been common in previous, smaller corpora.

The LDC transcripts were based on automatic segmentation of the audio
data, to identify the utterance end-points on both channels of each
conversation.  Given these time stamps, manual transcription was
simply a matter of typing in the words for each segment and doing a
rudimentary spell-check.  No attempt was made to modify the
segmentation boundaries manually, or to locate utterances that the
segmenter might have missed.  Portions of speech where the transcriber
could not be sure exactly what was said were marked with double
parentheses -- " (( ... )) " -- and the transcriber could hazard a
guess as to what was said, or leave the region between parentheses
blank.  The LDC transcription process yields one plain-text transcript
file per conversation, in which the first two lines show the call-ID
and the fact that the transcript was done at the LDC; the remainder of
the file contains one utterance per line (with blank lines separating
the utterances), with the start-time, end-time, speaker/channel-ID and
utterance text.  For example, here are the first few lines of an LDC
transcript file:


# fe_03_00001.sph
# Transcribed at the LDC

3.76 5.54 A: and i generally prefer 

5.82 6.48 A: eating at home 

7.92 9.52 B: hi my name is andy 


The time stamps are expressed in seconds from the beginning of the
audio file; the speaker/channel-ID is either "A:" (for channel 1) or
"B:" (for channel 2); the remaining text is mono-case with no
syntactic punctuation.

The BBN/WordWave approach involved producing a complete manual
transcription of the two-channel conversation first, without assigning
any time stamps to the utterances.  Then the transcription text and
audio data were processed through an automatic speech recognition
system, to do forced alignment of the text with the audio and assign
time stamps to utterances.  (The process is explained in more detail
in the file "bbn_trans_readme.txt", in the "doc" directory.)  The end
result was a set of five text files for each conversation: the
original manual transcript (with no time stamps), and four separate
outputs from the force-alignment process.  Taken together, the latter
four files contain roughly the same extent of information as the LDC
transcript: time stamps and text for most if not all utterances in the
conversation.

For the current publication, the BBN transcription files are being
provided in two forms: the original structure of five text files per
conversation, and the single-file LDC format.  The "bbn_orig"
directory contains just the transcript data created by BBN, while the
"trans" directory contains the union of BBN and LDC transcripts
(i.e. the entire corpus), rendered entirely in the LDC style.  (Calls
that were transcribed by the LDC will not be found under the
"bbn_orig" directory.)

A major division of transcript data in the BBN structure was between
"auto-segmented" and "rejected" segments (cf. "bbn_trans_readme.txt").
The former showed a good match between manual transcription and forced
alignment recognition, whereas the latter did not.  In coercing these
files into the LDC transcript format, utterances from the "rejected"
set were marked with double parentheses around the utterance text, to
reflect the uncertainty suggested by low alignment scores.  To
illustrate, the following excerpt shows a couple of utterances that
come from the "auto-segmented" set, and one utterance that comes from
the "rejected" set:


# fe_03_00092.sph
# Transcribed by BBN/WordWave

0.00 1.21 B: hello 

0.73 1.93 A: hello 

...

12.39 14.07 B: (( oh yeah )) 


The original files created by the BBN process did not use double
parentheses at all, hence all double-parens in this set of derived
transcript files (under the "trans" directory) have been introduced by
the transformation into LDC format.


File names and directory structure
----------------------------------

Each file is identified by a conversation-ID in the following form:

  fe_03_nnnnn

where "nnnnn" is a sequential number starting at 00001; the numeric
sequence simply represents the relative order in which the calls were
recorded; "fe" refers to "Fisher English" (similar CTS collections
were done in Arabic and Mandarin Chinese); the "_03_" refers to the
2003 collection phase (a follow-on collection, to be published later,
was conducted in 2004).

In the "trans" directory, all file names have a final ".txt"
extension, indicating the plain-text LDC transcript format (in the
companion corpus of audio data, each speech file uses the same file-ID
as the corresponding transcript file, and has a ".sph" extension).

In order to keep directory sizes more manageable, the calls have been
divided into a series of directories containing subsets of 100 calls
each.  Each directory name is simply the first three digits of the
five-digit conversation-ID number (e.g. "000/fe_03_00001.txt", etc);
these subset directories are found directly under both "trans" and
"bbn_orig" (under "bbn_orig", each "nnn" directory contains the three
file-type directories, "auto-segmented", "reject" and "originals").
In the companion audio corpus, the equivalent series of subset
directories are located under a single "audio" directory.

In addition to the "trans" and "bbn_orig" directories,
the top-level directory also contains a "doc" directory (for
documentation and tables) and an "index.htm" file.


Overview of database tables
---------------------------

The Fisher telephone collection was driven by a relational database
that kept track of speakers, telephone information, and details on
each successful call.  The "doc" directory provides three tables drawn
from this database, together with a text file describing the contents
of each table; these are described briefly below:

1.  fe_03_p1_filelist.tbl (cf. doc_filelist_tbl.txt)

This is a tab-delimited plain-text table, with one row for each call
in the Fisher English Part1 corpus.  The columns indicate the call-ID,
the volume-ID for the DVD in the corresponding Speech corpus that
contains the audio for the call, the gender of the two speakers
involved in the call, and where the call was transcribed.

2.  fe_03_p1_calldata.tbl (cf. doc_calldata_tbl.txt)

This is a comma-separated-value (CSV) plain-text table, with one row
for each call in the Part1 corpus.  (The first row provides column
labels.)  The columns indicate call-ID, date and time of the call,
topic-ID used in the call, and details about the speakers and phones
used.

3.  fe_03_pindata.tbl (cf. doc_pindata_tbl.txt)

This is a CSV plain-text table, with one row for each speaker who
participated in a Fisher English Training call.  (The first row
provides column labels.)  The columns indicate speaker-ID, demographic
information as provided by the speaker, and a list of call-sides in
which the speaker is represented.  (For speakers who occur in more
than one call, the list of calls in the last field are separated by
semi-colons.)

For reasons discussed in the next section, the speaker information
in the "pindata" table might not reflect the properties of the voice
that was actually recorded in a given call.  For example, a particular
speaker-ID might have been assigned to a man, but when the Fisher
collection system dialed out to the phone number for that speaker, a
woman answered and completed the process of recording a conversation.

In order to reduce the amount of uncertainty in the database tables
being presented with the corpus, the "calldata" table presents only
the information derived from manual audits of each call.  (The audit
process is described in the next section, and details about how the
audit information is presented in the "calldata" table are described
in the associated "doc" file).  In the "pindata" table, you'll find
the demographic data provided by each speaker during the recruiting
process (including gender); combined with this, in the final field of
"pindata", you'll find the list of calls that involved the PIN
assigned to the speaker, including call-ID, channel (A or B) and the
gender/dialect information from manual audits.  Here is an example of
a row taken from "pindata" that demonstrates a discrepancy between
stated demographics and audit results:

2637,F,54,16,English,WA,2,06972_A/m.a;08175_A/f.a

This row describes speaker PIN 2637, who registered as a 54-year-old
female with 16 years of education, a native speaker of American
English raised in Washington state; two calls were recorded involving
this PIN, one of which (call-ID 06972, channel A) was found to contain
a male voice (also a native speaker of American English).  We can't
infer any other demographic information about the male speaker (except
his approximate age as determined by manual audit, to be found in the
"calldata" table for call-ID 06972); conceivably, the female speaker
in call-ID 08175 (channel A) might also be different from the
54-year-old woman who registered to participate in the collection, but
it's probably safe to assume that most of the demographic data is
applicable, given the matching gender.

Note that the "pindata" table contains information on all the speakers
in the entire Fisher English collection, drawn from all 11,699 calls
comprising both Part 1 (the 2004 release) and Part 2 (the 2005
release).  As a result, half of the call-ID's referenced in this table
will not be found in the Part 1 corpus.  The "calldata" and "filelist"
tables reflect only the contents of the Part 1 corpus.


Method of data creation
-----------------------

The telephone calls were recorded digitally from a T-1 trunk line that
terminates at a host computer at the LDC (the "robot-operator").  Over
12,000 speakers had been recruited from around the United States, both
native and non-native speakers of English.  The vast majority of
recruits submitted their demographic and contact information to the
LDC via a specialized Fisher enrollment page on the LDC's web server,
in response to a wide range of advertising and announcements, both on
commercial media and through various Internet channels.

The enrollment form requested age, sex, and geographic background, as
well as information about the telephone(s) to be used by each recruit;
a scheduling grid was provided to allow recruits to indicate hours and
days of the week when they would be able to accept calls from the
robot operator.  A staff of recruiters at the LDC reviewed each of the
enrollment forms submitted via the web, and also fielded phone calls
and email from other prospective recruits.  Enrollment information
went into a relational database for tracking subjects, phones, and all
call activity on the robot operator.

The T-1 telephone circuit dedicated to Fisher English collection was
configured so that some lines would service people who dialed in to
the system while other lines would be used for dialing out to people
according to their hours of availability, as provided in the
enrollment process.

During the hours when people had indicated availability to receive
calls, the robot operator queried the database continuously for
available callees and dialed out to multiple people simultaneously,
while also accepting dial-ins.  Whenever any two active lines (dial-in
or dial-out) reached a point where the callees were ready to proceed
with a conversation, the robot operator bridged the two lines,
announced the topic of the day to both parties, and began recording by
copying the digital mu-law sample data from each line directly to disk
files.

At enrollment, each recruit was assigned a unique PIN; subjects who
dialed in to the robot operator were required to supply this PIN
before being accepted for a recording.  However, each time the system
dialed out to a specific PIN selected from the database, the person
answering the phone could accept the call, and proceed with recording a
conversation, without supplying a PIN to verify his or her identity.

Avoiding PIN verification on dial-outs was viewed as a worthwhile
trade-off.  It would introduce some amount of uncertainty regarding
speaker characteristics in the recorded calls: the person to whom a
given PIN was assigned might not be the one who was actually recorded
in a given call when that PIN was selected for dial-out; but the
number of calls where the actual speaker was not the "expected"
speaker would be relatively small.  Meanwhile, the likelihood would be
relatively high that a large proportion of subjects would not be able
to find or recall their assigned PIN's when they received a call from
the robot operator, and this would severely limit the success of the
Fisher collection strategy.  The barriers and complications that would
result from PIN verification problems on dial-outs would have been
unmanageable, owing to the large number of people involved (over
14,000 recruits were enrolled over the course of the collection), the
necessarily sparse communications between these people and the LDC
recruiting staff, and the fact that a maximum of three successful
calls would be collected for each PIN.

On each day of call collection a single topic of discussion was chosen
sequentially from a set of 40 topics prepared in advance, and in all
calls conducted on a given day, all callees would be presented with
the same topic.  After each cycle of 40 days, the same topic list was
repeated.  For the most part, people tended to adhere to the suggested
topic in their conversations.

After calls were recorded, automatic utterance segmentation was
applied to both channels of every file.  If the segmentation did not
yield at least 5 minutes of detected speech, the call was rejected
from further consideration.  Otherwise, up to four segments of
approximately 30 seconds each were automatically selected at intervals
throughout each call, and these segments were used for manual audit.

LDC staff listened to at least two segments from every call, and the
following audit judgments were recorded in the central Fisher
database:

 For each channel/speaker:
    - sex
    - approximate age (young adult, adult or senior)
    - native speaker of American English (or not)

 For each 30-second segment:
    - relative signal quality (poor, fair, good)
    - relative conversation quality (poor, fair, good)

In assessing conversation quality, a segment was marked "poor" if
people were talking about the Fisher project (as opposed to some other
topic), or if people were having a hard time coming up with things to
say.  Auditors did not have access to information about what the
assigned topic was for each call, and so could not judge whether
speakers were adhering to the assigned topic, but if the segments
showed an engaged discussion about anything other than the Fisher
project, it was marked "good" for conversation quality.

The file "doc_calldata_tbl.txt" describes how the audit information is
presented in the associated database table file.

David Graff
Linguistic Data Consortium
December, 2004

