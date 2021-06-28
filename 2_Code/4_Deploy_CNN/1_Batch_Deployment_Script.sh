folder_subjects=../../1_Data/2_X-mask_manual
folder_t1w=../../1_Data/1_T1w_Images/

connectivities='3' #'1 2'
thresholds='0.25 0.5 0.75 1'
weights='13ep_00025lr 15ep_0003lr 30ep_00025lr 40ep_00015lr 100ep_00005lr'
groups='HCP CHIASM'

for connectivity in $connectivities; do
	for threshold in $thresholds; do
		for weight in $weights; do
			for group in $groups; do
				for subject in $folder_subjects/$group/*; do
					
					sub=$(basename $subject)

					mkdir -p ../../1_Data/5_X-mask_CNN/training_$weight/connectivity_$connectivity/threshold_$threshold/$group/$sub
					python 0_Deployment_Script.py $folder_t1w/$group/$sub/t1.nii.gz ../../1_Data/5_X-mask_CNN/training_$weight/connectivity_$connectivity/threshold_$threshold/$group/$sub X-mask_CNN -weights ../../1_Data/0_CNN_weights/${weight}.pt -threshold $threshold -connectivity $connectivity -output_format 'nii.gz'
					echo $sub

				done
			done
		done
	done
done

