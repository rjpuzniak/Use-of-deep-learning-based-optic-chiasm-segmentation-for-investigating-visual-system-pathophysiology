# Use of deep learning-based optic chiasm segmentation for the investigation of visual system pathophysiology and neuroplasticity 

### Overview

This folder contains the code linked to the publication _"Use of deep learning-based optic chiasm segmentation for the investigation of visual system pathophysiology and neuroplasticity"(in review)_. 

### Contents

This folder in structured into sub-folders corresponding to consequtive steps of analyis, specifically:

- `1_Download_base_data` - provides the code downloading the T1-weighted images, as well as previously prepared X-mask<sub>manual</sub> and X-mask<sub>atlas-initial</sub>.
- `2_Correct_optic_chiasm_masks` - provides the code creating X-mask<sub>atlas-corrected</sub>. The scripts support both computing X-mask<sub>atlas-corrected</sub> from the data acquired in previous step, or downloading the already exisiting masks directly from brainlife.io.
- `3_Train_CNN` - this folder contains a single file, which grants detailed insight into process of CNN training, as well as enables user to train the CNN from scratch.
- `4_Deploy_CNN` - this folder contains scripts allowing for deployment of trained CNN on T1-weighted images.
- `5_Evaluate_results` - scripts included in this folder provide quantitative evaluation of X-mask<sub>CNN</sub> output by trained CNN and generate figures presented in the publication (saved to `../2_Figures` location)


### Usage

In order to reproduce the  experiment please follow the instructions provided in consecutive folders, starting from `1_Download_base_data`.


