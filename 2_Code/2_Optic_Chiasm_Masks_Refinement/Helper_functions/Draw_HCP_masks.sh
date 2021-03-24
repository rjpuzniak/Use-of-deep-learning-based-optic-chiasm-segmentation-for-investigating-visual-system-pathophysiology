folder=/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/4_Optic_Chiasm_Labels_Handmade_Original/1_HCP

for i in $folder/*; do

	sub=$(basename $i)

	echo $sub

	mrview /home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/1_T1w_Images/1_HCP/$sub/t1.nii.gz

done
