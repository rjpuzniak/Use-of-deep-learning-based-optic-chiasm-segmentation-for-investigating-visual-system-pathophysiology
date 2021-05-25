# Download T1w images of optic chiasm masks

This code will download T1w images and optic chiasm masks (which were previously generated with FreeSurfer software) from both HCP 3T 1200S and CHIASM datasets.

## Requirements
- brainlife CLI
- MRtrix

## Usage
In order to download all the data run `source 0_download_data.sh` from the terminal. In order to select the chosen subset, please comment out the corresponding lines from `0_download_data.sh` script accordingly. The data will be downloaded to the `../1_Data` folder (the detailed location is specified in README).
