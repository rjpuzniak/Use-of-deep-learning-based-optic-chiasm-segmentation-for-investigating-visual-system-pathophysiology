#!/usr/bin/python3
import argparse
import numpy as np

from collections import OrderedDict

from nilearn import image

from skimage.measure import label

import nibabel as nib

import torch
import torch.nn as nn

parser = argparse.ArgumentParser(prog='Optic Chiasm Segmentator', description='Neural network creating the optic chiasm mask from T1-weighted images')
parser.add_argument('input', metavar='Input T1w path', nargs='?',help='Path to T1w image to be segmented')
parser.add_argument('output', metavar='Output path', nargs='?',help='Path to output folder')
parser.add_argument('filename', metavar='Output filename', nargs='?',help='Name of the output file')
parser.add_argument('-weights', metavar='Parameters of the neural network', nargs='?', help='Path to file containing all parameters of the network')
parser.add_argument('-threshold', metavar='Voxel cutoff threshold for postprocessing of prediction', nargs='?', default=1 , help='Cutoff threshold for final selection of voxels, in range 0-1')
parser.add_argument('-connectivity', metavar='Connectivity for selection of final cluster', nargs='?', default=1 , help='The parameter defining the connectivity for the final selection of voxels')
parser.add_argument('-output_format', choices=('nii.gz','nii'), default=('nii.gz'), nargs='?',help='Format of the output file')

args = parser.parse_args()

output_path = args.output + '/' + args.filename + '.' + args.output_format

# Load the file, resize to (160,160,160) and normalize intensities
file = image.load_img(args.input)

file_resampled = image.resample_img(file, file.affine, (160,160,160))

data = file_resampled.get_fdata()
min, max = np.min(data), np.max(data)
data = (data - min)/(max - min)
data = torch.from_numpy(data).unsqueeze(0).unsqueeze(0)
#print(data.shape)

# Load the network architecture, create and instance and load trained parameters
class UNet(nn.Module):
    
    def __init__(self, in_channels=1, out_channels=1, init_features=10):
        super(UNet, self).__init__()
        
        # Parameter determining depth of layers when going down the network
        features = init_features
        
        # Encoding layers
        self.encoder1 = self.unet_block(in_channels, features, "enc1")
        self.pool1 = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)
        self.encoder2 = self.unet_block(features, features*2, name='enc2')
        self.pool2 = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)
        self.encoder3 = self.unet_block(features*2, features*4, name='enc3')
        self.pool3 = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)
        self.encoder4 = self.unet_block(features*4, features*8, name='enc4')
        self.pool4 = nn.MaxPool3d(kernel_size=2, stride=2, padding=0)
        
        # Bottleneck layer
        self.bottleneck = self.unet_block(features*8, features*8*2, name='bottleneck')
        
        # Decoding layers (where merge with prevois encoding layers occurs)
        self.upconv4 = nn.ConvTranspose3d(features*8*2, features*8, kernel_size=2, stride=2)        
        self.decoder4 = self.unet_block(features*8*2, features*8, name='dec4')
        
        self.upconv3 = nn.ConvTranspose3d(features*4*2, features*4, kernel_size=2, stride=2)
        self.decoder3 = self.unet_block(features*4*2, features*4, name='dec3')
        
        self.upconv2 = nn.ConvTranspose3d(features*2*2, features*2, kernel_size=2, stride=2)
        self.decoder2 = self.unet_block(features*2*2, features*2, name='dec2')
        
        self.upconv1 = nn.ConvTranspose3d(features*2, features, kernel_size=2, stride=2)
        self.decoder1 = self.unet_block(features*2, features, name='dec1')
        
        # Final convolution - output equals number of output channels
        self.conv = nn.Conv3d(features, out_channels, kernel_size=1)
        self.softmax = nn.Softmax(dim=1)   
        
    def forward(self,x):
        
        # Encoding
        enc1 = self.encoder1(x)
        enc2 = self.encoder2(self.pool1(enc1))
        enc3 = self.encoder3(self.pool2(enc2))
        enc4 = self.encoder4(self.pool3(enc3))  
        # Bottleneck
        bottleneck = self.bottleneck(self.pool4(enc4))
        
        # Upconvolving, concatenating data from respective encoding phase and executing UNet block
        dec4 = self.upconv4(bottleneck)
        
        dec4 = torch.cat((dec4, enc4), dim=1)
        dec4 = self.decoder4(dec4)
        dec3 = self.upconv3(dec4)
        dec3 = torch.cat((dec3, enc3), dim=1)
        dec3 = self.decoder3(dec3)
        dec2 = self.upconv2(dec3)
        dec2 = torch.cat((dec2, enc2), dim=1)
        dec2 = self.decoder2(dec2)
        dec1 = self.upconv1(dec2)
        dec1 = torch.cat((dec1, enc1), dim=1)
        dec1 = self.decoder1(dec1)
        
        out_conv = self.conv(dec1)
        
        return self.softmax(out_conv)
    
    def unet_block(self, in_channels, features, name):
        
        return nn.Sequential(OrderedDict([(name+'conv1',nn.Conv3d(in_channels=in_channels, out_channels=features, kernel_size=3, padding=1, bias=False)),
                             (name+'bnorm1', nn.BatchNorm3d(num_features=features)),
                             (name+'relu1', nn.ReLU(inplace=True)),
                             (name+'conv2', nn.Conv3d(in_channels=features, out_channels=features, kernel_size=3, padding=1, bias=False)),
                             (name+'bnorm2', nn.BatchNorm3d(num_features=features)),
                             (name+'relu2', nn.ReLU(inplace=True))])
                            )

soc = UNet(1,2)
soc.load_state_dict(torch.load(args.weights, map_location=lambda storage, loc: storage))

# Run network on the image
if torch.cuda.is_available():
    device='cuda'
else:
    device='cpu'


with torch.no_grad():
    soc.eval()      
    prediction = soc.to(device)(data.to(device=device, dtype=torch.float))

tmp = (prediction[0,0].cpu().numpy().squeeze()>=float(args.threshold)).astype(int)

clusters = label(tmp, connectivity=int(args.connectivity), background=0)
clusters_sizes = [np.sum(clusters == i) for i in list(np.unique(clusters))]

ordered_sizes = clusters_sizes.copy()
ordered_sizes.sort()
try:
   target_cluster = clusters_sizes.index(ordered_sizes[-2])
except:
   target_cluster = clusters_sizes.index(ordered_sizes[-1])

output = (clusters==target_cluster).astype(int)
            
# Save the output
img_pred = nib.Nifti1Image(output, file.affine)
nib.save(img_pred,output_path)
