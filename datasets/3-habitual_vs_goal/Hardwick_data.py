import numpy as np 
import csv
import pandas as pd

import matplotlib.pyplot as plt


# change this to extract different subject
subject = 1

# %untrained (minimal practice condition)
#     %001 (data from hand 'practice' on assessment day)
#     %002 (criterion assessment, original map)
#     %003 (criterion assessment, revised map)
#     %004 (timed response assessment, revised map)

# %trained (4 days practice condition)
#     %001 (data from trained day 1)
#     %002 (data from trained day 2)
#     %003 (data from trained day 3)
#     %004 (data from trained day 4)
#     %005 (data from hand 'practice' on assessment day
#     %006 (criterion assessment, original (trained) map)
#     %007 (criterion assessment, revised map)
#     %008 (timed response assessment, revised map)


# 1 'Subject', 			# subject
# 2 'Session', 			# session within the condition
# 3 'Stamp', 			??? idk, remove
# 4 'Trial', 			# trial num within session
# 5 'DesOnset', 		# used for calculating prep time: PT = RT - DesOnset
# 6 'RecOnset', 		??? recorded onset - remove
# 7 'Stimulus', 		# which symbol was shown
# 8 'TargetButton', 	# correct button to be pressed
# 9 'ResponseNum',  	# if subjects correct response, how many repeats
# 10 'ResponseButton',  # button pressed
# 11 'RT', 				# RT
# 12 'Correct', 		# yes/no
# 13 'Tally']			??? idk, remove




longdat = pd.DataFrame()

# data from minimal training condition
for i in range(1,5):
	filename = '/Users/heike/Downloads/osfstorage-archive/Experiment1/10%.0f/00%.0f.dat' %(subject, i)

	lines = open(filename).readlines()

	# read flash.dat to a list of lists
	datContent = [i.strip().split() for i in open(filename).readlines()]

	# make matrix from trials
	mat = np.array(datContent[1:], dtype='float')

	# columns
	cols = datContent[0][:-2]
	
	# dataframe
	dat = pd.DataFrame(mat, columns=cols)

	longdat = longdat.append(dat)

# # add column encoding condition
longdat['condition'] = 'minimal'


# add data from 4 day training condition
for i in range(1,9):
	filename = '/Users/heike/Downloads/osfstorage-archive/Experiment1/50%.0f/00%.0f.dat' %(subject, i)

	lines = open(filename).readlines()

	# read flash.dat to a list of lists
	datContent = [i.strip().split() for i in open(filename).readlines()]

	# make matrix from trials
	mat = np.array(datContent[1:], dtype='float')

	# columns
	cols = datContent[0][:-2]
	
	# dataframe
	dat = pd.DataFrame(mat, columns=cols)
	dat['condition'] = 'four_day'

	longdat = longdat.append(dat)

longdat = longdat.reset_index(drop=True)

# replace matlab nan with real nan
longdat.replace(999, np.nan, inplace=True)

# add columns
longdat['PT'] = longdat['RT'] - longdat['DesOnset']

# change format from float to integer, rename variables
longdat['subject'] = longdat['Subject'].values.astype('int')-100
longdat['session'] = longdat['Session'].values.astype('int')

longdat['Trial'].values[np.where(np.isnan(longdat['Trial']))] = 999

longdat['trial'] = longdat['Trial'].values.astype('int')
longdat['stimulus'] = longdat['Stimulus'].values.astype('int')
longdat['response'] = longdat['ResponseButton'].values.astype('int')
longdat['target'] = longdat['TargetButton'].values.astype('int')
longdat['num_resp'] = longdat['ResponseNum'].values.astype('int')
longdat['correct'] = longdat['Correct'].values.astype('int')
longdat['stim_onset'] = longdat['DesOnset']

longdat = longdat.drop(columns=['Subject', 'Session', 'Stamp', 'Trial', 'DesOnset', 'RecOnset', 
			  'Stimulus', 'TargetButton', 'ResponseNum', 'ResponseButton',
			  'Correct', 'Tally'])


kill


longdat.to_pickle('Hardwick_subj-%.0f.p' %subject)
