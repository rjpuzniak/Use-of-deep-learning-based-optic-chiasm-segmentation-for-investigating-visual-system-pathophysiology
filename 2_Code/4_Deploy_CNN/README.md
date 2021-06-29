# Deploy CNN

## Overview

The code provided in this folder allows to (a) download the X-mask<sub>CNN</sub> computed by the trained CNN or (b) deploy the trained CNN on testing datasets (T1-weighted images) by oneself.

## Requirements

In case of (a) downloading:
- brainlife CLI

In case of (b) self-handed deployment of CNN:

Following python libraries:
- numpy
- nibabel
- nilearn
- glob
- matplotlib
- time
- random
- collections
- torch
- torchvision
- torchio

## Usage

In case of (a) downloading please execute the `2_Download_X-mask_CNN` bash script. The script will download the previously stored X-mask<sub>CNN</sub>, which correspond to CNN with the optimal set of parameters (as determined in the study). The X-mask will be downloaded to the `../../1_Data/5_X-mask_CNN/training_30ep_00025lr/connectivity_3/threshold_1/` folder.

Alternatively, in case of (b) self-handed deployment it is necessary to acquire the saved CNN's parameters (either by downloading the provided files from https://osf.io/4cvgq/ and saving them to `../../1_Data/0_CNN_weoghts` or training the CNN using the code provided in `../3_Train_CNN`). The following deployment of CNN on the data is performed by executing the bash script `1_Batch_Deployment_Script`. In order to adjust the parameters it is however necessary to edit the provided default script, which structure is explained below:

The script uses 6 variables:
- `folder_subjects` - which provides the path to the folder containing IDs of all the subjects to be processed. This variable, combined with `groups` variable (defining the groups to be processed) determined the images which will processed by the CNN.
- `folder_t1w` - path to the folder containing T1-weighted images to be processed by the CNN - attempt of processing the subject for whom the T1-weighted image is not provided will result in error.
- `connectivities` - determines the definition of connectivity used when determining the cluster of voxels belonging to the optic chiasm. By default = 3.
- `thresholds` - defines the cut-off threshold used to turn the voxels of continuous values in range 0-1 to binary masks. For most sets of combinations cut-off threshold of 1 is optimal.
- `weights` - saved sets of network's parameters.
- `groups` - control for inclusion/exclusion of participants from chosen datasets/groups.

The script will extract all IDs from `folder_subjects/group`, extract all corresponding T1-weighted images, input the image to the CNN (defined by loaded set of weights) and will output the final prediction to `../../1_Data/5_X-mask_CNN/training_$weight/connectivity_$connectivity/threshold_$threshold/$group/$sub`

