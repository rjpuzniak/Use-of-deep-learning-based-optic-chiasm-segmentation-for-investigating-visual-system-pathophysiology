# Postprocess X-mask_CNN

## Overview

Prior to comparison of candidate X-mask<sub>candidate</sub> with the ground truth-defining X-mask<sub>manual</sub> the former is cropped to axial slices where the latter is defined. This ensures that the comparison of both masks is only limted to common slices and is not affected by portions of X-mask<sub>candidate</sub> belonging to optic nerves or tracts (since the analysis is limited to optic chiasm).
The scripts provided in this folder perform described cropping of X-mask<sub>candidate</sub> to X-mask<sub>manual</sub>. It should be noted however, that cropped mask are already being downloaded with the scripts provided in previous steps. As such, the scripts provided in this folder are necessary only in case where the X-mask were being generated on the local machine, rather than downloaded from the brainlife.io repository.

## Requirements

Following python libraries:

- nibabel
- nilearn
- skimage
- scipy

## Usage

The cropped masks, tagged on brainlife.io repository as `cropped_to_gt` are downloaded together with their uncropped (tag `complete`) versions with the scripts provided in the previous steps. In case where new masks were generated rather than downloaded it is necessary to run the provided scripts in order to create cropped versions of the X_mask<sub>candidate</sub>. This can be achieved by running either provided python (`1_Crop_to_ground_truth`) or jupyter-notebook (`2_Crop_to_groundtruth`) scripts. 
