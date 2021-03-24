import nibabel as nib
import numpy as np
import os

from nilearn.image import resample_img
from skimage.measure import label
from scipy.ndimage.morphology import binary_dilation

def bounding_box(img, x_offset, y_offset, z_offset):

    a = np.any(img, axis=(1, 2))
    b = np.any(img, axis=(0, 2))
    c = np.any(img, axis=(0, 1))

    amin, amax = np.where(a)[0][[0, -1]]
    bmin, bmax = np.where(b)[0][[0, -1]]
    cmin, cmax = np.where(c)[0][[0, -1]]

    return amin-x_offset, amax+x_offset, bmin-y_offset, bmax+y_offset, cmin-z_offset, cmax+z_offset

def view_compare(img1, img2, start_slice, number_slices, x_s, x_e, y_s, y_e, alone=False, overlaid=False):

    fig = plt.figure(figsize=(50,50))
    
    if alone:
            for i in range(number_slices):
                fig.add_subplot(number_slices/3,3,i+1)
                plt.imshow(img1[x_s:x_e,y_s:y_e,start_slice+i], cmap='gray')
                plt.title(str(i), fontsize=40)
    
    elif overlaid:
            for i in range(number_slices):
                fig.add_subplot(number_slices/3,3,i+1)
                plt.imshow(img1[x_s:x_e,y_s:y_e,start_slice+i], cmap='gray')
                plt.imshow(img2[x_s:x_e,y_s:y_e,start_slice+i]>0.1, cmap='plasma', alpha=0.25)  
                plt.title(str(i), fontsize=40)
    else:
            for i in range(number_slices):
                fig.add_subplot(number_slices,2,2*i+1)
                plt.imshow(img1[x_s:x_e,y_s:y_e,start_slice+i], cmap='gray')
                fig.add_subplot(number_slices,2,2*i+2)
                plt.imshow(img2[x_s:x_e,y_s:y_e,start_slice+i], cmap='gray', alpha=1)
                plt.title(str(i), fontsize=40)

# Function creating ground truth label for all participants (subj) within given repository (group)
def create_groundtruth(group, subj, box_margin=(5,5,0)):
    
    # Define paths to images and load images
    t1w_path='../../1_Data/1_T1w_Images_and_Labels/1_T1w_Images/'+group+'/'+str(subj)+'/t1.nii.gz'
    ocmask_path='../../1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Initial/'+group+'/'+str(subj)+'/OC_mask_FS.nii.gz'
    
    # Load images
    t1w_file, ocmask_file = nib.load(t1w_path), nib.load(ocmask_path)

    # Resample mask image to the T1w
    ocmask_resampled_file = resample_img(ocmask_file, t1w_file.affine, t1w_file.shape, 'linear')
    
    # Extract data
    t1w_data = t1w_file.get_fdata()
    ocmask_resampled_data = ocmask_resampled_file.get_fdata()
    
    # Calculate bounding box of the optic chiasm
    a_min, a_max, b_min, b_max, c_min, c_max = bounding_box(ocmask_resampled_data,*box_margin)
    
    # Find value of 66th percentile of voxel intensity within initial optic chiasm mask (bottom cutoff threshold for non-white matter voxels)
    med_in_chiasm = np.percentile((t1w_data)[np.nonzero(ocmask_resampled_data)],66)
    
    # Find 98th percentile (top cutoff for hypterintense blood vessels)
    top_in_chiasm = np.percentile((t1w_data)[np.nonzero(ocmask_resampled_data)],98)
    
    # Apply thresholds
    t1w_thresh_tmp = (t1w_data> med_in_chiasm)*t1w_data
    t1w_thresh = (t1w_thresh_tmp< top_in_chiasm)*t1w_thresh_tmp

    # Extract T1w and OC mask according to box boundaries and threshold T1w image using calculated mean
    t1w_box = t1w_thresh[a_min:a_max,b_min:b_max,c_min:c_max]    
    oc_box = ocmask_resampled_data[a_min:a_max,b_min:b_max,c_min:c_max]
    
    t1w_box_original = t1w_data[a_min:a_max,b_min:b_max,c_min:c_max] 
    
    # Extract 2nd biggest cluster from the bounded box (the biggest one is background)
    clusters = label(np.where(t1w_box!=0,1,0), connectivity=1)
    clusters_sizes = [np.sum(clusters == i) for i in list(np.unique(clusters))]
    
    ordered_sizes = clusters_sizes.copy()
    ordered_sizes.sort()
    
    target_cluster = clusters_sizes.index(ordered_sizes[-2])
    
    # Dilate the target cluster slice-by-slice (due to conservative threshold used)
    final_cluster = (clusters==target_cluster).astype(int)
    for slice in range(final_cluster.shape[2]):
        final_cluster[:,:,slice] = binary_dilation(final_cluster[:,:,slice])

    # Modify the OC mask image using calculated optimal mask
    ocmask_resampled_data[a_min:a_max,b_min:b_max,c_min:c_max] = final_cluster

    # Save the updated file
    groundtruth_image = nib.Nifti1Image(ocmask_resampled_data, ocmask_resampled_file.affine, ocmask_resampled_file.header)
    os.makedirs('../../1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Refined/'+group+'/'+str(subj))
    nib.save(groundtruth_image,'../../1_Data/1_T1w_Images_and_Labels/2_Optic_Chiasm_Labels_Refined/'+group+'/'+str(subj)+'/OC_mask_refined.nii.gz')
        
    return str(subj)   
