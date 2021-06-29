#!/bin/bash

#########################################################################################################################################################################################################
#Script Name	: 2_download_CHIASM_T1w.sh                                                                                            
#Description	: This script interacts with brainlife.io CLI in order to download T1w images (of controls and participants with albinism) from the CHIASM dataset.
#Args           :                                                                                           
#Author       	: Robert J. Puzniak                                               
#Email         	: rjpuzniak@gmail.com                                         
#########################################################################################################################################################################################################

# Select the CHIASM project
project_id=5ddfa986936ca339b1c5f455

# Define the datatype of interest containing mask of optic chiasm
datatype='neuro/anat/t1w'

#Cache the list of datasets that we could download
if [ ! -f all.json ]; then
    bl dataset query --limit 5000 --project $project_id --datatype $datatype --json > all.json
fi

for subject in $(jq -r '.[].meta.subject' all.json | sort -u); do
    echo "downloading subject:$subject ---------------"
    outdir=../../1_Data/1_T1w_Images/CHIASM/$subject
    mkdir -p $outdir
    # Get the ID of desired T1w image
    ids=$(jq -r '.[] | select(.meta.subject == '\"$subject\"') | ._id' all.json)
    ids_arr=($ids)
    # Download it to respective location
    bl dataset download $ids_arr --directory $outdir   
done

rm all.json

: <<'END'
END
