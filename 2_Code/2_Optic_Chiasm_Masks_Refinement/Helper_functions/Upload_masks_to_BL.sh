#!/bin/bash

bl login

project_id=6043cb8966d5ce5fc26f5f73

# Upload initial masks
folder=/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Initial

for i in $folder/1_HCP/*; do
	echo $(basename $i)
done

for i in $folder/2_CHIASM/*; do
	echo $(basename $i)

: <<'END'
	bl dataset upload --mask $i/OC_mask_FS.nii.gz \
	--project $project_id \
	--datatype neuro/mask \
	--subject $(basename $i) \
	--desc 'Optic chiasm mask segmented from T1w image using FreeSurfer v7.1.1' \
	--datatype_tag 'optic_chiasm' \
	--tag  'initial' 
END
done

# Upload refined masks

folder=/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Refined

for i in $folder/1_HCP/*; do
	echo $(basename $i)
done

for i in $folder/2_CHIASM/*; do
	echo $(basename $i)

	bl dataset upload --mask $i/OC_mask_refined.nii.gz \
	--project $project_id \
	--datatype neuro/mask \
	--subject $(basename $i) \
	--desc 'Refined optic chiasm mask obtained by running custom script on mask obtained from T1w image using FreeSurfer v7.1.1 (initial)' \
	--datatype_tag 'optic_chiasm' \
	--tag  'refined'
done









