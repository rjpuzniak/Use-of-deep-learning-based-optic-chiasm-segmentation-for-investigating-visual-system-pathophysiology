# Use of deep learning-based optic chiasm segmentation for the investigation of visual system pathophysiology and neuroplasticity 

### Overview

This repository provides a framework for reproduction (and further investigation) of the analysis presented in _"Use of deep learning-based optic chiasm segmentation for the investigation of visual system pathophysiology and neuroplasticity"(in review)_. As such it links other external repositories containing the data linked to the publication (OSF repository containing saved parameters of the neural networks https://osf.io/4cvgq/ and brainlife.io repository containing necessary masks of the optic chiasm https://brainlife.io/project/6043cb8966d5ce5fc26f5f73/dataset) and provides the code (in form of bash, python and jupyter-notebook scripts) required to repeat the presented experiment.

### Contents

The repository consists of 3 basic folders:

- `1_Data` - where all the project-related data will be saved and stored.
- `2_Code` - divided into several subfolders, corresponding to consequtive stages of analysis (download of the base data, data preprocessing, network training, deployment of the trained neural network and evaluation of the results).
- `3_Figures` - containing all the generated figures.

### Usage

In order to reproduce the published experiment please clone the repository and follow the instructions provided in the `2_Code` folder.


