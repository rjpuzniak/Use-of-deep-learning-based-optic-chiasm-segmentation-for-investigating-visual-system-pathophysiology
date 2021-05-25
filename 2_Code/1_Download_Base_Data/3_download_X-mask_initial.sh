#!/bin/bash

###########################################################################################################################################################################################################################
#Script Name	: 3_download_X-mask_initial.sh                                                               
#Description	: This script interacts with brainlife.io CLI in order to download "X-mask initial" of the optic chiasm, which were created by running FreeSurfer on both HCP 3T 1200 Subjects Release and CHIASM datasets.
#Args           :                                                                                           
#Author       	: Robert J. Puzniak                                               
#Email         	: rjpuzniak@gmail.com                                         
###########################################################################################################################################################################################################################

# Select the HCP project
project_id=6043cb8966d5ce5fc26f5f73

# Define the datatype of interest containing mask of optic chiasm
datatype='neuro/mask'
datatag='initial'

# Loop through HCP and CHIASM datasets
datasets='CHIASM HCP'

for dataset in $datasets; do

	echo $dataset

	#Cache the list of files (belonging to given dataset) that can be downloaded
	if [ ! -f all.json ]; then
	    bl dataset query --limit 4 --project $project_id --datatype $datatype --tag $dataset --datatype_tag $datatag --json > all.json
	fi

	for subject in $(jq -r '.[].meta.subject' all.json | sort -u); do
	    echo "downloading subject:$subject ---------------"
	    outdir=../../1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Initial/$dataset/$subject
	    mkdir -p $outdir
	    for id in $(jq -r '.[] | select(.meta.subject == '\"$subject\"') | ._id' all.json); do
		# Download the file		
		bl dataset download $id --directory $outdir
		# Rename the file
		tags=($(jq -r '.[] | select(._id == '\"$id\"') | .datatype_tags' all.json | tr -d '[],"'))
		mv $outdir/mask.nii.gz $outdir/${tags[0]}_${tags[1]}_${tags[2]}.nii.gz

	    done
	done

rm all.json

done

: <<'END'
END




