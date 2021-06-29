# Import of libraries

import nibabel as nib
import numpy as np
import os
import glob

from nilearn.image import resample_img
from skimage.measure import label
from scipy.ndimage.morphology import binary_dilation

# Function selecting a bounding box (with a margin of choice) around optic chiasm mask created by FreeSurfer

def bounding_box(img, x_offset, y_offset, z_offset):

    a = np.any(img, axis=(1, 2))
    b = np.any(img, axis=(0, 2))
    c = np.any(img, axis=(0, 1))

    amin, amax = np.where(a)[0][[0, -1]]
    bmin, bmax = np.where(b)[0][[0, -1]]
    cmin, cmax = np.where(c)[0][[0, -1]]

    return amin-x_offset, amax+x_offset, bmin-y_offset, bmax+y_offset, cmin-z_offset, cmax+z_offset

def crop_masks(gt_path, mask_path, t1w_path):
    
    # Load masks
    t1w_file = nib.load(t1w_path)
    gt_file=nib.load(gt_path)
    mask_file=nib.load(mask_path)
    
    # Transform mask to be transformed to reference space
    gt_resampled_file = resample_img(gt_file, t1w_file.affine, t1w_file.shape, 'linear')
    mask_resampled_file = resample_img(mask_file, t1w_file.affine, t1w_file.shape, 'linear')

    # Get data
    gt = gt_resampled_file.get_fdata()
    mask = mask_resampled_file.get_fdata()
    t1w = t1w_file.get_fdata()
    
    # Find bounding box
    a_min, a_max, b_min, b_max, c_min, c_max = bounding_box(gt,0,0,0)
    
    # Crop the mask to bounding box
    mask[:,:,0:c_min]=0
    mask[:,:,c_max+1:]=0
    mask[np.nonzero(mask)]=1
    
    # Save the mask
    mask_cropped_to_gt=nib.Nifti1Image(mask, t1w_file.affine, t1w_file.header)
    nib.save(mask_cropped_to_gt, mask_path[:-16]+'_cropped_to_gt.nii.gz' ) 

# Run it on CHIASM dataset
CHIASM=os.listdir('../../1_Data/1_T1w_Images/CHIASM')

for subject in CHIASM:
    
    print(subject)
    
    # Path to ground truth mask
    gt_path='../../1_Data/2_X-mask_manual/CHIASM/'+subject+'/X-mask_manual.nii.gz'    
    
    # Path to T1w image
    t1w_path='../../1_Data/1_T1w_Images/CHIASM/'+subject+'/t1.nii.gz'
    
    mask_to_be_processed=[]

    # Path to initial 
    mask_to_be_processed.append('../../1_Data/3_X-mask_atlas-initial/CHIASM/'+subject+'/X-mask_atlas-initial_complete.nii.gz')
    
    # Path to corrected
    mask_to_be_processed.append('../../1_Data/4_X-mask_atlas-corrected/CHIASM/'+subject+'/X-mask_atlas-corrected_complete.nii.gz')
    
    # Paths to all predictions
    mask_to_be_processed+=glob.glob('../../1_Data/5_X-mask_CNN/*/*/*/CHIASM/'+subject+'/X-mask_CNN.nii.gz')
        
    # Run the script through all
    i=0
    for filename in mask_to_be_processed:
        crop_masks(gt_path, filename, t1w_path)
        i+=1

# Run it on HCP dataset
HCP=os.listdir('/home/rjp/1_OVGU/2_Chiasmal_Abnormalities_Deep_Learning_Based_Segmentation/1_Data/1_T1w_Images_and_Labels/4_Optic_Chiasm_Labels_Handmade_Original/HCP/')

for subject in HCP:
    
    print(subject)
    
    # Path to ground truth mask
    gt_path='../../1_Data/2_X-mask_manual/HCP/'+subject+'/X-mask_manual.nii.gz'    
    
    # Path to T1w image
    t1w_path='../../1_Data/1_T1w_Images/HCP/'+subject+'/t1.nii.gz'
    
    mask_to_be_processed=[]

    # Path to initial 
    mask_to_be_processed.append('../../1_Data/3_X-mask_atlas-initial/HCP/'+subject+'/X-mask_atlas-initial_complete.nii.gz')
    
    # Path to corrected
    mask_to_be_processed.append('../../1_Data/4_X-mask_atlas-corrected/HCP/'+subject+'/X-mask_atlas-corrected_complete.nii.gz')
    
    # Paths to all predictions
    mask_to_be_processed+=glob.glob('../../1_Data/5_X-mask_CNN/*/*/*/HCP/'+subject+'/X-mask_CNN.nii.gz')
        
    # Run the script through all
    i=0
    for filename in mask_to_be_processed:
        crop_masks(gt_path, filename, t1w_path)
        i+=1


