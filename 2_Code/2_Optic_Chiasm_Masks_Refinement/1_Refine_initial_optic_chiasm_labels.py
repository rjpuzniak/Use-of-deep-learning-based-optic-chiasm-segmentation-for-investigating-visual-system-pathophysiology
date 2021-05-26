from functions import bounding_box, create_groundtruth

import os

groups=['HCP','CHIASM']

for group in groups:
	for subject in os.listdir('../../1_Data/1_T1w_Images_and_Labels/1_T1w_Images/'+group):
		try:
			print(create_groundtruth(group,subject))
		except:
			continue
