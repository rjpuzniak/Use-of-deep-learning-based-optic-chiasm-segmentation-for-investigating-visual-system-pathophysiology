#!/bin/bash

#########################################################################################################################################################################################################
#Script Name	:  0_download_data.sh                                                                                            
#Description	:  This script interacts with brainlife.io CLI in order to download subset of data from HCP and CHIASM repositories as required by (Puzniak & Hoffmann, In preparation)
#Args           :                                                                                           
#Author       	: Robert J. Puzniak                                               
#Email         	: rjpuzniak@gmail.com                                         
#########################################################################################################################################################################################################

# Log in to brainlife
bl login

# Call scripts downloading respective data files (for selective downloading, please comment the code line with # symbol), as described below:

# (1) Download T1w MRI images from HCP dataset
source 1_download_HCP_T1w.sh

# (2) T1w MRI images from CHIASM dataset
source 2_download_CHIASM_T1w.sh

# (3) FreeSurfer-based masks of optic chiasm from HCP dataset
source 3_download_HCP_OC_masks.sh

# (4) FreeSurfer-based masks of optic chiasm from CHIASM dataset
source 4_download_CHIASM_OC_mask.sh

# Block to comment out
: <<'END'
END
