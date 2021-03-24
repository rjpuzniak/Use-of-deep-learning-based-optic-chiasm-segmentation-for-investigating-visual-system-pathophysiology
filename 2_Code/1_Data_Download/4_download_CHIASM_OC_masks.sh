#!/bin/bash

#########################################################################################################################################################################################################
#Script Name	: 4_download_CHIASM_OC_masks.sh                                                                                            
#Description	: This script interacts with brainlife.io CLI in order to download masks of the optic chiasm, which were created by running FreeSurfer on the CHIASM dataset.
#Args           :                                                                                           
#Author       	: Robert J. Puzniak                                               
#Email         	: rjpuzniak@gmail.com                                         
#########################################################################################################################################################################################################

# Select the CHIASM project
project_id=5ddfa986936ca339b1c5f455

# Define the datatype of interest containing mask of optic chiasm
datatype='neuro/freesurfer'

#Cache the list of datasets that we could download
if [ ! -f all.json ]; then
    bl dataset query --limit 10000 --project $project_id --datatype $datatype --json > all.json
fi

for subject in $(jq -r '.[].meta.subject' all.json | sort -u); do
    echo "downloading subject:$subject ---------------"
    outdir=../../1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Initial/CHIASM/$subject
    mkdir -p $outdir
    ids=$(jq -r '.[] | select(.meta.subject == '\"$subject\"') | ._id' all.json)
    ids_arr=($ids)
    if [ ! -f $outdir/OC_mask_FS.nii.gz ]; then
	    # Download it to respective location
	    bl dataset download $ids_arr --directory $outdir
	    # Extract optic chiasm mask from FreeSurfer segmentation output (aseg.mgz) file and save it
	    mrcalc $outdir/output/mri/aseg.mgz 85 -eq $outdir/OC_mask_FS.nii.gz
	    # Remove downloaded dataset
	    rm -rf $outdir/output
    fi
done


rm all.json

: <<'END'
END



