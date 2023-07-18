This dataset is a single subject (subject 1) from experiment 1 of Hardwick et al., Nature Human Behavior (2019).


It is a `n_trials x 12` pandas dataframe with columns 
`['subject', 'condition', 'session', 'trial', 'stimulus', 'target', 'response', 'stim_onset', 'num_resp', 'correct', 'RT', 'PT']`.
- `condition` encodes whether the session was part of the minimal or four-day training protocol
- `session` encodes the session (from 1-4 in minimal condition, 1-8 in four-day training).
  -  minimal practice 1 (data from hand 'practice' on assessment day)
  -  minimal practice 2 (criterion assessment, original map)
  -  minimal practice 3 (criterion assessment, revised map)
  -  minimal practice 4 (timed response assessment, revised map)
  - four-days practice 1 (data from trained day 1)
  - four-days practice 2 (data from trained day 2)
  - four-days practice 3 (data from trained day 3)
  - four-days practice 4 (data from trained day 4)
  - four-days practice 5 (data from hand 'practice' on assessment day)
  - four-days practice 6 (criterion assessment, original (trained) map)
  - four-days practice 7 (criterion assessment, revised map)
  - four-days practice 8 (timed response assessment, revised map)
- `trial` within session
- `stimulus` encodes the identity of the presented symbol
- `target` the correct response button
- `response` the chosen response button
- `stim_onset` the onset time of the stimulus
- `num_resp` the count of responses for the same trial
- `correct` whether response was correct or not
- `RT` and `PT` the response time (from trial start to response) and preparation time (from stimulus presentation to response)

Moreover, you can find the script to extract the same data from other subjects, if you want: 
Hardwick_data.py, which reads files from the Experiment1 folder that you can download (here)[https://osf.io/3fjez/?view_only=].
