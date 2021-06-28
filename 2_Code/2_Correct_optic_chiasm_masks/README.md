# Correct optic chiasm masks

## Overview

The code gathered here allows to obtain the `X-mask_atlas-corrected` by either (a) directly downloading them from the brainlife.io repository or (b) create them from the downloaded T1w images and `X-mask_atlas-initial` (see `../1_Download_base_data` for detailed instructions).
Additionally, provided jupyter-notebook file `Explain_X-mask_atlas-corrected.ipynb` grants inside into detailed steps of custom correction algorithm.


## Requirements
In case of:
(a) downloading from the brainlife.io
- brainlife CLI
(b) running a custom correction algorithm
- Python 3 with installed `nibabel`, `nilearn`, `skimage` and `scipy` libraries

## Usage
In order to (a) download all the data evoke the bash script from the terminal using command `source 0_Download_X-mask_atlas-corrected.sh`, otherwise if (b) running a custom correction algorithm run python script `1_Create_X-mask_atlas-corrected.py`.
