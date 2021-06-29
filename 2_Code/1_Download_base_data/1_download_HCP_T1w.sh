#!/bin/bash

#########################################################################################################################################################################################################
#Script Name	: 1_download_HCP_T1w.sh                                                                                            
#Description	: This script interacts with brainlife.io CLI in order to download T1w images of the control participants from HCP 3T 1200 Subject Release dataset.
#Args           :                                                                                           
#Author       	: Robert J. Puzniak                                               
#Email         	: rjpuzniak@gmail.com                                         
#########################################################################################################################################################################################################

# Select the HCP project
project_id=5941a225f876b000210c11e5

# Define the datatype of interest containing mask of optic chiasm
datatype='neuro/anat/t1w'

#Cache the list of datasets that we could download
if [ ! -f all.json ]; then
    bl dataset query --limit 5000 --project $project_id --datatype $datatype --json > all.json
fi

for subject in $(jq -r '.[].meta.subject' all.json | sort -u); do
    echo "downloading subject:$subject ---------------"
    outdir=../../1_Data/1_T1w_Images/HCP/$subject
    mkdir -p $outdir
    # Get the ID of desired T1w image
    ids=$(jq -r '.[] | select(.meta.subject == '\"$subject\"') | ._id' all.json)
    for id in $ids; do
	# Download it to respective location
        bl dataset download $id --directory $outdir        
    done
done

rm all.json

: <<'END'
END
