# Load T1w
# Load mask we adjust to as layer
# Load the mask we adjust as ROI
# Save the adjusted mask
# Do it for initial and refined masks

t1w_folder=/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/1_T1w_Images

groups='1_HCP'

for group in $groups; do
	
	# Crop handmade masks to inital ones
	folder=/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/5_Optic_Chiasm_Labels_Handmade_Cropped_to_initial
	for i in $folder/$group/*; do

		subj=$(basename $i);
		
		mrview $t1w_folder/$group/$subj/t1.nii.gz -overlay.load /home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Initial/$group/$subj/OC_mask_FS.nii.gz -overlay.threshold_min 0.01 -overlay.opacity 0.75 -overlay.interpolation 0 -overlay.colour 1,0,0 -roi.load $folder/$group/$subj/OC_mask_handmade_cropped_to_initial.nii.gz -roi.opacity 0.5 -roi.colour 0,1,0

	done


	# Crop handmade masks to refined ones
	folder=/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/6_Optic_Chiasm_Labels_Handmade_Cropped_to_refined
	for i in $folder/$group/*; do

		subj=$(basename $i);
		
		mrview $t1w_folder/$group/$subj/t1.nii.gz -overlay.load /home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/3_Optic_Chiasm_Labels_Refined/$group/$subj/OC_mask_refined.nii.gz -overlay.threshold_min 0.01 -overlay.opacity 0.75 -overlay.interpolation 0 -overlay.colour 1,0,0 -roi.load $folder/$group/$subj/OC_mask_handmade_cropped_to_refined.nii.gz -roi.opacity 0.5 -roi.colour 0,1,0


	done
done


